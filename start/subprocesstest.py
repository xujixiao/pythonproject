import subprocess

print('$ nslookup www.python.org')
r = subprocess.call(['nslookup', 'www.python.org'])
p = subprocess.call(['ipconfig'])
print('Exit code:', r)
print('Exit code:', p)
