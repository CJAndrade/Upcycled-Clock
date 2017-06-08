## Visual indicator using diffusion panels
as part of the build five glass panels were switched out for 3D printed LED diffusion panel, which are meant to give an visual indicator when I wake up in the morning. Here is a brief description of the panels -

- Weather - this lights up based on the weather conditions from openweathermap.org. Yellow for sunny, blue for rainy and white for cloudy.
- Traffic – based on the Google Maps Distance Matrix API, gives me an indicator if I need to leave early because of heavy traffic.
- Twitter - this will be set to blue , if the hashtag that I am tracking has been used more that 5 times  in a tweets today on the twittersphere.
- Gmail - this panel will light up red, if I have more than 10 unread messages, and green if less than 10.
- Home - this panel is to monitor values from the Air quality and Temperature sensors connected to the back of the clock.

For more info checkout the blog post at -
https://www.element14.com/community/community/design-challenges/upcycleit/blog/2017/06/03/upcycled-clock-led-diffusion-panel-integration


If you want to implement only this feature on your Edison download the PanelDiffusion folder from the github repo and run the following commands to setup a service to autorun every time the Edison boots up.

    mkdir Upcycled-Clock
    cd Upcycled-Clock
    svn checkout https://github.com/CJAndrade/Upcycled-Clock/trunk/PanelDiffusion
    cd PanelDiffusion
    chmod +x panel_schedule.py

put the file paneldiffusion.service in  /lib/systemd/system/ and enable the service

    cp paneldiffusion.service /lib/systemd/system/paneldiffusion.service
    systemctl enable paneldiffusion.service
    systemctl start paneldiffusion.service

to check the status of the service use

    systemctl status paneldiffusion.service

![N|Solid](https://www.element14.com/community/servlet/JiveServlet/showImage/38-25612-419340/DSC05493+%28copy%29.JPG)
