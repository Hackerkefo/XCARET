import os, platform
try:
    import requests
except:
    os.system('pip install requests')
os.system('git pull')
import requests
os.system('git pull')
bit = platform.architecture()[0]
if bit == '64bit':
    from XCARET64 import 64 bit
    login()
elif bit == '32bit':
    from XCARET32 import 32 bit
    login()
