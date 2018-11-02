# coding=gbk
import requests
from bs4 import BeautifulSoup

r1 = requests.get('https://github.com/login')

soup = BeautifulSoup(r1.text, features='lxml')

s1 = soup.find(name='input', attrs={'name': 'authenticity_token'}).get('value')
r1_cookies = r1.cookies.get_dict()
print(r1_cookies)
print(s1)

r2 = requests.post(
    'https://github.com/session',
    data={
        'commit': 'Sign in',
        'utf8': '?',
        'authenticity_token': s1,
        'login': '1107313740@qq.com',
        'password': 'xiaoaina1129'
    },
    cookies=r1.cookies.get_dict(),
)

# 查看个人详情页

print(r2.cookies.get_dict())

r3 = requests.get(
    'https://github.com/13131052183/product',  # 查看个人的详情页
    cookies=r2.cookies.get_dict()

)
print('文本内容----------')
print(r3.text.encode('utf-8'))
