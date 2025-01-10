import psutil
import pygetwindow as gw

# 替换为你的应用程序窗口标题
window_title = "Your Application Window Title"

try:
    # 获取所有窗口
    windows = gw.getWindowsWithTitle(window_title)

    if windows:
        # 获取第一个匹配的窗口
        window = windows[0]

        # 获取进程 ID
        pid = window._hWnd

        # 查找进程
        for proc in psutil.process_iter(['pid', 'name', 'exe']):
            if proc.pid == pid:
                print(f"窗口: {window_title}")
                print(f"对应的 .exe 路径: {proc.exe()}")
                break
    else:
        print("未找到指定的窗口。")

except Exception as e:
    print(f"发生错误: {e}")