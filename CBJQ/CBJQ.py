import tools
import time
from IO_tools import Visual_tools
from IO_tools import mouses
from IO_tools import keyboards
import datetime
def main():
    keyboards.key_combo('win+d')
while True:  # 回到主页
    time.sleep(0.5)
    if tools.find_once("CBJQ_esc_sign"):
        print('s')
        keyboards.key_combo('esc')
        time.sleep(0.5)
        break
    keyboards.key_combo('esc')