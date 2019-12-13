# Smart-Agriculture
**Major Technical Project - Developing an IOT based system for Health Prediction and Disease Classification of Crops using Machine Learning** <br/>

	In /home/pi directory a folder named rasp1 (slave1) ,rasp2 (slave2) ,rasp3(slave3),master(Local master),main_master (Main Master) are made which is basically for naming convention. 


	1.Setting up Password less SSH between slaves and local master & local master and main master 
	https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/ and in “.ssh” folder in home directory there is a ‘config’ file where a new entry will be added for every new key pair generation

	2.Create Crontab jobs for slaves to automatically send the data to local master on Reboot.
	To open crontab file type the following command in shell:
	“crontab -e” also create a shell script which will be needed by crontab. The shell script will have the path to the python file.For example “scriptx.sh” in /home/pi/ directory in slaves raspberry pi’s.

	3.All the python codes are in /home/pi directory of all raspberry pi’s named as “code1.py” and “codex.py” 
	fun() - runs camera 
	fux() - create subprocess to send data using scp 
	remfile() - removes files from respective directories after sending the files to parents. “codex.py” in local master /home/pi directory basically runs in background and checks weather there is any file in /home/master/raspx/idata/ folders where raspx = rasp1 , rasp3 in every 5 minutes. 
	
	4.IP’s of all the raspberry pi’s :
	Local master 		:
	Hip 			- 	192.168.43.112 
	Ethip 			-	169.254.51.217
	Tpip (wlan0)  		-	192.168.1.102		(static ip)

	Main Master 		:
	Hip			-	192.168.43.231
	TpIp			-	192.168.1.110		(static ip)   
	USBIP(JioFi)		-	192.168.225.56		(static ip)

	Slave1			:
	Hip			-	192.168.43.169
	EthIP			-	169.254.105.228
	TpIP			-	192.168.1.105		(static ip)

	Slave3			:
	Hip			-	192.168.43.212
	Ethip			-	169.254.101.168
	TpIP			-	192.168.1.106		(static ip)
	
	RouterIp		:
	JioFiIP			- 	192.168.225.201
				


	5.How to set static IP ?: https://electrondust.com/2017/11/25/setting-raspberry-pi-wifi-static-ip-raspbian-stretch-lite/ 
     
	6.For wlan/usb to eth bridge (only when JioFi is connected)
	https://www.instructables.com/id/Share-WiFi-With-Ethernet-Port-on-a-Raspberry-Pi/  
	https://github.com/arpitjindal97/raspbian-recipes/blob/master/wifi-to-eth-bridge.sh 
	There is file in /home/pi directory “wifi_to_eth_bridge.sh” , change the variable wlan accordingly to bridge usb0 or wlan0 to eth0.
	To bridge run the script in shell : “sh wifi_to_eth_bridge.sh” (this will provide JioFi internet to router via usb0)   

    	7.To access raspberry pi via router on JioFi use commands : 
    	ssh pi@(TPLinkRouterIP) -p portnumber 
		portnumber as per entry added on “tplinkwifi.net”

    	8.There is data transfer between local master and main master as all the raspberry pi’s are connected to TP-Link_9236

    	9.For error handling in the “codex.py” when connection is lost and we don’t want that files to get removed by “remfile() function” see link (third answer) :
	https://stackoverflow.com/questions/25079140/subprocess-popen-checking-for-success-and-errors

	10.Log files for each python file i.e “camera.py”,”code1.py” and “codex.py” are created in log_files folder in /home/pi directory of local master and rasp1(slave)
