import cv2 as cv

img = cv.imread('reading_text_images/photo.jpg')
img = cv.cvtColor(img, cv.COLOR_RGB2GRAY )

_, result = cv.threshold(img, 150, 255, cv.THRESH_BINARY) 
# I made the thresh 150 bcs my image is shiny

adaptive= cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 81, 8)
# can dinamically change according to the light 

#cv.imshow('Image', img)
cv.imshow('Adaptive', adaptive)
#cv.imshow('Result', result)
cv.waitKey(0)
cv.destroyAllWindows()