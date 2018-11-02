# coding=gbk
# ! /usr/bin/env python


'''

��ȡ���������ָ���ȫ������
Author: zhouzying
URL: https://www.zhouzying.cn
Date: 2018-09-14
Update: 2018-09-27         Add data argument.
Update: 2018-10-04         Get replied comments and add users name who shared comments.

'''

import requests
import math
import random
# pycrypto
from Crypto.Cipher import AES
import codecs
import base64


# ���캯����ȡ������Ϣ
def get_comments_json(url, data):
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip, deflate',
               'Accept-Language': 'zh-CN,zh;q=0.9',
               'Connection': 'keep-alive',
               'Cookie': 'WM_TID=36fj4OhQ7NdU9DhsEbdKFbVmy9tNk1KM; _iuqxldmzr_=32; _ntes_nnid=26fc3120577a92f179a3743269d8d0d9,1536048184013; _ntes_nuid=26fc3120577a92f179a3743269d8d0d9; __utmc=94650624; __utmz=94650624.1536199016.26.8.utmcsr=google|utmccn=(organic)|utmcmd=organic|utmctr=(not%20provided); WM_NI=2Uy%2FbtqzhAuF6WR544z5u96yPa%2BfNHlrtTBCGhkg7oAHeZje7SJiXAoA5YNCbyP6gcJ5NYTs5IAJHQBjiFt561sfsS5Xg%2BvZx1OW9mPzJ49pU7Voono9gXq9H0RpP5HTclE%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eed5cb8085b2ab83ee7b87ac8c87cb60f78da2dac5439b9ca4b1d621f3e900b4b82af0fea7c3b92af28bb7d0e180b3a6a8a2f84ef6899ed6b740baebbbdab57394bfe587cd44b0aebcb5c14985b8a588b6658398abbbe96ff58d868adb4bad9ffbbacd49a2a7a0d7e6698aeb82bad779f7978fabcb5b82b6a7a7f73ff6efbd87f259f788a9ccf552bcef81b8bc6794a686d5bc7c97e99a90ee66ade7a9b9f4338cf09e91d33f8c8cad8dc837e2a3; JSESSIONID-WYYY=G%5CSvabx1X1F0JTg8HK5Z%2BIATVQdgwh77oo%2BDOXuG2CpwvoKPnNTKOGH91AkCHVdm0t6XKQEEnAFP%2BQ35cF49Y%2BAviwQKVN04%2B6ZbeKc2tNOeeC5vfTZ4Cme%2BwZVk7zGkwHJbfjgp1J9Y30o1fMKHOE5rxyhwQw%2B%5CDH6Md%5CpJZAAh2xkZ%3A1536204296617; __utma=94650624.1052021654.1536048185.1536199016.1536203113.27; __utmb=94650624.12.10.1536203113',
               'Host': 'music.163.com',
               'Referer': 'http://music.163.com/',
               'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/66.0.3359.181 Safari/537.36'}

    try:
        r = requests.post(url, headers=headers, data=data)
        r.encoding = "utf-8"
        if r.status_code == 200:
            # ����json��ʽ������
            return r.json()

    except:
        print("��ȡʧ��!")


# ����16������ַ�
def generate_random_strs(length):
    string = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
    # ���ƴ�������i
    i = 0
    # ��ʼ������ַ���
    random_strs = ""
    while i < length:
        e = random.random() * len(string)
        # ����ȡ��
        e = math.floor(e)
        random_strs = random_strs + list(string)[e]
        i = i + 1
    return random_strs


# AES����
def AESencrypt(msg, key):
    # �������16�ı�����������(paddiing)
    padding = 16 - len(msg) % 16
    # ����ʹ��padding��Ӧ�ĵ��ַ��������
    msg = msg + padding * chr(padding)
    # �������ܻ��߽��ܵĳ�ʼ����(������16λ)
    iv = '0102030405060708'

    cipher = AES.new(key.encode('utf-8'), AES.MODE_CBC, iv.encode('utf-8'))
    # ���ܺ�õ�����bytes���͵�����
    encryptedbytes = cipher.encrypt(msg)
    # ʹ��Base64���б���,����byte�ַ���
    encodestrs = base64.b64encode(encryptedbytes)
    # ��byte�ַ�����utf-8���н���
    enctext = encodestrs.decode('utf-8')
    return enctext


# RSA����
def RSAencrypt(randomstrs, key, f):
    # ����ַ�����������
    string = randomstrs[::-1]
    # ������ַ���ת����byte��������
    text = bytes(string, 'utf-8')
    seckey = int(codecs.encode(text, encoding='hex'), 16) ** int(key, 16) % int(f, 16)
    return format(seckey, 'x').zfill(256)


