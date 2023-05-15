"""
Date: 2023/5/15 10:52

Author: Fengchunyang

Contact: fengchunyang

Record:
    2023/5/15 Create file.

Desc:
    给定一个字符串s，根据指定的行数n，以从上往下、从左到右进行Z字形排列

    e.g
        输入  s = "PAYPALISHIRING"   n = 3

        输出  P   A   H   N
             A P L S I I G
             Y   I   R

    最后再将进行Z字转换的字符串从左往右读取，返回新的字符串，上述例子最终输出结果：PAHNAPLSIIGYIR
"""


def z_change(s, numRows):
    """Z字转换

    Args:
        s(str): 输入字符串
        numRows(int): 行数

    Returns:
        s(str): 结果
    """
    result = ""

    if numRows == 1:
        return s

    if numRows == 2:
        for i in range(0, len(s), 2):
            result += s[i]
        for i in range(1, len(s), 2):
            result += s[i]
        return result

    # 构造二维数组,模拟矩阵，由于矩阵的行数是已知的，因此只需要获取矩阵的列数，构造对应长度的数组即可
    # 观察Z字形的结构可知，连接Z的两条平行线的字符长度为行数-2，去掉Z字的下横线，构成Z字上横线与连接
    # 线的字符数，用字符总数向上整除，可以得到矩阵的最大列数
    array = list()
    char_length = len(s)
    link_length = numRows - 2
    char_remainder = char_length // (numRows + link_length)
    char_quotient = char_length % (numRows + link_length)
    if char_quotient <= numRows:
        col_length = char_remainder * (link_length + 1) + 1
    else:
        col_length = char_remainder * (link_length + 1) + 1 + (char_quotient - numRows)
    for i in range(numRows):
        array.append(['', ] * col_length)
    # print(array)

    loc_row, loc_col = 0, 0
    action = "positive"

    for index, char in enumerate(s):
        # print(f"set value: {char}, position: ({loc_row}, {loc_col})")
        array[loc_row][loc_col] = char
        if action == "positive":
            loc_row += 1
        if action == "negative":
            loc_row -= 1

        if loc_row == numRows and action == "positive":
            loc_row -= 2
            action = "negative"
            loc_col += 1
        if loc_row == 0 and action == "negative":
            loc_col += 1
            action = "positive"

    for _array in array:
        result += ''.join(_array)
    return result


if __name__ == '__main__':
    assert z_change("PAYPALISHIRING", 3) == "PAHNAPLSIIGYIR", "结果异常"
    assert z_change("PAYPALISHIRING", 4) == "PINALSIGYAHRPI", "结果异常"
    assert z_change("A", 1) == "A", "结果异常"
    assert z_change("ABC", 2) == "ACB", "结果异常"
    assert z_change("ABCDE", 2) == "ACEBD", "结果异常"
