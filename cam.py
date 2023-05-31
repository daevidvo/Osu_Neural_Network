import cv2
from PIL import ImageGrab
import numpy as np

while(True):
    # converts the ImageGrab image (800x600) and turns it into a numpy array
    printscreen =  np.array(ImageGrab.grab(bbox=(0,40,800,600)))
    
    # shows the frame but converts it into a grayscaled image
    cv2.imshow('Frame', cv2.cvtColor(printscreen, cv2.COLOR_BGR2GRAY))

    # when the esc key is pressed the process is ended
    if cv2.waitKey(1) == (27):
        break

ImageGrab.release()
cv2.destroyAllWindows()

