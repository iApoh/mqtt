import paho.mqtt.client as mqtt
from gpiozero import LED

led = LED(17)
def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))

    client.subscribe("glblcd/lightbulb")
    client.subscribe("glblcd/register")
    client.subscribe("glblcd/iApoh")
def on_message(client, userdata, msg):
    global led
    print(msg.topic + " \n " + msg.payload.decode("utf-8") + " \n ")
    x = msg.payload.decode("utf-8")
    if x == "on":
        led.on()
    elif x == "off":
        led.off()

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect("mqtt.eclipseprojects.io", 1883, 60)

client.loop_forever()