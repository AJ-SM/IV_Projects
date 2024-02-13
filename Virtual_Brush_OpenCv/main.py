#Importing Requirements
import os 
from Compare import Compare_image



# Setting Required Folders 
images_folder = "imgs"
image = os.listdir("target")


#Getting Succed Match As Dictonary 
Succed_Match = {}


# Looping Through DataBase Of Images 
file_names = []


# Threshold Value For Better  Comparison Of Images 
threshold_value = 0.80


# Grabing Image File If Images Are Greate Than One Then Throwing Error 

if len(image) == 1:
    file_name = image[0]
    file_path = os.path.join("target", file_name)
    target = file_path
    print(f"The Image Is Being Compared Is : {file_path}")
else:
    print("There Are Many Images In The Directory. Please Throw Any One --> ")


# Walking Through Each Image File , Comparing And Storing The Output Value Into Succed Match
for root, dirs, files in os.walk(images_folder):
 
    for file in files:
        # Calculating Result By Comparision 
        result = Compare_image(target,os.path.join(root, file))

        if result >=float(threshold_value):
            Succed_Match.update({file : result})


# Sorting The Dictonary For Better Comparion
Succed_Match = {k: v for k, v in sorted(Succed_Match.items(), key=lambda item: item[1])}


#Printing The Dict Of Succed_Match
print(Succed_Match)






        




    




