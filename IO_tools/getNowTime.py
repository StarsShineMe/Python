import datetime
def getNowTime():
    # 获取当前时间
    current_time = datetime.datetime.now()
    # 将时间格式化为指定的字符串格式
    formatted_time = current_time.strftime("%Y%m%d-%H.%M.%S")
    return formatted_time
