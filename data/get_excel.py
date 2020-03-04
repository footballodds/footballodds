# from django.test import TestCase

# Create your tests here.
# import requests, re
# from lxml import etree
# import time
# url = 'http://landing-sb.188sbk.com/zh-cn/Service/CentralService'
#
# headers = {
#     "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
#     "Accept-Encoding": "gzip, deflate",
#     "Accept-Language": "zh-CN,zh;q=0.9",
#     # "Connection": "keep-alive",
#     # "Content-Length": "25",
#     # "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
#     # "Host": "landing-sb.188sbk.com",
#     # "Cookie": "JSESSIONID=7FE3D1F9A78DB03F2C5D49090F024A75",
#     # "Origin": "http://landing-sb.188sbk.com",
#     # "Referer": "http://landing-sb.188sbk.com/zh-cn/sports/football/in-play/full-time-asian-handicap-and-over-under",
#     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.130 Safari/537.36",
#     "X-Requested-With": "XMLHttpRequest",
#
# }
#
# page_text = requests.post(url=url, headers=headers,data=data).text
# print(page_text)
# # tree = etree.HTML(page_text)
# print(round(time.time()*1000))


import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import os
import time
from lxml import etree


def startDriver():  # 启动chrome浏览器
    # 构造模拟浏览器
    chromedriver = "C:/Program Files (x86)/Google/Chrome/Application/chromedriver"  # 驱动所在路径
    os.environ["webdriver.chrome.driver"] = chromedriver
    driver = webdriver.Chrome(chromedriver)  # 模拟打开浏览器
    time.sleep(2)
    return driver


def getDatenumber(url):  # 获取主页中的赛事日期和赛事编号
    r = requests.get(url)
    r.raise_for_status()
    r.encoding = r.apparent_encoding
    html = r.text
    soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    tag = soup.find_all('table', attrs={"class": {"eventTable"}})
    # tag1 = tag.find_all('th',attrs={"class": "th-score"})
    print(tag)
    # dateNumber = []
    # for i in range(len(tag1)):
    #     tag2 = tag1[i].find_all('span')
    #     try:
    #         info = tag2[0].text + tag2[1].text  # 获取标中的内容
    #     except:
    #         break
    #     dateNumber.append(info)
    # del dateNumber[-1]
    # return dateNumber


def getHTML(driver, url, xpath):  # 模拟浏览器打开网页，并获得最新窗口中的网页
    driver.get(url)  # 打开网址
    # 模拟点击更多评论
    time.sleep(2)
    driver.find_element_by_xpath(xpath).click()
    time.sleep(10)
    driver.switch_to_window(driver.window_handles[-1])  # 跳转到当前窗口
    html = driver.page_source
    return html


