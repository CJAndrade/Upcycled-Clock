#!/usr/bin/python
# Create by Carmelito to show the IP address and temperature on the grove LCD based on
# Grove RGB LCD https://github.com/intel-iot-devkit/upm/blob/master/examples/python/jhd1313m1-lcd.py
# Grove rotary https://github.com/intel-iot-devkit/upm/blob/master/examples/python/groverotary.py
# Grove temp https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovetemp.py
# and for the ip address http://code.activestate.com/recipes/439094-get-the-ip-address-associated-with-a-network-inter/

from upm import pyupm_jhd1313m1 as lcd
from time import sleep
from upm import pyupm_grove as grove
import socket
import fcntl
import struct

def get_ip_address(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    return socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,  # SIOCGIFADDR
        struct.pack('256s', ifname[:15])
    )[20:24])


def main():
    #POT connected to AIO pin 0
    knob = grove.GroveRotary(0)
    #Temperature sensor connected to AIO pin 1
    temp = grove.GroveTemp(1)
    # Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
    myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)
    # Loop indefinitely
    while True:
        # Read values
        abs = knob.abs_value()
        print("Abs values: " + str(abs))
        sleep(1)
        if abs <100:
            myLcd.clear()
            # Set background color to Blue
            myLcd.setColor(0, 0, 255) #RGB
            # Zero the cursor
            myLcd.setCursor(0,0)
            # Print the IP address for wlan0
            ip = get_ip_address('wlan0')
            myLcd.write("IP " + ip)
            sleep(1)
        elif abs >100 and abs <500:
            #Getting grove temperature value
            print(temp.name())
            for i in range(0, 10):
                celsius = temp.value()
                fahrenheit = celsius * 9.0/5.0 + 32.0;
                print("%d degrees Celsius, or %d degrees Fahrenheit" \
                         % (celsius, fahrenheit))
                sleep(1)
            myLcd.clear()
            myLcd.setColor(255, 0, 0) #RGB
            myLcd.setCursor(0,0)
            myLcd.write("Temp "+str(fahrenheit) + " F" )
        else:
            #Printing a big thank you!
            myLcd.clear()
            myLcd.setColor(0, 255, 0) #RGB
            myLcd.setCursor(0,0)
            myLcd.write("Thanks element14")
            myLcd.setCursor(1,0)
            myLcd.write("and Intel")
            sleep(1)

if __name__ == '__main__':
    main()
