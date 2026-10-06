import cv2

cap=cv2.VideoCapture(0)

if not cap.isOpened():
    "linux not let you,solve that shit"
    exit()

print("opened webcam, q to quit")

while True:
    ret, frame=cap.read()

    if not ret:
        print("cant grab frame")
        break

    cv2.imshow('webcamtest',frame)

    if cv2.waitKey(1)&0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()