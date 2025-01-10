import time
from IO_tools import Visual_tools
from IO_tools import mouses
from IO_tools import keyboards
import datetime
def now_time():
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 将时间格式化为指定的字符串格式
    formatted_time = current_time.strftime("%Y%m%d-%H.%M.%S")
    return formatted_time
def find_once(img_name,quantity = 'one',click = 0 ,move = 0,precise = 0.90,region = None):
    V_result = Visual_tools.image_find_mod(f'D:/code/python/Projects/Scripting tools3.0/CBJQ/img/{img_name}.png'
                                    ,quantity=quantity,precise=precise,region=region)
    if (move == 1 or click == 1) and V_result:
        left,top,width,height = V_result
        x = int(left)+int(width/2)
        y = int(top)+int(height/2)
        mouses.move_to(x,y)

    if click == 1 and V_result:
        mouses.left_click()
    return V_result
def find_until(img_name,quantity = 'one',click = 0 ,move = 0,precise = 0.90, cycle_times=1, cycle_time: float = 0,region = None):
    V_result = Visual_tools.pyautogui_find_image(f'D:/code/python/Projects/Scripting tools3.0/CBJQ/img/{img_name}.png'
                                    ,quantity=quantity,precise=precise,cycle_times=cycle_times,cycle_time=cycle_time,region=region)
    if (move == 1 or click == 1) and V_result:
        left,top,width,height = V_result
        x = int(left)+int(width/2)
        y = int(top)+int(height/2)
        mouses.move_to(x,y)

    if click == 1 and V_result:
        mouses.left_click()
    return V_result


def message_QQ(text,signal = '0'):
    keyboards.key_combo('win+d')
    if signal == 'X':
        mouses.move_to(2205,1401)
        mouses.left_click()
        a1 = time.time()
        while True:
            b1 = time.time()
            if b1 - a1 > 3:
                message_QQ(text=text,signal ='0')
                break
            if find_once("QQ_ztl_2",move = 1) :
                mouses.right_click()
                time.sleep(0.5)
                mouses.move_r(10,-20)
                mouses.left_click()
                message_QQ(text=text, signal='0')
                break
            if find_once("QQ_ztl_1",move = 1):
                mouses.right_click()
                time.sleep(0.5)
                mouses.move_r(10, -20)
                mouses.left_click()
                message_QQ(text=text,signal = '0')
                break
        return 0

    if signal == '0':
        find_until('QQ_sign',click=1,region = (500,1370,2100,1440))
        signal = '1'
    if signal == '1':
        a = time.time()
        while True :
            b = time.time()
            if b-a > 3:
                message_QQ(text,signal = 'X')
                return 0
            if find_once("QQ_start_pkq",region=(1030,340,1520,1020)):
                signal = 'wait_change_account'
                time.sleep(0.5)
                mouses.move_to(1344,744)
                mouses.left_click()
                time.sleep(0.5)
                mouses.move_to(1180,630)
                mouses.left_click()
                time.sleep(0.5)
                mouses.move_to(1370, 630)
                mouses.left_click()
                time.sleep(0.5)
                mouses.move_to(1275, 894)
                mouses.left_click()
                time.sleep(0.5)
                signal = 'online'
                break
            if find_once("QQ_start_pc"):
                find_once("QQ_dl",click=1,region=(1030,340,1520,1020))
                signal = 'online'
                break
            if find_once("QQ_windows_gps",region=(561,324,632,1086)):
                signal = 'online'
                break
        if find_until("jym",click=1,region=(648,300,750,1140)):
            time.sleep(0.5)
            mouses.move_to(1414,1070)
            mouses.left_click()
            signal = "start_speak"
        if signal == "start_speak":keyboards.key_input(str(text))
        find_until("QQ_enter",click = 1)

