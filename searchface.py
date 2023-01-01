import cv2

img = cv2.imread('images/3.png')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = cv2.CascadeClassifier('faces.xml')
result = faces.detectMultiScale(gray, scaleFactor=1.2, minNeighbors=4)
for (x, y, w, h) in result:
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), thickness=3)
cv2.imshow("Result", img)
cv2.waitKey(0)
