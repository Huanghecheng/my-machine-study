import os      # 用于处理文件路径和创建目录
import time    # 用于获取时间戳和计算帧率
import cv2     # OpenCV，用于读取摄像头、处理图像和显示窗口

# 截图保存目录：当前脚本所在目录下的 screenshots 文件夹
SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "screenshots")

# 窗口标题
WINDOW_NAME = "Camera"           # 实时画面窗口
PREVIEW_WINDOW = "Screenshot"    # 截图弹窗窗口

# 是否弹出独立的截图预览窗口（True 开启，False 只保存文件不弹窗）
SHOW_PREVIEW_WINDOW = True

# 高清分辨率（摄像头不支持时会自动回退到最接近的分辨率）
WIDTH, HEIGHT = 1920, 1080

# 保存 JPEG 的质量，范围 0-100，数值越高质量越好、文件越大
JPEG_QUALITY = 95

# 截图弹窗参数
PREVIEW_MAX_W = 960      # 弹窗最大宽度
PREVIEW_MAX_H = 720      # 弹窗最大高度
POPUP_DURATION = 100.0     # 弹窗显示时长（秒）

# 右上角旋转按钮参数
BUTTON_W, BUTTON_H = 260, 70   # 按钮尺寸
BUTTON_MARGIN = 10             # 按钮与画面边缘的距离

# 如果保存目录不存在，则创建它
os.makedirs(SAVE_DIR, exist_ok=True)

# 保存运行状态，用字典便于在鼠标回调中修改
state = {
    "lclick": None,      # 待处理的左键点击位置（窗口坐标）——截图
    "rclick": None,      # 待处理的右键点击位置（窗口坐标）——旋转
    "mouse": None,       # 鼠标当前位置（窗口坐标），用于按钮悬停高亮
    "angle": 0,          # 当前旋转角度：0 / 90 / 180 / 270
    "preview": None,     # 独立弹窗显示的截图
    "popup_until": 0,    # 弹窗显示到什么时候
}

# 鼠标回调函数：只记录坐标，具体处理放在主循环里
def on_mouse(event, x, y, flags, param):
    if event == cv2.EVENT_LBUTTONDOWN:      # 左键按下 -> 截图
        state["lclick"] = (x, y)
    elif event == cv2.EVENT_RBUTTONDOWN:    # 右键按下 -> 可能触发旋转按钮
        state["rclick"] = (x, y)
    elif event == cv2.EVENT_MOUSEMOVE:      # 鼠标移动
        state["mouse"] = (x, y)


# 把窗口内的鼠标坐标换算成画面（帧）坐标，兼容窗口缩放和旋转后的尺寸变化
def to_frame_coords(x, y, frame_w, frame_h):
    try:
        _, _, win_w, win_h = cv2.getWindowImageRect(WINDOW_NAME)
    except cv2.error:
        win_w, win_h = frame_w, frame_h
    if win_w <= 0 or win_h <= 0:
        return x, y
    return int(x * frame_w / win_w), int(y * frame_h / win_h)


# 计算旋转按钮在画面中的矩形位置（右上角）
def button_rect(frame_w, frame_h):
    x1 = frame_w - BUTTON_MARGIN
    x0 = x1 - BUTTON_W
    y0 = BUTTON_MARGIN
    y1 = y0 + BUTTON_H
    return x0, y0, x1, y1


# 打开摄像头（0 表示默认摄像头）
cap = cv2.VideoCapture(0)

# 摄像头打开失败时提示并退出
if not cap.isOpened():
    print("无法打开摄像头")
    exit(1)

# 记录摄像头打开的时间，用于在画面左上角显示
open_time = time.time()
open_time_str = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(open_time))

