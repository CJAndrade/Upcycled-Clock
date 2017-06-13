#Create for the Upcycle clock project using the Intel Edison -- to recive message from the ESP8266 connected to door on the topic- door
#once the message open is recived on topic door, after 4PM read out the weather conidtion and tweets for a specfic hashTag
#Author : @CarmelitoA 06/09/2017
import paho.mqtt.client as mqtt
import datetime
import speakingEdison

def on_connect(client, userdata, flags, rc):
    print("Connected to server. Connection code: "+str(rc))
    #subscribe to "door" topic
    client.subscribe("door")


def on_message(client, userdata, msg):
    #print message on the topic,in this case door published from ESP8266
    print("Topico: "+msg.topic+" -message recived: "+str(msg.payload))
    #possible values msg.payload - connected, open and closed
    if msg.payload == 'open' and datetime.datetime.now().hour > 7: # changed to 16 aka 4PM
        print ("The door is open in the evening")
        speakingEdison.speak()

date = datetime.datetime.now()
hour = datetime.datetime.now().hour
print date
print hour

#main program
client = mqtt.Client()
client.on_connect = on_connect   #configures callback for new connection established
client.on_message = on_message   #configures callback for new message received

client.connect("test.mosquitto.org", 1883, 60)  #connects to broker (the '60' parameter means keepalive time). If no messages are exchanged in 60 seconds, This program automatically sends ping to broker (for keeping connection on)

#Stay here forever. Blocking function.
client.loop_forever()
