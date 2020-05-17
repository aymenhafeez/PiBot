# PiBot
Scripts for a Raspberry Pi robotics project I worked on.

## Parts
Raspberry Pi 3 B+  
L298n H-bridge motor controller  
HC-SR04 ultrasonic distance sensors  
Raspberry pi camera module  
DC motors and wheels  

## Dependencies

### RPi.GPIO
This module allows control of the GPIO pins and should come pre-installed if you
are using Raspbian on your Raspberry Pi. Otherwise, it can be installed with
pip:
```shell
sudo pip install RPi.GPIO
```
### Opencv
Installing opencv on the Raspberry Pi can be a bit awkward and can take several
hours to install all of the relevant dependencies. <a
href="https://hackaday.io/project/7008-fly-wars-a-hackers-solution-to-world-hunger/log/23068-installing-opencv-on-a-raspberry-pi-the-easy-way">This
method</a> outlined by Michael Ratcliffe from Hackaday worked fine for me for
use in this project, and is much less time consuming:
```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libcv-dev
sudo apt-get install python-opencv
sudo apt-get install libopencv-dev
sudo apt-get install libcv2.3
sudo apt-get install opencv-doc
```
A lot of credit goes to <a
href="https://www.youtube.com/user/sentdex">Sentdex</a> and <a
href="https://www.youtube.com/explainingcomputers">Explaining Computers</a>
which helped get me going as I was starting the project.
