import cv2
import datetime

cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')


out = cv2.VideoWriter('output.avi', fourcc, 30.0, (1280, 720))

while cap.isOpened():
    ret, frame = cap.read()
    if ret:

        font = cv2.FONT_HERSHEY_SIMPLEX
        text = 'Width: ' + str(cap.get(3)) + ' Height: ' + str(cap.get(4))
        datet = str(datetime.datetime.now())
        cv2.putText(frame, text, (10, 50), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        cv2.putText(frame, datet, (10, 90), font, 1, (0, 255, 255), 2, cv2.LINE_AA)
        out.write(frame)
        cv2.imshow('frame', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()
