# # """
# # 字符串有三种编辑操作:插入一个字符、删除一个字符或者替换一个字符。
# # 给定两个字符串，编写一个函数判定它们是否只需要一次(或者零次)编辑。
# #
# # 示例 2:
# #
# # 输入:
# # first = "pale"
# # second = "ple"
# # 输出: True
# #
# # 示例 2:
# #
# # 输入:
# # first = "pales"
# # second = "pal"
# # 输出: False
# #
# # """
# #
# #
# # class Solution:
# #     def oneEditAway(self, first: str, second: str) -> bool:
# #         # 编辑距离为1时：
# #         # 插入字符串或者删除字符串意味着两个字符串长度相差1
# #         # 替换字符意味着长度相等
# #         # 编辑距离为0时：两字符串相等
# #         if first == second:
# #             return True
# #         if abs(len(first) - len(second)) > 1:
# #             return False
# #
# #         i, j, count = 0, 0, 0  # 设置指针和相异数统计变量
# #         if len(first) == len(second):
# #             while i < len(first):
# #                 if first[i] != second[j]:
# #                     count += 1
# #                     if count > 1:
# #                         return False
# #                 i += 1
# #                 j += 1
# #         else:
# #             if len(first) < len(second):
# #                 first, second = second, first
# #             while i < len(first) and j < len(second):
# #                 if first[i] != second[j]:
# #                     count += 1
# #                     if count > 1:
# #                         return False
# #                     i += 1
# #                 else:
# #                     i += 1
# #                     j += 1
# #             if i < len(first):  # 较长字符串的指针若没有完整的遍历一次，count+1
# #                 count += 1
# #
# #         return count <= 1
#
#
# class Solution(object):
#     def oneEditAway(self, first, second):
#         """
#         :type first: str
#         :type second: str
#         :rtype: bool
#         """
#         # 两个字符串长度大于2
#         if abs(len(first)-len(second)) >= 2:
#             return False
#         # 把长的换到first
#         if len(first) < len(second):
#             first, second = second,first
#         # 如果两字符串相等，比较每一个字符
#         if len(first) == len(second):
#             temp = 0
#             for i in range(len(second)):
#                 if first[i] != second[i]:
#                     temp += 1
#                 if temp > 1:
#                     return False
#             if temp < 2:
#                 return True
#         else:
#             for i in range(len(first)):
#                 if (first[0:i] + first[i+1:]) == second[:]:
#                     return True
#             else:
#                 return False


# def compressString(S: str) -> str:
# 1.遍历数组进行压缩
# 1.1 定义一个字典dic_S
# 1.2对数组进行遍历，使用字典存储字符串的数据，key为字符，value为字符的个数
# 1.3取出字典中的数据并将其拼接为一个字符串
# 2.比较压缩前后的字符串的长度大小
#     dic_S = {}
#     ret_S = ""
#     count = 0
#
#     for i in range(len(S)-1):
#         if S[i] == S[i+1]:
#             count += 1
#         else:
#             ret_S += S[i] + str(count)
#
#     if len(S) > len(ret_S):
#         return ret_S
#     else:
#         return S
#
# S = "aabcccccaaa"
# ret = compressString(S)
# print(ret)

#
# def compressString(S):
#     if not S:
#         return ''
#     count = 1
#     ret = ""
#     cur_char = S[0]
#     for char in S[1:]:
#         if char == cur_char:
#             count += 1
#         else:
#             ret += cur_char + str(count)
#             count = 1
#             cur_char = char
#     ret += cur_char + str(count)
#     if len(ret) > len(S):
#         return S
#     else:
#         return ret
#
# S = "aabcccccaaa"
# ret = compressString(S)
# print(ret)

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
"""
1.如何遍历二维数组
2.将二维中的每一列倒叙排列在相对应的那一行
row : 行
column ： 列
"""

# class Solution:
#     def rotate(self, matrix: List[List[int]]) -> None:
#         """
#         Do not return anything, modify matrix in-place instead.
#         """
#         length = len(matrix)
#         # 先在纵向上进行上下翻转
#         # 切片会创建新的对象进而开辟新地址
#         matrix[:] = matrix[::-1]
#         # 然后沿对角线翻转
#         for i in range(length):
#             for j in range(i):
#                 matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


# 冒泡排序
# def MaP(lis):
#     for j in range(len(lis) - 1):
#         for i in range(len(lis) - 1):
#             if lis[i] > lis[i + 1]:
#                 lis[i], lis[i + 1] = lis[i + 1], lis[i]
#         print(lis)
#
#
# numlis = [10, 1, 35, 61, 89, 36, 55]
# MaP(numlis)

# 选择排序
# def XuZe(lis):
#     for i in range(len(lis) - 1):
#         min = lis[i]
#         for j in range(i + 1, len(lis) - 1):
#             if lis[j] < min:
#                 min = lis[j]
#             minIndx = j
#         lis[i], lis[minIndx] = lis[minIndx], lis[i]
#     print(lis)


# def SelecSort(lis):
#     for i in range(len(lis) - 1):
#         maxIndex = i
#         for j in range(i + 1, len(lis)):
#             if lis[maxIndex] > lis[j]:
#                 maxIndex = j
#         if i != maxIndex:
#             lis[i], lis[maxIndex] = lis[maxIndex], lis[i]
#         print(lis)
#
#
# numlis = [20, 40, 30, 10, 60, 50]
# print(SelecSort(numlis))

# a = [1, 2, 3]
# b = [4, 5, 6]
# a.extend(b)
# print(a)

