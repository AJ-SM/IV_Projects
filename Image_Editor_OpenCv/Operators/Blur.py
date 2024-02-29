
import numpy as np
import matplotlib.pyplot as plt



def Blur_Image(img):
  img1 = img

  while True:
    scale = int(input("Enter Your Bluring Scale : "))
    if scale <=10 :
      break
    else:
      print("Only <10 Values Are Accepted !!! ")



# Get image dimensions
  imgHeight, imgWidth, imgColumn = img1.shape 

# Create a new image (initialized with zeros)
  imgblur = np.zeros_like(img1)

# Blur each pixel
  for y in range(imgHeight):
      for x in range(imgWidth):
        # Compute indices for surrounding pixels
          xStart = (x + scale) % imgWidth
          xEnd = (x - scale) % imgWidth
          yStart = (y + scale) % imgHeight
          yEnd = (y - scale) % imgHeight

        # Cacluting Value wrt Respective Channel 
          r = np.mean(img1[yEnd:yStart , xEnd:xStart , 2])
          g = np.mean(img1[yEnd:yStart , xEnd:xStart , 1])
          b = np.mean(img1[yEnd:yStart , xEnd:xStart , 0])

        # Update new image
          imgblur[y, x] = [b, g, r]

  # Display the original and blurred images
  plt.figure(figsize=(10, 5))
  plt.subplot(1, 2, 1)
  plt.imshow(img1)
  plt.title('Original Image')

  plt.subplot(1, 2, 2)
  plt.imshow(imgblur)
  plt.title('Blurred Image')

  plt.show()