# ---------- 摄像头高清参数设置 ----------
# 使用 MJPG 编码，高分辨率下才能跑出流畅帧率
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*"MJPG"))
cap.set(cv2.CAP_PROP_FRAME_WIDTH, WIDTH)     # 设置画面宽度
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, HEIGHT)   # 设置画面高度
cap.set(cv2.CAP_PROP_FPS, 30)                # 期望帧率
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)          # 只缓存 1 帧，减少延迟

# 读取摄像头上报的实际参数（不支持高清时会自动回退）
real_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
real_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
real_fps = cap.get(cv2.CAP_PROP_FPS)
print(f"摄像头实际分辨率: {real_w}x{real_h}，上报帧率: {real_fps:.1f}")
print(f"摄像头打开时间: {open_time_str}")

# 创建可缩放窗口并绑定鼠标回调
cv2.namedWindow(WINDOW_NAME, cv2.WINDOW_NORMAL)
cv2.resizeWindow(WINDOW_NAME, 1280, 720)     # 窗口缩放显示，保存的仍是原始高清图
cv2.setMouseCallback(WINDOW_NAME, on_mouse)

print(f"保存目录: {SAVE_DIR}")
print("左键单击画面截图，右键单击右上角 Rotate 按钮每次旋转 90°，按 q 或 ESC 退出")

index = 1                                 # 截图序号，避免同一秒内文件重名
prev_time = time.time()                   # 上一帧的时间，用于计算帧率
fps = 0.0                                 # 平滑后的帧率

