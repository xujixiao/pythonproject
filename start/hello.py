print("徐杰差额")
print("hello.world");
if True:
    print("true")
else:
    print("false")
item_one = "xjixiao"
item_two = "xjixiao"
item_three = "xjixiao"
total = item_one \
        + item_two \
        + item_three
print(total)
print(total[2:8])
print(total[2:])

total = ['item_one', 'item_two', 'item_three',
         'item_four', 'item_five']
print(total)

word = '字符串'
sentence = "这是一个句子。"
paragraph = """这是一个段落，
可以由多行组成"""

# !/usr/bin/python3

str = 'Runoob'

print(str)  # 输出字符串
print(str[0:-1])  # 输出第一个到倒数第二个的所有字符
print(str[0])  # 输出字符串第一个字符
print(str[2:5])  # 输出从第三个开始到第五个的字符
print(str[2:])  # 输出从第三个开始的后的所有字符
print(str * 2)  # 输出字符串两次
print(str + '你好')  # 连接字符串

print('------------------------------')

print('hello\nrunoob')  # 使用反斜杠(\)+n转义特殊字符
print(r'hello\nrunoob')  # 在字符串前面添加一个 r，表示原始字符串，不会发生转义

import sys;

x = 'runoob';
sys.stdout.write(x + '\n')

import sys

print('================Python import mode==========================');
print('命令行参数为:')
for i in sys.argv:
    print(i)
print('\n python 路径为', sys.path)
