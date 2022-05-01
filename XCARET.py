import os

if __name__ == "__main__":
   try:
       os.system("git pull")
       __import__("XCARET")
   except Exception as a:
       exit(str(a))
