import urllib.request
from bs4 import  BeautifulSoup
import datetime
import random
import re
import ssl

context = ssl._create_unverified_context()
header = {"User-Agent":"Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Mobile Safari/537.36"}

random.seed(datetime.datetime.now())
def getlinks(articleUrl):
    url = ("https://en.wikipedia.org"+articleUrl)
    request = urllib.request.Request(url, headers=header)
    print(url)
    html = urllib.request.urlopen(request, context=context)

    bsObj = BeautifulSoup(html, 'lxml')
    return bsObj.find("div", {"id":"bodyContent"}).find_all("a", herf=re.compile("^(/wiki/)((?!:).)*$"))
links = getlinks("/wiki/Kevin_Becon")
while len(links) > 0:
    newArticle = links[random.randint(0, len(links) - 1)].attrs["href"]
    print(newArticle)
    links = getlinks(newArticle)