import time
import win32gui
import win32ui
from ctypes import windll
from PIL import Image

a = time.time()
def get_windows_scaling_factor():
    try:
        # 调用 Windows API 函数获取缩放比例
        user32 = windll.user32
        user32.SetProcessDPIAware()
        scaling_factor = user32.GetDpiForSystem()
        # 计算缩放比例
        return scaling_factor / 96.0
    except Exception as e:
        print("获取缩放比例时出错:", e)
        return None

# 调用函数获取 Windows 桌面的缩放比例
Screen_zoom = 1.5
scaling_factor = get_windows_scaling_factor()
if scaling_factor is not None:
    Screen_zoom *= scaling_factor
def capture_background_window(hwnd):
    # 获取窗口的设备上下文
    hwndDC = win32gui.GetWindowDC(hwnd)
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    saveDC = mfcDC.CreateCompatibleDC()

    # 创建位图对象
    saveBitMap = win32ui.CreateBitmap()
    left, top, right, bot = win32gui.GetWindowRect(hwnd)
    width = int((right - left) * Screen_zoom)
    height = int((bot - top) * Screen_zoom)
    saveBitMap.CreateCompatibleBitmap(mfcDC, width, height)
    saveDC.SelectObject(saveBitMap)

    # 使用 PrintWindow 函数截图
    result = windll.user32.PrintWindow(hwnd, saveDC.GetSafeHdc(), 1)

    # 将位图保存为图像
    bmpinfo = saveBitMap.GetInfo()
    bmpstr = saveBitMap.GetBitmapBits(True)
    im = Image.frombuffer(
        'RGB',
        (bmpinfo['bmWidth'], bmpinfo['bmHeight']),
        bmpstr, 'raw', 'BGRX', 0, 1
    )
    win32gui.DeleteObject(saveBitMap.GetHandle())
    saveDC.DeleteDC()
    mfcDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, hwndDC)

    if result == 1:
        im.save("screenshot.png")
        print("Screenshot saved as screenshot.png")
    else:
        print("Failed to capture screenshot")


# 示例：获取计算器窗口的句柄并截图
hwnd = win32gui.FindWindow(None, 'MuMu模拟器12')
capture_background_window(hwnd)

def get_windows_scaling_factor():
    try:
        # 调用 Windows API 函数获取缩放比例
        user32 = windll.user32
        user32.SetProcessDPIAware()
        scaling_factor = user32.GetDpiForSystem()
        # 计算缩放比例
        return scaling_factor / 96.0
    except Exception as e:
        print("获取缩放比例时出错:", e)
        return None

# 调用函数获取 Windows 桌面的缩放比例
scaling_factor = get_windows_scaling_factor()
if scaling_factor is not None:
    print("Windows 桌面的缩放比例:", scaling_factor)
    b = time.time()
    print(b-a)