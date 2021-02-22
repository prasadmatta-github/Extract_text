import cv2, numpy as np 

# cv2 module is used to reading and performing tasks on the images
# Numpy module is used to create or perform matrix operations or manipulations

def run(img):
    
    # Converting BGR image into Gray scale image using cv2 module
    # Kernel is used to perform the dilation 
    gray, kernel = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), np.ones((3,3), np.uint8) 
    
    #  Dilation will add pixels to edges of an objects which are present
    # in the images
    img_dilation = cv2.dilate(gray, kernel, iterations=1)
    # After applying image dilation only text is Black in color.  
    # So replacing all the values of dilation image which are grater 
    # then 85 with 255 to get Text. 
    img[img_dilation > 85] = 255 
    # imwrite function is used to save image locally.
    cv2.imwrite('output.jpg',img)

run(cv2.imread("input.png"))
