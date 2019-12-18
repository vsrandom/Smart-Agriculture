# Smart-Agriculture

Major Technical Project - Developing an IOT based system for Health Prediction and Disease Classification of Crops using Machine Learning

## Automated Data Collection From Salgi and Neri Field via SSH
![Neri Field](https://github.com/vsrandom/Smart-Agriculture/blob/master/neri_field.PNG) <br />
![Salgi Field](https://github.com/vsrandom/Smart-Agriculture/blob/master/salgi_field.PNG)

* Setting up Password less SSH between slaves and local master & local master and main master <br />
https://www.tecmint.com/ssh-passwordless-login-using-ssh-keygen-in-5-easy-steps/ <br /> 
and in “.ssh” folder in home directory there is a ‘config’ file where a new entry will be added for every new key pair generation.

* Create Crontab jobs for slaves to automatically send the data to local master on Reboot.
To open crontab file type the following command in shell:
> crontab -e <br />

also create a shell file with name scriptx.sh which will be needed by crontab. Add the following entry at the bottom:
> @reboot ( sleep 180; sh /home/pi/scriptx.sh )

* How to set static IP ?<br />
https://electrondust.com/2017/11/25/setting-raspberry-pi-wifi-static-ip-raspbian-stretch-lite/ 

* For wlan/usb to eth bridge (only when JioFi is connected) <br />
https://www.instructables.com/id/Share-WiFi-With-Ethernet-Port-on-a-Raspberry-Pi/ <br />  
https://github.com/arpitjindal97/raspbian-recipes/blob/master/wifi-to-eth-bridge.sh <br />
There is file in /home/pi directory “wifi_to_eth_bridge.sh” , change the variable wlan accordingly to bridge usb0 or wlan0 to eth0.

* To access raspberry pi via router on JioFi use commands : <br /> 
> ssh pi@(TPLinkRouterIP) -p portnumber <br />

portnumber as per entry added on “tplinkwifi.net” <br />

* For error handling in the “codex.py” when connection is lost and we don’t want that files to get removed by “remfile() function” see link (third answer) : <br /> https://stackoverflow.com/questions/25079140/subprocess-popen-checking-for-success-and-errors

* Log files for each python file i.e “camera.py”,”main_code.py” and “code_functions.py” are created in log_files folder in /home/pi directory of local master and slave


## License

This project is licensed under the IIT License.
