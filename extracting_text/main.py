import cv2 as cv
import pytesseract
from pytesseract import Output
import PIL.Image

"""
Page segmentation modes: 
O Orientation and script detection (OSD) only
1 Automatic page segmentation with OSD. ‘
2 Automatic page segmentation, but no OSD, or OCR.
3 Fully automatic page segmentation, but no OSD. (Default)
4 Assume a single column of text of variable sizes.
5 Assume a single uniform block of vertically aligned text.
6 Assume a single uniform block of textJ
7 Treat the image as a single text line.
8 Treat the image as a single word.
9 Treat the image as a single word in a circle.
10 Treat the image as a single character.
11 Sparse text. Find as much text as possible in no particular order.
12 Sparse text with OSD.
13 Raw line. Treat the image as a single text line, bypassing hacks that are Tesseract—specific.
"""

myconfig = r"--psm 11 --oem 3"

#text = pytesseract.image_to_string(PIL.Image.open("logos.jpg"), config=myconfig)
#print(text)

img = cv.imread("signs.jpg")
height, width, _ = img.shape

data = pytesseract.image_to_data(img, config=myconfig, output_type=Output.DICT)

amount_boxes = len(data['text'])

for i in range(amount_boxes):
    if float(data['conf'][i]) > 40:
        (x, y, width, height) = (data['left'][i],data['top'][i],data['width'][i],data['height'][i])
        img = cv.rectangle(img, (x,y), (x+width, y+height), (0,255,0))
        img= cv.putText(img, data['text'][i], (x, y+height+20), cv.FONT_HERSHEY_SIMPLEX, 0.7, color=(0,200,0),
                        thickness=2 ,lineType= cv.LINE_AA )




# boxes = pytesseract.image_to_boxes(img, config=myconfig)
# #print(boxes)

# for box in boxes.splitlines():
#     box = box.split(" ")
#     img = cv.rectangle(img, (int(box[1]), height - int(box[2])),(int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv.imshow("Image", img)
cv.waitKey(0)