import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

def Change_Brightness(img1):
    img1 = img.imread(img1)
    amount_Brightness = int(input("Enter Amout In % : "))
    " Only Work When .png Img !!"
    img2 = (img1.max() - img1.min())*(amount_Brightness /100) + img1

    plt.suptitle("Brightness")
    plt.subplot(2,2,1)
    plt.title("Image1" )
    plt.imshow(img1)

    plt.subplot(2,2,2)
    plt.title("Edited Image Image")
    plt.imshow(img2)

    plt.show()     
