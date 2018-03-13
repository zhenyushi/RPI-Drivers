#!/usr/bin/python

import smbus2 as smbus
import time
import numpy as np

chan=1       # 0 for rev1 boards etc.
bus = smbus.SMBus(chan)
address=0x68

ACCEL_XOUT0 = 0x3B
ACCEL_YOUT0 = 0x3D
ACCEL_ZOUT0 = 0x3F

prev_x = 0
prev_y = 0
prev_z = 0

para_exp = 80
a = np.exp(-1*para_exp*0.01)


def read_i2c_word(address,register):
    """Read two i2c registers and combine them.
    register -- the first register to read from.
    Returns the combined read results.
    """
    # Read the data from the registers
    high = bus.read_byte_data(address, register)
    low = bus.read_byte_data(address, register + 1)

    value = (high << 8) + low

    if (value >= 0x8000):
        return -((65535 - value) + 1)
    else:
        return value


if __name__ == '__main__':
    
    while(1):

        x_read = read_i2c_word(address,ACCEL_XOUT0)
        y_read = read_i2c_word(address,ACCEL_YOUT0)
        z_read = read_i2c_word(address,ACCEL_ZOUT0)


        curr_x = np.exp(-1*para_exp*0.01)*x_read + (1-np.exp(-1*para_exp*0.01))*prev_x
        curr_y = np.exp(-1*para_exp*0.01)*y_read + (1-np.exp(-1*para_exp*0.01))*prev_y
        curr_z = np.exp(-1*para_exp*0.01)*z_read + (1-np.exp(-1*para_exp*0.01))*prev_z

        prev_x = curr_x
        prev_y = curr_y
        prev_z = curr_z


        curr_x -= 300
        curr_x /= 16750
        curr_y -= -400
        curr_y /= 16550
        curr_z -= 300
        curr_z /= 16350


        if(1):
            print("x = ",curr_x)
            print("y = ",curr_y)
            print("z = ",curr_z)

        if(0):
            print(x_read)
            print(y_read)
            print(z_read)


