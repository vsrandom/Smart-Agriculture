import os
import time
from datetime import datetime
import subprocess
import sys
import json
params = json.loads(open('/home/pi/configuration.json').read())
sys.stdout = open(params['Codex_Log_File'],'a')     #Creating all the logs in log_files directory


#checkfiles() function checks if there is any file present in the slaves (rasp1/rasp2/rasp3) folder , if there is any file it runs
# python file code1.py which basically sends the data to main master and deletes the files(images) from the folder
def fun():
    #subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
    subprocess.Popen("{cmd}".format(cmd="mkdir  -p /mnt/sda1"), shell=True, stdout=subprocess.PIPE).communicate()

    subprocess.Popen("{cmd} {usbpath} {mountpath}".format(cmd="sudo mount -o rw", usbpath=params['usblocation'],mountpath=params['destination']), shell=True, stdout=subprocess.PIPE).communicate()
    #subprocess.Popen("{cmd} {mainmaster} {mountpath}".format(cmd="sudo cp -r",mainmaster=params['main_master'],mountpath=params['destination']), shell=True, stdout=subprocess.PIPE).communicate()

def runCode1():
	res = subprocess.Popen("{cmd}".format(cmd="python code1.py"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
	print(res)

def unMountUSB():
	subprocess.Popen("{cmd} {usbpath}".format(cmd="sudo umount", usbpath=params['usblocation']), shell=True, stdout=subprocess.PIPE).communicate()

print(datetime.now())
print('hi')
fun()
while True:
	time.sleep(params['Image_Capture_Interval'])
	file = open('/home/pi/configuration.json')
	params = json.loads(file.read())
	if params['stopCodex']:
		#unMountUSB()
		break
	file.close()
	runCode1()

    #checkfiles(path1,path2,path3)
    #time.sleep(params['Image_Capture_Interval'])

