import numpy
import cv2 as cv
import matplotlib.image as img

# Defining Blending Function -- > 

def Img_Blend(img1,img2):
        if img1.size == img2.size:
                 alpha = float(input("Enter Weight_1 : "))
                 beta = float(input("Enter Weight_2 : "))
                 blend = alpha*img1 + beta*img2
                 return blend
             
                        
        else :
                print("Image Dimension Aren't Matching,Please Add Images Of Same Dimension !! ")
                return img.imread('Image_Editor_OpenCv\Input_Images\error.jpg')

    