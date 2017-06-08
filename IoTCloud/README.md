## Uploading sensor data to Cayenne
This feature was a great addition to the clock, and as part of the feature I am uploading the temperature,Light and Air quality sensor to Cayenne IoT dashboard

For more info checkout the blog post at -
https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/05/26/upcycled-clock-posting-sensor-data-to-cayenne

To setup your cayenne dashboard create an account at - https://mydevices.com/ , and then add your own device using "Bring Your Own Thing API selection" icon, and make a note of the following
- MQTT Username
- MQTT Password
- Client ID

If you want to implement only this feature on your Edison download the IoTCloud folder from the github repo and run the following commands to setup a service to autorun every time the Edison boots up.

    mkdir Upcycled-Clock
    cd Upcycled-Clock
    svn checkout https://github.com/CJAndrade/Upcycled-Clock/trunk/IoTCloud
    cd LCD
    chmod +x upload_data_schedule.py

put the file uploadingdata.service in  /lib/systemd/system/ and enable the service

    cp uploadingdata.service /lib/systemd/system/uploadingdata.service
    systemctl enable uploadingdata.service
    systemctl start uploadingdata.service

to check the status of the service use

    systemctl status uploadingdata.service

![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25577-416386/caynnneDashboard.png)
