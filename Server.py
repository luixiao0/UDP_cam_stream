import socket
import cv2
import numpy as np

def handle_stream(sendArr):
    udpSocket = socket.socket(type=socket.SOCK_DGRAM)
    while True:
        grabbed, feed = camera.read()
        encode_param = [int(cv2.IMWRITE_JPEG_QUALITY), 90]
        result, encimg = cv2.imencode('.jpg', feed, encode_param)
        print(encimg.shape)
        udpSocket.sendto(encimg, sendArr)
        cv2.waitKey(30)


camera = cv2.VideoCapture(0)
sendArr = ('192.168.1.202', 9999)
print(sendArr)
handle_stream(sendArr)
print("SERVER ONLINE")
