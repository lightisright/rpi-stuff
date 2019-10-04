import sys
import time
import RPi.GPIO as io
import subprocess
from threading import Thread

io.setmode(io.BCM)

class PirManager(Thread):

    def __init__(self, pir_pin, shutoff_delay, debug):

        Thread.__init__(self)
        self.SHUTOFF_DELAY = shutoff_delay
        self.PIR_PIN = pir_pin
        self.debug = debug


    def print(self, msg):
        if self.debug:
            print(msg)
            sys.stdout.flush()


    def run(self):

        io.setup(self.PIR_PIN, io.IN)
        #io.setup(LED_PIN, io.OUT)
        turned_off = True
        last_motion_time = time.time()

        while True:
        #print io.input(PIR_PIN)
            if io.input(self.PIR_PIN):
                last_motion_time = time.time()
                #io.output(LED_PIN, io.LOW)
                self.print(".")
                if turned_off:
                    turned_off = False
                    self._turn_on()
            else:
                if not turned_off and time.time() > (last_motion_time + self.SHUTOFF_DELAY):
                    turned_off = True
                    self._turn_off()
                #if not turned_off and time.time() > (last_motion_time + 1):
                    #io.output(LED_PIN, io.HIGH)
            time.sleep(.1)

    def _turn_on(self):
        # activate HDMI output & right terminal display
        self.print("PIR ON")
        subprocess.call("tvservice -p && sleep 0.2 && chvt 1 && sleep 0.2 && chvt 2", shell=True)

    def _turn_off(self):
        # deactivate HDMI output
        self.print("PIR OFF")
        subprocess.call("tvservice -o", shell=True)

