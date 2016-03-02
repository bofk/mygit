import os,time,urllib.request
from bs4 import BeautifulSoup

path = os.getcwd()
new_path = os.path.join(path,u'百思不得姐')
if not os.path.isdir(new_path):
    os.mkdir(new_path)

def sip_video():
    if not os.path.isdir(new_path+'/视频'):
        os.mkdir(new_path+'/视频')
    url ='http://www.budejie.com'
    headers=('User-Agent','Mozilla/5.0 (windows NT 6.1 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    contents = opener.open(url).read()
    soup = BeautifulSoup(contents,'html.parser')
    content = soup.find_all('div',class_='j-r-list-c')
    for con in content:
        try:
            video = con.find('div',class_='j-video')
            if video is None:
                continue
            else:
                x = con.find('div',class_='j-r-list-c-desc').string.strip()
                mp4 = video.get('data-mp4')
                if not os.path.exists('百思不得姐/视频/'+x+'.mp4'):
                    urllib.request.urlretrieve(mp4,'百思不得姐/视频/'+x+'.mp4')
                    print('视频来啦..........')
                    time.sleep(0.5)

        except:
            continue

def sip_image():
    if not os.path.isdir(new_path+'/图片'):
        os.mkdir(new_path+'/图片')
    url ='http://www.budejie.com'
    headers=('User-Agent','Mozilla/5.0 (windows NT 6.1 AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1547.66 Safari/537.36 LBBROWSER')
    opener = urllib.request.build_opener()
    opener.addheaders = [headers]
    contents = opener.open(url).read()
    soup = BeautifulSoup(contents,'html.parser')
    content = soup.find_all('div',class_='j-r-list-c')
    for con in content:
        try:
            image = con.find('div',class_='j-r-list-c-img')
            if image is None:
                continue
            else:
                x = con.find('div',class_='j-r-list-c-desc').string.strip()
                png = con.find('img').get('data-original')
                if not os.path.exists('百思不得姐/图片/'+x+png[-4:]):
                    urllib.request.urlretrieve(png,'百思不得姐/图片/'+x+png[-4:])
                    print('图片来啦..........')
                    time.sleep(0.5)
        except:
            continue

print('百思不得姐爆笑视频、图片\n')
try:
    i = input('a.视频 \nb.图片\n(please input a or b)\n')

    if i == 'b':
        sip_image()


    if i == 'a':
        sip_video()
except:
    pass

input('--------------输入任意键关闭--------------')

