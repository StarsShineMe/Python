import time
def with_for(func, *args, cycle=-1, times=float(-1), once_time=float(0), display_time=0,
             wait_return='waiting...',nois_exit = 'None',** kwargs):
    """"
    循环装饰器不加限制死循环
    :param **kwargs: 函数关键词
    :param func: 所需循环的函数
    :param args: 函数参数
    :param cycle: 循环次数
    :param times: 循环时间
    :param once_time: 单词循环时间
    :param display_time: 是否显示代码执行时间 0 不显示 1 显示 默认0
    :param wait_return: 等待返回值wait-return终止程序
    :param nois_exit: 等待返回值不为nois_away_return时终止程序
    :return:
    """
    star_time = time.time()
    results = []  # 创建一个空列表来存储每次的返回值
    while True:
        once_star_time = time.time()
        a = time.time()
        result = func(*args)
        b = time.time()
        if display_time == 1: print(f'函数{func}运行时间:', b - a)
        if cycle != -1: cycle -= 1
        if cycle == 0: break
        end_time = time.time()
        if end_time - star_time >= times != -1: break
        if end_time - once_star_time < once_time: time.sleep(once_time - end_time + once_star_time)
        results.append(result)  # 将返回值添加到列表中
        if result == wait_return:
            return result
        if result != nois_exit and nois_exit != 'off':
            return result
    return results