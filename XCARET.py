import os,platform

comb =platform.architecture()[0]

if name == "main":
 os.system("git pull")
 if comb == "64bit":
  import("xctate64").main()
 elif comb == "32bit":
  import("xctate32").main()
 else:
  print("UNKNOWN SYSTEM ")
  exit()
