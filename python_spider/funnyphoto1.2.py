from bs4 import BeautifulSoup
import os, urllib.request

# 创建文件夹
path = os.getcwd()   	     # 获取此脚本所在目录
new_path = os.path.join(path,u'图片')
if not os.path.isdir(new_path):
    os.mkdir(new_path)

def page_loop():
    page = 0
    p=input('输入你想要的搞笑图片的数量：A.一点点 B.来一些 C.很多..(请输入字母)\n')
    if p == 'A':
        x = 20
    if p == 'B':
        x = 70
    if p == 'C':
        x = 300
    for x in range(1,int(x)):
        url = 'http://www.3jy.com/egao/%d/3500%d.html' % (x,x)
        content = urllib.request.urlopen(url)
        soup = BeautifulSoup(content,'html.parser')
        all_photo = soup.find_all('div',class_='content2')
        for photo in all_photo:
            jokes = photo.find('img')
            link = jokes.get('src')
            content = urllib.request.urlopen(link).read()
            with open(u'图片'+'/'+str(page)+'.jpg','wb') as code:
                code.write(content)
                page = page + 1
                print('一大波图片来袭')
    print('一共获得%d张图片' % page)
                
page_loop()
input('哈哈哈\n\n\n---------------按任意键退出-----------------')
