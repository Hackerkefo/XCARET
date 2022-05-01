
import platform

arc = str(platform.uname().machine)
if 'arm' in arc:
	__import__("XCARET32").login()
elif 'aarch' in arc:
	__import__("XCARET").login()
else:
	exit(f' Unknow device machine {arc}')