# 主循环：持续读取摄像头画面
while True:
    # 读取一帧画面
    # ok 表示是否读取成功，frame 是图像数据
    ok, frame = cap.read()
    if not ok:
        print("读取画面失败")
        break

    # ---------- 画面镜像 ----------
    # 1 表示水平翻转，得到和照镜子一样的画面
    frame = cv2.flip(frame, 1)

    # ---------- 画面旋转 ----------
    # 按右上角按钮设定的角度旋转画面
    if state["angle"] == 90:
        frame = cv2.rotate(frame, cv2.ROTATE_90_CLOCKWISE)
    elif state["angle"] == 180:
        frame = cv2.rotate(frame, cv2.ROTATE_180)
    elif state["angle"] == 270:
        frame = cv2.rotate(frame, cv2.ROTATE_90_COUNTERCLOCKWISE)

    # 当前画面尺寸（旋转后宽高会互换）
    frame_h, frame_w = frame.shape[:2]

    # 右上角旋转按钮的矩形位置
    bx0, by0, bx1, by1 = button_rect(frame_w, frame_h)

    # ---------- 判断鼠标是否悬停在旋转按钮上 ----------
    hover = False
    if state["mouse"] is not None:
        mx, my = to_frame_coords(state["mouse"][0], state["mouse"][1], frame_w, frame_h)
        hover = (bx0 <= mx <= bx1) and (by0 <= my <= by1)

    # ---------- 处理右键：只对右上角按钮生效 ----------
    if state["rclick"] is not None:
        cx, cy = to_frame_coords(state["rclick"][0], state["rclick"][1], frame_w, frame_h)
        state["rclick"] = None
        if (bx0 <= cx <= bx1) and (by0 <= cy <= by1):
            state["angle"] = (state["angle"] + 90) % 360   # 每次顺时针旋转 90°
            print(f"旋转角度: {state['angle']}°")

    # ---------- 处理左键：任意位置都截图 ----------
    if state["lclick"] is not None:
        state["lclick"] = None
        stamp = time.strftime("%Y%m%d_%H%M%S")

        # 文件名：日期时间 + 分辨率 + 序号，例如 20260922_143000_1920x1080_0001.jpg
        filename = os.path.join(SAVE_DIR, f"{stamp}_{frame_w}x{frame_h}_{index:04d}.jpg")

        # 按指定质量将图像编码为 JPEG
        ok, buf = cv2.imencode(".jpg", frame, [cv2.IMWRITE_JPEG_QUALITY, JPEG_QUALITY])
        if ok:
            # 用 tofile 写入，避免中文路径导致 imwrite 失败
            buf.tofile(filename)
            print(f"已保存: {filename}")

            # 独立弹窗：截图按比例缩小，避免弹窗比屏幕还大
            if SHOW_PREVIEW_WINDOW:
                scale = min(PREVIEW_MAX_W / frame_w, PREVIEW_MAX_H / frame_h, 1.0)
                preview = cv2.resize(frame, (int(frame_w * scale), int(frame_h * scale)))
                preview = preview.copy()
                # 在弹窗图片底部标注文件名
                cv2.putText(preview, os.path.basename(filename),
                            (10, preview.shape[0] - 15),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)
                state["preview"] = preview

            state["popup_until"] = time.time() + POPUP_DURATION
        index += 1

    # ---------- 计算实时帧率 ----------
    now = time.time()                 # 当前时间
    dt = now - prev_time              # 与上一帧的时间差
    prev_time = now
    if dt > 0:
        cur_fps = 1.0 / dt            # 瞬时帧率
        # 指数平滑，避免数字跳动太剧烈
        fps = cur_fps if fps == 0 else fps * 0.9 + cur_fps * 0.1

    # ---------- 在画面上叠加文字信息 ----------
    # 第一行：摄像头打开时间
    cv2.putText(frame, f"Open: {open_time_str}", (10, 40),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)
    # 第二行：帧率和分辨率
    cv2.putText(frame, f"FPS: {fps:.1f}  {frame_w}x{frame_h}", (10, 80),
                cv2.FONT_HERSHEY_SIMPLEX, 1.0, (0, 255, 0), 2)

    # ---------- 右上角旋转按钮 ----------
    # 悬停时用亮绿色，未悬停时用深绿色，便于识别
    btn_color = (0, 200, 0) if hover else (0, 90, 0)
    cv2.rectangle(frame, (bx0, by0), (bx1, by1), btn_color, -1)      # 填充按钮
    cv2.rectangle(frame, (bx0, by0), (bx1, by1), (0, 255, 0), 2)     # 按钮边框
    # 按钮第一行：当前旋转角度
    label = f"Rotate {state['angle']} deg"
    (tw, _), _ = cv2.getTextSize(label, cv2.FONT_HERSHEY_SIMPLEX, 0.8, 2)
    cv2.putText(frame, label, (bx0 + (BUTTON_W - tw) // 2, by0 + 32),
                cv2.FONT_HERSHEY_SIMPLEX, 0.8, (255, 255, 255), 2)
    # 按钮第二行：提示用右键触发
    hint = "Right-Click"
    (hw, _), _ = cv2.getTextSize(hint, cv2.FONT_HERSHEY_SIMPLEX, 0.55, 1)
    cv2.putText(frame, hint, (bx0 + (BUTTON_W - hw) // 2, by0 + 60),
                cv2.FONT_HERSHEY_SIMPLEX, 0.55, (255, 255, 255), 1)

    # 显示实时画面
    cv2.imshow(WINDOW_NAME, frame)

    # ---------- 独立截图弹窗：显示到时间后自动关闭 ----------
    if state["preview"] is not None:
        if time.time() < state["popup_until"]:
            cv2.imshow(PREVIEW_WINDOW, state["preview"])
        else:
            state["preview"] = None
            try:
                cv2.destroyWindow(PREVIEW_WINDOW)   # 超过显示时长后关闭弹窗
            except cv2.error:
                pass

    # 等待按键，返回按键的 ASCII 码
    key = cv2.waitKey(1) & 0xFF

    # 按下 r 也可以旋转 90°
    if key in (ord("r"), ord("R")):
        state["angle"] = (state["angle"] + 90) % 360

    # 按下 q、Q 或 ESC 时退出循环
    if key in (ord("q"), ord("Q"), 27):
        break

# 释放摄像头资源
cap.release()

# 关闭所有 OpenCV 窗口
cv2.destroyAllWindows()
