import cv2
import mediapipe as mp

capture = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

def hand_coordinates():
    i=0
    while i<1:
        i+=1
        ret, frame = capture.read()
        img = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = hands.process(img)

        h, w, c = img.shape

        if results.multi_hand_landmarks:
            for result in results.multi_hand_landmarks:
                thisrow = []
                for i in range(1,6):
                    cx, cy = result.landmark[i*4].x, result.landmark[i*4].y
                    thisrow.extend([cx, cy])
                return thisrow