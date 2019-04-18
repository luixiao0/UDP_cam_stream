import threading
import numpy as np
import socket
import cv2
import time


def recv(socket):
    raw = socket.recvfrom(65535)
    if raw == None:
        print("failed_recv")
        recv(socket)
    return raw


def bind():
    UDP_PORT = 9999
    print("BIND")
    udpSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        udpSocket.bind(("", UDP_PORT))
        return udpSocket
    except:
        print("bindfailed")
        bind()
def start():
    udpSocket = bind()
    while True:
        raw = recv(udpSocket)
        array = np.frombuffer(raw[0], np.uint8)
        decimg = cv2.imdecode(array, cv2.IMREAD_COLOR)
        #decimg = np.asarray(array, dtype="uint8")  # decode packet in queue
        cv2.imshow("Cam", decimg)  # show the image
        cv2.waitKey(10)


def close():
    cv2.destroyAllWindows()


timeout = 20
socket.setdefaulttimeout(timeout)
start()