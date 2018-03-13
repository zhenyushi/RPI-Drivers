#!/usr/bin/python

import smbus2 as smbus
import math
import time


# Registers/etc:
PCA9685_ADDRESS    = 0x40
MODE1              = 0x00
MODE2              = 0x01
SUBADR1            = 0x02
SUBADR2            = 0x03
SUBADR3            = 0x04
PRESCALE           = 0xFE
LED0_ON_L          = 0x06
LED0_ON_H          = 0x07
LED0_OFF_L         = 0x08
LED0_OFF_H         = 0x09
ALL_LED_ON_L       = 0xFA
ALL_LED_ON_H       = 0xFB
ALL_LED_OFF_L      = 0xFC
ALL_LED_OFF_H      = 0xFD

# Bits:
RESTART            = 0x80
SLEEP              = 0x10
ALLCALL            = 0x01
INVRT              = 0x10
OUTDRV             = 0x04



class multiplex:
    
    def __init__(self, bus):
        self.bus = smbus.SMBus(bus)

    def channel(self, address=0x40,reg=0xFE,action=0x00):      
 
        self.bus.write_byte_data(address,reg,action)  


if __name__ == '__main__':

    bus=1       # 0 for rev1 boards etc.
    address=0x40

    prescaleval = 25000000.0    # 25MHz
    prescaleval /= 4096.0       # 12-bit
    prescaleval /= float(50)
    prescaleval -= 1.0
    prescale = int(math.floor(prescaleval + 0.5))

    
    plexer = multiplex(bus)

    plexer.channel(address,MODE1,SLEEP)
    plexer.channel(address,PRESCALE,prescale)
    plexer.channel(address,MODE1, 0x01)
    time.sleep(0.005)
    plexer.channel(address,MODE1, 0x01 | 0x80)

    
    pwm = 400 # 1~400

    off = 100 + pwm

    plexer.channel(address,LED0_ON_L, 0x01 )
    plexer.channel(address,LED0_ON_H, 0x01 >> 8)
    plexer.channel(address,LED0_OFF_L, off & 0xFF)
    plexer.channel(address,LED0_OFF_H, off >> 8)


    while(1):

        pwm = 400 # 1~400
        off = 100 + pwm
        plexer.channel(address,LED0_ON_L, 0x01 )
        plexer.channel(address,LED0_ON_H, 0x01 >> 8)
        plexer.channel(address,LED0_OFF_L, off & 0xFF)
        plexer.channel(address,LED0_OFF_H, off >> 8)


        pwm1 = 400 # 1~400
        off1 = 100 + pwm1
        plexer.channel(address,LED0_ON_L +4, 0x01 )
        plexer.channel(address,LED0_ON_H +4, 0x01 >> 8)
        plexer.channel(address,LED0_OFF_L +4, off1 & 0xFF)
        plexer.channel(address,LED0_OFF_H +4, off1 >> 8)

        time.sleep(0.5)


        pwm = 1 # 1~400
        off = 100 + pwm
        plexer.channel(address,LED0_ON_L, 0x01 )
        plexer.channel(address,LED0_ON_H, 0x01 >> 8)
        plexer.channel(address,LED0_OFF_L, off & 0xFF)
        plexer.channel(address,LED0_OFF_H, off >> 8)


        pwm1 = 200 # 1~400
        off1 = 100 + pwm1
        plexer.channel(address,LED0_ON_L +4, 0x01 )
        plexer.channel(address,LED0_ON_H +4, 0x01 >> 8)
        plexer.channel(address,LED0_OFF_L +4, off1 & 0xFF)
        plexer.channel(address,LED0_OFF_H +4, off1 >> 8)

        time.sleep(0.5)





    print("Done")




