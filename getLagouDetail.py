# -*- codeing=uft-8 -*-
import urllib.request
from bs4 import BeautifulSoup
import ssl
import time

# 此方法用来添加请求头，伪装成浏览器，使用ssl访问https
url = 'https://www.lagou.com/zhaopin/3/?filterOption=3'
header = {'User-Agent':'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36'}
context = ssl._create_unverified_context()

for i in range(1, 50, 1):

    if i == 1:
        i = ""
    new_url = ('https://www.lagou.com/zhaopin/%s/?filterOption=3' %( i))
    print(new_url)
    res = urllib.request.Request(url, headers=header)
    html = urllib.request.urlopen(res, context=context)
    bsObj = BeautifulSoup(html, 'lxml')
    # 根据div来爬去所需要的数据
    for work_li in bsObj.find_all('li', class_='con_list_item default_list'):
        # 获得上半部分
        work_top = work_li.find('div', class_='list_item_top')
        work_name = work_top.find('h3').string
        work_address = work_top.find('em').string
        work_sendtime = work_top.find('span', attrs={'calss', 'format-time'}).string
        work_money = work_top.find('span', class_='money').string

        work_experience = work_top.find('div', attrs={'calss', 'li_b_l'}).contents[-1]
        company_name_a = work_top.find('div', class_='company_name')
        company_name = company_name_a.find('a').string

        compay_industry = work_top.find('div', class_='industry').string
        work_logo = work_top.find('img')['src']

        print('工作岗位:%s， 工作地址:%s， 发布时间:%s， 薪资:%s， 工作经验:%s， 公司名称:%s， 公司简介:%s， 公司LOGO:%s' %(work_name, work_address, work_sendtime, work_money, work_experience, company_name, compay_industry, work_logo))

        # 获得下半部分
        work_bottom = work_li.find('div', class_='list_item_bot')
        work_nices = work_bottom.find('div', class_='li_b_l').find_all('span')
        nice_str = ''
        for nice in work_nices:
            nice_str = nice_str + nice.string + ' '

        work_info = work_bottom.find('div', class_='li_b_r').string

        print('公司福利:%s， 公司说明:%s' % (nice_str, work_info))

        # 休眠一秒钟，不然抓不到数据
        time.sleep(1)


