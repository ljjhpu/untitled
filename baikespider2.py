'''
Created on 2017年12月15日
@filename: baiduInfoBox.py
@author: geng
'''
import time
import re
import os
import sys
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains

driver = webdriver.PhantomJS(executable_path=r'D:\sofeware\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\phantomjs-2.1.1-windows\bin\phantomjs.exe')
wait = ui.WebDriverWait(driver, 3)

global info


# 获取5A景区的infobox
def getInfoBox(name):
    global info
    # 创建文件
    basePathDir = "Tourist_spots_5A"
    if not os.path.exists(basePathDir):
        os.makedirs(basePathDir)
    baiduFile = os.path.join(basePathDir, "BaiduSpider.txt")
    if not os.path.exists(baiduFile):
        info = codecs.open(baiduFile, 'w', 'utf-8')
    else:
        info = codecs.open(baiduFile, 'a', 'utf-8')

    # 搜索百度百科
    driver.get("http://baike.baidu.com/")
    elem_inp = driver.find_element_by_xpath("//form[@id='searchForm']/input")
    elem_inp.send_keys(name)
    elem_inp.send_keys(Keys.RETURN)
    # info.write(name)
    time.sleep(2)
    # print(driver.title, ": ", driver.current_url)
    info.writelines(driver.title + ": " + driver.current_url + "\r\n")

    # 查找相关信息
    elem_names = driver.find_elements_by_xpath('//div[@class="basic-info cmn-clearfix"]/dl/dt')
    elem_values = driver.find_elements_by_xpath('//div[@class="basic-info cmn-clearfix"]/dl/dd')
    # 字典存储
    elem_vn = dict(zip(elem_names, elem_values))
    for key in elem_vn.keys():
        # print(key.text, ': ', elem_vn[key].text)
        info.writelines(key.text + ': ' + elem_vn[key].text + "\r\n")
    info.writelines("\r\n")
    info.close()
    time.sleep(2)


if __name__ == "__main__":
    source = open("TipsColumn.txt", 'r', encoding='UTF-8')
    for name in source:
        name = name.strip()
        getInfoBox(name)
    source.close()
    print("Over")
