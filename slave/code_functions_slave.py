import subprocess
from datetime import datetime
import time
import sys
import json
params = json.loads(open('/home/pi/configuration.json').read())
argv = sys.argv[1:]
sys.stdout=open(params['Code1_Log_File'],'a')
print(datetime.now())


def camerafun():
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def senddata():
	res=subprocess.Popen("scp {ImgSourceFiles}*.jpg {user}@{host}:{ImgDestFiles}".format(ImgSourceFiles=params['Image_Path'], user=params['User'], host=params['LocalMIP'], ImgDestFiles=params['ImageDestination'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	return res[1]
def remfile():
	 subprocess.Popen("rm {ImgSourceFiles}*.jpg".format(ImgSourceFiles=params['Image_Path']), shell=True, stdout=subprocess.PIPE).communicate()
	

if params['runCamera']:
	camerafun()
	time.sleep(10)

if params['SendFiles']:
	x=senddata()
	if len(x)==0 and params['removeFiles']:
		time.sleep(10)
		remfile()
	
