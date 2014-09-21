import interact
import threading
import cv2

from src.define import *

class FaceInteract(interact.Interact, threading.Thread):

  def __init__(self, threadID, cameraIndex):
    threading.Thread.__init__(self)
    self.threadID = threadID
    self.isRunning = True
    self.shouldShowWebcam = False
    self.cameraIndex = cameraIndex

    self.rightBoundary = 60 + 33
    self.leftBoundary = 60 + 63
    self.turboBoundary = 120

    self.initDirections()
    self.init_matrix()
    self.init_capture_vars()

  def init_capture_vars(self):
    self.cascade = cv2.CascadeClassifier("assets/cascade/haarcascade_frontalface_alt.xml")
    self.faces = [] #var that stores face rect coords
    self.origin = [] #var that will store the origin coords
    self.o_x = 0
    self.o_y = 0
    self.o_wid = 0

  def setShowWebcam(self, shouldShow):
    self.shouldShowWebcam = shouldShow

  def initDirections(self):
    self.goingRight = False
    self.goingLeft = False
    self.isBoosting = False

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

  def detect_faces(self, image):
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

    if(self.f_x < self.rightBoundary and not self.goingRight):
      self.listener.listen(GameDefine.COMMAND_RIGHT)
      self.goingLeft = False
      self.goingRight = True

    elif (self.f_x > self.leftBoundary and not self.goingLeft):
      self.listener.listen(GameDefine.COMMAND_LEFT)
      self.goingLeft = True
      self.goingRight = False

    elif (self.f_x <= self.leftBoundary and self.f_x >= self.rightBoundary):
      self.goingLeft = False
      self.goingRight = False

    if self.f_wid > self.turboBoundary and not self.isBoosting:
      self.listener.listen(GameDefine.COMMAND_BOOST)
      self.isBoosting = True
    elif self.f_wid <= self.turboBoundary and self.isBoosting:
      self.listener.listen(GameDefine.COMMAND_UNBOOST)
      self.isBoosting = False

  def isDetecting(self):
    return self.faces != []

  def stop(self):
    self.isRunning = False

  def run(self):
    if(self.shouldShowWebcam):
      cv2.namedWindow("Video", 400)

    i = 0
    capture = cv2.VideoCapture(self.cameraIndex)
    self.f_x = 0
    self.f_wid = 0
    while self.isRunning:
      retval, image = capture.read()

      if i % 3 == 0:
        self.faces = self.detect_faces(image)

      if i % 25==0:
        if self.faces != []:
          self.matrix1[0][0] = self.faces[0][0]
          self.matrix1[0][1] = self.faces[0][1]
          self.matrix1[0][2] = self.faces[0][2]
          self.matrix1[0][3] = self.faces[0][3]

          self.o_x = (self.matrix1[0][0] + self.matrix1[0][2])/2
          self.o_y = (self.matrix1[0][1] + self.matrix1[0][3])/2
          self.o_wid = self.matrix1[0][2]

      if self.o_x != 0 and self.faces != []:
        self.f_x = (self.faces[0][0] + self.faces[0][2]) / 2
        #f_y = (self.faces[0][1] + self.faces[0][3]) / 2
        self.f_wid = self.faces[0][2]

      if(self.shouldShowWebcam):
        cv2.imshow("Video",image)

      i += 1
      if i>100:
        i=0
