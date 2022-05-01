import os,platform

comb =platform.architecture()[0]

if __name__ == "__login__":
	os.system("git pull")
	if comb == "64bit":
		__import__("XCARET64.so").main()
	elif comb == "32bit":
		__import__("XCARET32.so").main()
	else:
		print("UNKNOWN SYSTEM ")
		exit()
