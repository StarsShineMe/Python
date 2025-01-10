import pygetwindow as gw
import win32api
import win32con
import win32gui


def get_window_handle_by_keyword(keyword):
    """
    获取窗口句柄
    :param keyword: 窗口关键字
    :return:
    """
    # 获取所有窗口
    windows = gw.getWindowsWithTitle(keyword)

    # 如果匹配的窗口数量为1，则返回该窗口的句柄
    if len(windows) == 1:
        print(f"窗口句柄:P{windows[0]._hWnd}")
        return windows[0]._hWnd  # _hWnd是窗口句柄

    # 如果没有或者多个窗口匹配，返回空
    return None

import pygetwindow as gw

def get_window_size_by_handle(WindowsName,scaling_percentage = 1.5):
    """
    获取窗口尺寸
    :param WindowsName:窗口关键词
    :param scaling_percentage:显示器缩放大小
    :return:
    """
    try:
        handle = get_window_handle_by_keyword(WindowsName)
        window = gw.Window(handle)  # 获取窗口对象
        print(f"窗口缩放:{scaling_percentage}")
        print(f"窗口长度:{int(window.width*scaling_percentage)}  窗口高度:{int(window.height*scaling_percentage)}")

        return int(window.width*scaling_percentage), int(window.height*scaling_percentage)
    except Exception as e:
        print(f"无法获取窗口大小: {e}")
        return None
def move_window_to_position(hwnd, x, y,scaling_percentage = 1.5):
    """
    根据句柄调整窗口大小
    :param hwnd: 句柄
    :param x: 长
    :param y: 宽
    :param scaling_percentage: 显示器缩放
    :return:
    """
    # SetWindowPos 函数可以改变窗口的位置和大小
    win32gui.SetWindowPos(hwnd, 0, x, y, 0, 0, win32con.SWP_NOSIZE)
def move_window_to_position_by_name(WindowName, x,y, scaling_percentage = 1.5):
    """
    调整窗口左上角位置为
    :param WindowName:
    :param x:
    :param y:
    :param scaling_percentage:
    :return:
    """
    handle = get_window_handle_by_keyword(WindowName)
    move_window_to_position(handle,int(x/scaling_percentage),int(y/scaling_percentage))
    print(f"已固定应用:{win32gui.GetWindowText(handle)} 位置为({x},{y})")


import win32gui
import win32con


def resize_window(WindowName, width, height,scaling_percentage = 1.5):
    """
    调整窗口的大小

    参数:
    hwnd (int): 窗口的句柄
    width (int): 要设置的窗口宽度
    height (int): 要设置的窗口高度

    功能:
    通过窗口句柄，调整窗口的大小，不改变其位置。
    """
    # SetWindowPos 用于调整窗口的位置和大小
    widths = int(width/scaling_percentage)
    heights = int(height/scaling_percentage)
    handle = get_window_handle_by_keyword(WindowName)
    win32gui.SetWindowPos(
        handle,  # 窗口的句柄
        0,  # 不改变窗口的 Z 顺序 (0 表示不改变)
        0,  # 不改变窗口位置的 X 坐标
        0,  # 不改变窗口位置的 Y 坐标
        widths,  # 新的宽度
        heights,  # 新的高度
        win32con.SWP_NOMOVE  # 保持当前窗口位置不变
    )
    print(f"窗口 {WindowName} 已调整大小为 {width}x{height}")

if __name__ == '__main__':
    move_window_to_position_by_name("三国",888,60)
    resize_window("三国",1600,880)

