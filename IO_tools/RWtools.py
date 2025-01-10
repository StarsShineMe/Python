import time
def fileRead(file_path,mylstrip ='on'):
    """
        提取字符串，按编译器方式

        Args:
            file_path (txt or other):文件路径
            mylstrip: 是否去除左边的空格

        Returns:
            列表
        Raises:
            可能的异常
        """
    with open(file_path, 'r', encoding='utf-8') as file:
        # 读取文件内容
        lines = file.readlines()
        if mylstrip == 'on':
            lines = [line.strip() for line in lines]
        return lines
def str_EX(lines, keywords=None, endwords=None,type=None):
    """
    提取字符串，按编译器方式

    Args:
        lines (list(str) or str): 需要提取的字符串。
        keywords (list(str) or str): 括号左侧部分可以是['for','(']或是'('
        endwords (list(str) or str): 括号左侧部分可以是['end',')']或是')'
        type:返回类型若传入'str'则返回list(str)

    Returns:
        提取出的字符串列表。

    Raises:
        可能的异常

    Example:
        s = "123(45(67)76(34))"
        mod[0] = 67
        mod[1] = 34
        mod[2] = 45(67)76(34)
    """
    if keywords is None:
        keywords = ['for', 'if',]
    if endwords is None:
        endwords = ['end', '}']
    arr1 = []  # 介质
    result = []
    for i in range(len(lines)):
        if any(keyword in lines[i] for keyword in keywords):
        #if any(lines[i].find(keyword) != -1 for keyword in keywords):
            arr1.insert(0, i)  # 在索引为0的位置插入一个元素
        if any(endword in lines[i] for endword in endwords):
        #if any(lines[i].find(endword) != -1 for endword in endwords): #效率高
            result_d = []
            for j in range(len(lines)):
                if arr1[0] < j < i:
                    result_d.append(lines[j])  # 在列表末尾添加一个元素
                if j == i - 1:
                    result.append(result_d)
                    # result.insert(0,result_d)
                    break
            del arr1[0]  # 删除列表中的第一个元素
    if type == 'str':
        result = [''.join(item) for item in result]  # 转为字符串
    return result


def clear_str(string):
    string = [[s.replace(' ', '') for s in sublist] for sublist in string]
    return string
def use_this(file_path,str_EX = 'off', **kwargs):
    string = fileRead(file_path)
    string = str_EX(string, **kwargs)
    string = clear_str(string)
    return string


# a = use_this('hallo',keywords=["(5","(2",'(3'],endwords = [')'])
# print(a)

