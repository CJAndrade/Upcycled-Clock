#!/usr/bin/python
# Created by Carmelito to test LED strip and this is based on
# Grove Pot https://github.com/intel-iot-devkit/upm/blob/master/examples/python/groverotary.py
# Led Strip https://github.com/intel-iot-devkit/upm/blob/master/examples/python/apa102.py
from upm import pyupm_grove as grove
import time, sys, signal, atexit
from upm import pyupm_apa102 as mylib
from time import sleep


def main():
    # Instantiate the strip of 60 LEDs on SPI bus 0 connect Data-D11 and Clk- D13
    ledStrip = mylib.APA102(60, 0, False)
    knob = grove.GroveRotary(0)
    abs = knob.abs_value()
    while True:
        # Read values
        abs = knob.abs_value()
        print("Abs values: " + str(abs))
        lightValue = lightSensor.raw_value()
        print ("Light Value: " + str(lightValue))
        sleep(1)
        if abs <100:
            print("Setting all LEDs to Green")
            ledStrip.setAllLeds(60, 0, 255, 0)
            time.sleep(2)
        elif abs >100 and abs <300:
            print("Setting all LEDs to Red")
            ledStrip.setAllLeds(60, 255, 0, 0)
            time.sleep(2)
        elif abs >300 and abs <600:
            print("Setting all LEDs to Blue")
            ledStrip.setAllLeds(60, 0, 0, 255)


        elif abs >600 and abs <900:
            print("Setting LEDs between 10 and 20 to Red")
            ledStrip.setLeds(10, 20, 60, 255, 0, 0)
            time.sleep(2)
        else:
            print("setting all LEDS off")
            ledStrip.setAllLeds(60,0,0,0)
            time.sleep(2)


if __name__ == '__main__':
    main()  
