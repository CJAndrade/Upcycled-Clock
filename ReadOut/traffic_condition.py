#Create for the Upcycle clock project using the Intel Edison -- to get time it would take to get to work using Google Maps API
#Author : @CarmelitoA 05/22/2017
# Google Maps API -Distance Matrix - https://developers.google.com/maps/documentation/distance-matrix/intro#traffic-model
import urllib2, json
import time

def get_time_intraffic():
    #modify the URL below based to add your orgin, destination address and API Key from google
    response = urllib2.urlopen('https://maps.googleapis.com/maps/api/distancematrix/json?origins=395+santa+monica+place,+Santa+Monica,+CA&destinations=21821+Oxnard+St,+Woodland+Hills,+CA|&traffic_model=best_guess&key=XXXXXXXXXXXXXXXXXXX-XXX&departure_time=now')
    data = json.load(response)
    timeInTraffic = data['rows'][0]['elements'][0]['duration']['value']
    distanceInTraffic = data['rows'][0]['elements'][0]['distance']['value']
    print ('distance :'+str(distanceInTraffic/1000)+ ' km' + ' time to work :' + str(timeInTraffic/60) + ' mins')
    return timeInTraffic/60
