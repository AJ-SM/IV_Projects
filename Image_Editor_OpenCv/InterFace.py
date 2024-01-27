

# Printing Menu And Comparing And Cataching Error 
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
                print("Crop")
            elif input_number == 2 :
                print("Blending")
            elif input_number == 3 :
                print("Rotation")           
            elif input_number == 4 :
                print("Brightness")

            elif input_number == 5 :
                break  

            else:

                print("Enter Valid Number " , end="\\n")       



        except ValueError:
            print("!!Please Enter Number !!")




