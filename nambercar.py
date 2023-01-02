import cv2
import numpy as np
import imutils
import easyocr
from matplotlib import pyplot as pl

img =cv2.imread('images/1623477926.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # відкрили зображення

img_filter = cv2.bilateralFilter(gray, 11, 15, 15) # оптимізували
adges = cv2.Canny(img_filter, 30, 200)

cont = cv2.findContours(adges.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE) # знайшли края та контури та відсортували
cont = imutils.grab_contours(cont)
cont = sorted(cont, key=cv2.contourArea, reverse=True)

pos = None
for c in cont:
    approx = cv2.approxPolyDP(c, 10, True)
    if len(approx) == 4:
        pos = approx
        break

mask =np.zeros(gray.shape, np.uint8)
new_img = cv2.drawContours(mask, [pos], 0, 255, -1)
bitwise_img = cv2.bitwise_and(img, img, mask=mask)

(x, y) = np.where(mask == 255)
(x1, y1) = (np.min(x), np.min(y))
(x2, y2) = (np.max(x), np.max(y))
cropp = gray[x1:x2, y1:y2]

text = easyocr.Reader(['en'])
text = text.readtext(cropp)

res = text[0][-2]
final_image = cv2.putText(img, (x1 - 200, y2 + 60), cv2.FONT_HERSHEY_PLAIN, 3, (0, 0, 255), 2)
final_image = cv2.rectangle(img, (x1, x2), (y1, y2), (0, 255, 0), 2)

pl.imshow(cv2.cvtColor(final_image, cv2.COLOR_BGR2RGB))
pl.show()
