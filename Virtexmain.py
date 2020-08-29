#coding: -UTF-8

import os
import sys
import time
import json
from time import sleep

def bersih():
	time.sleep(0.1)
	os.system("clear")

def tab():
	print ""

def slep():
	time.sleep(0.5)

def p1():
	os.system("mv virtex1.txt /sdcard")

def p2():
	os.system("mv virtex2.txt /sdcard")

def p3():
	os.system("mv virtex3.txt /sdcard")

def p4():
	os.system("mv virtex4.txt /sdcard")

def p5():
	os.system("mv virtex5.txt /sdcard")

def lagi():
	tab()
	pilih = raw_input(" \033[37m[\033[32m+\033[37m] \033[0;37mIngin Mencoba Lagi \033[33m? \033[35m[\033[34my\033[0;32m/\033[34mn\033[35m] \033[0;36m: \033[37m")
	if pilih == "y":
	   time.sleep(0.50)
	   os.system("python2 Virtexmain.py")
	if pilih == "n":
	   time.sleep(0.50)
	   sys.exit()
	   tab()

bersih()
print """\033[35m
\033[35m┬  ┬┬┬─┐┌┬┐┌─┐\033[31m═╗ ╦
\033[35m└┐┌┘│├┬┘ │ ├┤ \033[31m╔╩╦╝
\033[35m └┘ ┴┴└─ ┴ └─┘\033[31m╩ ╚═  \033[33;1mv1
"""
print " -\033[34;1m═════════════════════════════════════\033[33;1m- "
print "  \033[35;1m[\033[32;1m+\033[35m] \033[37mAuthor   \033[34m:  \033[37mNemuv "
print "  \033[35m[\033[32m+\033[35m] \033[37mYouTube  \033[34m:  \033[37mNem Croco "
print "  \033[35m[\033[32m+\033[35m] \033[37mGithub   \033[34m:  \033[37mGithub.com/NemuvSpZi "
print " \033[33m-\033[34m═════════════════════════════════════\033[33m- "
tab()
print "  \033[37;1m[\033[32m1\033[37m] \033[35m> \033[0;32m๑۩ [ evil ] ๑۩ "
tab()
print "  \033[37m[\033[32m2\033[37m] \033[35m> \033[0;32m█.⚝.B.U.D.D.Y.█"
tab()
print "  \033[37m[\033[32m3\033[37m] \033[35m> \033[0;32mV̺͆I̺͆R̺͆T̺͆E̺͆X̺͆T̺͆ B̺͆Y̺͆ G̺͆H̺͆O̺͆S̺͆T̺͆N̺͆A̺͆M̺͆E̺͆-"
tab()
print "  \033[37m[\033[32m4\033[37m] \033[35m> \033[0;32m☆☆WE ARE WOLF-1"
tab()
print "  \033[37m[\033[32m5\033[37m] \033[35m> \033[0;32mV̶i̸̶͟͞r̶t̶e̶x̶√D̸͟͞I̸͟͞M̸͟͞A̸͟͞S̸͟͞&R̸͟͞A̸͟͞F̸͟͞L̸͟͞Y̸͟͞[G̸͟͞A̸͟͞N̸͟͞A̸͟͞S̸͟͞]"
tab()

tak = raw_input(" \033[37m[\033[35m-\033[37m] \033[33mPilih \033[31mBwank \033[34m: \033[0;37m")

if tak == "1":
   bersih()
   p1()
   tab()
   print " \033[37m[\033[32m+\033[37m] \033[0;37mFile Sudah Tersimpan Di \033[33mInternal \033[0;32m✓ "
   print " \033[37m[\033[32m-\033[37m] \033[0;37mNama File \033[34m: \033[35mvirtex1.txt "
   lagi()

if tak == "2":
   bersih()
   p1()
   tab()
   print " \033[37m[\033[32m+\033[37m] \033[0;37mFile Sudah Tersimpan Di \033[33mInternal \033[0;32m✓ "
   print " \033[37m[\033[32m-\033[37m] \033[0;37mNama File \033[34m: \033[35mvirtex2.txt "
   lagi()

if tak == "3":
   bersih()
   p1()
   tab()
   print " \033[37m[\033[32m+\033[37m] \033[0;37mFile Sudah Tersimpan Di \033[33mInternal \033[0;32m✓ "
   print " \033[37m[\033[32m-\033[37m] \033[0;37mNama File \033[34m: \033[35mvirtex3.txt "
   lagi()

if tak == "4":
   bersih()
   p1()
   tab()
   print " \033[37m[\033[32m+\033[37m] \033[0;37mFile Sudah Tersimpan Di \033[33mInternal \033[0;32m✓ "
   print " \033[37m[\033[32m-\033[37m] \033[0;37mNama File \033[34m: \033[35mvirtex4.txt "
   lagi()

if tak == "5":
   bersih()
   p1()
   tab()
   print " \033[37m[\033[32m+\033[37m] \033[0;37mFile Sudah Tersimpan Di \033[33mInternal \033[0;32m✓ "
   print " \033[37m[\033[32m-\033[37m] \033[0;37mNama File \033[34m: \033[35mvirtex5.txt "
   lagi()

else:
     tab()
     bersih()
     print " \033[37m[\033[32m+\033[37m] \033[0;37mPilih Yang Benar \033[33m!! "
     tab()
