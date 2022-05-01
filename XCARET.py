P = '\x1b[1;97'
import os,requests
xr = requests.get("http://ip-api.com/json/").json()
try:
	fc = xr["country"]
except KeyError:
	print('%s\nNO INTERNET CONNECTION\n'%(M))
	exit()

if __name__ == "__main__":
	os.system("git pull")
	if "Nigeria" == fc:
		__import__("XCARET").login()
		__import__("XCARET").login()
	print("UNKNOWN SYSTEM ")
		
