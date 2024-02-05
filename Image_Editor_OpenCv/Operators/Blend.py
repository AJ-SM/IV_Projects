import numpy as np
import cv2 as cv
from matplotlib import image as img, pyplot as plt






# Defining Blending Function -- > 

def Img_Blend(img1,img2):
                img1 = img.imread(img1)
                img2 = img.imread(img2)
   
                alpha = float(input("Enter Weight_1 : "))
                beta = 1 - alpha
                #beta = float(input("Enter Weight_2 : "))
                blend=(alpha*img1 + beta*img2)
                blend=(np.clip(blend,0,255))

                show_blend(img1,img2,blend)   

def show_blend(img1,img2,blend):
        plt.suptitle("Blending")
        plt.subplot(2,2,1)
        plt.title("Image1" )
        plt.imshow(img1)

        plt.subplot(2,2,2)
        plt.title("Image2")
        plt.imshow(img2)
  
        plt.subplot(2,2 ,(3,4))
        plt.title("Blended Image")
        plt.imshow(blend)

        plt.show()     





