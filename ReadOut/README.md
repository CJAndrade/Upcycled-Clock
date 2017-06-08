## Making the clock Speak in the morning
as part of the setup I am using an amplifier and speaker connected to the USB sound card, to read out the weather condition,the latest 5 tweets for a specific hashtag that I am tracking. As part of this feature, I would also like to add the top 5 news headline in a future enhancement.

For more info on how to setup USB sound card and eSpeak, checkout the blog post at
https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/04/30/upcycled-clock-getting-the-weather-using-espeak


If you want to implement only this feature on your Edison download the ReadOut folder from the github repo and run the following commands to setup a service to autorun every morning.

    mkdir Upcycled-Clock
    cd Upcycled-Clock
    svn checkout https://github.com/CJAndrade/Upcycled-Clock/trunk/ReadOut
    cd ReadOut
    chmod +x readout_schedule.py

put the file readouts.service in  /lib/systemd/system/ and enable the service

    cp paneldiffusion.service /lib/systemd/system/readouts.service
    systemctl enable readouts.service
    systemctl start readouts.service

to check the status of the service use

    systemctl status readouts.service

![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25597-417848/IMG_20170529_130926.jpg)
