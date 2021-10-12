"""
Date: 2021/9/24 16:28

Author: Fengchunyang

Contact: fengchunyang@58.com

Record:
    2021/9/24 Create file.

Title:
    给定两个以字符串形式表示的非负整数 num1 和 num2，返回 num1 和 num2 的乘积，它们的乘积也表示为字符串形式。

    示例 1:
    输入: num1 = "2", num2 = "3"
    输出: "6"

    示例 2:
    输入: num1 = "123", num2 = "456"
    输出: "56088"

    说明：
        num1 和 num2 的长度小于110。
        num1 和 num2 只包含数字 0-9。
        num1 和 num2 均不以零开头，除非是数字 0 本身。
        不能使用任何标准库的大数类型（比如 BigInteger）或直接将输入转换为整数来处理。

    链接：https://leetcode-cn.com/problems/multiply-strings

Thought：
    1.不允许使用类型强转直接转换入参，可以考虑自己实现强转逻辑。自己实现的话，需要使用for循环，两个被乘数，则需要进行两轮循环，执行效率受
      num长度的影响
    2.根据乘法的定义，两个被乘数的各个位都需要进行相乘并乘以进制的值，最后将所有结果累加得到结果

"""


class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # 自定义类型强转
        def str_to_int(num: str, base=10) -> int:
            result = 0
            length = len(num)
            for i, n in enumerate(num):
                result += base ** (length - i - 1) * int(n)
            return result
        product = str_to_int(num1) * str_to_int(num2)
        return str(product)


class SolutionNew:
    def multiply(self, num1: str, num2: str) -> str:
        result = 0
        length1 = len(num1)
        length2 = len(num2)
        for i, n1 in enumerate(num1):
            for j, n2 in enumerate(num2):
                result += (10 ** (length1 - i - 1) * int(n1) * 10 ** (length2 - j - 1) * int(n2))
        return str(result)


if __name__ == '__main__':
    # s = Solution()
    s = SolutionNew()
    assert s.multiply("2", "3") == "6"
    assert s.multiply("123", "456") == "56088"
