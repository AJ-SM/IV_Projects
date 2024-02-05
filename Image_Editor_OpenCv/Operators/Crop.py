import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt



# Defining Function For Image Croping -->

def Img_Crop(img1):
    img1 = img.imread(img1)
    dist1 = int(input("D1 : "))
    dist2 = int(input("D2 : "))
    dist3 = int(input("D3 : "))
    dist4 = int(input("D4 : "))


    img2 =  img1[dist4:(img1.shape[0]-dist2),dist1:(img1.shape[1]-dist3)] 

    plt.suptitle("Crop")
    plt.subplot(2,2,1)
    plt.title("Image1" )
    plt.imshow(img1)

    plt.subplot(2,2,2)
    plt.title("Edited Image Image")
    plt.imshow(img2)

    plt.show()

''' Anbody Explain it !! '''





