#!/usr/bin/env python

# =============================================
# Slideshow GPIO commands listener script
# =============================================
# Version : 0.1
# Status : sid
# Date / Author : 2015-01-04 / XCO
# =============================================

import sys
import time
import RPi.GPIO as io
import subprocess

io.setmode(io.BCM)


PIR_PIN = 17        # 11 on the board

# Listen to GPIO 22, 23, 24, 25


#LED_PIN = 16	    # NOT USED FOR NOW

def main():
    io.setup(PIR_PIN, io.IN)
    #io.setup(LED_PIN, io.OUT)
    turned_off = False
    last_motion_time = time.time()

    while True:
	#print io.input(PIR_PIN)
        if io.input(PIR_PIN):
            last_motion_time = time.time()
            #io.output(LED_PIN, io.LOW)
            print ".",
            sys.stdout.flush()
            if turned_off:
                turned_off = False
                turn_on()
        else:
            if not turned_off and time.time() > (last_motion_time + 
                                                 SHUTOFF_DELAY):
                turned_off = True
                turn_off()
            #if not turned_off and time.time() > (last_motion_time + 1):
                #io.output(LED_PIN, io.HIGH)
        time.sleep(.1)

def turn_on():
    subprocess.call("sh /opt/slideshow/hdmi-on.sh", shell=True)

def turn_off():
    subprocess.call("sh /opt/slideshow/hdmi-off.sh", shell=True)

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        io.cleanup()

