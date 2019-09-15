# Setting up Wifi

Wifi on the Pis is a bit tricky. This is mainly due to UCSD's wifi protections
for the guest network. Remember to abide by the UCSD Guest wifi terms of use
whenever you use the network. Transcribed they are :
* You will use UC San Diego Guest Wireless services in an ethical and lawful manner, including compliance with University policies.
* You will not engage in activities that may degrade network performance, not attempt to compromise network or machine security.
* You will cooperate with us and provide requested information in connection with all security and use matter.
* UC San Diego reserves the right to terminate your connection at any time.
* Your unencrypted Internet traffic will be monitored.

## WPASupplicant
In order for the PI to connect to the UCSD Guest wifi network it must have
the SSID specified in the WPASupplicant file. On flam this file is located
at /etc/wpa_supplicant/wpa_supplicant.conf. This file should read
```
ctrl_interface=DIR=/var/run/wpa_supplicant GROUP=netdev
update_config=1
country=US

network={
	ssid="UCSD-GUEST"
	key_mgmt=NONE
}
```

## The connection script
UCSD Guest wifi requires clients to authenticate through a web form. We wrote
a script to allow the Pis to connect to UCSD Guest by authenticating through
this web form. This script is called resnetconnect2.py and is found in this
repository. It is recommended to place this script in the /etc/ directory.

To have the Pis networking work all the time the script is started via a
systemctl service. To add this service to systemctl open the editor with
the command ```sudo systemctl edit --force --full resnetconnect.service```.
Then paste the following configuration file.
```
[Unit]
Description=Register yourself with the resenet servers
Wants=network-online.target
After=network-online.target
Before=ntp.service

[Service]
Type=simple
User=root
WorkingDirectory=/home/pi
ExecStart=/usr/bin/python /etc/resnetconnect2.py &> /tmp/resnetconnect.log

[Install]
WantedBy=multi-user.target
```
To start this service automatically we need to enable it. Do this with the
following command. ```sudo systemctl enable resnetconnect.service```. Now every
time the Pis restart the script will be run. To make sure the script works
we want to run it manually at this point. The easiest way to do this is
with the command ```sudo systemctl start resnetconnect.service```. Then to
see if the script has finished without errors run ```systemctl status
 resnetconnect.service```. A sucessfuly run will look like this.
```
● resnetconnect.service - Register yourself with the resenet servers
   Loaded: loaded (/etc/systemd/system/resnetconnect.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Sun 2019-09-08 16:01:36 PDT; 6 days ago
 Main PID: 404 (code=exited, status=0/SUCCESS)

Sep 08 16:01:36 flam-1 sudo[900]:     root : TTY=unknown ; PWD=/home/pi ; USER=root ; COMMAND=/usr/sbin/service nt
Sep 08 16:01:36 flam-1 sudo[900]: pam_unix(sudo:session): session opened for user root by (uid=0)
Sep 08 16:01:36 flam-1 sudo[900]: pam_unix(sudo:session): session closed for user root
Sep 08 16:01:36 flam-1 python[404]: Starting
Sep 08 16:01:36 flam-1 python[404]: Slept for 10
Sep 08 16:01:36 flam-1 python[404]: Getting redirect URL.
Sep 08 16:01:36 flam-1 python[404]: Generating form data.
Sep 08 16:01:36 flam-1 python[404]: Making post.
Sep 08 16:01:36 flam-1 python[404]: Done
Sep 08 16:01:36 flam-1 systemd[1]: resnetconnect.service: Succeeded.
```

## Verifying connections
After the script has successfully run make sure you can connect to the internet
by either running an apt update command or pinging example.com.

## Troubleshooting
### No network connection
Run the command ```ip route```. Make sure that there is not a default gateway
added to the ethernet interface. If there is make sure you have set up your
ethernet interface correctly and included the nogateway flag. A good ip route
table looks like this:
```
default via 100.64.64.1 dev wlan0 proto dhcp src 100.64.81.235 metric 303
10.3.14.0/24 dev eth0 proto dhcp scope link src 10.3.14.1 metric 202
100.64.64.0/18 dev wlan0 proto dhcp scope link src 100.64.81.235 metric 303
```
### Exception on line with sudo service ntp restart
Execute the command ```ip route```. Check if the output has two default routes
such as the one below.
```
default via 10.3.14.239 dev eth0 src 10.3.14.11 metric 202
default via 100.64.64.1 dev wlan0 proto dhcp src 100.64.93.103 metric 303
10.3.14.0/24 dev eth0 proto dhcp scope link src 10.3.14.11 metric 202
100.64.64.0/18 dev wlan0 proto dhcp scope link src 100.64.93.103 metric 303
```
If there are two default routes run ```sudo ip route del default```, if there
is only one default you must skip this command. Now you should be able to
ping example.com.

The next step is to install npt using apt with the command ```sudo apt install
ntp```.

After this run ```sudo systemctl start resnetconnect.service``` again. The
output of ```systemctl status resnetconnect.service``` should look something
like this:
```
● resnetconnect.service - Register yourself with the resenet servers
   Loaded: loaded (/etc/systemd/system/resnetconnect.service; enabled; vendor preset: enabled)
   Active: inactive (dead) since Sun 2019-09-15 20:29:33 BST; 9s ago
  Process: 1271 ExecStart=/usr/bin/python /etc/resnetconnect2.py &> /tmp/resnetconnect.log (code=exited, status=0/SUCCE
 Main PID: 1271 (code=exited, status=0/SUCCESS)

Sep 15 20:29:33 flam-11 sudo[1278]:     root : TTY=unknown ; PWD=/home/pi ; USER=root ; COMMAND=/usr/sbin/service ntp r
Sep 15 20:29:33 flam-11 sudo[1278]: pam_unix(sudo:session): session opened for user root by (uid=0)
Sep 15 20:29:33 flam-11 sudo[1278]: pam_unix(sudo:session): session closed for user root
Sep 15 20:29:33 flam-11 python[1271]: Starting
Sep 15 20:29:33 flam-11 python[1271]: Slept for 10
Sep 15 20:29:33 flam-11 python[1271]: Getting redirect URL.
Sep 15 20:29:33 flam-11 python[1271]: We got an error from the socket
Sep 15 20:29:33 flam-11 python[1271]: Seems like we already authenticated.
Sep 15 20:29:33 flam-11 python[1271]: Done
Sep 15 20:29:33 flam-11 systemd[1]: resnetconnect.service: Succeeded.
```
