# Setting up Wifi

Wifi on the Pis is a bit tricky. This is mainly due to UCSD's wifi protections
for the guest network. Remember to abide by the UCSD Guest wifi terms of use
whenever you use the network. Transcribed they are :
* You will use UC San Diego Guest Wireless services in an ethical and lawful manner, including compliance with University policies.
* You will not engage in activities that may degrade network performance, not attempt to compromise network or machine security.
* You will cooperate with us and provide requested information in connection with all security and use matter.
* UC San Diego reserves the right to terminate your connection at any time.
* Your unencrypted Internet traffic will be monitored.

## The connection script
UCSD Guest wifi requires clients to authenticate through a web form. We wrote
a script to allow the Pis to connect to UCSD Guest by authenticating through
this web form. This script is called resnetconnect2.py and is found in this
repository.

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
