# coding=gbk
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

import smtplib


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# from_addr = input('From: ')
# password = input('Password: ')
# to_addr = input('To: ')
# smtp_server = input('SMTP server: ')

from_addr = '1107313740@qq.com'
password = 'utmisueyjwawgchg'
to_addr = '1375481607@qq.com'
smtp_server = 'smtp.qq.com'

msg = MIMEText('���Ϻã�����', 'plain', 'utf-8')
msg['From'] = _format_addr('Python������ <%s>' % from_addr)
msg['To'] = _format_addr('����Ա <%s>' % to_addr)
msg['Subject'] = Header('���������python�ű��Զ����㷢���ʼ�', 'utf-8').encode()

server = smtplib.SMTP(smtp_server, 25)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()
