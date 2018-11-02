# coding=gbk
from bs4 import BeautifulSoup
import requests

url = 'http://www.weather.com.cn/textFC/hb.shtml'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.9 Safari/537.36',
    'charset': 'utf-8',
    'Referer': 'http://www.weather.com.cn/textFC/hb.shtml'
}

res = requests.get(url=url, headers=headers)
res.encoding = 'utf-8'

soup = BeautifulSoup(res.text, 'lxml')

for div in soup.select('div.conMidtab2'):
    for tr in div.select('tr'):
        if tr.find('td', width='83'):
            if tr.find('td', width='83').a:
                print(tr.find('td', width='83').a.string)

                if tr.find('td', width='89'):
                    print('���磺', end=',')
                    print(tr.find('td', width='89').string, end=',')  # ����
                    print(tr.find('td', width='162').contents[1].string, end=',')  # ��������
                    print(tr.find('td', width='162').contents[3].string, end=',')  # ��������
                    print('����¶�' + tr.find('td', width='92').string, end=',')  # ����¶�
                    print('���ϣ�')
                    print(tr.find('td', width='98').string, end=',')  # ����
                    print(tr.find('td', width='177').contents[1].string, end=',')  # ��������
                    print(tr.find('td', width='177').contents[3].string, end=',')  # ��������
                    print('����¶�' + tr.find('td', width='86').string)  # �������
                    print('*****************')
            else:
                continue
