#Create for the Upcycle clock project using the Intel Edison -- to get the weather from OpenWeatherMap
#Author : @CarmelitoA 05/28/2017
from time import sleep
import pyowm
APIKey = 'XXXXXXXXXXXXXXXXX'
placeName = 'Los Angeles,US'
owm = pyowm.OWM(APIKey)
observation = owm.weather_at_place(placeName)
w = observation.get_weather()

def weatherData():
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
    return temp,humidity,status

outTemp,outHumidity,outCondition = weatherData()
print ("Weather " +outCondition)

#Getting forecast
#fc = owm.daily_forecast('Los Angeles,US', limit=3)
#f = fc.get_forecast()
#lst = f.get_weathers()
#for weather in f:
#      print (weather.get_reference_time('iso'),weather.get_status())
