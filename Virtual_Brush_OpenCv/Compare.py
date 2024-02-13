#importing Requirements
import cv2 as cv
import numpy as np





def Compare_image(target, sample):

    # Reading The Images For Comparison
    image = cv.imread(target)
    image2 = cv.imread(sample)


    # Seperating Histograms According TO Chamnels Of Target Image
    hist_blue = cv.calcHist([image],[0],None,[256],[0,256]) 
    hist_green = cv.calcHist([image],[1],None,[256],[0,256]) 
    hist_red = cv.calcHist([image],[2],None,[256],[0,256]) 
 


   # Seperating Histograms According TO Chamnels Of Samples 
    hist2_blue = cv.calcHist([image2],[0],None,[256],[0,256]) 
    hist2_green = cv.calcHist([image2],[1],None,[256],[0,256]) 
    hist2_red = cv.calcHist([image2],[2],None,[256],[0,256]) 


    # Comparing The Histograms Of RGB Channels And Getting Respective Values
    blue_r= cv.compareHist(hist2_blue,hist_blue, cv.HISTCMP_CORREL)
    green_r= cv.compareHist(hist2_green,hist_green, cv.HISTCMP_CORREL)
    red_r= cv.compareHist(hist2_red,hist_red, cv.HISTCMP_CORREL)

    # Taking Average As Final Result
    result = (blue_r + green_r + red_r )/3

    return result 

