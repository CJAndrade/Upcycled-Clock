#!/usr/bin/python
#Create for the Upcycle clock project using the Intel Edison -- to readout weather conditions,time to work, and tweets
#Author : @CarmelitoA 06/02/2017
#Based on - https://pypi.python.org/pypi/schedule

import schedule
import time, datetime
import PanelDiffusion

def panels():
    print("Reading out..")
    print datetime.datetime.now()
    PanelDiffusion.panels()

#edison readouts at 7:10 using eSpeak via the speaker attached to an USB soundcard
schedule.every().day.at("6:30").do(panels)
schedule.every().day.at("6:50").do(panels)
schedule.every().day.at("7:10").do(panels)
schedule.every().day.at("7:30").do(panels)
schedule.every().day.at("7:50").do(panels)

while True:
    schedule.run_pending()
    time.sleep(1)
