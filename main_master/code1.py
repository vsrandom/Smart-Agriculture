import os
import time
from datetime import datetime
import subprocess
import sys
import json
params = json.loads(open('/home/pi/configuration.json').read())
sys.stdout = open(params['Code1_Log_File'],'a')     #Creating all the logs in log_files directory
print(datetime.now())

#checkfiles() function checks if there is any file present in the slaves (rasp1/rasp2/rasp3) folder , if there is any file it runs
# python file code1.py which basically sends the data to main master and deletes the files(images) from the folder
def fun():
    #subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
    subprocess.Popen("{cmd}".format(cmd="mkdir  -p /mnt/sda1"), shell=True, stdout=subprocess.PIPE).communicate()

    subprocess.Popen("{cmd}".format(cmd="sudo mount -o rw /dev/sda1 /mnt/sda1/"), shell=True, stdout=subprocess.PIPE).communicate()

def checkfiles(path,file):
    sourcepath = params['source'] + path
    destinationpath = params['destination'] + path
    if len(os.listdir(sourcepath)) > 0:
        print(datetime.now())
	print(sourcepath)
        print('Files found')
        #time.sleep(10)
        if file=='idata':
		res = subprocess.Popen("{cmd1} {path1}*.jpg {path2}".format(cmd1="sudo mv",path1 =sourcepath ,path2=destinationpath), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
		print(res)
	if file=='sdata':
		res2 = subprocess.Popen("{cmd1} {path1}*.txt {path2}".format(cmd1="sudo mv",path1 =sourcepath ,path2=destinationpath), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
    		print(res2)
    else:
		print('Files not found')
		print(path)

def transferFiles():
	count = params['count']
	for i in range(1,count+1):
		sourcepath = params['main_master']+params['master']+str(i)+'/'
		#print(sourcepath)
		masterpath = sourcepath + params['lmaster']
		finalfolderidata = masterpath+params['idata']+'/'
		finalfoldersdata = masterpath+params['sdata']+'/'
		checkfiles(finalfolderidata,'idata')
		checkfiles(finalfoldersdata,'sdata')
		slavecount = params['slave_count']
		for j in range(1,slavecount+1):
			slavepath = sourcepath + params['slave'] + str(j) + '/'
			finalfolderidatar = slavepath+params['idata']+'/'
			finalfoldersdatar= slavepath+params['sdata']+'/'
			checkfiles(finalfolderidatar,'idata')
			checkfiles(finalfoldersdatar,'sdata')

transferFiles()
print(datetime.now())
