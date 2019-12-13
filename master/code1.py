import subprocess
import time
import sys
from datetime import datetime
argv = sys.argv[1:]
sys.stdout=open('/home/pi/log_files/code1.txt','a')    #creating log files with time
print(datetime.now())

#fun() runs the camera.py
#fux() send the data to the main master
#remfile() removes the data from the folder


def fun():
	#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def fux():	
	res =	subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp1/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp1/idata"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print(res)
	return res[1]
	#subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp2/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp2/idata"), shell=True, stdout=subprocess.PIPE).communicate()
	#subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp3/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp3/idata"), shell=True, stdout=subprocess.PIPE).communicate()
def remfile():
	print('Remove files')
	subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp1/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
	#subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp2/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
	#subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp3/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
def shutdown():
	subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="169.254.105.228",cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()
	#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="169.254.101.168",cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()	

#fun()
#time.sleep(10)
try:

	val = fux()
	if len(val) == 0:
		time.sleep(20)
		remfile()
except:
	print('Error')
	
#time.sleep(10)
#shutdown()

	
