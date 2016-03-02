from bs4 import BeautifulSoup
import os, urllib.request

# 创建文件夹
path = os.getcwd()   	     # 获取此脚本所在目录
new_path = os.path.join(path,u'图片')
if not os.path.isdir(new_path):
    os.mkdir(new_path)


def page_loop():
    page = 1
    for x in range(10,50):
        url = 'http://www.3jy.com/egao/%d/3500%d.html' % (x,x)
        #print(url)
        '''
        webheader1 = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:23.0) Gecko/20100101 Firefox/23.0'}
        webheader2 = {
        'Connection': 'Keep-Alive',
        'Accept': 'text/html, application/xhtml+xml, */*',
        'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko',
        #'Accept-Encoding': 'gzip, deflate',
        'Host': 'baozoumanhua.com',
        'DNT': '1'
        } #伪装成浏览器
        req = urllib.request.Request(url=weburl, headers=webheader2)
        '''
        content = urllib.request.urlopen(url)
        soup = BeautifulSoup(content)  
        all_photo = soup.find_all('div',class_='content2')
        for photo in all_photo:
            jokes = photo.find('img')
            link = jokes.get('src')
            print(link)
            content = urllib.request.urlopen(link).read()
            with open(u'图片'+'/'+str(page)+'.jpg','wb') as code:
                code.write(content)
                page = page + 1
                
page_loop()

