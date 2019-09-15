# Setting up Slurm

The Pis use Slurm as the job scheduler. In this case "jobs" are bash scripts
which users want to run on the cluster. Each job has an associated number of
nodes it wants to run on. Slurm then distributes the nodes among different jobs.
This avoids multiple users running programs on the same nodes.

## Slurm Prerequisites
Slurm requires munge to run. This can be installed via apt with the
command ```sudo apt install munge```. This should start the munge demon which can
be checked with ```systemctl status munge.service```. That command should print
the the service is active.

The next step is to copy the munge key used by flam from flam-1. The munge key
is stored in /usr/local/etc/munge/munge.key. After copying the file use the
chown command to make the user ```munge``` the owner of /usr/local/etc/munge/.
This can be done with the command ```sudo chown -R munge /usr/local/etc/munge/```.
Make sure munge starts again with ```sudo systemctl restart munge.service```
and check the output with ```systemctl status munge.service```.

## Building Slurm
Slurm does not have an arm package so we have to build one ourselves. The latest
version can be found on the
[downloads page](https://www.schedmd.com/downloads.php). After extracting
the file run the configure command with deprecated parts enabled ```./configure --enable-deprecated```.
Then run the make command. Then run ```sudo make install```.

## Setup slurm systemctl
Slurm will not start automatically to make it start we must add a slurm service
to systemctl. Do this by running the command ```sudo systemctl edit --force --full slurmd.service```.
This will allow us to edit the slurmd service. Paste the following
configurations into the opened file.
```
[Unit]
Description=Slurm node daemon
After=munge.service network.target remote-fs.target
ConditionPathExists=/usr/local/etc/slurm.conf

[Service]
Type=forking
EnvironmentFile=-/etc/sysconfig/slurmd
ExecStart=/usr/local/sbin/slurmd $SLURMD_OPTIONS
ExecReload=/bin/kill -HUP $MAINPID
PIDFile=/run/slurmd.pid
KillMode=process
LimitNOFILE=131072
LimitMEMLOCK=infinity
LimitSTACK=infinity
Delegate=yes


[Install]
WantedBy=multi-user.target
```

Next make sure to copy the slurm config file from flam-1 located at
Next we will want to enable the service with ```sudo systemctl enable slurmd.service```
and then start it with ```sudo systemctl start slurmd.service```.
