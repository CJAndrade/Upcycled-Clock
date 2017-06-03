#!/usr/bin/python
#create by Carmelito to use espeak to read out the weather on a speaker connected to the Intel Edison
#For more detials on pyowm https://github.com/csparpa/pyowm/blob/master/pyowm/docs/usage-examples.md
#Follow the blog on element14 to install espeak
import subprocess
import pyowm
APIKey = 'XXXXXXXXXXXXXXXXXXXXXXX'
placeName = 'Los Angeles,US'
owm = pyowm.OWM(APIKey)
observation = owm.weather_at_place(placeName)
w = observation.get_weather()

temp = w.get_temperature(unit='celsius')['temp']
status = w.get_status()
detailedStatus = w.get_detailed_status()
windSpeed = w.get_wind()['speed']
humidity = w.get_humidity()
pressure = w.get_pressure()['press']
print ('Temperature : '+ str(temp) + ' C')
print ('Weather Condition : ' + status)
print ('Wind Speed : '+ str(windSpeed) + ' m/s')
print ('Humidity : ' + str(humidity) + ' %')
print ('Pressure : ' + str(pressure) + ' hpa')
print ('Details Weather :' + detailedStatus)

#for the future, read out for the future weather condition
fc = owm.daily_forecast('Los Angeles,US', limit=3)
f = fc.get_forecast()
lst = f.get_weathers()
for weather in f:
      print (weather.get_reference_time('iso'),weather.get_status())
#text that will be spoken out using espeak
text = 'Rise and shine, Todays weather is ' + detailedStatus + ' and the Temperature is '+ str(temp) + ' degree celsius with humidity ' + str(humidity) + ' percent'
try:
    subprocess.check_output(['espeak', text])
except subprocess.CalledProcessError:
    print ("Errr something is not working..")
