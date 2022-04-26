# Installing software from command line

Many programs for cutting-edge science are built by scientists for scientists. This means they often have minimal interface and little to no technical support is available. This means that sometimes installing scientific software is half the challenge. There are many ways you can install new programs on `Ubuntu` and other Unix/Linux-like operating systems. Today we will talk about three: 1) using a package manager, 2) compiling from source code, and 3) installing from PyPI, the Python Package Index. You will need an internet connection for any of this to work. 

## Installing using Ubuntu package manager
Just like you can easily install supported packages in `R` using the so-called R package manager, operating systems have their own managers. For Ubuntu the common package manager is called `aptitude` (more precisely this is only the interface to Ubuntu's package manager). You can install things through this interface using `apt install`. Let us try installing `MrBayes`, which is a commonly-used program for making phylogenetic trees. If you have not used the package manager for a while, first you want to update the catalog of packages available for `aptitude`:
```bash
apt update
```
Depending on how your system is configured, you may find that this does not work because you do not have the right permissions to install new programs. This is to avoid obvious issues with someone doing harm to the system. The solution is to use the `sudo` command. In short, this command gives you priviledges to act as the [superuser](https://en.wikipedia.org/wiki/Superuser):
```bash
sudo apt update
```
This will work on your system but most often will not work on someone else's computer, like the UIdaho cluster. In that case you may need to contact whoever is in charge to install new software for you.
```bash
sudo apt install mrbayes
```
Assuming this worked as intended, `aptitude` should take care of everything for you, including putting `MrBayes` to where it should be, so no need to think about which directory you are when running this command. You can now run MrBayes with:
```bash
mb
```
You can also uninstall programs using `aptitude`:
```bash
sudo apt remove mrbayes
``` 

## Installing from source code
Unfortunately not all software that you may need is available through `aptitude`. Often it is necessary to install things from source code. This often requires downloading some compressed files, unpacking ("unzipping") them, and compiling the code. Our example here will be `bioawk`, a lightning-fast program for many handy operations on genetic data files, including `FASTA` and `FASTQ`, which works very similarly to `awk`, which you already know.

The first step is finding out where you can find source code of the program you need to install. In this case, it is available on the popular code repository called `GitHub`. Go to https://github.com/lh3/bioawk/releases/tag/v1.0 and use point-and-click to download `bioawk` source code in the `tar.gz` format OR copy the link address to the file itself and download from command line:
```bash
wget https://github.com/lh3/bioawk/archive/refs/tags/v1.0.tar.gz
```
This will either download the file to your `Downloads` directory or to wherever you were when running the `wget` command.

The extension `tar.gz` means that this file was archived using the command `tar` and compressed to save space with `gzip`. You can unpack it using `tar` with some hard to remember options:
```bash
tar -xvzf v1.0.tar.gz
```
Now you have a directory with `bioawk` source code files. As you know from the short video you watched, source code for some programs needs to be compiled to use. At this point go inside the newly created directory and look for any files that are called `INSTALL` or `README`. Also note there is no file called `bioawk`. We see there are two readme files, so we look at both. `README.awk` says:
```
The program itself is created by
        make
which should produce a sequence of messages roughly like this:

        yacc -d awkgram.y
```      
Now try running `make`:
```bash
make
```
Unfortunately, here you will see an error that says you are missing something called `yacc`. After some Googling you discover that you can install it with
```bash
sudo apt install bison
```
Now we try `make` again and we see a different error `gcc` is not found. `gcc` is the compiler needed for `C`, the language in which `awk` and `bioawk` are written. We cannot install any programs written in `C` from source code without having a `C` compiler. After more Googling you find out that you can install the `build-essential` suite of packages to get this compiler. This will take a while:
```bash
sudo apt install buld-essential
```
Finally, we should be able to create a compiled bioawk program:
```bash
make
```
You should now see `bioawk` program in the directory you unpacked. You can use it by calling it from this directory, like so `./bioawk` or move it somewhere where the computer will find it wherever you're calling it from:
```bash
sudo cp bioawk /usr/bin/bioawk
```
Now you can all `bioawk` by simply typing `bioawk` anywhere.

## Installing third-party Python modules
We already used the Ubuntu package manager and you may be familiar with the one that comes with `R`. Turns out that Python uses its own package manager called `pip`. There are many Python packages useful in bioinformatics, `Biopython` being one of the most popular. Before we can install it, however, we need to install `pip` using the now-familiar command `apt`:
```bash
sudo apt install python-pip 
```
After this, all it should take is:
```bash
sudo pip install biopython
```
