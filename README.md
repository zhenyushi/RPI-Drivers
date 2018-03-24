# RPI_drivers
Sample codes for driving different hardware with Raspberry Pi 

## Hardware
Raspberry Pi Zero Wireless<br />
- datasheet: https://cdn-learn.adafruit.com/downloads/pdf/introducing-the-raspberry-pi-zero.pdf

PCA9685 I2C 16 Channels PWM driver<br />
- datasheet: https://cdn-shop.adafruit.com/datasheets/PCA9685.pdf

MPU 9250 9 Axes Accelerometer<br />
- datasheet: https://www.invensense.com/wp-content/uploads/2015/02/PS-MPU-9250A-01-v1.1.pdf

TCA9548A 8 Channels I2C Multiplexer<br />
- datasheet: http://www.ti.com/lit/ds/symlink/tca9548a.pdf

28015 REV C PING))) Ultrasonic Distance Sensor<br />
- datasheet: http://users.ece.utexas.edu/~valvano/Datasheets/PingDocs.pdf

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
WIFI setup:<br />
- Add the following lines to `/etc/wpa_supplicant/wpa_supplicant.conf`:
~~~
network={
ssid="MySSID"
psk="MyPsk"
key_mgmt=WPA-PSK
}
~~~~

- Set WIFI connection to defult, change the couter line in `etc/network/interfaces` to:
~~~
auto wlan0
~~~

Show all connected I2C devices:
~~~
$ sudo i2cdetect -y
~~~
Make the scripts executable:
~~~
$ chmod +x something.py
~~~