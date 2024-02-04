import matplotlib.pyplot as plot

from Operators.Crop import Img_Crop
from Operators.Blend import Img_Blend
from Operators.Rotation import image_input
from Operators.Brightness import Change_Brightness
import matplotlib.image as img




img2 = 'Image_Editor_OpenCv\Input_Images\img2.png'
img3 = 'Image_Editor_OpenCv\Input_Images\pngimg.com - pokemon_PNG148.png'


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
                imgplot = plot.imshow(Img_Crop(img3))
                plot.show()
            elif input_number == 2 :
                imgplot = plot.imshow(Img_Blend(img3,img2))
                plot.show()
            elif input_number == 3 :
                image_input(img2)
         
            elif input_number == 4 :
                imgplot = plot.imshow( Change_Brightness(img3))
                plot.show()

            elif input_number == 5 :
                print("Bluer")
                

            elif input_number == 6 :
                break  

            else:

                print("Enter Valid Number ")       



        except ValueError:
            print("!!Please Enter Number !!")




