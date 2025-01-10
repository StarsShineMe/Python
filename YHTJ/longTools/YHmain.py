import time
import takeThinks
from IO_tools import Visual_tools
from IO_tools import mouses
from IO_tools import keyboards
import threading
import winsound
ldown = 0
rdown = 0
czlz = 0
endPying = 0
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
def arrive_hmpg():
    for i in range(4):
        keyboards.key_combo("esc")
# 准备物资
def prepareThings():
    """
    从大厅进入背包准备物资
    :return:
    """
    global ldown,rdown
    ldown = 0
    rdown = 0
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\xingdongzhunbei.png',x0=-350,y0=-14)
    mouses.left_click()
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_4.png',wait_time_max = 0.5,click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_2.png',wait_time_max = 0.5,click=1)
    time.sleep(0.5)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\qingkong.png',wait_time_max=2, click=1)
    resultMF = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_3.png', wait_time_max=0.5)
    xMF,yMF = resultMF
    takeThinks.bbFind_move(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_1.png')
    mouses.left_down()
    time.sleep(0.5)
    mouses.move_to(xMF,yMF)
    time.sleep(0.5)
    mouses.left_up()
    time.sleep(0.5)
    takeThinks.bbFind_move(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img.png')
    mouses.left_down()
    time.sleep(0.5)
    mouses.move_to(xMF, yMF)
    time.sleep(0.5)
    mouses.left_up()
def MumuStart(name,waitTime:float = 0):
    global czlz
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img.png', click=1,precise=0.8)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_1.png', click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_10.png',x0=845, click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_8.png', click=1)
    keyboards.key_input(f'{name}')
    time.sleep(0.3)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_9.png', click=1)
    time.sleep(1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\czlz.png')
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img.png', click=1, x0=-400,precise=0.8)
def start_game():
    #状态好进游戏
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\xingdongzhunbei.png',click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\queding.png', click=1)
    weichongwu = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\nothappy.png',wait_time_max=1)
    if weichongwu is not None:
        MumuStart(r"weichongwu",waitTime=27)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\querenpeizhuang.png', click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\zhunbeijinru.png', click=1,wait_time_max=5)
    # 匹配到
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\zhunbei.png', click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\iknow.png', click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\ziluolan.png', click=1)
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\queren1.png', click=1)
    # 游戏开始检测
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\bbn.png',precise=0.8)
    thread_endgm = threading.Thread(target=end_game)
    thread_findGold = threading.Thread(target=findGold)
    thread_findGold.start()
    thread_endgm.start()
    time.sleep(0.5)
    # 打开地图
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img.png', click=1, x0=101, y0=182,precise=0.8)
    while True:
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\AAAAA.png',move = 0,wait_time_max=0.1)
        if a is not None:
           # MumuStart('AAAAA')
            winsound.MessageBeep()
            break
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\BBBBB.png', move=0, wait_time_max=0.1)
        if a is not None:
            MumuStart('BBBBB')
            break
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\CCCCC.png', move=0, wait_time_max=0.1)
        if a is not None:
            MumuStart('CCCCC')
            break

    # 识别地图内容
    thread_findGold.join()
    thread_endgm.join()
def end_game():
    global endPying
    # 死亡
    global czlz
    while True:
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\fangqixingdong.png',wait_time_max=0.1,click=1)
        czlz = -1
        if a is not None:
            break
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\tuichuzhanchang.png', move=0, wait_time_max=0.1)
        czlz = -1
        if a is not None:
            break
    endPying = 1
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_2.png', click=1, wait_time_max=0.1)
    MumuStart('exitgame1')
    modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\iknow.png', click=1,wait_time_max=20)
    MumuStart('exitgame2')
    endPying = 0

def findGold():
    global rdown,ldown,endPying
    while True:
        if endPying == 1:
            break
        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\juneijinbi.png', precise=0.8,move=0,
                      wait_time_max=0.1)

        if a is not None:
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_6.png', click=1,
                      wait_time_max=0.1)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\juneijinbi.png', precise=0.8,
                          click=1,
                          wait_time_max=0.1)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\bbn.png', precise=0.8, x0=-1340, y0=600,
                      click=1)
            xMF, yMF = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_4.png',
                                 precise=0.8,
                                 wait_time_max=2)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_6.png', precise=0.8)  #
            if ldown == 0:
                mouses.left_down()
                time.sleep(0.5)
                mouses.move_to(xMF + 131, yMF + 96)
                time.sleep(0.5)
                mouses.left_up()
                ldown = 1
            elif rdown == 0:
                mouses.left_down()
                time.sleep(0.5)
                mouses.move_to(xMF + 245, yMF + 100)
                time.sleep(0.5)
                mouses.left_up()
                rdown = 1
            keyboards.key_combo('esc')
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_7.png', click=1,
                      wait_time_max=0.1)

        a = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\juneijiangpai.png', precise=0.8,
                      wait_time_max=0.1, move=0)

        if a is not None:
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_6.png', click=1,
                      wait_time_max=0.1)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\juneijiangpai.png', precise=0.8,
                      wait_time_max=0.1, click=1)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\ui\bbn.png', precise=0.8, x0=-1340, y0=600,
                      click=1)
            xMF, yMF = modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_4.png',
                                 precise=0.8,
                                 wait_time_max=2)
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\things\img_7.png', precise=0.8)  #
            if ldown == 0:
                mouses.left_down()
                time.sleep(0.5)
                mouses.move_to(xMF + 131, yMF + 96)
                time.sleep(0.5)
                mouses.left_up()
                ldown = 1
            elif rdown == 0:
                mouses.left_down()
                time.sleep(0.5)
                mouses.move_to(xMF + 245, yMF + 100)
                time.sleep(0.5)
                mouses.left_up()
                rdown = 1
            keyboards.key_combo('esc')
            modFind_m(r'D:\code\python\Projects\Scripting tools3.0\YHTJ\img\Mumu\need\img_7.png', click=1,
                      wait_time_max=0.1)


if __name__ == '__main__':
    while True:
        arrive_hmpg()
        prepareThings()
        arrive_hmpg()
        start_game()
