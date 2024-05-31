import cv2
import mediapipe as mp
import csv

capture = cv2.VideoCapture(0)

# filename = "hand_data_10.csv"

# csvfile = open(filename, 'a')
# csvwriter = csv.writer(csvfile)
# csvwriter.writerow(['thumb_x', 'thumb_y', 'index_x', 'index_y', 'middle_x', 'middle_y', 'ring_x', 'ring_y', 'small_x', 'small_y', 'runs'])

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

while True:
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
            thisrow.append(10)
            print(thisrow)
            # csvwriter.writerow(thisrow)
            mpDraw.draw_landmarks(img, result, mpHands.HAND_CONNECTIONS)
            input()

    cv2.imshow("Video", img)
    if cv2.waitKey(25) & 0xFF == ord('q'):
        break