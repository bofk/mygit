# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import time,urllib.request,os,sys
 
page = 1
fp=open('jokes.txt','w',encoding='gbk')           
url = 'http://www.jokeji.cn/jokehtml/bxnn/20090504133055.htm'
q=input('输入需要的笑话数量： 100？200？500？ 也可以更多...\n')        
while page < int(q):
    
    try:
        content= urllib.request.urlopen(url)
        soup = BeautifulSoup(content, "html.parser",from_encoding="gbk")
        soup.prettify()
        all = soup.find('div',class_='left_up')
        c = all.find_all('p')
        for x in c:
            page = page + 1
            print(x.get_text(),file=fp)
            print('\n',file=fp)            
        tz = soup.find('div',class_='zw_page1')
        tz1 = tz.find('a')
        tz2 = tz1.get('href')
        url = 'http://www.jokeji.cn/'+tz2[6:]
        print('一大波笑话来袭')
    except:
        tz = soup.find('div',class_='zw_page1')
        tz1 = tz.find('a')
        tz2 = tz1.get('href')
        url = 'http://www.jokeji.cn/'+tz2[6:]
        continue
    

 
print('你的笑话已就绪')    
fp.close()
input('哈哈哈\n\n\n-------输入任意键关闭--------')

