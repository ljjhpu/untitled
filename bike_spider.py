from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://baike.baidu.com/item/%E5%8D%8E%E5%B1%B1/198"

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\携程西安景点.xls"
    # 3.保存数据
    saveData(datalist, savepath)


# 景点名称
# [^\x00-\xff]
findName = re.compile(r'<dt class="basicInfo-item name">(.*?)</dt>')  # 创建正则表达式对象，表示规则（字符串的模式）

findValue = re.compile(r'[A0-9_\u4e00-\u9fa5]')


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        # url = baseurl + "s0-p%d"
        html = askURL(baseurl)  # 保存获取的网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")

        data = []
        for item in soup.find_all('dt', class_="basicInfo-item name"):
            item = str(item)

            # 名称
            name = re.findall(findName, item)
            data.append(name)

            datalist.append(data)

        for item in soup.find_all('dd', class_="basicInfo-item value"):
            item = str(item)

            # 属性值
            val = re.findall(findValue, item)
            data.append(val)

            datalist.append(data)

    print(datalist)
    return datalist


# 得到一个指定的URL的网页内容

def askURL(url):
    # 模拟浏览器头部信息，向豆瓣服务器发送消息
    head = {
        "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.111Safari/537.36"
    }
    # 用户代理：表示告诉豆瓣服务器我们是什么类型的机器，浏览器（本质上是告诉服务器，我们可以接收什么水平的信息）

    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)

    return html


# 保存数据
def saveData(datalist, savepath):
    print("save............")
    book = xlwt.Workbook(encoding="utf-8", style_compression=0)
    sheet = book.add_sheet("携程西安景点", cell_overwrite_ok=True)
    # col = ("名称", "地址", "评分", "等级")
    col = ("名称", "值")

    for i in range(0, 2):
        sheet.write(0, i, col[i])
    for i in range(0, 1):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 20):
            sheet.write(i + 1, j, data[j])
        for j in range(0, 20):
            sheet.write(i + 2, j, data[20 + j])
    book.save('baike222.xls')


if __name__ == '__main__':
    main()
