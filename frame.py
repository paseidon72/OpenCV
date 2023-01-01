import cv2
import numpy as np

photo = np.zeros((450, 450, 3), dtype='uint8')
# RGB - standart
# BGR - format v OpenCV
# photo[100:150, 200:280] = 4, 203, 217

cv2.rectangle(photo, (30, 30), (100, 100), (4, 203, 217), thickness=cv2.FILLED)
# cv2.line(photo, (200, 200), (0, 200), (4, 203, 217), thickness=3)
cv2.line(photo, (0, photo.shape[0] // 2), (photo.shape[1], photo.shape[0] // 2), (4, 203, 217), thickness=3)
cv2.circle(photo, (photo.shape[1] // 2, photo.shape[0] // 2), 100, (4, 203, 217), thickness=1)
cv2.putText(photo, 'Text', (100, 150), cv2.FONT_HERSHEY_TRIPLEX, 1, (255, 0, 0), 1)
cv2.imshow('Photo', photo)
cv2.waitKey(0)