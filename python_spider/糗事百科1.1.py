#抓取糗事百科段子

from bs4 import BeautifulSoup
import re, os, time, urllib.request


def funtext():
    need=int(input('你需要多少段子呢？\n'))
    page = 0
    funny = open('fun.txt','w')
    for x in range(1,30):
        url = 'http://www.qiushibaike.com/8hr/page/%d/?s=4852675'% x  #伪装浏览器
        headers = ('User-Agent','Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER')
        opener = urllib.request.build_opener()
        opener.addheaders = [headers]
        content= opener.open(url).read()
        soup = BeautifulSoup(content,'html.parser')
        main_jokes = soup.find('div',class_='main')
        jokes = main_jokes.find_all('div',class_='article block untagged mb15')
        for joke in jokes:
            try:
                if joke.find('div',class_='thumb') is None:
                    j = joke.find('div',class_='content')
                    page = page + 1
                    print('%d '%page,file=funny,end='')
                    print(j.get_text().strip(),file=funny)
                    print('\n',file=funny)
                    print('一大波段子正在接近...')
                    time.sleep(0.2)
                    if need == page:
                        break
            except:
                continue
        if need == page:
            break

    if need > page:
        print('很遗憾,段子不够了....')
    if need == page:
        print('你的段子已准备完毕...')
    funny.close()

funtext()

i=input('--------------输入任意键关闭---------------')