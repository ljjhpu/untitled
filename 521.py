# class Solution:
#     def jumpFloor(self, number):
#         # write code here
#         if number == 1:
#             return 1
#         elif number == 2:
#             return 2
#         else :
#             res = self.jumpFloor(number - 1) + self.jumpFloor(number - 2)
#             return res


# 实现斐波那契数列
"""
1,2,3,5,8,13，........

"""
#
#
# def Fib(n):
#     if n == 1:
#         return 1
#     if n == 2:
#         return 2
#     return Fib(n - 1) + Fib(n - 2)
#
#
# print(Fib(5))


"""
题1：
    循环打印输入的月份的天数（使用continue实现）
    - 要有判断输入的月份是否错误的语句
"""


def InputDate():
    while True:
        year = int(input("请输入年："))
        month = int(input("请输入月："))
        monthLis = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
        if month in monthLis:
            date = int(input("请输入日："))
            print("{}年{}月{}日".format(year, month, date))
        else:
            print("输入月份错误！")


InputDate()
