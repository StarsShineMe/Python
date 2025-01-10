import time
import datetime
import cv2
import numpy as np
import pyautogui


def find_target_in_screenshot(target_image_path, region=(0, 0, 0, 0), save=0, ishow=0):
    """
    :param target_image_path: 图片路径
    :param region: 寻找范围
    :param save: 1保存图片  0不保存
    :param ishow: 1展示目标位置   0不显示
    :return:
    """
    a = time.time()
    # 读取目标图片和屏幕截图
    target_image = cv2.imread(target_image_path)
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    x1, y1, x2, y2 = region

    if region == (0, 0, 0, 0):
        result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    else:
        # 获取截图上需要寻找目标图片的区域
        cropped_screenshot = screenshot[y1:y2, x1:x2]
        # 进行模版匹配
        result = cv2.matchTemplate(cropped_screenshot, target_image, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 计算匹配位置在完整屏幕上的坐标
    match_x = max_loc[0] + x1
    match_y = max_loc[1] + y1
    w, h = target_image.shape[:-1]
    b = time.time()
    if save == 1 or ishow == 1:
        cv2.rectangle(screenshot, (match_x, match_y), (match_x + h, match_y + w), (0, 0, 255), 2)
        if ishow == 1:
            cv2.imshow('Matching Result', screenshot)
            cv2.waitKey(0)
        if save == 1:
            # 获取当前时间
            current_time = datetime.datetime.now()
            # 将时间格式化为指定的字符串格式
            formatted_time = current_time.strftime("%Y%m%d-%H.%M.%S")
            print(formatted_time)
            cv2.imwrite(f"D:/code/python/Projects/Scripting tools3.0/saveImage/{formatted_time}.png", screenshot)
            with open(r"D:\code\python\Projects\Scripting tools3.0\database\TestLog.txt", 'a') as file:
                file.write(f"\n{formatted_time} max val:{max_val} location{(match_x + h / 2, match_y + w / 2)}"
                           f" run time:{b - a}")
    return max_val, (match_x + h / 2, match_y + w / 2), b - a

if __name__ == '__main__':
    # 示例使用
    target_image_path = r"D:\code\python\Projects\Scripting tools3.0\image\img_1.png"
    max_val, match_position, times = find_target_in_screenshot(target_image_path, region=(0, 0, 2560, 1440),
                                                               save=1)
    print("最大匹配值:", max_val)
    print("匹配位置:", match_position)


