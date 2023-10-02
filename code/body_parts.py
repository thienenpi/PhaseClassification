import mediapipe as mp
from utilities import *

mediapipe_pose = mp.solutions.pose

class BodyPart:
    nose = 0
    leftEyeInner = 1
    leftEye = 2
    leftEyeOuter = 3
    rightEyeInner = 4
    rightEye = 5
    rightEyeOuter = 6
    leftEar = 7
    rightEar = 8
    mouthLeft = 9
    mouthRight = 10
    leftShoulder = 11
    rightShoulder = 12
    leftElbow = 13
    rightElbow = 14
    leftWrist = 15
    rightWrist = 16
    leftPinky = 17
    rightPinky = 18
    leftIndex = 19
    rightIndex = 20
    leftThumb = 21
    rightThumb = 22
    leftHip = 23
    rightHip = 24
    leftKnee = 25
    rightKnee = 26
    leftAnkle = 27
    rightAnkle = 28
    leftHeel = 29
    rightHeel = 30
    leftFootIndex = 31
    rightFootIndex = 32

    cords = []

    def average_cord(self, p1: list, p2: list):
        return [(p1[0] + p2[0]) / 2,
                (p1[1] + p2[1]) / 2]