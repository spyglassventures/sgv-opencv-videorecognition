import os
import cv2
import numpy as np

# RTSP is your camera
# UDP the output stream
os.system("ffmpeg -i rtsp://admin:pwd@192.168.0.100:554 '-s' '800x600' -f mpegts udp://127.0.0.1:3000 & output_800x600.avi") #worked
