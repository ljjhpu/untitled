import os
import time
import codecs
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium.webdriver.support.ui as ui

global info  # 全局变量
driver = webdriver.Chrome(executable_path="C:\Program Files\Google\Chrome\Application\chromedriver.exe")


def getInfo(name):
    try:
        # 创建路径和文件
        global info
        basePath = "scenic_spots_5A"
        if not os.path.exists(basePath):
            os.makedirs(basePath)
        # scenicFile = os.path.join(basePath, "nationwide_introduc2.txt")
        scenicFile = os.path.join(basePath, "nationwide_introduc_test.txt")
        if not os.path.exists(scenicFile):
            info = codecs.open(scenicFile, 'w', 'utf-8')
        else:
            info = codecs.open(scenicFile, 'a', 'utf-8')
        driver.get("https://www.ctrip.com/")
        # elem_input = driver.find_element_by_xpath("//input[@id='_allSearchKeyword']")
        # driver.find_element_by_id("kw").send_keys("selenium")
        # driver.refresh()
        elem_input = driver.find_element_by_id("_allSearchKeyword")

        name = name.rstrip('\n')  # 景点名称是从文件中读取的，含有换行符（最后一行的景点名称可能不含护身符）
        elem_input.send_keys(name)
        elem_input.click()
        elem_input.send_keys(Keys.RETURN)

        # driver.switch_to.window(driver.window_handles[0])

        info.write(name + '\r\n')  # codecs不支持'\n'换行
        time.sleep(2)
        driver.switch_to.window(driver.window_handles[-1])
        time.sleep(3)
        print(driver.current_url)
        print(driver.title)
        # elem_name = driver.find_elements_by_xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dt")
        # elem_value = driver.find_elements_by_xpath("//div[@class='basic-info J-basic-info cmn-clearfix']/dl/dd")
        elem_name = driver.find_elements_by_xpath("//*[@id='__next']/div[3]/div/div[4]/div[1]/div[2]/div/div[1]")
        elem_value = driver.find_elements_by_xpath(
            "//*[@id='__next']/div[3]/div/div[4]/div[1]/div[2]/div/div[2]/div/div/p[1]",)

        # create dictionary key-value
        # 字典是一种散列表结构,数据输入后按特征被散列,不记录原来的数据,顺序建议元组
        elem_dic = dict(zip(elem_name, elem_value))
        for key in elem_dic:
            print(key.text, elem_dic[key].text)
            info.writelines(key.text + " " + elem_dic[key].text + '\r\n')
        time.sleep(10)  # 让程序停5秒，以便把信息写入文件
    except Exception as e:
        print("Error: ", e)
    finally:
        print('\n')
        info.write('\r\n')  # 每篇信息之后，多一行空行


def main():
    global info
    source = open("nationwide_introduc_lis_test.txt", 'r')
    for name in source:
        getInfo(name)
    print('End Read Files!')
    time.sleep(5)
    source.close()
    info.close()
    driver.close()


main()
