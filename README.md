## How to Set Up The Pi to Capture Video
First, flash a microSD card with the Rasperian OS (link here: https://projects.raspberrypi.org/en/projects/raspberry-pi-setting-up/2) and plug it into your Pi. Then, connect your Raspberry Pi 4 to a monitor, keyboard and mouse using the provided USB and micro-HDMI ports. As well as this,
plug in the camera module to the provided camera port. From here, you can power on the Raspberry Pi 4 by providing power to the USB-C power supply port (you can use a normal wall outlet/phone charger) - follow the given setup instructions on the monitor. From here,
you need to connect to WiFi and also enable SSH (go to preferences under the Raspberry Pi icon in the top left). Once you have finished this, you are done with the Raspberry Pi setup. You can unplug the monitor, mouse, power supply and keyboard (keep the camera attached). 
When you resupply power to the Raspberry Pi, it will automatically boot up and connect to the provided WiFi. From there, you can SSH into it and you are good to go!

## How to Capture Video
First, clone this repository into your Raspberry Pi 4. Next, navigate into the repository and run "python testcamera.py --duration DURATION --direction DIRECTION --speed SPEED --camera_height CAMERA_HEIGHT". DURATION is the duration of the recording (in seconds),
DIRECTION is the direction of the flow (you can say "left" or "right", since ideally the stream will only flow in one main direction), SPEED is the speed of the flow (in m/s), and CAMERA_HEIGHT is the distance from the camera to the surface of the water (in meters). 

