import mouse

import LockWindows
import time
from IO_tools import Create_Popup_windows
from IO_tools import mouses
import pyautogui
from IO_tools import ocr

def capture_rect(x1, y1, x2, y2):
    # 计算矩形的左上角和右下角坐标
    left = min(x1, x2)
    top = min(y1, y2)
    right = max(x1, x2)
    bottom = max(y1, y2)

    # 截取指定区域的截图
    screenshot = pyautogui.screenshot(region=(left, top, right - left, bottom - top))

    # 保存截图
    screenshot.save(r'D:\code\python\Projects\Scripting tools3.0\NSLG\screenshot.png')
    print(f"截图已保存到 'screenshot.png'")
def left_click(aim_XY = (0,0)):
    mouses.move_to(aim_XY[0],aim_XY[1])
    mouses.left_click()
    print(f"点击({aim_XY[0]},{aim_XY[1]})")
time.sleep(1)
# 准备工作
LockWindows.move_window_to_position_by_name("三国",888,60,1)
LockWindows.resize_window("三国",1600,880,1)

one_left_top = (2370,291)
one_right_bottom = (2460,336)
two_left_top = (2370,393)
two_right_bottom = (2460,438)
three_left_top = (2370,495)
three_right_bottom = (2460,540)
four_left_top = (2370,597)
four_right_bottom = (2460,642)
five_left_top = (2370,699)
five_right_bottom = (2460,744)

middle_aim = (1685,500)

top_aim = (0,0)
left_top_aim = (1764,464)
left_bottom_aim = (1809,537)
bottom_aim = (1728,552)
right_bottom_aim = (1602,549)
right_top_aim = (1577,482)

#capture_rect(1650,452,1719,471)"""
while True:
    txt = str(ocr.extract_text((1650, 452), (1719, 471)))
    Create_Popup_windows.create_popup(txt)
    time.sleep(100)
