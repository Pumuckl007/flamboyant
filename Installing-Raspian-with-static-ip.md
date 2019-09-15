# Installing Raspbian

To install Raspbian onto the Raspberry Pis first download the image from the [Raspberry foundation's website](https://www.raspberrypi.org/downloads/raspbian/). Extract the generated zip file and copy it over to an SD card with the dd command.

```bash
$ dd if=/path/to/extracted/raspbian/image of=/media/path/to/sd/card status=progress bs=32M
```

This will set up all of the partitions and wipe the data from the SD card.

## Setting up the network config

To setup the static IP for the Raspberry Pis we will need to edit the dhcpcd.conf file. To do this open the rootfs partition in the terminal, on Ubuntu it is mounted in /media/USERNAME/rootfs/, and cd into the etc directory. Then edit the dhcpcd.conf file.

```bash
$ cd /media/USERNAME/rootfs/etc/
$ nano dhcpcd.conf
```

Comment out every line in the file and append the following.

```
interface eth0

static ip_address=10.3.14.{id}/24
static routers=10.3.14.239
static domain_name_servers=10.3.14.2

nohook lookup-hostname
static domain_search=
nogateway
```

Make sure to replace {id} with the Pi's id. 10-24 for the compute nodes or 1 for the head node.

## Enabling SSH

Finally you will have to enable the ssh client. To do this navigate to the boot partition and create a file called ssh.

```bash
$ cd /media/USERNAME/boot/
$ touch ssh
```

Now the Pi should be set up. Make sure you can SSH into it at the IP you gave it. To do this you might have to set your computer to a static ip in the 10.3.14.[200-220] block.
