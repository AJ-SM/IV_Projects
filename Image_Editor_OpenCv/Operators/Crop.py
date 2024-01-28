
# Defining Function For Image Croping -->

def Img_Crop(img):
    dist1 = int(input("D1 : "))
    dist2 = int(input("D2 : "))
    dist3 = int(input("D3 : "))
    dist4 = int(input("D4 : "))


    return img[dist4:(img.shape[0]-dist2),dist1:(img.shape[1]-dist3)] 

''' Anbody Explain it !! '''





