import cv2

image = cv2.imread("input/sketch/sajjad.jpg", 0)


invert = 255 - image
blurred = cv2.GaussianBlur(invert, (21, 21), 0)
invert_blurred = 255 - blurred

sketch = image / invert_blurred
sketch = sketch * 255

cv2.imshow("sketch_photo", sketch)
cv2.imwrite("output/sketch/sketch_photo.jpg", sketch)
cv2.waitKey()


