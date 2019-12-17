import os
import time
from datetime import datetime
import subprocess
import sys
import json
params = json.loads(open('/home/pi/configuration.json').read())
sys.stdout = open(params['Codex_Log_File'],'a')     #Creating all the logs in log_files directory
print(datetime.now())
path1 = params['Image_Path_Slave_1']
path2 = params['Image_Path_Local']
path3 = params['Image_Path_Slave_2']

#path1='/home/pi/master/rasp1/idata/'
#path2='/home/pi/master/rasp2/idata/'
#path3='/home/pi/master/rasp3/idata/'

#checkfiles() function checks if there is any file present in the slaves (rasp1/rasp2/rasp3) folder , if there is any file it runs
# python file code1.py which basically sends the data to main master and deletes the files(images) from the folder
def fun():
    #subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
    subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def checkfiles(path1,path2,path3):
    if len(os.listdir(path1)) > 0 or len(os.listdir(path2)) > 0 or len(os.listdir(path3)) > 0:
        print(datetime.now())
        print('Files found')
        time.sleep(10)
        subprocess.Popen("{cmd}".format(cmd="python /home/pi/code1.py"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

while  True:
    if params['runCamera']:
        fun()
    checkfiles(path1,path2,path3)
    time.sleep(params['Image_Capture_Interval'])

