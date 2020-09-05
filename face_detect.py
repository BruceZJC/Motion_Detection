import cv2 
face_cascade= cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
first_frame=None

video = cv2.VideoCapture(0)
while True:
    check, frame = video.read()
    print(check)
    print(frame)
    gray_img=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    face=face_cascade.detectMultiScale(gray_img,scaleFactor=1.05, minNeighbors=5)
    #decrease the img size by 0.05 in every search
    for x,y,w,h in face:
        frame=cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,),3)

    cv2.imshow("Color Frame",frame)
    
    key = cv2.waitKey(1)
    if key == ord('q'):
        break
video.release()
cv2.destroyAllWindows() 