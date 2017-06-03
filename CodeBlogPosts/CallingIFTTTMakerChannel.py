#!/usr/bin/python
# Create by Carmelito to send sensor data to IFTTT so that you work your magic,this is based on
# Grove Light sensor https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovelight.py
# Grove Temp https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovetemp.py
# Grove Pot https://github.com/intel-iot-devkit/upm/blob/master/examples/python/groverotary.py
import requests
from time import sleep
from upm import pyupm_grove as grove

#get the api key from Maker Webhooks channel https://ifttt.com/services/maker_webhooks/settings
#example URL https://maker.ifttt.com/use/xxxxxxxxxxxxxxxxxxxxx
api_key = 'xxxxxxxxxxxxxxxxxxxxx'
event = 'from_edison'
#Grove Pot connected to connected A0 on the Grove shield
potSensor= grove.GroveRotary(0)
#Grove Temperature sensor connected A1
tempSensor = grove.GroveTemp(1)
#Grove Light sensor connected A2
lightSensor = grove.GroveLight(2)

def send_IFTTT_event(api_key, event, temp=None, lightValue=None, potValue= None):
    #posting data to IFTTT
    url = "https://maker.ifttt.com/trigger/{e}/with/key/{k}/".format(e=event,k=api_key)
    payload = {'value1': temp, 'value2': lightValue, 'value3': potValue}
    try:
        requests.post(url, data=payload)
    except requests.exceptions.RequestException as resp:
        print("Error from IFTTT: {e}".format(e=resp))

def main():
    temp = '0'
    lightValue = '00'
    #Getting Pot value
    potValue = potSensor.abs_value()
    print("Pot value: " + str(abs))
    sleep(1)
    #Getting grove temperature value
    print(tempSensor.name())
    for i in range(0, 10):
        celsius = tempSensor.value()
        fahrenheit = celsius * 9.0/5.0 + 32.0;
        print("%d degrees Celsius, or %d degrees Fahrenheit" \
                 % (celsius, fahrenheit))
    temp = fahrenheit
    #Getting light sensor value
    print(lightSensor.name() + " raw value is %d" % lightSensor.raw_value() + \
    ", which is roughly %d" % lightSensor.value() + " lux");
    lightValue = lightSensor.raw_value()
    sleep(1)

    send_IFTTT_event(api_key, event, temp, lightValue, potValue)

if __name__ == "__main__":
    main()
