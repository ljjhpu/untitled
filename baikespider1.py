from bs4 import BeautifulSoup
import requests
import csv

# 初始化一个存放待爬取关键词的列表
keywordlist = []
# 打开文件
with open('qita.txt', 'r', encoding='UTF-8') as f:
    # 逐行读取要爬取的实体名
    for keyword in f.readlines():
        keyword = keyword.strip("\n")
        keywordlist.append(keyword)
print(keywordlist)


def getHTMLText(url):
    i = 0
    while i < 3:  # 最大重连次数为3
        try:
            # 构造headers，user-agent看上述获取方法
            headers = {
                "User-Agent": "Mozilla/5.0(Windows NT 10.0;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/86.0.4240.111Safari/537.36"}
            r = requests.get(url, headers=headers, timeout=5)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            soup = BeautifulSoup(r.text, 'html.parser')
            return soup
        except requests.exceptions.RequestException:
            i += 1
    return 0


for keyword in keywordlist:
    url = 'http://baike.baidu.com/search/word?word=' + keyword
    objSoup = getHTMLText(url)
    # 找标题
    title = objSoup.find('h1')
    title = title.get_text()
    title = "".join(title.split())
    # 找属性名
    attr = objSoup.find_all('dt', class_="basicInfo-item name")
    # 找属性值
    info = objSoup.find_all('dd', class_="basicInfo-item value")  # 找到所有dd标签，返回一个列表

attrlist = []
infolist = []
titlelist = []
for i in attr:
    t = i.get_text()
    t = "".join(t.split())  # 去除空白符
    attrlist.append(t)
    titlelist.append(title)  # 重复title
for j in info:
    n = j.get_text()
    n = "".join(n.split())
    infolist.append(n)
# 文件写入方式为在文件后继续写内容，而不覆盖原有内容，故选择'a'这种打开方式。
with open('qita.csv', 'a', newline='')as f:
    writer = csv.writer(f)
    writer.writerows(zip(titlelist, attrlist, infolist))
