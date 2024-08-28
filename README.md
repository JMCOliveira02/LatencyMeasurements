# LatencyMeasurements
* In the context of the remote operation af an automated vehicle, the total latency refers to the interval in time between a command being sent to the vehicle and its consequences being visible on the remote stream.
* This repository contains a program that measures the latency between the instant that a **MQTT** message is sent to a remote vehicle with the command to turn a **LED** light on, and the instant that the video stream of the **LED** shows it turned on

## Prerequisites
### Python 
* Python 3.11.8
  * [Python 3.11.8 download page](https://www.python.org/downloads/release/python-3118/)
### numpy, pyautogui and paho.mqtt
```python
pip install numpy pyautogui paho.mqtt
```
## Installation
* Clone this repository to your pc
```console
git clone https://github.com/JMCOliveira02 LatencyMeasurements2
```

## Usage
* Open a terminal in the same directory as the script **Detect.py** and run it with **python 3.11.8**
```sh
python Detect.py
```
* Then move the cursor to the place on the screen where the streamed **LED** is, and press **Enter**
* The script will then send a command to turn the LED on, and measure the latency
  * Keep in mind that this latency will include the time of execution of the script itself, which can be measured by placing the cursor on top of something white, in hte beginning of execution, and then pressing Enter. This is equivalent to a situation where latency should be 0, so any measured value is due to the execution of the script.
* The measured latencies are then written into a .txt file, with the name "tests.txt"
