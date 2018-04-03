#!/usr/bin/python

import smbus2 as smbus
import time
import numpy as np
import rospy

from visualization_msgs.msg import Marker

import tf

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
    

    rospy.init_node('talker', anonymous=True)
    pub = rospy.Publisher('Visulization', Marker, queue_size=1)
    rate = rospy.Rate(100) 

    while not rospy.is_shutdown():

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


        phi = np.arctan2(curr_y,curr_z)
        theta = -1*np.arcsin(curr_x)


        if(0):
            print("x = ",curr_x)
            print("y = ",curr_y)
            print("z = ",curr_z)
            

        if(1):
            print("Roll = ",phi)
            print("Pitch = ",theta)
            print(' ')


        if(0):
            print(x_read)
            print(y_read)
            print(z_read)

        marker = Marker()
        marker.header.frame_id = "map"
        marker.type = marker.CUBE
        marker.action = marker.ADD
        marker.scale.x = 0.5
        marker.scale.y = 0.5
        marker.scale.z = 0.2
        marker.color.a = 1.0
        marker.color.r = 1.0
        marker.color.g = 1.0
        marker.color.b = 0.0





        #marker.pose.orientation = tf.transformations.quaternion_from_euler(phi, theta, 0)
        marker.pose.orientation.x =tf.transformations.quaternion_from_euler(phi, theta, 0)[0]
        marker.pose.orientation.y =tf.transformations.quaternion_from_euler(phi, theta, 0)[1]
        marker.pose.orientation.z =tf.transformations.quaternion_from_euler(phi, theta, 0)[2]
        marker.pose.orientation.w =tf.transformations.quaternion_from_euler(phi, theta, 0)[3]


        marker.pose.position.x = 1
        marker.pose.position.y = 0
        marker.pose.position.z = 0

        pub.publish(marker)