# nulis = [30, 40, 60, 10, 20, 50]
# print(QuickSort(nulis))
"""
快速排序
"""
# def quick_sort(lst):
#     def partition(lst, left, right):
#         povit_value = lst[left]
#         while left < right:
#             while left < right and lst[right] >= povit_value:
#                 right -= 1
#             lst[left] = lst[right]
#
#             while left < right and lst[left] <= povit_value:
#                 left += 1
#             lst[right] = lst[left]
#         lst[left] = povit_value
#         return left
#
#     def q_sort(lst, left, right):
#         if left >= right:
#             return
#         pivot_key = partition(lst, left, right)
#         q_sort(lst, left, pivot_key - 1)
#         q_sort(lst, pivot_key + 1, right)
#
#     if not lst or len(lst) == 0:
#         return lst
#     q_sort(lst, 0, len(lst) - 1)
#     return lst
#
#
# nulis = [30, 40, 60, 10, 20, 50]
# print(quick_sort(nulis))

"""
插入排序
"""


# def InsertSort(lis):
#     for i in range(1, len(lis)):
#         j = i-1
#         temp = lis[i]
#         while j >= 0:
#             if lis[j] > temp:
#                 lis[j+1] = lis[j]
#                 lis[j] = temp
#             j -= 1
#     return lis
#
#
# nulis = [30, 40, 60, 10, 20, 50]
# print(InsertSort(nulis))

# lines = sys.stdin.readlines()
# lines = sys.stdin.readlines()
# n = int(lines[0])
# x1 = list(map(int, lines[1].split()))  # 分割字符串，以空格进行分割
# x2 = list(map(int, lines[2].split()))
# x3 = list(map(int, lines[3].split()))
# print(n, x1, x2, x3)

# y = "1 5 6"
# y1 = y.split()
# y11 = list(map(int,y1))
# print(y1)
# print(y11)

# x = "1 5"
# x1 = x.split()
# x11, x12 = map(int, x1)
# print(x11, x12)

# 多行输入格式
# lines = sys.stdin.readlines()
# n = int(lines[0])
# x1 = list(map(int, lines[1].split()))
# x2 = list(map(int, lines[2].split()))
# x3 = list(map(int, lines[3].split()))
# print(n, x1, x2, x3)

# 单行输入
# line = sys.stdin.readline()
# n, m = map(int, line.split())
# print(n, m)

# class ListNode(object):
#     pass
#
#
# class Solution:
#     def reverseList(self,head:ListNode) ->ListNode:
#         stack = []
#         if not head:
#             return head
#         # 将链表中的值放入栈中
#         while head:
#             stack.append(head.val)
#             head = head.next
#         # 取出栈中的最后一个值为头结点
#         cur = ListNode(stack.pop())
#         # 记住头部的索引
#         res = cur
#         # 依次从栈中取出
#         while stack:
#             res.next = ListNode(stack.pop())
#             res = res.next
#         return cur

# class ListNode(object):
#     pass
#
#
# class Solution:
#     def reverseList(self, head: ListNode) -> ListNode:
#         def recur(cur, pre):
#             if not cur: return pre  # 终止条件
#             res = recur(cur.next, cur)  # 递归后继节点
#             cur.next = pre  # 修改节点引用指向
#             return res  # 返回反转链表的头节点
#
#         return recur(head, None)  # 调用递归并返回

# class ListNode(object):
#     pass
#
#
# def mergeTwoList(l1,l2):
#     dum = cur = ListNode
#     while l1 and l2:
#         if l1.var < l2.val:
#             cur.next = l1
#             l1 = l1.next
#         else:
#             cur.next = l2
#             l2 = l2.next
#         cur = cur.next
#     cur.next = l1 if l1 else l2
#     return dum.next

# class CQueue:
#     def __init__(self):
#         self.A, self.B = [], []
#
#     def appendTail(self, value: int):
#         self.A.append(value)
#
#     def deleteHead(self):
#         if self.B: return self.B.pop()
#         if not self.A: return -1
#         while self.A:
#             self.B.append(self.A.pop())
#         return self.B.pop()

# def MergeTwoArr(arr1, arr2):
#     arr = []
#     count = 0
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             arr.append(arr1[i])
#             i += 1
#             count += 1
#         else:
#             arr.append(arr2[j])
#             j += 1
#             count += 1
#         if count == 10:
#             print(arr[9])
#             break

# arr11 = [1, 3, 4, 6, 6, 9, 11, 13, 15, 16]
# arr22 = [2, 3, 5, 6, 7, 10, 12, 13, 14, 18]
# MergeTwoArr(arr11, arr22)

# def MergeTwoArr(arr1, arr2):
#     arr = []
#     i, j = 0, 0
#     while i < len(arr1) and j < len(arr2):
#         if arr1[i] <= arr2[j]:
#             arr.append(arr1[i])
#             i += 1
#         else:
#             arr.append(arr2[j])
#             j += 1
#
#     if i == len(arr1):
#         arr = arr + arr2[j:]
#         # arr.extend(arr2[j:])
#     if j == len(arr2) - 1:
#         arr = arr+arr1[i:]
#
#     print(arr)
#
#
# arr11 = [1, 3, 4, 6, 6, 9, 11, 13, 15, 16]
# arr22 = [2, 3, 5, 6, 7, 10, 12, 13, 14, 18,19]
# MergeTwoArr(arr11, arr22)

# class ListNode:
#     def __init__(self, val, next):
#         self.val = val
#         self.next = next
#
#
# def CycleList(head: ListNode):
#     seen = set()
#     while head:
#         if head in seen:
#             return False
#         seen.add(head)
#         head = head.next
#     return False
#
#
# ListN = [3, 2, 0, -4, 2]
# CycleList(ListN)

testlis = []
text = '中文名 北京故宫博物院'
if '中文名' in text.split(' '):
    testlis.append(str)

print(testlis[1])
# test = text.split(' ')
# print(test)
