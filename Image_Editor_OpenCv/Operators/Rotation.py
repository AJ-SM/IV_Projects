from math import cos, radians, sin, sqrt
from matplotlib import image as img, pyplot as plt
import numpy as np

def rotate_at_angle(image, direction, angle):
    rotate_sense=direction.lower()
    
    angle=angle if rotate_sense=="clockwise" else -angle

    img1=image
    img1_height,img1_width,_=img1.shape
    img1_center=[img1_height//2 ,img1_width//2]

    
    rotated_img1_dimn=round(sqrt(pow(img1_height,2)+pow(img1_width,2)))
    rotated_img1=np.empty((rotated_img1_dimn+1,rotated_img1_dimn+1,3)).astype(np.uint8)
    rotated_img1+=255
    rotated_img1_center=[rotated_img1_dimn//2,rotated_img1_dimn//2] 


    for i in range(img1_height):
        y=img1_center[0]-i

        for j in range(img1_width):
            x=j-img1_center[1]
            new_x,new_y=new_coordinate_genertor([x,y],img1_center,radians(angle))
            actual_y=round(-new_y+rotated_img1_center[1])
            actual_x=round(new_x+rotated_img1_center[0])
            rotated_img1[actual_y,actual_x]=img1[i,j]
    
    return img1,rotated_img1




def new_coordinate_genertor(original_coords, center, angle):
    return [original_coords[0]*cos(angle)+original_coords[1]*sin(angle), -original_coords[0]*sin(angle)+original_coords[1]*cos(angle)]




def image_input():
    image_location=input("image location :")

    image_rotation_direction=0
    while  image_rotation_direction not in ['clockwise','anticlockwise']:
        image_rotation_direction=input("enter rotation direction (clockwise / anticlockwise) :").lower()

    image_rotation_angle=input("enter angle of rotation :")
    print(image_location)

    image=img.imread(image_location)
    return (rotate_at_angle(image,image_rotation_direction,float(image_rotation_angle)))


def image_show(image,rotated_image):
    plt.subplot(1,2,1)
    plt.imshow(image)
    plt.axis('off')
    plt.subplot(1,2,2)
    plt.imshow(rotated_image)
    plt.axis('off')
    plt.show()
        



image,rotated_image = image_input()
image_show(image,rotated_image)