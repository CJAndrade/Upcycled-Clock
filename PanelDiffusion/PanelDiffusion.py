#Create for the Upcycle clock project using the Intel Edison -- to test the features on the LED duffusion pannels
#Author : @CarmelitoA 05/29/2017
from upm import pyupm_grove as grove
from upm import pyupm_apa102 as mylib
from time import sleep
import sensor_values, weather_condition,traffic_condition,twitter_messages,gmail_check
numberOfLEDs = 31
def panels():
    #POT connected to pin A0 -using this to test the pannels indivisually
    knob = grove.GroveRotary(0)
    # Instantiate the LED strip
    ledStrip = mylib.APA102(numberOfLEDs, 0, False)
    ledStrip.setAllLeds(numberOfLEDs,0,0,0)
    #ledStrip.setLeds(2, 3, 10, 255, 0, 0) #setting 2 and 3  to red of the 10 LEDs
    #ledStrip.setLed(7, 10, 255, 0, 255) #setting 7 to blue only
    #ledStrip.setLeds(4, 5, 10, 255, 255, 0) #yellow
    #ledStrip.setLeds(8, 9, 10, 0, 255, 255) #sky blue
    #ledStrip.setLeds(6, 7, 10, 255, 0, 255) #pink
    #ledStrip.setLeds(6, 7, 10, 100, 100, 100)  #white
    sleep(4)

    print("Weather condition outside - lower most panel")
    outTemp,outHumidity,outCondition = weather_condition.weatherData()
    print ("Weather outside : " + outCondition)
    if outCondition == 'Rains':ledStrip.setLeds(0, 1, numberOfLEDs, 0, 0, 255) #blue for Rains
    elif outCondition == 'Sunny':ledStrip.setLeds(0, 1, numberOfLEDs, 255, 255, 0) #yellow
    else:ledStrip.setLeds(0, 1, numberOfLEDs, 100, 100, 100)#white -Cloudy,Haze,Snow showers
    sleep(5)

    print("Traffic- time to work panel")
    timeToWork = traffic_condition.get_time_intraffic()
    print("Time in traffic" +str(timeToWork))
    if timeToWork <= 30 : ledStrip.setLeds(2, 3, numberOfLEDs, 0, 255, 0)#green leave home now!!
    elif timeToWork>30 and timeToWork>45 : ledStrip.setLeds(2, 3, numberOfLEDs, 0, 255, 255)#yellow-orange
    else:ledStrip.setLeds(2, 3, numberOfLEDs, 255, 0, 0) #>45 mins a lot of traffic
    sleep(5)

    print ("Twitter Pannel")
    hastagCount = twitter_messages.tweet_count_today()
    print ("Upcycleit hashtag count")
    if hastagCount <=5: ledStrip.setLeds(4, 5, numberOfLEDs, 255, 0, 255) #pink
    else:ledStrip.setLeds(4, 5, numberOfLEDs, 0, 0, 255) #more than 5 blue
    sleep(5)

    print ("Gmail - unread emails")
    numberOfEmails = gmail_check.un_read_email()
    print ("Number of unread emails : " + str(numberOfEmails))
    if numberOfEmails >= 5 :ledStrip.setLeds(6, 7, numberOfLEDs, 255, 0, 0) #red
    else:ledStrip.setLeds(6, 7, numberOfLEDs, 0, 255, 0) #green
    sleep(5)

    print ("Home - temperature and Gas")
    airQualityVal = sensor_values.airQuality()
    temperature = sensor_values.temperature()
    print  ("Temperature " + str(temperature) + " C" + "Air quality: " + str(airQualityVal))
    if temperature <30 :ledStrip.setLeds(8, 9, numberOfLEDs, 0, 255, 0) #green don't need to turn on the AC
    else :ledStrip.setLeds(8, 9, numberOfLEDs, 0, 255, 0)
    sleep(5)
