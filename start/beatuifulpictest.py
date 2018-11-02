# -*- coding: UTF-8 -*-
from urllib import request
from bs4 import BeautifulSoup
import uuid
import time

# 目标抓取网页
src = 'http://www.mzitu.com/all'
# 浏览器请求头（大部分网站没有这个请求头可能会报错）
mheaders = {
    'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/22.0.1207.1 Safari/537.1"}


# 读取一个网页
def getHtml(url):
    req = request.Request(url, headers=mheaders)  # 添加headers避免服务器拒绝非浏览器访问
    page = request.urlopen(req)
    html = page.read()
    return html.decode('utf-8')  # python3 python2版本直接返回html


# 从入口爬取所有的目标链接
def getallUrl(html):
    # 构造一个bs对象
    soup = BeautifulSoup(html, 'html.parser')
    # 使用bs对象寻找class为all的div 然后再寻找这些div里面的a标签，可能我们需要多试几次才能准确的get
    all = soup.find('div', class_='all').find_all('a')
    print(len(all))  # 无聊打印点什么
    for li in all:
        subSrc = li.attrs['href']
        subHtml = getHtml(subSrc)
        subSoup = BeautifulSoup(subHtml, 'html.parser')
        page = subSoup.find('div', class_='pagenavi').find_all('span')
        # page[-2]是表示数组从右(末端数2个) maxpage拿到套图最后一页
        maxPage = page[-2].get_text()
        i = 1
        while (i <= int(maxPage)):
            time.sleep(0.08)  # 休息0.08s，防止服务器拒绝频繁请求
            tagetSrc = subSrc + '/' + str(i)
            tagetHtml = getHtml(tagetSrc)
            tagetSoup = BeautifulSoup(tagetHtml, 'html.parser')
            img = tagetSoup.find('div', class_='main-image').find('img')
            print(time.time())  # 无聊打印点什么
            # uuid()构造一个世界唯一字符串，为了防止文件重名
            name = img.attrs['alt'] + str(uuid.uuid4())
            imgsrc = img.attrs['src']
            print(imgsrc + "-----" + name)  # 无聊打印点什么
            try:
                # 这里的指定存储路径，需要注意的是这里需手动创建文件夹，如需自动想、可以使用os库
                request.urlretrieve(imgsrc, 'D:\\meizi\\' + '%s.jpg' % name)  # 指定目录位置
            except BaseException:
                # 捕获异常情况
                print('Error:there is something wrong!')
                # 遇到IOError: [Errno socket error] [Errno 10060]服务器拒绝频繁访问 阻塞1s
                time.sleep(1)
                try:
                    request.urlretrieve(imgsrc, 'D:\\meizi\\' + '%s.jpg' % name)  # 指定目录位置
                except BaseException:
                    print('Error:there is something wrong!over')
            # print(tagetSrc)
            i += 1
        print('end')


# 开始
print('begin')
getallUrl(getHtml(src))
# 结束
print('over')
