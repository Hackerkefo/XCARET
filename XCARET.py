import os,platform

comb =platform.architecture()[0]

if name == "login":
 os.system("git pull")
 if comb == "64bit":
  import("xctate64.so").login()
 elif comb == "32bit":
  import("xctate32.so").login()
 else:
  print("UNKNOWN SYSTEM ")
  exit()
