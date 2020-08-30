import numpy as np
import cv2

cap = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('videos/output.avi',fourcc, 20.0, (640,480))

while (True):
    ret, frame = cap.read()
    if ret:
        frame = cv2.flip(frame, 0)    # 이미지 반전,  0:상하, 1 : 좌우
        out.write(frame)
        cv2.imshow('frame', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

cap.release()
out.release()
cv2.destroyAllWindows()