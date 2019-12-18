import subprocess
import time
import sys
import json
from datetime import datetime
params = json.loads(open('/home/pi/configuration.json').read())
argv = sys.argv[1:]

sys.stdout=open(params['Code1_Log_File'],'a')    
print(datetime.now())

#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()
#res=subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp1/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp1/idata"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()
#subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp2/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp2/idata"), shell=True, stdout=subprocess.PIPE).communicate()
#subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp1/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
#subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp2/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
#subprocess.Popen("{cmd}".format(cmd="rm /home/pi/master/rasp3/idata/*.jpg"), shell=True, stdout=subprocess.PIPE).communicate()
#subprocess.Popen("{cmd}".format(cmd="scp /home/pi/master/rasp3/idata/*.jpg pi@192.168.1.110:main_master/master1/rasp3/idata"), shell=True, stdout=subprocess.PIPE).communicate()
def senddata():
	res1=subprocess.Popen("scp {ImgSourceFiles}*.jpg {user}@{host}:{ImgDestFiles}".format(ImgSourceFiles=params['Image_Path_Slave_1'], user=params['User'], host=params['MainMIP'], ImgDestFiles=params['ImageDestination_MainM'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	res2=subprocess.Popen("scp {ImgSourceFiles}*.jpg {user}@{host}:{ImgDestFiles}".format(ImgSourceFiles=params['Image_Path_Slave_2'], user=params['User'], host=params['MainMIP'], ImgDestFiles=params['ImageDestination_MainM2'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	res3=subprocess.Popen("scp {Sensor_data_local}*.txt {user}@{host}:{Sensor_data_destination}".format(Sensor_data_local=params['sensor_data_local'], user=params['User'], host=params['MainMIP'], Sensor_data_destination=params['sensor_data_destination'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	res4=subprocess.Popen("scp {ImgSourceFiles}*.jpg {user}@{host}:{ImgDestFiles}".format(ImgSourceFiles=params['Image_Path_Local'], user=params['User'], host=params['MainMIP'], ImgDestFiles=params['ImageDestination_MainM_Local'] ), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE).communicate()
	return res1[1]

def remfile():
	print('Remove files')
	subprocess.Popen("rm {ImgSourceFiles}*.jpg".format(ImgSourceFiles=params['Image_Path_Slave_1']), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("rm {ImgSourceFiles}*.jpg".format(ImgSourceFiles=params['Image_Path_Slave_2']), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("rm {ImgSourceFiles}*.jpg".format(ImgSourceFiles=params['Image_Path_Local']), shell=True, stdout=subprocess.PIPE).communicate()

def shutdown():
	subprocess.Popen("ssh {user}@{host} {cmd}".format(user=params['User'],host=params['SlaveIP'],cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()
	subprocess.Popen("ssh {user}@{host} {cmd}".format(user=params['User'],host=params['SlaveIP2'],cmd="sudo shutdown -h now"), shell=True, stdout=subprocess.PIPE).communicate()
	

try:

	if params['SendFiles']:
		val = senddata()
		if len(val) == 0 and params['removeFiles']:
			time.sleep(20)
			remfile()
except:
	print('Error')
if params['shutdown_slave_1']:	
	time.sleep(10)
	shutdown()

	
