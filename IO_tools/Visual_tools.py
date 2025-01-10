import pyautogui
from pyautogui import ImageNotFoundException as PyAutoImageNotFoundException
from pyscreeze import ImageNotFoundException as PyScreezeImageNotFoundException
import time
import cv2
import numpy as np

def x_yProcess(a, b):
    # 计算矩形的左上角和右下角坐标
    x1, y1 = min(a[0], b[0]), min(a[1], b[1])  # 左上角坐标
    x2, y2 = max(a[0], b[0]), max(a[1], b[1])  # 右下角坐标
    return (x1, y1), (x2, y2)


def image_find_mod(image_path, quantity='one', precise=0.90, region=None):
    """

    :param image_path:
    :param quantity:
    :param precise:
    :param region: 四元组 (x,y,width,height),x,y为左上角
    :return:
    """
    try:
        if quantity == 'all':
            if region is None:
                locations = pyautogui.locateAllOnScreen(image_path, confidence=precise)
            else:
                locations = pyautogui.locateAllOnScreen(image_path, confidence=precise, region=region)
            locations_ls = []
            for region in locations:
                # 对每个位置进行操作
                locations_ls.append(region)
            return locations_ls
        if quantity == 'one':
            if region is None:
                locations = pyautogui.locateOnScreen(image_path, confidence=precise)
            else:
                locations = pyautogui.locateOnScreen(image_path, confidence=precise, region=region)
            return locations
    except (PyAutoImageNotFoundException, PyScreezeImageNotFoundException):
        # 如果未能找到图片，则执行以下代码        print("未找到图片", image_path)
        return False


def pyautogui_find_image(image_path, quantity='one', precise=0.95, region=None
                         , cycle_times=1, cycle_time: float = 0, exist_time=0,wait_time_max:float=0):
    global star_time_exist
    judge = 0
    find_star_time = time.time()
    aim_exist_time = 0
    while True:
        star_time_exist = time.time()
        result = image_find_mod(image_path, quantity, precise, region)
        find_end_time = time.time()
        if result != False:
            judge += 1
        if judge >= cycle_times:
            if cycle_times == 1 and exist_time == 0:
                return result
            elif exist_time == 0:
                return result
        run_time = find_end_time - find_star_time
        # print('run time', run_time, wait_time_max)
        if cycle_time != 0 and run_time > cycle_time:
            return result
        if exist_time != 0:
            if result != False:
                aim_exist_time += find_end_time - star_time_exist
            else:
                aim_exist_time = 0
            if aim_exist_time >= exist_time:
                return result
        if wait_time_max != 0:
            if run_time > wait_time_max:
                return False




def find_A_from_B(imgA, imgB, location=None, precise=0.8):
    """
    B中寻找A
    :param imgA:
    :param imgB:
    :param location:
    :param precise:
    :return:
    """
    # 读取图像
    imgA = cv2.imread(imgA, 0)
    imgB = cv2.imread(imgB, 0)

    # 如果指定了搜索位置，则裁剪被寻找的图片
    if location:
        x, y, w, h = location
        imgB = imgB[y:y + h, x:x + w]

    # 模板匹配
    result = cv2.matchTemplate(imgB, imgA, cv2.TM_CCOEFF_NORMED)

    # 获取匹配结果
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 如果匹配精度满足要求，则返回匹配位置
    if max_val >= precise:
        top_left = max_loc
        bottom_right = (top_left[0] + imgA.shape[1], top_left[1] + imgA.shape[0])
        return top_left, bottom_right, max_val
    else:
        return None, None, max_val
'''
pyautogui.locateOnScreen会返回一个图像位置
pyautogui.locateAllOnScreen会返回所有匹配图像的位置，然后使用循环遍历并打印每个匹配位置的信息。'''


if __name__ == '__main__':
    time.sleep(1)
    print('s')
    a = pyautogui_find_image(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\heikongwei.png',precise=0.80,quantity="two")
    print(a)
