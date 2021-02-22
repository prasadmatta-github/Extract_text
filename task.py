import cv2, numpy as np

def run(img):
    gray, kernel = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY), np.ones((5,5), np.uint8) 
    img_dilation = cv2.dilate(gray, kernel, iterations=1)
    img[img_dilation > 30] = 255 
    cv2.imwrite('output.jpg',img)

run(cv2.imread("input.png"))
