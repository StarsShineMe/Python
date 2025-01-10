import time

from IO_tools import Visual_tools
from IO_tools import mouses
def modFind_m(img_path,move = 1,click = 0,cycle_time:float = 0,precise = 0.95,x0 = 0,y0 = 0,wait_time_max:float =0):
    ifFind = Visual_tools.pyautogui_find_image(rf'{img_path}',cycle_time=cycle_time,precise=precise,wait_time_max=wait_time_max)
    if ifFind is not False:
        ifFind_x, ifFind_y, ifFind_w, ifFind_h = ifFind
        x = int(ifFind_x + ifFind_w / 2)
        y = int(ifFind_y + ifFind_h / 2)
        if move == 1:
            mouses.move_to(x+x0, y+y0)
        if click == 1:
            time.sleep(0.1)
            mouses.left_click()
        return x,y
    else:return None

def bbFind_move(img_path):
    """
    寻找物品 路径
    :param img_path:
    :return:
    """
    continueSign = 0
    nowbb = 1
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_5.png')
    mouses.move_r(0, -250)
    while True:
        modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_5.png',y0=250)
        ifFind = Visual_tools.pyautogui_find_image(rf'{img_path}',
                                                   cycle_time=0.5)
        if ifFind is False:
            mouses.wheel_down()
            time.sleep(1)
            continueSign = continueSign + 1
        else:
            ifFind_x,ifFind_y,ifFind_w,ifFind_h = ifFind
            x = int(ifFind_x + ifFind_w/2)
            y = int(ifFind_y + ifFind_h/2)
            mouses.move_to(x,y)
            break
        if continueSign == 2:
            if nowbb == 1:
                modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\bb2.png',click=1)
                nowbb = 2
                continueSign = 0
                continue
            if nowbb == 2:
                modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\bb3.png',click=1)
                continueSign = 0
                nowbb = 3
                continue

