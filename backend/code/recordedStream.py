#!/bin/python
import cv2
from threading import Thread

class RecordedStream:
    def __init__(self, videoFileName):
        self.stream = cv2.VideoCapture(videoFileName)
        self.frame = None
        self.stopped = False

    def start(self):
        return self

    def update(self):
        ret, self.frame = self.stream.read()

    def read(self):
        self.update()
        return self.frame

    def stop(self):
        self.stopped = True
