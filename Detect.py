import numpy as np
import time
import pyautogui

from paho.mqtt import client as mqtt

broker_host = "127.0.0.1"
broker_port = 1883
topic = "/moses/cmd_vel"

def read_message_from_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)
    
client = mqtt.Client(
    mqtt.CallbackAPIVersion.VERSION1)

client.connect(broker_host, broker_port)
client.on_connect = on_connect

prev_color_detected = False


# Define lower and upper bounds of the desired color in HSV
lower_color = np.array([220, 220, 220])
upper_color = np.array([255, 255, 255])

def check_color(pixel):
    if lower_color[0] <= pixel[0] <= upper_color[0]:
        if lower_color[1] <= pixel[1] <= upper_color[1]:
            if lower_color[2] <= pixel[2] <= upper_color[2] :
                return True
    return False

test_n=0

input("Move the mouse to the LED and press Enter to start the test...")
pixel_x, pixel_y = pyautogui.position()
bbox = (pixel_x, pixel_y, 1, 1)
print(f"Pixel to be evaluated at: ({pixel_x}, {pixel_y})")

###LATENCY TEST
while True:
    time.sleep(3)
    print("LED_ON")
    client.publish(topic,read_message_from_file("LED_on.xml"))
    timestamp1 = time.time()
    # Check if hue value falls within the desired interval
    while True:
        screen = np.array(pyautogui.screenshot(region=bbox))
        pixel = screen[0, 0]
        if check_color(pixel):
            timestamp2 = time.time()
            test_n+=1
            print("Latency_test#{} : {}".format(test_n, timestamp2-timestamp1))
            with open("testsWiFi.txt", "a") as file:
                # Write content to the file
                file.write("Latency_test,{}, {}\n".format(test_n, timestamp2-timestamp1))
            client.publish(topic,read_message_from_file("LED_off.xml"))
            break
        if time.time()-timestamp1>3:
            print("Latency_test,{},  : {}".format(test_n+1, "Timeout"))
            client.publish(topic,read_message_from_file("LED_off.xml"))
            print("LED_OFF")
            break
        
