## Getting more info from the LCD panel
As part of this feature, the clock house a Grove LCD and two buttons and a potentiometer, which are used to set alarms, show the weather condition, temperature and humidity outside, and also show temperature and air quality sensor values. In addition, you can also get the IP address assigned to the Intel Edison just in case you have to ssh in for maintenance,  and also switch off/on you phillips-hue smart bulbs at home.

For more info and pictures check out the blog post at -
https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/06/03/upcycled-clock-displaying-data-on-grove-lcd

If you want to implement only this feature on your Edison download the LCD folder from the github repo and run the following commands to setup a service to autorun every time the Edison boots up.

    mkdir Upcycled-Clock
    cd Upcycled-Clock
    svn checkout https://github.com/CJAndrade/Upcycled-Clock/trunk/LCD
    cd LCD
    chmod +x displayonLCD.py

put the file displayonlcd.service in  /lib/systemd/system/ and enable the service

    cp displayonlcd.service /lib/systemd/system/displayonlcd.service
    systemctl enable displayonlcd.service
    systemctl start displayonlcd.service

to check the status of the service use

    systemctl status displayonlcd.service


![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25616-419337/IMG_20170602_190940+%28copy%29.jpg)
