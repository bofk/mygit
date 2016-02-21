import urllib.request as request  
import urllib.parse as parse  
import string

def baidu_tieba(url, begin_page, end_page):  
    for i in range(begin_page, end_page + 1):  
        sName = 'd:/images/'+str(i)+'.html'  #保存的地址
        print('正在下载第'+str(i)+'个页面, 并保存为'+sName)  
        m = request.urlopen(url+str(i)).read()  
        with open(sName,'wb') as file:  
            file.write(m)  #下载网页内容 
if __name__ == "__main__":  
    url = "http://www.quanmin.tv/star/"  #目标网址
    begin_page = 666
    end_page = 668
    baidu_tieba(url, begin_page, end_page) 
