#!/usr/bin/env python
# Create by Carmelito to post data to Cayenne Dashboard using MQTT
# Cayenne https://github.com/myDevicesIoT/Cayenne-MQTT-Python
# Grove temperature sensor- https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovetemp.py
# Grove light sensor - https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovelight.py
# Grove Air quality sensor v1.3- https://software.intel.com/en-us/iot/hardware/sensors/air-quality-sensor


import cayenne.client
import time
from upm import pyupm_grove as grove
from upm import pyupm_gas as TP401 #for the Air quality sensor


# Cayenne authentication info. This should be obtained from the Cayenne Dashboard.
MQTT_USERNAME  = "xxxxxxx-xxxx-xxxxx-xxxx-xxxxxxxxxxx"
MQTT_PASSWORD  = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
MQTT_CLIENT_ID = "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxx"


client = cayenne.client.CayenneMQTTClient()
client.begin(MQTT_USERNAME, MQTT_PASSWORD, MQTT_CLIENT_ID)

# Give a qualitative meaning to the value from the Ait quality sensor
def airQuality(value):
    if(value < 50): return "Fresh Air"
    if(value < 200): return "Normal Indoor Air"
    if(value < 400): return "Low Pollution"
    if(value < 600): return "High Pollution - Action Recommended"
    return "Very High Pollution - Take Action Immediately"
# New Grove Air Quality Sensor on AIO pin 0
airSensor = TP401.TP401(0)


# Wait for Ait quality sensor to warm up - it takes about 3 minutes
print("Sensor is warming up for 3 minutes...")
for i in range (1, 4):
    time.sleep(60)
    print(i, "minute(s) passed.")
print("Sensor is ready!")


#temperature sensor object using AIO pin 1 on the Grove connector shield
temp = grove.GroveTemp(1)
#light sensor object using AIO pin 2
light = grove.GroveLight(2)
while True:
    client.loop()
    print(temp.name())
    # Read the temperature ten times, printing both the Celsius and
    # equivalent Fahrenheit temperature, waiting one second between readings
    #for i in range(0, 10):
    celsius = temp.value()
    fahrenheit = celsius * 9.0/5.0 + 32.0;
    print("%d degrees Celsius, or %d degrees Fahrenheit" \
        % (celsius, fahrenheit))
    time.sleep(1)


    # Read values of the light sensor
    lightLux = light.value()
    print(light.name() + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux");
    time.sleep(1)


    # Read values of Air quality sensor
    airValue = airSensor.getSample()
    ppm = airSensor.getPPM()
    print("raw: %4d" % airValue , " ppm: %5.2f   " % ppm , airQuality(airValue))


    #Uploading data to Cayenne
    print("Uploading data to Cayenne ...")
    client.celsiusWrite(1, celsius)
    client.luxWrite(2, lightLux)
    client.virtualWrite(3, airValue)
    #timestamp = time.time()
    #Sleep for
    time.sleep(5)
