import subprocess
from datetime import datetime
import time
import sys
argv = sys.argv[1:]
sys.stdout=open('/home/pi/log_files/code1.txt','a')
print(datetime.now())

def fun():
	#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def fux():
	res=subprocess.Popen("{cmd}".format(cmd="scp /home/pi/rasp1/idata/*.jpg pi@169.254.51.217:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	return res[1]
def remfile():
	 subprocess.Popen("{cmd}".format(cmd="rm /home/pi/rasp1/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()

def shutdown():
	subprocess.Popen("{cmd}".format(cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()
	

fun()
time.sleep(10)
x=fux()
if len(x)==0:
	time.sleep(10)
	remfile()

#time.sleep(10)
#shutdown()
	
