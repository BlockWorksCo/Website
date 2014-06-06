Build/Block
============

What is it?
-----------

A virtual machine based toolchain with that uses common Makefile & GDB based interfaces for
building and debugging.
Currently supports Linux, Win32, MSP430, STM32, AVR/Arduino platforms and RaspberryPi.

How many development environments for embedded systems have you collected over the years? 
Each has its own IDE, many versions of eclipse, all with their own perculiarities.

Open; Block/Build is a completely open Vagrant based virtual machine description that will
provision a Linux based virtual machine for building software for multiple targets.

Host-independent; being VM based, all dependencies on the host platform & OS have been 
abstracted away.

Get it.
-------
* Install VirtualBox

* Install Vagrant.

* Download the Rocket/Build Vagrantfile.

* Let Vagrant do the rest.


Why do it?
----------

* Consistency between developers machines.

* Ability to reproduce issues on different machines.

* Easy testing of upgraded environments.

* Time required to setup new users & environments.

* All using same hardware? probably not, so cant easily image machines or standardise installations. 
laptops/desktops/CI servers.

* One build server for multiple incompatible (and compatible) projects.

* Access rights? Nothing need to be installed other than Vagrant, VirtualBox and an IDE of your choice.

* Can compile for multiple versions of the toolchain and switch between them easily.

* Easily version the toolchain for control over release reproducability.

* editor & debugger can be used for all environments. Separates Editor&Debugger from the toolchain.

* Can easily and trasparently switch between a dedicated build server and local builds.

* Open source toolchains are good, but generally hard to setup. Block/Build takes the difficulty 
out of this.

* Host independence; Use Linux, OSX or Windows hosts... this will not affect the software that is 
generated. Even switch between them at will, use your favorite editors from any OS to develop
the software. The Build engine is abtracted from this.

Drawbacks?
----------

* Performance?  Embedded toolchains do not usually take lots of performance.

* Size?  Only toolchains are installed, fairly static.

