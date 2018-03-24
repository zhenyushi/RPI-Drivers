#!/usr/bin/python

import time
import RPi.GPIO as GPIO


if __name__ == '__main__':


    
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(21, GPIO.OUT)



    while(1):

        GPIO.setup(21, GPIO.OUT)
        GPIO.output(21, 0)
        time.sleep(2)



        time.sleep(2)
        print time.time()


