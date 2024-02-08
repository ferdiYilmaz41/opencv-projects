import cv2 as cv
import pytesseract
import PIL.Image

myconfig = r"--psm 8 --oem 3"

text = pytesseract.image_to_string(PIL.Image.open("logos.jpg"), config=myconfig)
#print(text)

img = cv.imread("logos.jpg")
height, width, _ = img.shape

boxes = pytesseract.image_to_boxes(img, config=myconfig)
#print(boxes)

for box in boxes.splitlines():
    box = box.split(" ")
    img = cv.rectangle(img, (int(box[1]), height - int(box[2])),(int(box[3]), height - int(box[4])), (0, 255, 0), 2)

cv.imshow("Image", img)
cv.waitKey(0)