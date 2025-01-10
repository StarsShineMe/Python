import threading
import time
import pynput.mouse as mouse
from pynput import keyboard
import ocr
import winsound
import Create_Popup_windows
import pyperclip
import mouses
import keyboards


print('程序加载完毕')
def warns(texts = "请输入文本",showtime = 2000):
    winsound.MessageBeep()
    Create_Popup_windows.create_popup(texts=texts , show_time=showtime)

warns(texts="程序加载完毕")
if_press = False
# 记录点击位置的列表
# 记录点击位置的列表
click_positions = []
ocr_again = False
def update_data():
    while True:
        time.sleep(0.2)
        ocr_exe()
def ocr_exe():
    global ocr_again
    global click_positions
    if ocr_again:
        first_result, test_result = ocr.extract_text(left_top=click_positions[0], right_bottom=click_positions[1])
        # 写入剪切板
        pyperclip.copy(test_result)
        load1 = threading.Thread(target=warns, kwargs={'texts': test_result, 'showtime': '2000'})
        load1.start()
        load1.join()

        # 清空列表以准备下一次记录
        click_positions.clear()
        keyboards.key_up('q')
        mouses.left_up()
        ocr_again = False
def on_click(x, y, button, pressed):
    global if_press
    global ocr_again
    global click_positions
    if pressed and if_press == True:
        print(f'{button} pressed at ({x}, {y})')
        click_positions.append((x, y))
        if len(click_positions) == 2:
            ocr_again = True
            if_press = False
# 1

def on_key_release():
    global if_press
    if not if_press:
        if_press = True
        print("Press Ctrl+Q to record mouse clicks.")
        load = threading.Thread(target=warns,kwargs={'texts': 'keypress ctrl+q', 'showtime': '2000'})
        load.start()
        load.join()


if __name__ == '__main__':
    # 创建鼠标监听器
    with mouse.Listener(on_click=on_click) as listener, keyboard.GlobalHotKeys({'<ctrl>+q': on_key_release}) as h:
        load2 = threading.Thread(target=update_data())
        load2.start()
        listener.join()
        h.join()




