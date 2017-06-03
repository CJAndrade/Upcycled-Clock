#Create for the Upcycle clock project using the Intel Edison -- display stuff on the Grove RGB LCD screen
#Author : @CarmelitoA 05/28/2017
from time import sleep
from upm import pyupm_jhd1313m1 as lcd
from upm import pyupm_grove as grove
import alarms,call_IFTTT
import get_IP, sensor_values, weather_condition,traffic_condition

import datetime

sleepTime = 3
#POT connected to pin A0
knob = grove.GroveRotary(0)
button1 = grove.GroveButton(2)
button2 = grove.GroveButton(3)
# Grove RGB LCD https://github.com/intel-iot-devkit/upm/blob/master/examples/python/jhd1313m1-lcd.py
# Initialize Jhd1313m1 at 0x3E (LCD_ADDRESS) and 0x62 (RGB_ADDRESS)
myLcd = lcd.Jhd1313m1(0, 0x3E, 0x62)

def showOnLCD(line1, line2, color):
    myLcd.clear()
    # Set background color
    if(color == 'blue'): myLcd.setColor(0, 0, 255) #blue
    if(color == 'green'): myLcd.setColor(0, 255, 0) #Green
    if(color == 'red'): myLcd.setColor(255, 0, 0) #Red
    if(color == 'yellow'): myLcd.setColor(255, 255, 0) #yellow
    # Zero the cursor
    myLcd.setCursor(0,0)
    myLcd.write(line1)
    myLcd.setCursor(1,0)
    myLcd.write(line2)
    sleep(sleepTime)

def main():
    # Loop indefinitely - and get POT values
    #outTemp,outHumidity,outCondition,outWindSpeed = weather_condition.weatherData()
    #airQualityDesc = sensor_values.airQualityDesc()
    while True:
        # Read values
        abs = knob.abs_value()
        button1Val = button1.value()
        button2Val = button2.value()
        print("button 1:", button1Val)
        print("button 2:", button1Val)
        print("Abs values: " + str(abs))
        sleep(0.5)
        if abs <100:
            print ("alarm 1")
            alarms.set_alarm1()
            #showOnLCD("Set Alarm 1", " 06:30", "red")

        elif abs >=100 and abs <200:
            print ("alarm 2")
            alarms.set_alarm2()
            #showOnLCD("Set Alarm 2", " 07:00", "blue")

        elif abs >=200 and abs <300:
            temperature = sensor_values.temperature()
            line2 = str(temperature) + " C"
            showOnLCD("Inside Temp :", line2, "green")
            print temperature

        elif abs >=300 and abs <400:
            print ("Temperature and humidity outside from openWeatherMap")
            outTemp,outHumidity,outCondition,outWindSpeed = weather_condition.weatherData()
            line1 = "Out Temp:"+ str(outTemp) + " C"
            line2 = "Humidity:" + str(outHumidity) + " %"
            showOnLCD(line1, line2, "blue")
            if button1Val == 1:
                showOnLCD("Weather outside", str(outCondition), "green")
            if button2Val == 1:
                line2 = str(outWindSpeed) + " m/s"
                showOnLCD("Wind Speed ", line2, "red")
            sleep(2)

        elif abs >=400 and abs <500:
            print ("Gas sensor")
            showOnLCD("Gas Sensor is", " heating up.. ", "yellow")
            airQualityDesc = sensor_values.airQualityDesc()
            sleep(5)
            showOnLCD(" Air Quality :", airQualityDesc, "green")
            sleep(5)

        elif abs >=500 and abs <600:
            IP = get_IP.getIP()
            print IP
            line2 = "IP: "+ str(IP)
            showOnLCD("Maintenance ..",line2, "green")

        elif abs >=600 and abs <700:
            print ("Time to work")
            timeToWork = traffic_condition.get_time_intraffic()
            line2 = str(timeToWork) + " mins"
            showOnLCD("Time to Work",line2, "red")

        elif abs >=700 and abs <800:
            print("Turn on/off the Light via IFTTT")
            showOnLCD("HUE Lights","ON/OFF", "red")
            if button1Val == 1:
                call_IFTTT.send_IFTTT_event('HUEON')
            if button2Val == 1:
                call_IFTTT.send_IFTTT_event('HUEOFF')

        elif abs >=800 and abs <950:
            print("Hue party mode")
            showOnLCD("HUE Lights","Cycle colors", "red")
            if button1Val == 1:
                call_IFTTT.send_IFTTT_event('HUECOLOR')

        else:
            date = datetime.datetime.now().date()
            print(date)
            line1 = "Date: "+str(date)
            #line2 = "A:06:30 "+"A2:07:00"
            line2 = "A:"+str(alarms.readAlarm1())+ "A2:"+str(alarms.readAlarm2())
            showOnLCD(line1,line2, "red")

if __name__ == '__main__':
    main()
