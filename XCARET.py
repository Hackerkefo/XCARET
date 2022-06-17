import os
import platform
import webbrowser
os.system('termux-setup-storage')
os.system('git pull')
try:os.system('mkdir /sdcard/CHI-DATA')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/OK')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/CP')
except:pass
try:os.system('mkdir /sdcard/CHI-DATA/TAP-A2F')
except:pass
try:os.system('touch .prox.txt')
except:pass
if __name__ == "__main__":
        try:
                __import__("XCARET").login()
        except Exception as e:
                exit(str(e))
