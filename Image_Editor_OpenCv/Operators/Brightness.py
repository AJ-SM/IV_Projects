import numpy
import cv2 as cv
import matplotlib.image as img

def Change_Brightness(img):
    amount_Brightness = int(input("Enter Amout In % : "))
    img = (img.max() - img.min())*(amount_Brightness /100)+ img

    return img
