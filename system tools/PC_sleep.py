import os
import time
def in_sleep():
    # 关闭休眠模式
    os.system('powercfg -h off')
    # 使电脑进入睡眠状态
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def end_sleep():
    # 使电脑进入休眠状态
    os.system('shutdown /h')
if __name__ == '__main__':
    time.sleep(2)
    in_sleep()