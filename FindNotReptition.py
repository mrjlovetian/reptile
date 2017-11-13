import urllib.request
from bs4 import BeautifulSoup
import re
import ssl

headers = {"user-agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"}
context = ssl._create_unverified_context()

pages = set()
def getLink(url, keyWork):
    global pages
    request = urllib.request.Request(url, headers=headers)
    html = urllib.request.urlopen(request, context=context)

    bsObj = BeautifulSoup(html, "lxml")
    # print(bsObj)
    for newUrl in bsObj.find_all("a", href=re.compile("(douban)+")):

        if "href" in newUrl.attrs:
            # print("********%s" % newUrl)
            if newUrl.attrs["href"] not in pages:
                # 找到新的页面
                print("----------------%s"%newUrl.attrs["href"])
                newPage = newUrl.attrs["href"]
                pages.add(newPage)
                getLink(newPage)

getLink("https://movie.douban.com/", "douban")