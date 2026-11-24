import json, os, random, time
import paho.mqtt.client as mqtt

THE_BROKER = os.getenv("MQTT_BROKER", "localhost")
THE_PORT = int(os.getenv("MQTT_PORT", "1883"))
THE_TOPIC = "controller/joystick"
THE_TOPIC2 = "controller/buttons"

mqttc=mqtt.Client()
while True:
    try:
        mqttc.connect(THE_BROKER, THE_PORT)
        break
    except OSError:
        print("Broker not ready, retrying in 3s...", flush=True)
        time.sleep(3)

while True:
    msg = {'X': random.randint(-10, 10), 'Y': random.randint(-10, 10)}
    msg2 = {'A': random.randint(0, 1), 'B': random.randint(0, 1)}

    mqttc.publish(THE_TOPIC, json.dumps(msg))
    mqttc.publish(THE_TOPIC2, json.dumps(msg2))
    time.sleep(5)