# ��ȡ����
def get_params(page):
    # msgҲ����д��msg = {"offset":"ҳ��ƫ����=(ҳ��-1) *��20", "limit":"20"},offset��limit����������������(js)
    # limit���ֵΪ100,����Ϊ100ʱ,��ȡ�ڶ�ҳʱ,Ĭ��ǰһҳ��20������,Ҳ����˵�ڶ�ҳ����������80��,��20���ǵ�һҳ��ʾ��
    # msg = '{"rid":"R_SO_4_1302938992","offset":"0","total":"True","limit":"100","csrf_token":""}'
    # ƫ����
    offset = (page - 1) * 20
    # offset��limit�Ǳ�ѡ����,���������ǿ�ѡ��,����������Ӱ��data���ݵ�����
    msg = '{"offset":' + str(offset) + ',"total":"True","limit":"20","csrf_token":""}'
    key = '0CoJUm6Qyw8W8jud'
    f = '00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7'
    e = '010001'
    enctext = AESencrypt(msg, key)
    # ���ɳ���Ϊ16������ַ���
    i = generate_random_strs(16)

    # ����AES����֮��õ�params��ֵ
    encText = AESencrypt(enctext, i)
    # RSA����֮��õ�encSecKey��ֵ
    encSecKey = RSAencrypt(i, e, f)
    return encText, encSecKey


def hotcomments(html, songname, i, pages, total, filepath):
    # д���ļ�
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("���ڻ�ȡ����{}�ĵ�{}ҳ����,�ܹ���{}ҳ{}�����ۣ�\n".format(songname, i, pages, total))
    print("���ڻ�ȡ����{}�ĵ�{}ҳ����,�ܹ���{}ҳ{}�����ۣ�\n".format(songname, i, pages, total))

    # ��������
    m = 1
    # �����ֵ����򷵻�True, ���򷵻�False
    if 'hotComments' in html:
        for item in html['hotComments']:
            # ��ȡ�����������۵��û���
            user = item['user']
            # д���ļ�
            print("��������{}: {} : {}    ���޴���: {}".format(m, user['nickname'], item['content'], item['likedCount']))
            with open(filepath, 'a', encoding='utf-8') as f:
                f.write("��������{}: {} : {}   ���޴���: {}\n".format(m, user['nickname'], item['content'], item['likedCount']))
                # �ظ�����
                if len(item['beReplied']) != 0:
                    for reply in item['beReplied']:
                        # ��ȡ����ظ����۵��û���
                        replyuser = reply['user']
                        print("�ظ���{} : {}".format(replyuser['nickname'], reply['content']))
                        f.write("�ظ���{} : {}\n".format(replyuser['nickname'], reply['content']))
            m += 1


def comments(html, songname, i, pages, total, filepath):
    with open(filepath, 'a', encoding='utf-8') as f:
        f.write("\n���ڻ�ȡ����{}�ĵ�{}ҳ����,�ܹ���{}ҳ{}�����ۣ�\n".format(songname, i, pages, total))
    print("\n���ڻ�ȡ����{}�ĵ�{}ҳ����,�ܹ���{}ҳ{}�����ۣ�\n".format(songname, i, pages, total))
    # ȫ������
    j = 1
    for item in html['comments']:
        # ��ȡ�������۵��û���
        user = item['user']
        print("ȫ������{}: {} : {}    ���޴���: {}".format(j, user['nickname'], item['content'], item['likedCount']))
        with open(filepath, 'a', encoding='utf-8') as f:

            f.write("ȫ������{}: {} : {}   ���޴���: {}\n".format(j, user['nickname'], item['content'], item['likedCount']))
            # �ظ�����
            if len(item['beReplied']) != 0:
                for reply in item['beReplied']:
                    # ��ȡ����ظ����۵��û���
                    replyuser = reply['user']
                    print("�ظ���{} : {}".format(replyuser['nickname'], reply['content']))
                    f.write("�ظ���{} : {}\n".format(replyuser['nickname'], reply['content']))

        j += 1


def main():
    # ����id��
    songid = 38592976

    # ��������
    songname = "Dream it possible"
    # �ļ��洢·��
    filepath = songname + ".txt"
    page = 1
    params, encSecKey = get_params(page)

    url = 'https://music.163.com/weapi/v1/resource/comments/R_SO_4_' + str(songid) + '?csrf_token='
    data = {'params': params, 'encSecKey': encSecKey}
    # url = 'https://music.163.com/#/song?id=19292984'
    # ��ȡ��һҳ����
    html = get_comments_json(url, data)
    # ��������
    total = html['total']
    # ��ҳ��
    pages = math.ceil(total / 20)
    hotcomments(html, songname, page, pages, total, filepath)
    comments(html, songname, page, pages, total, filepath)

    # ��ʼ��ȡ������ȫ������
    page = 2
    while page <= pages:
        params, encSecKey = get_params(page)
        data = {'params': params, 'encSecKey': encSecKey}
        html = get_comments_json(url, data)
        # �ӵڶ�ҳ��ʼ��ȡ����
        comments(html, songname, page, pages, total, filepath)
        page += 1


if __name__ == "__main__":
    main()
