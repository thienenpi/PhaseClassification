import numpy as np
import pandas as pd
import cv2
import mediapipe as mp
from utilities import *
from body_parts import BodyPart

Angles = {
    'Neck': 0,
    'Left Arm': 1,
    'Right Arm': 2,
    'Back' : 3,
    'Abodmen': 4,
    'Internal': 5,
    'Left Leg': 6,
    'Right Leg': 7,
}

class JointAngle:

    def __init__(self, lm):
        self.lm = lm
        
        
    def left_leg_angle(self, left_hip, left_knee, left_ankle):
        return calculate_joint_angle(left_hip, left_knee, left_ankle)
        

    def right_leg_angle(self, right_hip, right_knee, right_ankle):
        return calculate_joint_angle(right_hip, right_knee, right_ankle)
        

    def neck_angle(self, mouth, shoulder, hip):
        return abs(180 - calculate_joint_angle(mouth, shoulder, hip))
        

    def left_arm_angle(self, left_shoulder, left_elbow, left_wrist):
        return calculate_joint_angle(left_shoulder, left_elbow, left_wrist)
        
    
    def right_arm_angle(self, right_shoulder, right_elbow, right_wrist):
        return calculate_joint_angle(right_shoulder, right_elbow, right_wrist)
        

    def abdomen_angle(self, shoulder, hip, knee):
        return calculate_joint_angle(shoulder, hip, knee)
        
        
    def back_angle(self, shoulder, hip):
        ref = [hip[0], shoulder[1]]

        return calculate_joint_angle(shoulder, hip, ref)
    

    def internal_angle(self, hip, left_heel, right_heel):
        return calculate_joint_angle(left_heel, hip, right_heel)
    

    def body_angles(self, bp: BodyPart):
        angles = [0] * 8

        angles[Angles['Neck']] = self.neck_angle(
            mouth=bp.average_cord(bp.cords[bp.mouthLeft], bp.cords[bp.mouthRight]),
            shoulder=bp.average_cord(bp.cords[bp.leftShoulder], bp.cords[bp.rightShoulder]),
            hip=bp.average_cord(bp.cords[bp.leftHip], bp.cords[bp.rightHip])
        )
        angles[Angles['Left Arm']] = self.left_arm_angle(
            left_shoulder=bp.cords[bp.leftShoulder],
            left_elbow=bp.cords[bp.leftElbow],
            left_wrist=bp.cords[bp.leftWrist]
        )
        angles[Angles['Right Arm']] = self.right_arm_angle(
            right_shoulder=bp.cords[bp.rightShoulder],
            right_elbow=bp.cords[bp.rightElbow],
            right_wrist=bp.cords[bp.rightWrist]
        )
        angles[Angles['Abodmen']] = self.abdomen_angle(
            shoulder=bp.average_cord(bp.cords[bp.leftShoulder], bp.cords[bp.rightShoulder]),
            hip=bp.average_cord(bp.cords[bp.leftHip], bp.cords[bp.rightHip]),
            knee=bp.average_cord(bp.cords[bp.leftKnee], bp.cords[bp.rightKnee])
        )
        angles[Angles['Internal']] = self.internal_angle(
            hip=bp.average_cord(bp.cords[bp.leftHip], bp.cords[bp.rightHip]),
            left_heel=bp.cords[bp.leftHeel],
            right_heel=bp.cords[bp.rightHeel]
        )
        angles[Angles['Left Leg']] = self.left_leg_angle(
            left_hip=bp.cords[bp.leftHip],
            left_knee=bp.cords[bp.leftKnee],
            left_ankle=bp.cords[bp.leftAnkle]
        )
        angles[Angles['Right Leg']] = self.right_leg_angle(
            right_hip=bp.cords[bp.rightHip],
            right_knee=bp.cords[bp.rightKnee],
            right_ankle=bp.cords[bp.rightAnkle]
        )

        return angles