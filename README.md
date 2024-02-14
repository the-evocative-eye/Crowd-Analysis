The project is dedicated to apply on CCTV and other survailance system for simple crowd monitoring and crowd analysis. The system is able to monitor for abnormal crowd activity, social distance violation and restricted entry. The other part of the system can then process crowd movement data into optical flow, heatmap and energy graph.

Abnormal crowd activity is monitored by computing crowd movement energy level.

Social distace violation is simply calculating distance between individuals. Two modes are given to calculate distance from edge of individuals or center of individuals from camera at different scenario.

Human detection is implemented using YOLOv4 via OpenCV built-in function. Tracking algorithm is implemented using Deep SORT, referencing the implementation by Python Lessons.

Current functions implemented includes:
1. Human Detection and Recognition
2. Social distance rule violation
3. Entries to restriced areas

 Development:
 Clone this repo. Then, create a folder YOLOv4-tiny, download and put in the weight and config file. The files can be found here, yolov4-tiny.weights and yolov4-tiny.cfg. Or you can just run the scirpt below.

git clone https://github.com/lewjiayi/Crowd-Analysis.git
cd Crowd-Analysis
mkdir YOLOv4-tiny
wget -P YOLOv4-tiny https://github.com/AlexeyAB/darknet/releases/download/yolov4/yolov4-tiny.weights
wget -P YOLOv4-tiny https://raw.githubusercontent.com/AlexeyAB/darknet/master/cfg/yolov4-tiny.cfg

Requirements:
Install the requirements

pip3 install requirements.txt

Configuration
config.py contains all configurations for this program.
~Place the video source under VIDEO_CONFIG.VIDEO_CAP in config.py


Running:
Before you run the program, make sure you have input a valid video source. You have to provide your own video for the program. Replace the path at VIDEO_CONFIG.VIDEO_CAP in config.py with the path of your own video.

To process a video, run main.py

python3 main.py
main.py will yield a set of data from the video source in the form of csv and json. These data will be placed in the directory processed_data.
