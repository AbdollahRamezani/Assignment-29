import cv2
import numpy as np

room_background = cv2.imread("input/Virtual decoration/room_background.jpg")
spaces__room_mask = cv2.imread("input/Virtual decoration/spaces__room_mask.webp")
spaces_room_foreground = cv2.imread("input/Virtual decoration/spaces_room_foreground.webp")

room_background = cv2.cvtColor(room_background, cv2.COLOR_BGR2GRAY)
spaces__room_mask = cv2.cvtColor(spaces__room_mask, cv2.COLOR_BGR2GRAY)
spaces_room_foreground = cv2.cvtColor(spaces_room_foreground, cv2.COLOR_BGR2GRAY)

room_background = room_background.astype(np.float32) 
spaces__room_mask = spaces__room_mask.astype(np.float32)
spaces_room_foreground = spaces_room_foreground.astype(np.float32)


spaces__room_mask_1 = spaces__room_mask /255.0
result_1= np.multiply(spaces_room_foreground, spaces__room_mask_1)

spaces__room_mask_invert = 255 - spaces__room_mask
spaces__room_mask_invert = spaces__room_mask_invert / 255.0
result_2 = np.multiply(room_background, spaces__room_mask_invert)

result_3 = np.add(result_1, result_2)

result_3 = result_3.astype(np.uint8) 

cv2.imshow("result", result_3)
cv2.imwrite("output/Virtual decoration/result_3.jpg", result_3)
cv2.waitKey()