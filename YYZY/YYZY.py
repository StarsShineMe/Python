import time
from IO_tools import ocr
import winsound
from IO_tools import getNowTime
from IO_tools import Create_Popup_windows as Pop
from IO_tools import getAppScreenshot as GetImg
from PIL import Image
from IO_tools import Img_size
from IO_tools import Visual_tools as Vs
import win32gui
import win32con
# 1.加个数组校验
Pop.create_popup("月圆之夜程序加载完成")
Vs_start_time = time.time()
def get_img_size(imgPath):
    # 打开图像文件
    image_path = imgPath
    image = Image.open(image_path)

    # 获取图像尺寸
    width, height = image.size
    return width, height

def YYZY_time():
    global result
    global Vs_start_time
    start = 0
    while True:
        Vs_start_time = time.time() + 0.03
        times = getNowTime.getNowTime()
        GetImg.capture_background_window("MuMu模拟器12", savePath=
        rf"D:/code/python/Projects/Scripting tools3.0/YYZY/savePath/screenshot.png")
        width, height = get_img_size(rf"D:/code/python/Projects/Scripting tools3.0/YYZY/savePath/screenshot.png")
        x = int(0.776056338 * width)
        y = int(0.371932515 * height)
        w = int(0.114084507 * width)
        h = int(0.048312884 * height)
        ax = width/750
        ay = height/1370
        Img_size.Img_size(rf"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockClose.png",
                          size=(int(ax * 69), int(ay * 52)),
                          savePath=rf"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockCloseNow.png")
        Img_size.Img_size(fr"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockOpen.png",
                          size= (int(ax * 63), int(ay * 49)),
                          savePath=rf"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockOpenNow.png")
        if width < 340:
            time.sleep(0.5)
            continue
        a, b, c = Vs.find_A_from_B(r"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockCloseNow.png",
                                   r"D:\code\python\Projects\Scripting tools3.0\YYZY\savePath\screenshot.png",
                                   location=(x, y, w, h),precise=0.8)
        if a is not None:
                print(a, b, c)
                start = 1
        a, b, c = Vs.find_A_from_B(r"D:\code\python\Projects\Scripting tools3.0\YYZY\img\lockOpenNow.png",
                                   r"D:\code\python\Projects\Scripting tools3.0\YYZY\savePath\screenshot.png",
                                   location=(x, y, w, h),precise=0.8)
        if a is not None:
                print(a, b, c)
                start = 1
        if start == 1 :
            result, b = ocr.extract_text(r"D:/code/python/Projects/Scripting tools3.0/YYZY/savePath/screenshot.png",
                                         (int(0.807042254 * width), int(0.461656442 * height)),
                                         (int(0.869014085 * width), int(0.482361963 * height)))
            try:
                if result[0][2] <= 0.6:
                    continue
                result = int(result[0][1])
                print("tp：",type(result),"result:",result)
                start = 0
                break
            except ValueError as e:
                print(f"Error: {e}")
                start = 0
            except TypeError as e:
                print(f"Error: {e}")
                start = 0
            except IndexError as e:
                print(f"Error: {e}")
                start = 0
    while True:
        Vs_end_time = time.time()
        excessTime = result - (Vs_end_time - Vs_start_time)
        if excessTime <= 0.0:
            break
        if excessTime <= 3.0:
            winsound.MessageBeep()
        excessTimeInt = int(excessTime)
        Pop.create_popup(f"{excessTimeInt}",int((excessTime-excessTimeInt)*1000))
    hwnd = win32gui.FindWindow(None, "MuMu模拟器12")
    win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
    YYZY_time()
YYZY_time()

