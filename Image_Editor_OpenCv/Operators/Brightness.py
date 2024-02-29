import numpy as np
import matplotlib.image as img
import matplotlib.pyplot as plt

def Change_Brightness(img1):
    # Reading Image
    img1 = img.imread(img1)

    
    # Only Work When .png Img !!
    amount_Brightness = int(input("Enter Amout In % : "))

    # Adding A Float value with the difference of the max and min pixel in the image 
    img2 = (img1.max() - img1.min())*(amount_Brightness /100) + img1

    plt.suptitle("Brightness")
    plt.subplot(2,2,1)
    plt.title("Image1" )
    plt.imshow(img1)

    plt.subplot(2,2,2)
    plt.title("Edited Image Image")
    plt.imshow(img2)

    # Simpliy showing the image
    plt.show()     
