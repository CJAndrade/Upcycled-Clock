#Create for the Upcycle clock project using the Intel Edison -- to get the sensor values connected to the Grove shield
#Author : @CarmelitoA 05/28/2017
#Based on the python examples intels UPM - https://github.com/intel-iot-devkit/upm/tree/master/examples/python
from time import sleep
from upm import pyupm_grove as grove
from upm import pyupm_gas as TP401
#Grove temperature sensor connected A2 on the Grove connector shield
temp = grove.GroveTemp(2)
#Grove light sensor connected to pin A3
light = grove.GroveLight(3)
#Grove Air Quality Sensor on A1 - note the sensor take 3 mins to heat up and get ready
airSensor = TP401.TP401(1)

#getting the temperature in C
#Grove temperature sensor- https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovetemp.py
def temperature():
    celsius = temp.value()
    fahrenheit = celsius * 9.0/5.0 + 32.0;
    print("%d degrees Celsius, or %d degrees Fahrenheit" \
        % (celsius, fahrenheit))
    return celsius

# Grove light sensor - https://github.com/intel-iot-devkit/upm/blob/master/examples/python/grovelight.py
def lightValue():
    # Read values of the light sensor , in approx lux
    lightLux = light.value()
    print(light.name() + " raw value is %d" % light.raw_value() + \
        ", which is roughly %d" % light.value() + " lux");
    return lightLux

# Grove Air quality sensor v1.3- https://software.intel.com/en-us/iot/hardware/sensors/air-quality-sensor
def airQuality():
    #Wait for Air quality sensor to warm up - it takes about 3 minutes
    print("Sensor is warming up for 3 minutes...")
    for i in range (1, 4):
        sleep(60)
        print(i, "minute(s) passed.")
    print("Sensor is ready!")
    # Read values of Air quality sensor
    airValue = airSensor.getSample()
    ppm = airSensor.getPPM()
    print("raw: %4d" % airValue , " ppm: %5.2f   " % ppm)
    return airValue
#Grove Air Quality sensor descriptive format based on the sensor value
def airQualityDesc():
    value = airQuality()
    if(value < 50): return "Fresh Air"
    if(value < 200): return "Normal Indoor Air"
    if(value < 400): return "Low Pollution"
    if(value < 600): return "High Pollution - Action Recommended"
    return "Very High Pollution - Take Action Immediately"
