import matplotlib.pyplot as plot

from Operators.Crop import Img_Crop
from Operators.Blend import Img_Blend
from Operators.Brightness import Change_Brightness
import matplotlib.image as img




img1  = img.imread('Image_Editor_OpenCv\Input_Images\Sample.jpeg')
img2 = img.imread('Image_Editor_OpenCv\Input_Images\img2.png')


# Printing Menu , Comparing And Cataching Error 
def Interface():
    while True:
        print("1. Crop ")
        print("2. Blending  ")
        print("3. Rotation ")
        print("4. Brightness manipulation ")
        print("5. Exit ")
        print()
        input_number = input("Enter Your Choice : ")
        


        try:
            input_number = int(input_number) 
            if input_number == 1 :
                imgplot = plot.imshow(Img_Crop(img1))
                plot.show()
            elif input_number == 2 :
                imgplot = plot.imshow(Img_Blend(img1,img2))
                plot.show()
            elif input_number == 3 :
                print("Rotation")           
            elif input_number == 4 :
                imgplot = plot.imshow( Change_Brightness(img2))
                plot.show()

            elif input_number == 5 :
                break  

            else:

                print("Enter Valid Number ")       



        except ValueError:
            print("!!Please Enter Number !!")