def getTableName(html):  # 获取每个table的表名
    tree = etree.HTML(html)
    lis = tree.xpath(
        "/html/body")
    all_data_list = []

    # for i in range(len(lis)):
    #     time = lis[i].xpath('.//th[@class="th-score"]/span//text()')
    #     if time == []:
    #         continue
    #     else:
    #         fav = lis[i].xpath(
    #             './/tbody[@class="selectionHover"]/tr[@class=" fav"]/td[@class="td-teameName amkt h-amkt pd-l-12"]//text()')[
    #             0]
    #         fav_odds = \
    #         lis[i].xpath('.//tbody[@class="selectionHover"]/tr[@class=" fav"]/td[@class="td-odds-1x2"]/span//text()')[0]
    #
    #         away = lis[i].xpath(
    #             './/tbody[@class="selectionHover"]/tr[@class=""]/td[@class="td-teameName amkt h-amkt pd-l-12"]//text()')[
    #             0]
    #         away_odds = \
    #         lis[i].xpath('.//tbody[@class="selectionHover"]/tr[@class=""]/td[@class="td-odds-1x2"]/span//text()')[0]
    #
    #         # peace = lis[i].xpath('.//tbody[@class="selectionHover"]/tr/td[@class="td-teameName amkt h-amkt pd-l-12"]//text()')[0]
    #         peace_odds = \
    #         lis[i].xpath('.//tbody[@class="selectionHover"]/tr/td[@class="td-odds-1x2"]/span[@title="和局"]//text()')[0]
    #         dic = {
    #             "time": time[0].replace(" ", "") + "/" + time[1].replace(" ", ""),
    #             fav: fav_odds,
    #             away: away_odds,
    #             "和局": peace_odds
    #         }
    #         all_data_list.append(dic)
    # print(all_data_list, len(all_data_list))

    # soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    # tag = soup.find_all('div', attrs={'class': {'cp-container'}})
    #
    # div_event=tag[0].find_all('div',attrs={'class':{'event'}})
    # game_info={}
    # for event in div_event:
    #     # 比赛时间
    #     spanTh_date = event.find_all('span', attrs={'class': {'date'}})
    #     spanTh_eventTime = event.find_all('span', attrs={'class': {'eventTime'}})
    #     # 主方
    #     fav=event.find_all('tr',attrs={'class':{'far'}})
    #     pri_fav=fav.find_all('td',attrs={'class':{'td-teameName amkt h-amkt pd-l-12'}}).text
    #     # 赔率
    #     pri_odds=fav.find_all('span',attrs={'class':{'odds'},'title':{pri_fav}}).text
    #     # 反方
    #     fav_one = event.find_all('tr', attrs={'class': {''}})
    #     one_fav = fav_one.find_all('td',attrs={'class':{'td-teameName amkt h-amkt pd-l-12'}}).text
    #     one_fav_odds=fav_one.find_all('span',attrs={'class':{'odds'},'title':{one_fav}}).text
    #
    #     game_info['time'] = spanTh_date.text.replace(" ", "") + " " + spanTh_eventTime.text.replace(" ", "")
    #     game_info[pri_fav]=pri_odds
    #     game_info[one_fav]=one_fav_odds
    # print(game_info)
    # print('表',tag[1])
    # spanTh_date = tag[1].find_all('span', attrs={'class': {'date'}})
    # spanTh_eventTime = tag[1].find_all('span', attrs={'class': {'eventTime'}})
    # print(spanTh_date[0].text.replace(" ", ""), spanTh_eventTime[0].text.replace(" ", ""))
    tableName = []
    # for infoi in tag:
    #     tableName.append(infoi.text.replace("\n", "").replace(" ", ""))
    # return tableName


def fillUnivlist(driver, url):  # 保存网页中间两个表格的内容
    # dateNumbers = getDatenumber(url)
    result = []
    count = 0
    xpath = "/html"  # 表单列表
    html = getHTML(driver, url, xpath)  # 获取HTML
    print(html)
    # tableNames = getTableName(html)  # 获取表名
    # soup = BeautifulSoup(html, 'html.parser')  # 用HTML解析网址
    # tag = soup.find_all('table', attrs={'class': {'eventTable'}})  # 获取所有表格
    # # print(str(tag[0]))
    # for i in range(len(tag)):
    #     infoTag = tag[i]
    #     contentTr = infoTag.find_all('tr')
    #     for j in range(len(contentTr)):
    #         if j == 0:
    #             contentTh = contentTr[j].find_all('span')
    #             info1 = contentTh[0].text + "/" + contentTh[1].text
    #         else:
    #             contentTd = contentTr[j].find_all('td')
    #             info1 = dateNumbers[0] + "," + tableNames[i]
    #             for infok in contentTd:
    #                 info1 = info1 + "," + infok.text
    #         result.append(info1)
    # count += 1
    # print("\r当前页进度: {:.2f}%".format(count * 100 / len(dateNumbers)), end="")
    # return result


def writeUnivlist(result, fpath, num):
    with open(fpath, 'a', encoding='utf-8') as f:  # 以追加的方式存储内容
        for i in range(num):
            f.write(result[i] + '\n')
        f.close()


def main():
    driver = startDriver()
    url = "https://www.838365.com/#/AC/B1/C1/D14/E0/F2/J0/Q1/F^12/"  # 要访问的网址
    xpath = '/html/body/div[3]/div/section/section/div[1]/div[3]/div[2]/div/div/div[2]/div/div[1]/table'
    result = fillUnivlist(driver, url)
    driver.close()
    time.sleep(2)


if __name__ == '__main__':
    main()
