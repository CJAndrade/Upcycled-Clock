## Detect door opening to make the clock Speak
As part of this feature, allow the clock to detect opening of the door in the evening when I get back home from work to read out the temperature, weather condition and tweets. After looking into my components box at home, I found two thing that would help me achieve this, that is an ESP8266 board and Magnetic contact switch aka a door sensor. Basically as part of the setup I am using MQTT to publish a message from the ESP8266 when the door opened, which is then received by the Intel Edison attached at the back of the clock , that reads out the weather condition and tweets via a speaker connected to a USB soundcard.


Upload the code ESP8266_door_publish.ino file to the ESP8266 Huzzah using the Arduino IDE, follow the guide at - https://learn.adafruit.com/adafruit-huzzah-esp8266-breakout

Now to implement the feature on your Edison download the DoorMQTT folder from the github repo and run the following commands to setup a service to autorun every morning.

    mkdir Upcycled-Clock
    cd Upcycled-Clock
    svn checkout https://github.com/CJAndrade/Upcycled-Clock/trunk/DoorMQTT
    cd DoorMQTT
    chmod +x door_subscribe.py

put the file readouts.service in  /lib/systemd/system/ and enable the service

    cp readoutdoor.service /lib/systemd/system/readoutdoor.service
    systemctl enable readoutdoor.service
    systemctl start readoutdoor.service

to check the status of the service use

    systemctl status readoutdoor.service

For more info on how to setup USB sound card and eSpeak, checkout the blog post at

https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/04/30/upcycled-clock-getting-the-weather-using-espeak
