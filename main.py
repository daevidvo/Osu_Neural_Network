import numpy as np
import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
from PIL import ImageGrab
import pyautogui as pag

def main():

    while(True):
        # converts the ImageGrab image (800x600) and turns it into a numpy array
        printscreen =  np.array(ImageGrab.grab(bbox=(1321,409,2122,1005)))
        printscreen = cv2.resize(printscreen, (160, 120))

        # shows the frame but converts it into a grayscaled image
        cv2.imshow('Frame', cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY))

        model = tf.keras.Sequential([
            tf.keras.layers.Flatten(input_shape=(160, 120)),
            tf.keras.layers.Dense(128, activation='relu'),
            tf.keras.layers.Dense(4)
        ])

        labels = ['up', 'down', 'left', 'right']

        model.compile(optimizer='adam', loss=tf.keras.losses.SparseCategoricalCrossentropy(from_logits=True), metrics=['accuracy'])

        model.fit(printscreen, labels, epochs=10)
        # when the esc key is pressed the process is ended
        if cv2.waitKey(1) == (27):
            cv2.destroyAllWindows()
            break


    # model = tf.keras.Sequential([
    #     tf.keras.layers.Flatten()
    # ])


main() 