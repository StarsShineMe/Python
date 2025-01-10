import win32api
import win32con
import time
def move_r(x, y):
    """
    鼠标相对移动x,y
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(int(x)/1.5),int(int(y)/1.5))

def move_ri(x, y):
    """
    鼠标相对移动x,y 怕打断人不能碰鼠标
    """
    global move_x  # 将 move_x 变量声明为全局变量
    global move_y  # 将 move_x 变量声明为全局变量
    time_x = int(x / 32)
    time_y = int(y / 18)
    time_r = time_x if time_x > time_y else time_y
    if time_r != 0:
        move_x = int(x / time_r)
        move_y = int(y / time_r)
        for i in range(time_r):
            win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(move_x / 1.5), int(move_y / 1.5))
    win32api.mouse_event(win32con.MOUSEEVENTF_MOVE, int(int(x / 1.5 - int(move_x / 1.5) * time_r)),
                         int(int(y / 1.5 - int(move_y / 1.5) * time_r)))
def move_to(x, y):
    """
    鼠标绝对移动x,y
    """
    # 将鼠标移动到指定的坐标（x，y）
    win32api.SetCursorPos((int(x/1.5), int(y/1.5)))
# 模拟鼠标左键单击
def left_click(time_sleep=0.06):
    """
    鼠标左键点击
    :param time_sleep:按下时间
    :return:
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(time_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
# 模拟鼠标中键单击
def middle_click(time_sleep=0.06):
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
    time.sleep(time_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)
# 模拟鼠标右键单击
def right_click(time_sleep=0.06):
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
    time.sleep(time_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
# 模拟鼠标滚轮下滚一次
def wheel_down(times=1):
    """
    滚轮下
    :param times: 滚动滚动次数，默认一次
    :return:
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, -120 * times)
def drag_r_left(x, y, time_sleep=0.06):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    move_r(x, y)
    time.sleep(time_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def drag_to_left(x, y, time_sleep=0.06):
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    move_to(x, y)
    time.sleep(time_sleep)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
# 模拟鼠标滚轮上滚一次
def wheel_up(times=1):
    """
    滚轮上
    :param times:滚轮滚动次数，默认一次
    :return:
    """
    win32api.mouse_event(win32con.MOUSEEVENTF_WHEEL, 0, 0, 120 * int(times))
def left_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
def left_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)
def middle_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEDOWN, 0, 0)
def middle_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_MIDDLEUP, 0, 0)
def right_down():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTDOWN, 0, 0)
def right_up():
    win32api.mouse_event(win32con.MOUSEEVENTF_RIGHTUP, 0, 0)
if __name__ == '__main__':
    time.sleep(120)
    left_click()
