import cv2 as cv

#video = cv.VideoCapture(0)

video= cv.VideoCapture("people1.mp4")

subtractor = cv.createBackgroundSubtractorMOG2(10, 100)

while True:
    ret, frame = video.read()

    if not ret:
        break

    mask = subtractor.apply(frame)
    cv.imshow("Deneme", mask)

    if cv.waitKey(5) == ord("x"):
        break
        


cv.destroyAllWindows()
video.release()