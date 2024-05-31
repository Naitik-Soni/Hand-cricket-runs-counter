from keras.models import load_model
import pandas as pd
import numpy as np
from prediction_supporter import hand_coordinates
import os

model = load_model('hand_pose_detection.h5')

def getData():
    keys = ['thumb_x', 'thumb_y', 'index_x', 'index_y', 'middle_x', 'middle_y', 'ring_x', 'ring_y', 'small_x', 'small_y']
    values = hand_coordinates()

    data_dict = dict(zip(keys, values))
    for key in data_dict.keys():
        data_dict[key] = [data_dict[key]]

    return pd.DataFrame(data_dict)

def preprocess(hand_coordinates):
    odd_columns = hand_coordinates.iloc[:, ::2]
    even_columns = hand_coordinates.iloc[:, 1::2]

    min_odd = odd_columns.min(axis=1)
    min_even = even_columns.min(axis=1)

    min_odd = pd.Series(min_odd, index=hand_coordinates.index)
    min_even = pd.Series(min_even, index=hand_coordinates.index)

    hand_coordinates.iloc[:, ::2] = hand_coordinates.iloc[:, ::2].sub(min_odd, axis=0)
    hand_coordinates.iloc[:, 1::2] = hand_coordinates.iloc[:, 1::2].sub(min_even, axis=0)

    return hand_coordinates

def predictRun(data):
    # print("D:", data)
    data = preprocess(data)
    # print("d:", data)

    predction = list(model.predict(data)[0])
    # print(predction)
    run = predction.index(max(predction)) + 1
    # print("Run:", run)
    return run

total = 0

while True:
    os.system("cls")
    data = getData()
    run = predictRun(data)
    total += run

    print("Total runs:", total)
    input("Press Enter")
