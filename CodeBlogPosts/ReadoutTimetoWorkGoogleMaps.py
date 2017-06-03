#!/usr/bin/python
# Create by Carmelito to test time it would take to get to work using Google Maps API and LED strip, and this is based on
# Google Maps API -Distance Matrix - https://developers.google.com/maps/documentation/distance-matrix/intro#traffic-model
# Grove Button https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovebutton.py
# Led Strip https://github.com/intel-iot-devkit/upm/blob/master/examples/python/apa102.py


import urllib2, json
from upm import pyupm_grove as grove
from upm import pyupm_apa102 as mylib
import time
import subprocess

def get_time_intraffic():
    #modify the URL below based to add your orgin, destination address and API Key from google
    response = urllib2.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?origins=395+santa+monica+place,+Santa+Monica,+CA&destinations=2… ')
    data = json.load(response)
    timeInTraffic = data['rows'][0]['elements'][0]['duration']['value']
    distanceInTraffic = data['rows'][0]['elements'][0]['distance']['value']
    print ('distance :'+str(distanceInTraffic/1000)+ ' km' + ' time to work :' + str(timeInTraffic/60) + ' mins')
    return timeInTraffic/60


def main():
    #Grove button connected to D2 on grove connector shield
    button = grove.GroveButton(2)
    # Grove light sensor connected to A2
    lightSensor = grove.GroveLight(2)
    #Instantiate a strip of 30 LEDs on SPI bus 0 connect data-D12 and Clk - D11
    ledStrip = mylib.APA102(60, 0, False)
    ledStrip.setAllLeds(61,0,0,0)
    time.sleep(1)
    text = 'Hello from the Intel Edison'
    while True:
        print(button.name(), ' value is ', button.value())
        print ("Light Value: " + str(lightSensor.raw_value()))
        if button.value() == 1:
            #get the time to work from home in mins
            timeInTraffic = get_time_intraffic()
            print (timeInTraffic)
            if timeInTraffic < 30:
                print("Setting all LEDs to Green- time to leave now")
                text = 'Leave now, there is no traffic, time to work  '+str(timeInTraffic) +'   minutes'
                try:
                    subprocess.check_output(['espeak', text])
                except subprocess.CalledProcessError:
                    print ("Something is not working..")
                ledStrip.setAllLeds(61, 0, 255, 0)
                time.sleep(2)
            elif timeInTraffic >= 30 and timeInTraffic <40:
                print("Setting all LEDs to orange - hmm flip a coin")
                text = 'Hmm, there is seems to be some traffic,  time to work  '+str(timeInTraffic) +'   minutes'
                try:
                    subprocess.check_output(['espeak', text])
                except subprocess.CalledProcessError:
                    print ("Something is not working..")
                ledStrip.setAllLeds(61, 200, 100, 100)
                time.sleep(2)
            elif timeInTraffic >= 40:
                print("Setting all LEDs to Red - to much traffic")
                text = 'It a bad idea to leave now, there is a lot of traffic and the time to work is  '+str(timeInTraffic) +'   minutes'
                try:
                    subprocess.check_output(['espeak', text])
                except subprocess.CalledProcessError:
                    print ("Something is not working..")
                ledStrip.setAllLeds(61, 255, 0, 0)
                time.sleep(2)
            else:
                print("Do nothing")
        if lightSensor.raw_value() < 150:
            print("Light value below threshold, setting all LEDS off")
            ledStrip.setAllLeds(61,0,0,0)
            time.sleep(2)
        time.sleep(1)
    # Delete the button object
    del button


if __name__ == '__main__':
    main()  
