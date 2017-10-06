# reptile

```
import urllib.request
import ssl
from bs4 import BeautifulSoup
import time

num = 1 # 用来计数的一共有多少书
start_time = time.time() # 计算爬虫的时间

url = 'https://read.douban.com/columns/category/all?sort=hot&start='

for i in range(0, 10, 10): # 这里的range(初始， 结束， 间隔)
    # urllib.request库用来网络请求的
    # ssl用来请求https的
    context = ssl._create_unverified_context()
    html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i, context=context)
    # html = urllib.request.urlopen('https://read.douban.com/columns/category/all?sort=hot&start=%d' % i)
    # BeautifulSoup用来解析网页
    bsobj = BeautifulSoup(html, 'lxml')
    # 根据类来查找标签（attrs={'calss', 'item store-item'} 可用 class_ ='item store-item'代替 ）
    li_list = bsobj.find_all('li', attrs={'calss', 'item store-item'})
    for li_node in li_list:
        node = li_node.find('div', attrs={'class', 'info'})


        h_div = node.find('h4', attrs={'class', 'title'}) #获得标题
        h_a = h_div.find('a').contents[0]

        h5_subtitle = node.find('h5', attrs={'class', 'subtitle'})
        suntitle = ''
        if h5_subtitle is not None:
            suntitle = h5_subtitle.contents[0]


        h_intro = node.find('div', attrs={'class', 'intro'})
        intro = h_intro.contents[0]

        print('得到的url', h_a, suntitle, intro)
    time.sleep(1)
    num += 1

end_time = time.time()
duration_time = end_time - start_time
print('运行时间%d', duration_time)
```

