from urllib import urlopen
import re
#p=re.compile('<pre>(.*?)</pre>')
p=re.compile('([0-9\\.]+)    (.*com)')
text=urlopen('http://www.360kb.com/kb/2_122.html').read()
f=open('/etc/hosts','w')
f.write('127.0.0.1   localhost\n255.255.255.255 broadcasthost\n::1             localhost\n\n')
ip=p.findall(text)[0][0]
print ip
f.write(ip+'    www.google.com.hk\n')
for ip,com in p.findall(text):
	f.write(ip+'    '+com+'\n')
f.close()
