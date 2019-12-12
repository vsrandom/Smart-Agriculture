import sys
import time
import subprocess
from datetime import datetime
sys.stdout=open('/home/pi/log_files/codex.txt','a')
print(datetime.now())


def loopfun():
	subprocess.Popen("{cmd}".format(cmd="python /home/pi/code1.py"), shell=True, stdout=subprocess.PIPE).communicate()


while True:
	loopfun()
	time.sleep(900)


