import cv2
cap=cv2.VideoCapture(0)

while True:
    ret,frame=cap.read()

    print(ret)

    img_gray=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    cv2.imshow("window",frame)

    if cv2.waitKey(1) & 0xFF ==ord('x'):
        break

cv2.destroyAllWindows()
