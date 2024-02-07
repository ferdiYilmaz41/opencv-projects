import cv2 as cv

#video = cv.VideoCapture(0)

video= cv.VideoCapture('Motion_filtering/people.mp4')

subtractor = cv.createBackgroundSubtractorMOG2(10, 100)

while True:
    ret, frame = video.read()

    if not ret:
        break
    
    cv.imshow('Original', frame)
    mask = subtractor.apply(frame)
    cv.imshow("Deneme", mask)

    if cv.waitKey(5) == ord("x"):
        break
        


cv.destroyAllWindows()
video.release()