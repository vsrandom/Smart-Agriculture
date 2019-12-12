import sys
from datetime import datetime
sys.stdout=open('/home/pi/log_files/camera.txt','a')
print(datetime.now())

from  picamera import PiCamera
from time import sleep
from datetime import datetime
camera = PiCamera()
camera.start_preview()
sleep(3)
now = datetime.now()
dt_string = now.strftime("%d_%m_%Y_%H_%M_%S")
camera.capture('/home/pi/rasp1/idata/img%s.jpg'%dt_string)
camera.stop_preview() 
print('Image Saved')

