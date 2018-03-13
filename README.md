# RPI_drivers
Sample codes for driving different hardware with Raspberry Pi 

## Hardware
Raspberry Pi Zero Wireless<br />
PCA9685 I2C 16 Channels PWM driver (driving standard PWM servo)<br />
MPU 9250 9 Axes Accelerometer<br />
TCA9548A 8 Channels I2C Multiplexer<br />
28015 REV C PING))) Ultrasonic Distance Sensor<br />

## Software
### Raspberry Pi
Raspbian Jessie Lite<br />
ROS
### PC
putty<br />
Winscp<br />
Advanced IP Scanner<br />
Win32DiskImager<br />

## Relvant Links
Raspberry Pi headless setup: https://hackernoon.com/raspberry-pi-headless-install-462ccabd75d0 <br />
I2C need to be enabled: https://learn.adafruit.com/adafruits-raspberry-pi-lesson-4-gpio-setup/configuring-i2c

## Relvant Issues
Show all connected I2C devices:
~~~
$ sudo i2cdetect -y
~~~
Make the scripts executable:
~~~
$ chmod +x something.py
~~~
