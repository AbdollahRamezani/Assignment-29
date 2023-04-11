import cv2
import numpy as np

image1 = cv2.imread("input/secret_text/image1.png")
image2 = cv2.imread("input/secret_text/image2.png")

result = cv2.subtract(image2, image1)  #تفریق در زمینه سفید جای متغییرها برعکس است
result = 255 -result

cv2.imshow("result", result)
cv2.imwrite("output/secret_text.jpg", result)
cv2.waitKey()