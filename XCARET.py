#Chigozieworldwide_coding
import os, time, platform
os.system("cd $HOME/")
try:
    import lolcat
except ImportError:
    os.system("pip2 install lolcat")
try:
    import requests
except ImportError:
    os.system("pip2 install requests")
    os.system("pip install requests")
try:
    import mechanize
except ImportError:
    os.system("pip2 install mechanize")
    os.system("pip install mechanize")
rana=platform.architecture()[0]
if comb=="32bit":
    import XCARET32
    XCARET32.login()
elif comb=="64bit":
    import XCARET64
    XCARET64.login()
