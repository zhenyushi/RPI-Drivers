#!/usr/bin/python

import time
import RPi.GPIO as GPIO


if __name__ == '__main__':


    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)


    while(1):

        GPIO.setup(21, GPIO.OUT)
        time.sleep(0.002)
        GPIO.output(21, 0)
        time.sleep(0.002)

        GPIO.output(21, 1)

        time.sleep(0.005)

        GPIO.output(21, 0)

        GPIO.setup(21, GPIO.IN)

        while GPIO.input(21)==0:
           starttime=time.time()

        while GPIO.input(21)==1:
           endtime=time.time()

        duration=endtime-starttime
        #print (duration)
        distance=duration*34000/2
        print int(distance)," cm"

        print time.time()


