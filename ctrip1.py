from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "http://www.lvmama.com/lvyou/scenery/select-340-t3.html"

    # 1.爬取网页
    datalist = getData(baseurl)
    savepath = ".\\携程西安景点.xls"
    # 3.保存数据
    saveData(datalist, savepath)
    # askURL("https://movie.douban.com/top250?start=")


# 景点名称
findName = re.compile(r'[^\x00-\xff]', re.S)  # 创建正则表达式对象，表示规则（字符串的模式）
# findName = re.compile(r'<img src="(.*?)"', re.S)  # 创建正则表达式对象，表示规则（字符串的模式）


# 景点地址
# findAdress = re.compile(r'<dd class="ellipsis">(.*?)</dd>', re.S)  # re.S 让换行符包含在字符中
# 评分
# findScore = re.compile(r'<strong>(.*)</strong>')
# 等级
# findLevel = re.compile(r'<dd>(.*?)<span class="fenline">|</span>', re.S)


# 爬取网页
def getData(baseurl):
    datalist = []
    for i in range(0, 1):
        # url = baseurl + "s0-p%d"
        html = askURL(baseurl)  # 保存获取的网页源码

        # 逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        # for item in soup.find_all('div', class_="ticket_price line_price com_dest_2"):
        for item in soup.find_all('div', class_="title"):
            # print(item)
            data = []
            item = str(item)
            # print(item)
            # break
            # 名称
            name = re.findall(findName, item)
            data.append(name)
            # 地址
            # adress = re.findall(findAdress, item)
            # data.append(adress)
            # 评分
            # score = re.findall(findScore, item)
            # data.append(score)
            # 等级
            # level = re.findall(findLevel, item)
            # data.append(level)

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
        # print(html)
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
    col = ("名称",)

    for i in range(0, 1):
        sheet.write(0, i, col[i])
    for i in range(0, 10):
        print("第%d条" % i)
        data = datalist[i]
        for j in range(0, 1):
            sheet.write(i + 1, j, data[j])
    book.save('lvmm5.xls')


if __name__ == '__main__':
    main()
