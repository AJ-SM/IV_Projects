import numpy as np
import matplotlib.image as img

def Change_Brightness(img):
    amount_Brightness = int(input("Enter Amout In % : "))
    " Only Work When .png Img !!"
    img = (img.max() - img.min())*(amount_Brightness /100) + img

    return img
