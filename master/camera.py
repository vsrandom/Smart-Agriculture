import json
import sys
from datetime import datetime
params = json.loads(open('/home/pi/configuration.json').read())
sys.stdout=open(params['Camera_Log_File'],'a')   #creating log files with time (see next line)
print(datetime.now())   
from  picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()
camera.start_preview()
sleep(3)
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
camera.capture(params['Image_Path_Local']+'img%s.jpg'%dt_string)      #storing the image in mentioned directory
camera.stop_preview() 
print('Image Saved')                   #This message will also be appended in the log file confirming Image is saved

