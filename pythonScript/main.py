import json, random, time
import paho.mqtt.client as mqtt

THE_BROKER= "localhost"
THE_TOPIC= "controller/joystick"
THE_TOPIC2= "controller/buttons"

mqttc=mqtt.Client()
mqttc.connect(THE_BROKER, 1883)

while True:
    joystickValueX= random.randint(-10,10)
    joystickValueY= random.randint(-10,10)
    msg={'X':joystickValueX, 'Y':joystickValueY}
    msgStr1=json.dump(msg)

    buttonValueA=random.randint(0,1)
    buttonValueB=random.randint(0,1)
    msg2={'A':buttonValueA, 'B':buttonValueB}
    msgStr2=json.dump(msg2)

    mqttc.publish(THE_TOPIC, msgStr1)
    mqttc.publish(THE_TOPIC2, msgStr2)
    time.sleep(5)