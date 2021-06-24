import os
import xlwt

# 创建一个workbook对象，相当于创建一个Excel文件
book = xlwt.Workbook(encoding='utf-8', style_compression=0)
'''
Workbook类初始化时有encoding和style_compression参数
encoding:设置字符编码，一般要这样设置：w = Workbook(encoding='utf-8')，就可以在excel中输出中文了。默认是ascii。
style_compression:表示是否压缩，不常用。
'''

# 创建一个sheet对象，一个sheet对象对应Excel文件中的一张表格。
sheet = book.add_sheet('Output', cell_overwrite_ok=True)
# 其中的Output是这张表的名字,cell_overwrite_ok，表示是否可以覆盖单元格，其实是Worksheet实例化的一个参数，默认值是False

# 向表中添加数据标题
sheet.write(0, 0, '中文名')  # 其中的'0-行, 0-列'指定表中的单元，'X'是向该单元写入的内容
sheet.write(0, 1, '外文名')
sheet.write(0, 2, '地理位置')
sheet.write(0, 3, '气候条件')
sheet.write(0, 4, '类别')
sheet.write(0, 5, '景点级别')
sheet.write(0, 6, '开放时间')
sheet.write(0, 7, '门票价格')
sheet.write(0, 8, '著名景点')
sheet.write(0, 9, '建议游玩时长')
sheet.write(0, 10, '适宜游玩季节')
sheet.write(0, 11, '景区类型')

with open('nationwide_5A_scenic_info.txt', 'r', encoding='utf-8') as fr, open('output.txt', 'w',
                                                                              encoding='utf-8') as fd:
    n = 1
    for text in fr.readlines():
        if '中文名' in text.split(' '):
            sheet.write(n, 0, text.split(' ')[1])
        if '外文名' in text.split(' '):
            sheet.write(n, 1, text.split(' ')[1:])
        if '地理位置' in text.split(' '):
            sheet.write(n, 2, text.split(' ')[1])
        if '气候条件' in text.split(' '):
            sheet.write(n, 3, text.split(' ')[1])
        if '类别' in text.split(' '):
            sheet.write(n, 4, text.split(' ')[1])
        if '景点级别' in text.split(' '):
            sheet.write(n, 5, text.split(' ')[1])
        if '开放时间' in text.split(' '):
            sheet.write(n, 6, text.split(' ')[1])
        if '门票价格' in text.split(' '):
            sheet.write(n, 7, text.split(' ')[1])
        if '著名景点' in text.split(' '):
            sheet.write(n, 8, text.split(' ')[1])
        if '建议游玩时长' in text.split(' '):
            sheet.write(n, 9, text.split(' ')[1])
        if '适宜游玩季节' in text.split(' '):
            sheet.write(n, 10, text.split(' ')[1])
        if '景区类型' in text.split(' '):
            sheet.write(n, 11, text.split(' ')[1])

        if text == '\n':
            n = n + 1

# 最后，将以上操作保存到指定的Excel文件中
book.save('Output.xls')
