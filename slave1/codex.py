import sys
import time
import json
import subprocess
from datetime import datetime
params = json.loads(open('/home/pi/configuration.json').read())
sys.stdout=open('/home/pi/log_files/codex.txt','a')

print(datetime.now())
print('Codex code has started...')

def loopfun():
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/code1.py"), shell=True, stdout=subprocess.PIPE).communicate()


while True:
	loopfun()
	time.sleep(params['Image_Capture_Interval'])


