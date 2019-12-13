import os
import time
from datetime import datetime
import subprocess
import sys
sys.stdout = open('/home/pi/log_files/codex.txt','a')		#Creating all the logs in log_files directory
print(datetime.now())

path1='/home/pi/master/rasp1/idata/'
path2='/home/pi/master/rasp2/idata/'
path3='/home/pi/master/rasp3/idata/'

#checkfiles() function checks if there is any file present in the slaves (rasp1/rasp2/rasp3) folder , if there is any file it runs
# python file code1.py which basically sends the data to main master and deletes the files(images) from the folder
def checkfiles(path1,path2,path3):
	if len(os.listdir(path1)) >0 or len(os.listdir(path2)) or len(os.listdir(path3)):
		print(datetime.now())
		print('Files found')
		time.sleep(10)
		subprocess.Popen("{cmd}".format(cmd="python /home/pi/code1.py"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

while True:
	checkfiles(path1,path2,path3)
	time.sleep(300)

