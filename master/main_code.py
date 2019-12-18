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


import RPi.GPIO as GPIO
from time import sleep # Import the sleep function from the time module
GPIO.setwarnings(False) # Ignore warning for now
GPIO.setmode(GPIO.BCM) # Use physical pin numbering
GPIO.setup(8, GPIO.OUT, initial=GPIO.HIGH) # Set pin 8 to be an output pin and set initial value to low (off)
###############
###############
import smbus
#######gy30####
# Define some constants from the datasheet
DEVICE     = 0x23 # Default device I2C address

POWER_DOWN = 0x00 # No active state
POWER_ON   = 0x01 # Power on
RESET      = 0x07 # Reset data register value

# Start measurement at 4lx resolution. Time typically 16ms.
CONTINUOUS_LOW_RES_MODE = 0x13
# Start measurement at 1lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_1 = 0x10
# Start measurement at 0.5lx resolution. Time typically 120ms
CONTINUOUS_HIGH_RES_MODE_2 = 0x11
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_1 = 0x20
# Start measurement at 0.5lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_HIGH_RES_MODE_2 = 0x21
# Start measurement at 1lx resolution. Time typically 120ms
# Device is automatically set to Power Down after measurement.
ONE_TIME_LOW_RES_MODE = 0x23

#bus = smbus.SMBus(0) # Rev 1 Pi uses 0
bus = smbus.SMBus(1)  # Rev 2 Pi uses 1

def convertToNumber(data):
  # Simple function to convert 2 bytes of data
  # into a decimal number. Optional parameter 'decimals'
  # will round to specified number of decimal places.
  result=(data[1] + (256 * data[0])) / 1.2
  return (result)

def readLight(addr=DEVICE):
  # Read data from I2C interface
  data = bus.read_i2c_block_data(addr,ONE_TIME_HIGH_RES_MODE_1)
  return convertToNumber(data)


thr = 100

#path1='/home/pi/master/rasp1/idata/'
#path2='/home/pi/master/rasp2/idata/'
#path3='/home/pi/master/rasp3/idata/'

#checkfiles() function checks if there is any file present in the slaves (rasp1/rasp2/rasp3) folder , if there is any file it runs
# python file code1.py which basically sends the data to main master and deletes the files(images) from the folder
#subprocess.Popen("ssh {user}@{host} {cmd}".format(user="pi",host="192.168.43.112",cmd="scp rasp1/idata/*.png pi@192.168.43.113:master/rasp1/idata"), shell=True, stdout=subprocess.PIPE).communicate()

def camerafun():
    subprocess.Popen("{cmd}".format(cmd="python /home/pi/camera.py"), shell=True, stdout=subprocess.PIPE).communicate()

def checkfiles(path1,path2,path3):
    if len(os.listdir(path1)) > 0 or len(os.listdir(path2)) > 0 or len(os.listdir(path3)) > 0:
        print(datetime.now())
        print('Files found')
        time.sleep(10)
        subprocess.Popen("{cmd}".format(cmd="python /home/pi/code_functions.py"), shell=True, stdout=subprocess.PIPE,stderr=subprocess.PIPE).communicate()

while  True:
    subprocess.Popen("{cmd}".format(cmd="python /home/pi/rest_sensor_local_master.py"), shell=True, stdout=subprocess.PIPE).communicate()
    lightLevel = readLight()
    res = int(lightLevel)
    print(res)
    if res > thr:
        camerafun()
        GPIO.output(8, GPIO.LOW) # Turn on relay for powering slave rpi
        time.sleep(params['Image_Waiting_Interval'])
        GPIO.output(8, GPIO.HIGH) # Turn off relay
        time.sleep(60)
        checkfiles(path1,path2,path3)

    time.sleep(params['Image_Capture_Interval'])

