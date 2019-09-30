
import os
import cv2
import numpy as np



cap = cv2.VideoCapture('udp://127.0.0.1:3000?overrun_nonfatal=1&fifo_size=50000000',cv2.CAP_FFMPEG)
# overrun_nonfatal and fifo has been added to avoid crashed, see https://stackoverflow.com/questions/16944024/udp-streaming-with-ffmpeg-overrun-nonfatal-option

if not cap.isOpened():
        print('VideoCapture not opened')


# rescaling does not work on IP cam yet
#https://www.youtube.com/watch?v=y76C3P20rwc
# def make_240p():
#     cap.set(3, 320) # width
#     cap.set(4, 240) # height
#
# def make_480p():
#     cap.set(3, 640) # width
#     cap.set(4, 480) # height
#
# def make_720p():
#     cap.set(3, 1280) # width
#     cap.set(4, 720) # height
#
# def change_res(width, height):
#     cap.set(3, width) # width
#     cap.set(4, height) # height
#
# make_720p()
# #make_480p()
# #make_240p()

# how to install imageai
# download file manually, put in folder


from imageai.Detection import VideoObjectDetection
import os
import cv2

execution_path = os.getcwd()


detector = VideoObjectDetection()
detector.setModelTypeAsYOLOv3()
detector.setModelPath(os.path.join(execution_path , "yolo.h5"))
detector.loadModel()

video_path = detector.detectObjectsFromVideo(camera_input=cap,
    output_file_path=os.path.join(execution_path, "camera_detected_video")
    , frames_per_second=20, log_progress=True, minimum_percentage_probability=30)

print(video_path)









while True:
    # capture frame by frame
    ret, frame = cap.read()

    # Display resulting frame
    cv2.imshow("frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break


# when done, release capture
cap.release()
cv2.destroyAllWindows()




#         exit(-1)
#
# while True:
#         ret, frame = cap.read()
#
#         if not ret:
#             print('frame empty')
#             break
#
#         cv2.imshow('image', frame)
#
#         if cv2.waitKey(1)&0XFF == ord('q'):
#             break
#
# cap.release()
# cv2.destroyAllWindows()


# crashes
