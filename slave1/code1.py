import subprocess
from datetime import datetime
import time
import sys
import json
params = json.loads(open('/home/pi/configuration.json').read())
argv = sys.argv[1:]
sys.stdout=open(params['Code1_Log_File'],'a')
print(datetime.now())

def fun():
	#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def fux():
	#res=subprocess.Popen("{cmd}".format(cmd="scp /home/pi/rasp1/idata/*.jpg pi@169.254.51.217:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	res=subprocess.Popen("scp {ImgSourceFiles}*.jpg {user}@{host}:{ImgDestFiles}".format(ImgSourceFiles=params['Image_Path'], user=params['User'], host=params['LocalMIP'], ImgDestFiles=params['ImageDestination'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	
	return res[1]
def remfile():
	 subprocess.Popen("rm {ImgSourceFiles}*.jpg".format(ImgSourceFiles=params['Image_Path']), shell=True, stdout=subprocess.PIPE).communicate()

def shutdown():
	subprocess.Popen("{cmd}".format(cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()
	

if params['runCamera']:
	fun()
	time.sleep(10)

if params['SendFiles']:
	x=fux()
	if len(x)==0 and params['removeFiles']:

		time.sleep(10)
		remfile()

#time.sleep(10)
#shutdown()
	
