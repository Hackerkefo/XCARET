import os,platform

comb =platform.architecture()[0]

if name == "login":
 os.system("git pull")
 if comb == "64bit":
  import("XCARET64").login()
 elif comb == "32bit":
  import("XCARET32").login()
 else:
  print("UNKNOWN SYSTEM ")
  exit()
