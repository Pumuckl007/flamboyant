# Flamboyant Cluster
### A student built and maintained Raspberry Pi cluster hosted by the Supercomputing Club at UCSD, sponsored by the San Diego Supercomputer Center.

_______________________________________________________________________________
				Hardware
_______________________________________________________________________________
* (16) Raspberry Pi 4 Model B ([Specs here, ](https://www.raspberrypi.org/products/raspberry-pi-4-model-b/specifications/) [details here](https://static.raspberrypi.org/files/product-briefs/Raspberry-Pi-4-Product-Brief.pdf))
	* A 1.5GHz quad-core 64-bit ARM Cortex-A72 CPU (~3× performance)
	* 1GB, 2GB, or 4GB of LPDDR4 SDRAM
	* Full-throughput Gigabit Ethernet
	* Dual-band 802.11ac wireless networking
	* Bluetooth 5.0
	* Two USB 3.0 and two USB 2.0 ports
	* Dual monitor support, at resolutions up to 4K
	* VideoCore VI graphics, supporting OpenGL ES 3.x
	* 4Kp60 hardware decode of HEVC video

_______________________________________________________________________________
				Infrastructure
_______________________________________________________________________________
* OS: [Raspbian Buster Lite ](https://www.raspberrypi.org/documentation/raspbian/)
	* Minimal image based on Debian Buster 10
	* Version: July 2019
	* Release Date: [2019-07-10](https://www.raspberrypi.org/downloads/raspbian/)
	* Kernel Version: 4.19.57
	* Size: 426 MB
	* SHA-256: 9e5cf24ce483bb96e7736ea75ca422e3560e7b455eee63dd28f66fa1825db70e
	* Package Manager: [Apt](https://www.raspberrypi.org/documentation/linux/software/apt.md)
	* [Configuration Details](https://www.raspberrypi.org/documentation/configuration/)
	* [Preinstalled Software](https://www.raspberrypi.org/documentation/usage/)
* Scheduling: [SLURM](https://slurm.schedmd.com/overview.html)
	* Version:
		* 19.05.1-2
			* md5: 35aa79ab7830f5914d6863957089d1f2
			* sha1: 1b43cdf3382889c1716c22c0c52efa53fce6dfe6
		* 18.08.8
			* md5: ca5d91345415363a60b40c26631c7572
			* sha1: 4a2c176b54a56763704bcc7abfd9b8a4f91c82b8
	* Release Date [07-10-19](https://www.schedmd.com/downloads.php)
	* Supported OS: Debian (jessie, stretch, buster, and newer)
	* [Documentation](https://slurm.schedmd.com/documentation.html)
* Monitoring: [Grafana](https://grafana.com/grafana)
	*  Version: 6.3.2
	*  Release Date: [08-07-2019](https://grafana.com/grafana/download)
	* [Documentation](https://grafana.com/docs/)
	* [Integration](https://grafana.com/products/cloud#features)
* [Remote Access](https://www.raspberrypi.org/documentation/remote-access/)

_______________________________________________________________________________
				Applications
_______________________________________________________________________________
* Containers:
	* [Singularity](https://sylabs.io/singularity/):
		* Version: 3.3
		* Release Date: [07-31-19](https://github.com/sylabs/singularity/releases/tag/v3.3.0)
		* [Documentation](https://sylabs.io/guides/3.3/user-guide/)
	* [Docker (via Singularity)](https://sylabs.io/guides/3.3/user-guide/singularity_and_docker.html)
		* [Community Edition for Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
		* Install via [script](https://docs.docker.com/install/linux/docker-ce/debian/#install-using-the-convenience-script)
		* [Prerequisites](https://docs.docker.com/install/linux/docker-ce/debian/#prerequisites)
			* 64-bit version of either Buster 10 or Stretch 9 (stable)/Raspbian Stretch
* File System: [Lustre](http://lustre.org/about/)
	* Version: 2.10.8/2.12.2
	* Release Date:  [05-27-19](http://lustre.org/lustre-2-10-8-released/)
	* [Documentation](http://lustre.org/documentation/)
	* 64-bit architectures are recommended for servers
	* Supports Ethernet and InfiniBand networks
