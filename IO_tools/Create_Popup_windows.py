import tkinter as tk
import time

import winsound


def toggle_visibility(label):  # 闪烁代码
    if label.winfo_ismapped():
        label.pack_forget()
    else:
        label.pack()

'''def fade_in_out(label):  # 实现了一个渐变慢慢过渡的闪烁弹窗
    for alpha in range(0, 100, 2):
        label.attributes("-alpha", alpha / 100)
        root.update()
        time.sleep(0.05)
    for alpha in range(100, 0, -2):
        label.attributes("-alpha", alpha / 100)
        root.update()
        time.sleep(0.05)'''

def create_popup(texts="请输入文本",show_time = 2000,WinSound = 0):
    """
    创建弹窗
    :param texts:文本
    :param show_time:显示时长
    :param WinSound:0关闭提示音 1打开
    :return:
    """
    if WinSound == 1:
        winsound.MessageBeep()

    # 创建主窗口

    root = tk.Tk()
    root.overrideredirect(True)  # 隐藏标题栏和边框
    root.attributes("-alpha", 0.9)  # 设置透明度

    # 设置弹窗内容
    label = tk.Label(root, text=texts, fg="white", bg="#2B2D30", font=("Times New Roman", 24))
    label.pack()

    # 获取屏幕尺寸
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    # 设置弹窗位置（右下角）
    x = screen_width - label.winfo_reqwidth() - 10
    y = screen_height - label.winfo_reqheight() - 50
    root.geometry(f"+{x}+{y}")
    a = time.time()
    # 定时闪烁弹窗
    ''' while True:
        toggle_visibility(label)
        root.update()
        time.sleep(0.2)
        b = time.time()
        if b - a >= show_time:
            break
    '''
    # 定时关闭弹窗
    root.after(show_time, root.destroy)

    # 置顶显示
    root.lift()
    root.attributes("-topmost", True)

    # 进入消息循环
    root.mainloop()

if __name__ == '__main__':
    # 调用函数创建弹窗
    create_popup("1")
