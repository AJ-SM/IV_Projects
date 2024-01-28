import numpy
import cv2 as cv
# Defining Blending Function -- > 

def Img_Blend(img1,img2):
    
    try:
   
            alpha = float(input("Enter Weight_1 : "))
            beta = float(input("Enter Weight_2 : "))
            blend = alpha*img1 + beta*img2
            return blend
    except :
       print("Image Dimension Aren't Matching,Please Add Images Of Same Dimension !! ")

    