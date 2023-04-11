import cv2
import numpy as np

image1 = cv2.imread("output/black_hole/good_black_hole1.jpg")
image2 = cv2.imread("output/black_hole/good_black_hole2.jpg")
image3 = cv2.imread("output/black_hole/good_black_hole3.jpg")
image4 = cv2.imread("output/black_hole/good_black_hole4.jpg")

image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
image3 = cv2.cvtColor(image3, cv2.COLOR_BGR2GRAY)
image4 = cv2.cvtColor(image4, cv2.COLOR_BGR2GRAY)

add_images = np.zeros((2000, 2000))

add_images[0:1000, 0:1000] = image1
add_images[0:1000, 1000:2000] = image2
add_images[1000:2000, 0:1000] = image3
add_images[1000:2000, 1000:2000] = image4


cv2.imshow("add_black_holes", add_images)
cv2.imwrite("output/black_hole/add_black_holes.jpg", add_images)
cv2.waitKey()

