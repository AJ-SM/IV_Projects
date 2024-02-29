import matplotlib.pyplot as plt

from Operators.Crop import Img_Crop
from Operators.Blend import Img_Blend
from Operators.Rotation import image_input
from Operators.Brightness import Change_Brightness
from Operators.Blur import Blur_Image


import matplotlib.image as img




img1 = 'Image_Editor_OpenCv\Input_Images\img2.png'
img2 = 'Image_Editor_OpenCv\Input_Images\img1.png'


# Printing Menu , Comparing And Cataching Error 
def Interface():
    while True:
        print("1. Crop ")
        print("2. Blending  ")
        print("3. Rotation ")
        print("4. Brightness manipulation ")
        print("5. Blur ")
        print("6. Exit ")
        print()
        input_number = input("Enter Your Choice : ")
        


        try:
            input_number = int(input_number) 
            if input_number == 1 :
                Img_Crop(img1)
     
            elif input_number == 2 :
                 Img_Blend(img1,img2)
       
            elif input_number == 3 :
                image_input(img1,img2)
         
            elif input_number == 4 :
                Change_Brightness(img2)
                

            elif input_number == 5 :
                
                

            elif input_number == 6 :
                break  

            else:

                print("Enter Valid Number ")       



        except ValueError:
            print("!!Please Enter Number !!")