def message_bluetooth(text):
    keyboards.key_combo('win+d')
    with open("D:/code/python/Projects/Scripting tools3.0/CBJQ/needsend.txt",'w') as file:
        file.write(now_time()+':'+text)
    mouses.move_to(2205, 1401)
    mouses.left_click()
    find_until("bluetooth",move = 1)
    mouses.right_click()
    time.sleep(0.5)
    keyboards.key_press('s')
    find_until("iqoo",click = 1)
    mouses.left_click()
    mouses.left_click()
    time.sleep(0.5)
    keyboards.key_press('r')
    time.sleep(0.5)
    mouses.move_to(1554,375)
    mouses.left_click()
    keyboards.key_input('D:/code/python/Projects/Scripting tools3.0/CBJQ/',time_sleep=0)
    find_until("arrive",click=1)
    find_until("needsend",click=1)
    mouses.left_click()
    mouses.left_click()
    find_until("next",click=1)


def CBJQ_main():
    start_time = now_time()
    keyboards.key_combo('win+d')
    find_until('CBJQ_sign',move=1)


























    mouses.left_click()
    mouses.left_click()
    find_until("CBJQ_play",click=1)
    find_until("CBJQ_dl")
    time.sleep(8)
    mouses.left_click()
    while True:   # 回到主页
        time.sleep(0.7)
        if find_once("CBJQ_esc_sign"):
            keyboards.key_combo('esc')
            time.sleep(0.7)
            break
        keyboards.key_combo('esc')
    mouses.move_to(1925,650)  # 活动入口坐标
    mouses.left_click()
    time.sleep(7)
    mouses.move_to(255, 657)  # 材料
    mouses.left_click()
    time.sleep(3)
    mouses.move_to(1464, 411)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1986, 1350)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1707, 963)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1269, 1103)  # 材料
    mouses.left_click()
    time.sleep(2)
    while True:
        time.sleep(0.7)
        if find_once("CBJQ_esc_sign"):
            keyboards.key_combo('esc')
            time.sleep(0.7)
            break
        keyboards.key_combo('esc')
    mouses.move_to(2375, 1364)  # 材# 料
    time.sleep(2)
    mouses.left_click()
    mouses.move_to(2252, 495)  # 材料
    time.sleep(2)
    mouses.left_click()
    mouses.left_click()
    mouses.move_to(2301, 1356)  # 材料
    time.sleep(2)
    mouses.left_click()
    while True:
        time.sleep(0.7)
        if find_once("CBJQ_esc_sign"):
            keyboards.key_combo('esc')
            time.sleep(0.7)
            break
        keyboards.key_combo('esc')
    mouses.move_to(2211, 630)  # 材料
    mouses.left_click()
    time.sleep(4)
    mouses.move_to(1056, 1130)  # 材料
    mouses.left_click()
    time.sleep(4)
    left,top,width,height = find_until("wushizhiyan",move=1)
    mouses.move_to(int(left) + int(int(width) / 2) + 105, int(top) + int(int(height) / 2) + 145)
    time.sleep(2)
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1545, 950)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1707, 953)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1250, 1111)  # 材料
    mouses.left_click()
    time.sleep(2)
    keyboards.key_combo('esc')
    time.sleep(2)
    left,top,width,height = find_until("shunke",move=1)
    mouses.move_to(int(left) + int(int(width) / 2) + 105, int(top) + int(int(height) / 2) + 145)
    time.sleep(2)
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1545, 950)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1707, 953)  # 材料
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(1250, 1111)  # 材料
    mouses.left_click()
    time.sleep(2)
    keyboards.key_combo("esc")
    while True:
        time.sleep(0.7)
        if find_once("CBJQ_esc_sign"):
            keyboards.key_combo('esc')
            time.sleep(0.7)
            break
        keyboards.key_combo('esc')

    mouses.move_to(1990, 474)
    mouses.left_click()
    time.sleep(2)
    mouses.move_to(171, 1326)
    mouses.left_click()
    time.sleep(2)
    end_time = now_time()
    message_QQ(f'Cen Bai Jin Qu complete  start time:{start_time}   end time:{end_time}')



if __name__ == '__main__':
    CBJQ_main()