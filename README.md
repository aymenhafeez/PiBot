# PiBot
PiBot is a project aiming to make an autonomous robot. It can currently follow a track by detecting the lane edges through a camera, and avoid obstacles. A lot of the code could do with some cleaning up (for example, the plethora of if/elif statements) , which I will hopefully do eventually, but currently I am just trying to get things to work.

## Parts
Raspberry Pi 3 B+
L298n H-bridge motor controller
HC-SR04 ultrasonic distance sensors
Raspberry pi camera module
DC motors and wheels

### Installing opencv
Installing opencv on the Raspberry Pi can be kind of awkward and can take several hours as it requires building to install ALL of the relevant dependencies. An easy way which works fine for me is the following:
```shell
sudo apt-get update
sudo apt-get upgrade
sudo apt-get install libcv-dev
sudo apt-get install python-opencv
sudo apt-get install libopencv-dev
sudo apt-get install libcv2.3
sudo apt-get install opencv-doc
```
