#Create for the Upcycle clock project using the Intel Edison -- using IFTTT to switch ON/OF and color cycle HUE bulbs
#Author : @CarmelitoA 06/01/2017

import requests
from time import sleep
#get the api key from Maker Webhooks channel https://ifttt.com/services/maker_webhooks/settings
api_key = 'xxxxxxxxxxxx-xxx'
#event = 'from_edison_HUE'

def send_IFTTT_event(event_recived):
    #posting data to IFTTT - HUEON,HUEOFF and HUECOLOR
    url = "https://maker.ifttt.com/trigger/{e}/with/key/{k}/".format(e=event_recived,k=api_key)
    payload = {'value1': event_recived}
    try:
        requests.post(url, data=payload)
    except requests.exceptions.RequestException as resp:
        print("Error from IFTTT: {e}".format(e=resp))

#Running a quick test
send_IFTTT_event('HUEON')
sleep(60)
send_IFTTT_event('HUEOFF')
sleep(90)
send_IFTTT_event('HUECOLOR')
