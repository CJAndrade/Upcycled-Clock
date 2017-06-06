# Upcycle Clock – using the Intel Edison
## Introduction
This is a code repository for the Upcycle Clock project – using the Intel Edison, which was part of Upcycle It design challenge hosted by element14.com and sponsored by Intel. As part of the challenge, I set-out modifying an old clock by removing the glass panel and replacing them with 3D printed part, printed in wood filament and LED diffusion panels printed in transparent PLA, and the Intel Edison and sensor added at the  back of the clock.

![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25612-419560/DSC05440+%28another+copy%29.JPG)

For more details on the features of the Upcycle Clock and the list of blog post that contain the build instruction check out blog post at-
https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/06/03/upcycled-clock-summary

## Hardware requirements
Here are the list of components and sensor connections to the Intel Edison
- A0 – Potentiometer which is used to control features on the clock and display things like weather condition, Temperature extra.
- D2 – Top button
- D3 -  Bottom button
- D5 – Grove buzzer sensor for sound notification
- D11 - LED strip (APA102) Data
- D13 – LED strip Clock
- A1 – Grove Air quality sensor v1.3
- A2 – Grove temperature sensor
- A3 – Grove Light sensor
- I2C connector on grove shield (A4, A5) - connected to the Grove RGB LCD display

![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25625-419450/circuitSidebySide.png)

In addition, I am also using Adafruit’s Stereo 3.7W Class D Audio Amplifier - MAX98306 with a 4 ohms 3 watt speaker connected to the USB sound card, which you see on the left of the picture above. But I should have ideally gone with Adafruit Mono 2.5W Class D Audio Amplifier - PAM8302, since I am using only one speaker,which means I will have to order one later.

To power the Intel Edison I am using the power adapter that came in as part of the kit that is Triad Magnetic  WSX120-2000 AC/DC Power Supply 1 Output 24 W 12 V,2 A. And power the LED strip I am currently using another power adapter 5V and 2.5 A.

## Software requirements
Flash the latest Yacto image on the Intel Edison , follow the guide on the Intel website - https://software.intel.com/en-us/flashing-firmware-on-your-intel-edison-board-linux

Once done,run the following commands on the edison to get the latest version of MRAA library and UPM
    
    echo "src mraa-upm http://iotdk.intel.com/repos/3.5/intelgalactic" > /etc/opkg/mraa-upm.conf
    $opkg update
    $opkg install mraa
    $opkg install upm
Intall pip to install the other packages required
   
    $opkg install python-pip

Install pyOWM which is a python wrapper for the OpenWeatherMap.org API

    $pip install pyowm
    
For twitter, install tweepy which is a python wrapper for the twitter API

    $pip install tweepy
To upload sensor data to Cyanne dashboard, which is a IoT platform

    $pip install cayenne-mqtt  

For sound using an USB sound card, install ALSA

    $opkg install alsa-utils
and create the asound.conf file in the /etc folder

    $vi /etc/asound.conf
and add the line
pcm.!default sysdefault:Device 
to test the sound on 

    $aplay /usr/share/sounds/alsa/Front_Center.wav

once the test is successful install eSpeak using

    $opkg install espeak
And also run a quick test using eSpeak, to hear the readout on the speakers

    $espeak ‘Hello from the Intel Edison’

If you plan to implement all the features install git to clone the repository, or use wget to get the individual directories

    $opkg install git

*To autorun the python program for each of the feature using systemd, checkout the instruction in each of the feature folders above.*

### Getting the API keys 

Update the respective python files with the keys

- OpenWeatherMap  - Weather_condition.py – https://home.openweathermap.org/api_keys
- Twitter –twitter_message.py -  https://dev.twitter.com/
- Google Matrix API –traffic_condition.py – https://developers.google.com/maps/documentation/distance-matrix/start
- Cayenne MQTT details – UploadSensorDataToCayenne.py – https://github.com/myDevicesIoT/Cayenne-MQTT-Python

