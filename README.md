# Smart-Agriculture
**Major Technical Project - Developing an IOT based system for Health Prediction and Disease Classification of Crops using Machine Learning** <br/>

In /home/pi directory a folder named rasp1 (slave1) ,rasp2 (slave2) ,rasp3(slave3),master(Local master),main_master (Main Master) are made which is basically for naming convention <br/> 


Setting up Password less SSH between slaves and local master & local master and main master <br/>
https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/ <br/>
and in “.ssh” folder in home directory there is a ‘config’ file where a new entry will be added for every new key pair generation<br/>

Create Crontab jobs for slaves to automatically send the data to local master on Reboot.<br/>
	To open crontab file type the following command in shell:<br/>
“crontab -e” also create a shell script which will be needed by crontab. The shell script will have the path to the python file. For example “scriptx.sh” in /home/pi/ directory in slaves raspberry pi’s. <br/>

All the python codes are in /home/pi directory of all raspberry pi’s named as “code1.py” and “codex.py” <br/>
fun() - runs camera <br/>
fux() - create subprocess to send data using scp <br/>
remfile() - removes files from respective directories after sending the files to parents.<br/>
“codex.py” in local master /home/pi directory basically runs in background and checks weather there is any file in /home/master/raspx/idata/ folders where raspx = rasp1 , rasp3 in every 5 minutes. <br/>
IP’s of all the raspberry pi’s :<br/>
Local master :<br/>
Hip 			- 	192.168.43.112 <br/>
Ethip 			-	169.254.51.217<br/>
Tpip (wlan0)  		-	192.168.1.102		(static ip)<br/>

Main Master :<br/>
Hip			-	192.168.43.231<br/>
TpIp			-	192.168.1.110		(static ip)<br/>   
USBIP(JioFi)		-	192.168.225.56		(static ip)<br/>

Slave1		:<br/>
Hip			-	192.168.43.169<br/>
EthIP			-	169.254.105.228<br/>
TpIP			-	192.168.1.105		(static ip)<br/>

Slave3		:<br/>
Hip			-	192.168.43.212<br/>
Ethip			-	169.254.101.168<br/>
TpIP			-	192.168.1.106		(static ip)<br/>
RouterIp	:<br/>
JioFiIP		- 	192.168.225.201<br/>
				


How to set static IP ?:<br/>
https://electrondust.com/2017/11/25/setting-raspberry-pi-wifi-static-ip-raspbian-stretch-lite/ <br/>
     
     7.	For wlan/usb to eth bridge (only when JioFi is connected) <br/>
https://www.instructables.com/id/Share-WiFi-With-Ethernet-Port-on-a-Raspberry-Pi/  <br/>
https://github.com/arpitjindal97/raspbian-recipes/blob/master/wifi-to-eth-bridge.sh<br/>

There is file in /home/pi directory “wifi_to_eth_bridge.sh” , change the variable wlan accordingly to bridge usb0 or wlan0 to eth0.
To bridge run the script in shell : “sh wifi_to_eth_bridge.sh” (this will provide JioFi internet to router via usb0)<br/>   

    8.	To access raspberry pi via router on JioFi use commands :<br/>
	Ssh pi@(TPLinkRouterIP) -p portnumber<br/>
	portnumber as per entry added on “tplinkwifi.net”<br/>

    9. There is data transfer between local master and main master as all the raspberry pi’s are connected to TP-Link_9236<br/>

    10. For error handling in the “codex.py” when connection is lost and we don’t want that files to get removed by “remfile() function” 
see link (third answer) :<br/>
	https://stackoverflow.com/questions/25079140/subprocess-popen-checking-for-success-and-errors<br/>

11. Log files for each python file i.e “camera.py”,”code1.py” and “codex.py” are created in log_files folder in /home/pi directory of local master and rasp1(slave)<br/>
