# Remote computing

## Why use remote computing

* Much more resources than your laptop (cpu, memory, disk space)
* Can use for specialized tasks - GPU, software not available locally

## Logging in using SSH

SSH stands for "secure shell". It is allows for a secure transfer of information between two computers. Different remote computers and clusters will have different names. For this tutorial you will log in with your UIdaho credentials by typing the following into the command line:
```
ssh youruidahoemail@jayne.ibest.uidaho.edu
```
For example, if your email is `mborowiec@uidaho.edu` you will type:
```
ssh mborowiec@jayne.ibest.uidaho.edu
```
If this is your first time logging in, you will need to type `yes` to the prompt about adding an SSH key. You will need to type in a password, which will be your UIdaho email password unless you already have a cluster account with another password. Once you are logged in, the basic navigation is the same as in your Lubuntu terminal:
```
ls
cd
mkdir
```
Etc. Computer clusters are usually set up such that each user has restricted access to the file system where they can create and destroy files and directories but cannot modify other user's files or destroy critical infrastructure.

The UIdaho Research Computing and Data Services (RCDS) has access to a number of shared computing resources. The list can be found [here](https://www.hpc.uidaho.edu/compute/Hardware/hardware.html) and [here](https://www.hpc.uidaho.edu/compute/Hardware/Standalone.html). There are a number of standalone servers as well as a super-computer with about 2,500 CPUs. You will need to modify the `ssh` login command from above to access each server and the cluster. [Helpful tutorials](https://www.hpc.uidaho.edu/compute/Tutorials/) are usually maintained by computer cluster staff and UIdaho is no exception. RCDS also occasionally runs workshops on cluster use; check their website for schedule. 

Some of the servers have access restricted in various ways and there is a difference in how they are used. Servers allow you to run programs directly, while the cluster requires that you submit so-called jobs via a special interface that organizes user requests into queues and assigns resources. A popular queuing system also used at UIdaho is `SLURM`.

You can see what resources are available by typing:
```
sinfo
```
This will show you how nodes in the cluster are organized into partitions. You can think of each node as one physical computer. Each node has one or more CPU cores and its own RAM memory. Some nodes also have graphics cards which are used for special kinds of calculations.

When running a program on the cluster you may need to specify a partition where it will be ran. Partitions are like different queues and each has limits on what resources it can use in terms of memory, CPUs, time etc. `sinfo` shows maximum time a program can run on each partition.

Clusters often have a number of programs installed on them but they are not available by default. You can see what programs are there by typing
```
module avail
```
The UIdaho cluster already has an impressive collections of software installed. If you want to add programs, usually you can just ask your system administrator.

Even though our list shows multiple versions of `R` installed, you can confirm that `R` isn't available by trying to type `R` or `Rscript`:
```
R
-bash: R: command not found
Rscript
-bash: Rscript: command not found
```
You can load it by typing:
```
module load R
R
```
On your laptop system create a new file `hello.sh`:
```
#! /bin/bash

sleep 30

echo "hello world from $HOSTNAME"
``` 
The `sleep` command makes the shell wait for 30 seconds before moving on. We will use this time to see where this script runs.

You can upload files into the remote computer using `sftp` (Secure File Transfer Protocol) instead of `ssh`. It is most convenient to keep `ssh` open and go to another tab or window.
```
sftp youruidahoemail@jayne.ibest.uidaho.edu
```
This will open a "tunnel" between your current working directory and your home directory on the cluster. You can orient yourself in the remote system by typing `pwd` and `lpwd` to see where you are on your local machine:
```
pwd
lpwd
```
`sftp` is a limited interface but you can use `ls` and `mkdir` to list files and make new directories, respectively, on the remote system and `lls` and `lmkdir` to accomplish the same on your local system. Analogous with `cd` and `lcd`. 

The two most useful commands in `sftp` are `put` and `get`. The former allows you to upload and the latter download. Let's upload our `hello.sh` script:
```
mkdir Sandbox
cd Sandbox
put hello.sh
```
Go back to your `ssh` terminal and look for the file. We can now submit our first job to the cluster:
```
sbatch hello.sh
```  
To check on the status of your job run
```
squeue -u youruidahoemail
```
This should show it as running for about 30 seconds because of the `sleep` command. You can see things like status and time, nodes on which it was ran etc. Sometimes large or long jobs will wait in the queue and/or take a while to complete. You will see that the job was assigned to a partition. After 30 seconds take a look at the output. `SLURM` assures that nothing gets printed to screen but goes into files instead. If you type `ls` you will see a file called `slurm-jobnumber.out`. You can view it with `cat` and, after switching to the `sftp` terminal, download:
```
get slurm-jobnumber.out
```
It will now sit in your local working directory.

This example was trivial. What we often want to do is to run a script using `SLURM` with some additional information, like number of nodes or cpus requested, specific partition, time allowed for the job to run, email address to notify when the script finished running etc. `SLURM` offers great flexibility in this but you need another script to accomplish this. Scripts running other scripts/computer programs are often called wrappers. Let's write a simple `R` script and `SLURM` wrapper for `sbatch` command that will run it in a specific partition. Your R script can simply contain:
```
rnorm(25)
```
This call of the `rnorm` function will draw 25 random numbers from normal distribution. Put it into `normal.R` file. Now make a `SLURM` script called `r-job1.sh` like this:
```
#! /bin/bash

#SBATCH -p tiny

module load R

Rscript normal.R

echo "Finished"
```
Normally `#` indicates comments and will be skipped by the computer. The `sbatch` command, however, will interpret any line starting with `#SBATCH` as an option. In this case we tell it to run this on the partition called `tiny`. These partitions are designed for quick jobs that don't require much resources, guaranteeing quick turnaround times and that your jobs won't be waiting in the queue.

Now we can upload both and run the wrapper with
```
sbatch r-job1.sh 
``` 
The job should run and finish instantly and you will see its output in the more recent `slurm-jobnumber.out` file.