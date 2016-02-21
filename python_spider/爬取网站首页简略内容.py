#-*- coding: utf-8 -*-  
#-------------------------------------  
#version: 0.1  
#note:实现了查找0daydown最新发布的10页资源。  
#-------------------------------------  
#-------------------------------------  
#version: 0.2  
#note:在v0.1基础上输出内容到一个指定TXT文件中  
#-------------------------------------  
  
import urllib.request  
import sys  
  
from bs4 import BeautifulSoup  
  
old = sys.stdout        #保存系统默认输出  
#fp = open("test1.txt",'w')  
fp = open("test1.txt",'w', encoding="utf-8")    #以utf-8进行文件编码  
sys.stdout = fp         #输出重定向到一个文件中  
  
for i in range(1,11):  
    url = "http://www.0daydown.com/page/" + str(i)  #每一页的Url只需在后面加上整数就行  
    page = urllib.request.urlopen(url)  
    soup_packtpage = BeautifulSoup(page,'html.parser')
    page.close()  
    num = " The Page of: " + str(i)     #标注当前资源属于第几页  
    print(num)  
    print("#"*40)  
    for article in soup_packtpage.find_all('article', class_="excerpt"):    #使用find_all查找出当前页面发布的所有最新资源  
        print("Category:".ljust(20), end=''), print(article.header.a.next)   #category  
        print("Title:".ljust(20), end=''), print(article.h2.string)       #title      
        print("Pulished_time:".ljust(19), end=''), print(article.p.find('i', class_="icon-time icon12").next)  #published_time  
        print("Note:", end='')  
        print(article.p.find_next_sibling().string)    #note  
        print('-'*50)  
  
fp.close()  
sys.stdout = old    #恢复系统默认输出  
print("Done!")  
input() #等待输入，为了不让控制台运行后立即结束
