import easyocr
import cv2
import time
import os
import numpy as np
import pyautogui
import threading
from PIL import Image
def x_yProcess(a, b):
    # 计算矩形的左上角和右下角坐标
    x1, y1 = min(a[0], b[0]), min(a[1], b[1])  # 左上角坐标
    x2, y2 = max(a[0], b[0]), max(a[1], b[1])  # 右下角坐标
    return (x1, y1), (x2, y2)
def loading_fun():
    global loading_done  # 声明 loading_done 为全局变量
    signal = 0
    while not loading_done:  # 添加一个标志，例如 loading_done
        if signal % 4 == 0:
            print("识别中——")
        if signal % 4 == 1:
            print("识别中\\")
        if signal % 4 == 2:
            print("识别中|")
        if signal % 4 == 3:
            print("识别中/")
        time.sleep(0.1)
        signal += 1
# 创建EasyOCR reader
reader = easyocr.Reader(['ch_sim', 'en'], gpu=True, model_storage_directory='C:/Users/23249/.EasyOCR/model', download_enabled=False)
os.environ["CUDA_VISIBLE_DEVICES"] = "0"
loading_done = False
def find_specific_char(image, left_top, right_bottom, specific_char):
    """
    在指定区域内寻找特定字符，并返回字符位置
    """
    # 解决2点的位置问题
    left_top, right_bottom = x_yProcess(left_top, right_bottom)
    # 截取指定区域
    cropped_img = image[left_top[1]:right_bottom[1], left_top[0]:right_bottom[0]]
    # 使用EasyOCR进行文字识别
    result = reader.readtext(cropped_img)
    # 寻找特定字符并返回位置
    locations = [item[0] for item in result if specific_char in item[1]]
    # 在找到的位置上画一个红色的框
    for location in locations:
        pts = np.array(location, np.int32)
        pts = pts.reshape((-1,1,2))
        cv2.polylines(cropped_img,[pts],True,(0,0,255),3)
    c = time.time()
    # 使用OpenCV在一个窗口中展示处理后的图片
    '''
    cv2.imshow('Image', cropped_img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()'''
    print(locations)
    return locations

def extract_text(image="0", left_top=(0, 0), right_bottom=(0, 0)):
    """
    从指定区域内提取文字
    """
    global loading_done  # 声明 loading_done 为全局变量
    global cropped_img
    loading_done = False
    # 解决2点的位置问题
    left_top,right_bottom = x_yProcess(left_top, right_bottom)

    if image == "0" and left_top == (0, 0) and right_bottom == (0, 0):
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()
        # 将图像对象转换为 NumPy 数组
        cropped_img = np.array(screenshot)
    elif image == "0" and (left_top != (0, 0) or right_bottom != (0, 0)):
        # 获取屏幕截图
        screenshot = pyautogui.screenshot()
        # 将图像对象转换为 NumPy 数组
        image = np.array(screenshot)
        # 截取指定区域
        cropped_img = image[left_top[1]:right_bottom[1], left_top[0]:right_bottom[0]]
    elif left_top != (0, 0) or right_bottom != (0, 0):
        image = cv2.imread(image)
        # 截取指定区域
        cropped_img = image[left_top[1]:right_bottom[1], left_top[0]:right_bottom[0]]
          # 在主线程中设置 loading_done 为 True，以终止 loading_fun


    # 使用easyocr进行图片文字提取
    result = reader.readtext(cropped_img)

    # 逐行输出文字
    print(result)
    #输出处理
    try:
        middle_result = []
        last_result = result[0]  # 用来储存上一个元素，用于比较如果处于同一行则不换行，反之换行输出
        for item in result:
            # 跳过第一个元素
            if item == last_result:
                middle_result.append(last_result[1])
                middle_result.append(' ')
                continue
            str_high = item[0][2][1] - item[0][0][1]
            if abs(item[0][0][1] - last_result[0][0][1]) < str_high / 5 and abs(
                    item[0][2][1] == last_result[0][2][1]) < str_high / 5:
                middle_result.append(item[1])
                middle_result.append(' ')
            else:
                middle_result.append('\n')
                middle_result.append(item[1])
                middle_result.append(' ')
            last_result = item
        end_result = ""
        for i in range(len(middle_result)):
            end_result += str(middle_result[i])  # 连接列表中的元素，间隔符为空
        print(end_result)
    except IndexError as e:
        print('未识别到内容')
        end_result = '未识别到内容'
    return result,end_result


def find_str(string):
    # 获取屏幕截图
    screenshot = pyautogui.screenshot()
    # 将图像对象转换为 NumPy 数组
    image = np.array(screenshot)
    # 获取屏幕左上角和右下角的坐标
    left, top, right, bottom = 0, 0, screenshot.width, screenshot.height
    find_specific_char(image, (left, top), (right, bottom), string)

    # 打印坐标

if __name__ == '__main__':
    extract_text(r"D:\code\python\Projects\Scripting tools3.0\YYZY\screenshot.png", (0, 0), (1604, 2945))


