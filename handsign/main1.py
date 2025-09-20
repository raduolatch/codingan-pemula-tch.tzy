import mediapipe as mp
import cv2

mpHands = mp.solutions.hands
mpDraw = mp.solutions.drawing_utils

class HandDetection:
    def __init__(self):