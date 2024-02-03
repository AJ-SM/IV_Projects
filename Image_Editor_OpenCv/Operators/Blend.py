import numpy as np
import cv2 as cv
from matplotlib import image as img, pyplot as plt

# Defining Blending Function -- > 

def Img_Blend(img1,img2):
        if img1.size == img2.size:
                alpha = float(input("Enter Weight_1 : "))
                beta = 1 - alpha
                #  beta = float(input("Enter Weight_2 : "))
                blend=(alpha*img1 + beta*img2)
                blend=(np.clip(blend,0,255).astype(np.uint8))
                show_blend(img1,img2,blend)        
        else :
                print("Image Dimension Aren't Matching,Please Add Images Of Same Dimension !! ")
                plt.imshow(img.imread('Image_Editor_OpenCv/Input_Images/error.jpg'))
                plt.axis('off')
                plt.show()
                

def show_blend(img1,img2,blend):
        plt.suptitle("Blending")
        plt.subplot(2,2,1)
        plt.title("Image1" )
        plt.imshow(img1)
        plt.axis('off')
        plt.subplot(2,2,2)
        plt.title("Image2")
        plt.imshow(img2)
        plt.axis('off')
        plt.subplot(2,2 ,(3,4))
        plt.title("Blended Image")
        plt.imshow(blend)
        plt.axis('off')
        plt.show()

img1_loc = input("img1 location :")
img2_loc = input("img2 location :")

img1=img.imread(img1_loc)
img2=img.imread(img2_loc)

Img_Blend(img1,img2)