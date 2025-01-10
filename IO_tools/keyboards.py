import win32api
import win32con
import time
import pypinyin
from pypinyin import Style


# 定义常量
VK_CODE = {
    'backspace': 0x08,
    'tab': 0x09,
    'shift': 0x10,
    'ctrl': 0x11,
    'alt': 0x12,
    'pause': 0x13,
    'capslock': 0x14,
    'esc': 0x1B,
    'space': 0x20,
    ' ': 0x20,
    'page_up': 0x21,
    'page_down': 0x22,
    'end': 0x23,
    'home': 0x24,
    'left_arrow': 0x25,
    'up_arrow': 0x26,
    'right_arrow': 0x27,
    'down_arrow': 0x28,
    'print_screen': 0x2C,
    'insert': 0x2D,
    'delete': 0x2E,
    '0': 0x30,
    '1': 0x31,
    '2': 0x32,
    '3': 0x33,
    '4': 0x34,
    '5': 0x35,
    '6': 0x36,
    '7': 0x37,
    '8': 0x38,
    '9': 0x39,
    'a': 0x41,
    'b': 0x42,
    'c': 0x43,
    'd': 0x44,
    'e': 0x45,
    'f': 0x46,
    'g': 0x47,
    'h': 0x48,
    'i': 0x49,
    'j': 0x4A,
    'k': 0x4B,
    'l': 0x4C,
    'm': 0x4D,
    'n': 0x4E,
    'o': 0x4F,
    'p': 0x50,
    'q': 0x51,
    'r': 0x52,
    's': 0x53,
    't': 0x54,
    'u': 0x55,
    'v': 0x56,
    'w': 0x57,
    'x': 0x58,
    'y': 0x59,
    'z': 0x5A,
    'win': 0x5B,
    'right_windows': 0x5C,
    'numpad_0': 0x60,
    'numpad_1': 0x61,
    'numpad_2': 0x62,
    'numpad_3': 0x63,
    'numpad_4': 0x64,
    'numpad_5': 0x65,
    'numpad_6': 0x66,
    'numpad_7': 0x67,
    'numpad_8': 0x68,
    'numpad_9': 0x69,
    'multiply_key': 0x6A,
    'add_key': 0x6B,
    'separator_key': 0x6C,
    'subtract_key': 0x6D,
    'decimal_key': 0x6E,
    'divide_key': 0x6F,
    'F1': 0x70,
    'F2': 0x71,
    'F3': 0x72,
    'F4': 0x73,
    'F5': 0x74,
    'F6': 0x75,
    'F7': 0x76,
    'F8': 0x77,
    'F9': 0x78,
    'F10': 0x79,
    'F11': 0x7A,
    'F12': 0x7B,
    'num_lock': 0x90,
    'scroll_lock': 0x91,
    'left_shift': 0xA0,
    'right_shift ': 0xA1,
    'left_control': 0xA2,
    'right_control': 0xA3,
    'left_menu': 0xA4,
    'right_menu': 0xA5,
    'browser_back': 0xA6,
    'browser_forward': 0xA7,
    'browser_refresh': 0xA8,
    'browser_stop': 0xA9,
    'browser_search': 0xAA,
    'browser_favorites': 0xAB,
    'browser_start_and_home': 0xAC,
    'volume_mute': 0xAD,
    'volume_Down': 0xAE,
    'volume_up': 0xAF,
    'next_track': 0xB0,
    'previous_track': 0xB1,
    'stop_media': 0xB2,
    'play/pause_media': 0xB3,
    'start_mail': 0xB4,
    'select_media': 0xB5,
    'start_application_1': 0xB6,
    'start_application_2': 0xB7,
    'attn_key': 0xF6,
    'crsel_key': 0xF7,
    'exsel_key': 0xF8,
    'play_key': 0xFA,
    'zoom_key': 0xFB,
    'clear_key': 0xFE,
    '.': 0xBE,
    ';': 0xBA,
    '\'': 0xDE,
    '[': 0xDB,
    ']': 0xDD,
    '-': 0xBD,
    '=': 0xBB,
    '/': 0xBF,
    '*': 0x6A, #(NumPad *)
    '+': 0x6B, ##(NumPad +)
    '`': 0xC0,
    '\\': 0xDC,
    'enter': 0x0D,
    ',':0xBC
}

INPUT_CODE = {
    '!': "shift+1",
    '@': "shift+2",
    '#': "shift+3",
    '$': "shift+4",
    '%': "shift+5",
    '^': "shift+6",
    '&': "shift+7",
    '*': "shift+8",
    '(': "shift+9",
    ')': "shift+0",
    '_': "shift+-",
    '+': "shift+=",
    '{': "shift+[",
    '}': "shift+]",
    ':': "shift+;",
    '"': "shift+'",
    '<': "shift+,",
    '>': "shift+.",
    '?': "shift+/",
}

def key_down(key):
    key = VK_CODE[key]
    # 按下键
    win32api.keybd_event(key, 0, 0, 0)


def key_up(key):
    key = VK_CODE[key]
    # 释放键
    win32api.keybd_event(key, 0, win32con.KEYEVENTF_KEYUP, 0)


def key_press(str_, time_sleep=0.06):
    """
    按下键盘按键，支持连续按下多个按键，支持长按time_sleep输入按键按下时间
    :param str_:按键/按键列表
    :param time_sleep:按下时间
    :return:无
    """
    str_ = str_.lower()
    for i in str_:
        key_down(i)
        time.sleep(time_sleep)
        key_up(i)


def key_input(str_, time_sleep=0.06):
    """
    按键按下，支持大小写区分
    :param str_: 按键
    :param time_sleep:按下时间
    :return:
    """

    for i in str_:
        if i in INPUT_CODE:
            key_combo_Input(str(INPUT_CODE[i]))
        elif i.islower():
            key_down(i)
            key_up(i)
            time.sleep(time_sleep)
        elif i.isupper() == True:
            i = i.lower()
            key_combo_Input(f'shift+{i}')
        else:
            key_down(i)
            key_up(i)
            time.sleep(time_sleep)


def hz_to_str(hz_str, split: str = ''):
    """
    汉字转字符串
    :param hz_str:
    :param split: 字符串的连接符号，默认无
    :return:
    """
    hz_str = pypinyin.pinyin(hz_str, style=Style.NORMAL, strict=True)
    hz_str = str(split).join([item[0] for item in hz_str])
    return hz_str


def hz_input(str_, time_sleep=0.06, split: str = ''):
    """
    输入汉字输出汉字需要输入法配合按下1,2,3进行选词
    :param str_:
    :param time_sleep:
    :param split:
    :return:
    """
    str_ = str_.lower()
    str_ = hz_to_str(str_, split)
    print(str_)
    key_press(str_, time_sleep)


def key_combo_Input(string, time_sleep=0.06):
    """
    组合键，可实现多个按键同时按下
    :param string:
    :param time_sleep:
    :return:
    """
    string = string.lower()
    string = string.split('+',1)
    for key in string:
        key_down(key)
    for key in string[::-1]:
        key_up(key)
        time.sleep(time_sleep)
def key_combo(string, time_sleep=0.06):
    """
    组合键，可实现多个按键同时按下
    :param string:
    :param time_sleep:
    :return:
    """
    string = string.lower()
    string = string.split('+')
    for key in string:
        key_down(key)
        time.sleep(time_sleep)
    for key in string[::-1]:
        key_up(key)
        time.sleep(time_sleep)
# def auto_input

if __name__ == '__main__':
    time.sleep(2)
    key_combo('w',time_sleep=3)
