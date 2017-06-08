#!/usr/bin/python
#Create for the Upcycle clock project using the Intel Edison -- create shedule to run every 10 mins to upload data to Cayenne
#Author : @CarmelitoA 06/02/2017
#Based on - https://pypi.python.org/pypi/schedule

import schedule
import time, datetime
import upload_sensordata_cayenne

def upload():
    print("Upload data to the IoT cloud..")
    print datetime.datetime.now()
    upload_sensordata_cayenne.uploadData()

#Upload sensor data to the IoT cloud- Cayenne every 10 mins
schedule.every(10).minutes.do(upload)

while True:
    schedule.run_pending()
    time.sleep(1)
