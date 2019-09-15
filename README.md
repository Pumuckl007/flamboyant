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
	* Pros: 
		* **Rasbian is the official linux distribution for Pis.** While other linux distributions support the Pi unofficially, our team did not find sufficient comparative advantage justify the loss of official support. 
		* **Rasbian is a minimal installation.** Other officially supported OS's, like NOOBS, come bundled with extraneous software that is unessential to the cluster. A major goal of Flamboyant is training team members in cluster construction and management. For this reason, starting from a minimal installation is preferable.
		* **We are most comfortable with Debian.** Some team members even have linux experience exclusively with Debian and Ubuntu.
		* **Rasbian is stable.** Debian updates rarely, meaning that a known good configuration will stay good for a long time.
	* Cons:
		* **Comet uses CentOS** Due to the changed OS, there will be some minor differences compared to our experience working with the Comet cluster.
		* **Rasbian is stable.** Cutting edge features and security patches will be more difficult to obtain if required compared with other linux distributions.
		* **Rasbian is the default** There may be a much more advantageous OS out there.
		
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
	* Pros:
		* **SLURM schedules jobs** Slurm allows many users to leverage the cluster without crowding each other out.
		* **SLURM is used on Comet** Our advisors have a wealth of experience in configuring this scheduler.
		* **SLURM is commonly used on supercomputing clusters** It occupies some 60% of supercomputers in the TOP500.
	* Cons:
		* **SLURM is CLI by default** The undergraduates and visual arts people who are expected to use Flamboyant will be required by default to submit jobs on the command line.
		* **SLURM is asynchronous** Slurm will make Flamboyant ill suited to certain types of real-time interactive jobs. Generated visual media will have to be stored. This is partially mitigated by the reservation of interactive nodes.
		* **SLURM has overhead in terms of computing power and configuration complexity** Slurm does not pay for itself if too few people use Flamboyant. This is mitigated by the educational advantages of comfiguring Slurm.
		
* Monitoring: [Grafana](https://grafana.com/grafana)
	*  Version: 6.3.2
	*  Release Date: [08-07-2019](https://grafana.com/grafana/download)
	* [Documentation](https://grafana.com/docs/)
	* [Integration](https://grafana.com/products/cloud#features)
	* Pros:
		* **Grafana monitors nodes** Grafana enables analysis and optimization of the cluster.
		* **Grafana is visual** Grafana has lots of pretty graphs and dashboards to present to tourists and patrons.
	* Cons:
		* **Grafana runs a daemon on every node** There will be a performance penalty.
		* **Grafana requires a central server** A Pi or some other computer will have allocated to the cluster and installed with a GUI to act as the Grafana server. Alternatively, a cloud server may be purchased.
	
* [Remote Access](https://www.raspberrypi.org/documentation/remote-access/)
	* Pros:
		* **Team members may contribute without being on campus** There are some members who cannot frequently travel to SDSC, some are even out of the country.
	* Cons:
		* **Open access** Remote access is a substantial attack vector and greatly increases our vulnerability surface.

_______________________________________________________________________________
				Applications
_______________________________________________________________________________
* Containers:
	* [Singularity](https://sylabs.io/singularity/):
		* Version: 3.3
		* Release Date: [07-31-19](https://github.com/sylabs/singularity/releases/tag/v3.3.0)
		* [Documentation](https://sylabs.io/guides/3.3/user-guide/)
		* Pros:
			* **Singularity is a container** Singularity allows user applications to run with dependencies that are not installed on the base system.
			* **Singularity lengthens the lifespan of known good configurations** System administration is not necessarily required to modify cluster images when a software package updates. 
		* Cons:
			* **Singularity has computational overhead** Applications run slower in Singularity. 
			* **Singularity makes job creation more complicated** Users who's applications require extra dependencies must bundle their jobs into singularity containers. This places an additional barrier to entry.
	* [Docker (via Singularity)](https://sylabs.io/guides/3.3/user-guide/singularity_and_docker.html)
		* [Community Edition for Debian](https://docs.docker.com/install/linux/docker-ce/debian/)
		* Install via [script](https://docs.docker.com/install/linux/docker-ce/debian/#install-using-the-convenience-script)
		* [Prerequisites](https://docs.docker.com/install/linux/docker-ce/debian/#prerequisites)
			* 64-bit version of either Buster 10 or Stretch 9 (stable)/Raspbian Stretch
		* Pros:
			* **Docker is more popular than Singularity** Users are more likely to be familar with container creation. It is easier to find pre-built containers for a particular job.
		* Cons:
			* **Docker has computational overhead** Yo Dawg, I heard you like containers, so we put a container in a container for even less performance.
			
* File System: [Lustre](http://lustre.org/about/)
	* Version: 2.10.8/2.12.2
	* Release Date:  [05-27-19](http://lustre.org/lustre-2-10-8-released/)
	* [Documentation](http://lustre.org/documentation/)
	* 64-bit architectures are recommended for servers
	* Supports Ethernet and InfiniBand networks
	* Pros:
		* **Lustre grants uniform storage access from any node** Jobs can access and store files without explicitly transfering data between nodes.
		* **Lustre allows nodes to be reset between jobs** Jobs can be expected to store results on the Lustre filesystem.
	* Cons:
		* **Lustre increases network load** Data is sent over the network to the storage servers. 
		* **Lustre increases configuration complexity** Lustre requires a metadata server and object storage server to be provisioned, among other things.
	
