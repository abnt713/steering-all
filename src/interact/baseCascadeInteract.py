import interact
import threading
import cv2

from src.define import *


class BaseCascadeInteract(interact.Interact, threading.Thread):

    def __init__(self, threadID, cameraIndex, cascade):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.isRunning = True
        self.shouldShowWebcam = False
        self.cameraIndex = cameraIndex
        self.cascade = cascade

        self.rightBoundary = 60 + 33
        self.leftBoundary = 60 + 63
        self.turboBoundary = 120

        self.matrix1 = None
        self.init_matrix()

        self.matched_squares = None
        self.origin = None
        self.o_x = 0
        self.o_y = 0
        self.o_wid = 0
        self.init_capture_vars()

        self.f_x = 0
        self.f_wid = 0

        self.isBoosting = False

    def set_boundaries(self, right_boundary, left_boundary, turbo_boundary):
        self.rightBoundary = right_boundary
        self.leftBoundary = left_boundary
        self.turboBoundary = turbo_boundary

    def init_capture_vars(self):
        self.cascade = cv2.CascadeClassifier(self.cascade)
        #self.cascade = cv2.CascadeClassifier("assets/cascade/haarcascade_upperbody.xml")
        self.matched_squares = [] #var that stores face rect coords
        self.origin = [] #var that will store the origin coords
        self.o_x = 0
        self.o_y = 0
        self.o_wid = 0

    def setShowWebcam(self, shouldShow):
        self.shouldShowWebcam = shouldShow

    def init_matrix(self):
        self.matrix1 = [[0 for x in xrange(4)] for x in xrange(1)]
        self.matrix1[0][0] = 0
        self.matrix1[0][1] = 0
        self.matrix1[0][2] = 0
        self.matrix1[0][3] = 0

    def set_boundaries(self, leftBoundary, rightBoundary, turboBoundary):
        self.leftBoundary = leftBoundary
        self.rightBoundary = rightBoundary
        self.turboBoundary = turboBoundary

    def detect_patterns(self, image):
        allDetected = []
        detected = self.cascade.detectMultiScale(image, 1.3, 4, cv2.cv.CV_HAAR_SCALE_IMAGE, (20,20))
        if detected != []:
            for x,y,w,h in detected: #for (x,y,w,h),n in detected:
                allDetected.append((x,y,w,h))
        return allDetected

    def checkInteraction(self):
        if(not self.isDetecting()):
            self.listener.listen(GameDefine.COMMAND_SIGNAL_LOST)
        else:
            self.listener.listen(GameDefine.COMMAND_SIGNAL_FOUND)

        if self.f_wid > self.turboBoundary and not self.isBoosting:
            self.listener.listen(GameDefine.COMMAND_BOOST)
            self.isBoosting = True
        elif self.f_wid <= self.turboBoundary and self.isBoosting:
            self.listener.listen(GameDefine.COMMAND_UNBOOST)
            self.isBoosting = False

    def isDetecting(self):
        return self.matched_squares != []

    def stop(self):
        self.isRunning = False

    def run(self):
        print('Running Cascade Interact')
        i = 0
        capture = cv2.VideoCapture(self.cameraIndex)
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_WIDTH, 320)
        capture.set(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT, 240)
        self.f_x = 0
        self.f_wid = 0
        while self.isRunning:
            print(self.f_wid)
            retval, image = capture.read()

            if i % 3 == 0:
                self.matched_squares = self.detect_patterns(image)

            if i % 25==0:
                if self.matched_squares != []:
                    self.matrix1[0][0] = self.matched_squares[0][0]
                    self.matrix1[0][1] = self.matched_squares[0][1]
                    self.matrix1[0][2] = self.matched_squares[0][2]
                    self.matrix1[0][3] = self.matched_squares[0][3]

                    self.o_x = (self.matrix1[0][0] + self.matrix1[0][2])/2
                    self.o_y = (self.matrix1[0][1] + self.matrix1[0][3])/2
                    self.o_wid = self.matrix1[0][2]

            if self.o_x != 0 and self.matched_squares != []:
                self.f_x = (self.matched_squares[0][0] + self.matched_squares[0][2]) / 2
                #f_y = (self.faces[0][1] + self.faces[0][3]) / 2
                self.f_wid = self.matched_squares[0][2]

            if(self.shouldShowWebcam):
                cv2.imshow("Video",image)

            i += 1
            if i>100:
                i=0
