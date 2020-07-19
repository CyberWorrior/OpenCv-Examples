import cv2 as cv

face_cascade = cv.CascadeClassifier('haarcascade_frontalface_default.xml')

# img = cv.imread('test3.jpg')

cap = cv.VideoCapture(4)
cap.set(3, 1920)
cap.set(4, 1080)

while cap.isOpened():
    ret, frame = cap.read()
    if ret:
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)

        for (x, y, w, h) in faces:
            cv.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 3)

        cv.imshow('faceDetect', frame)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
cv.destroyAllWindows()
