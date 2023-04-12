import numpy as np
import cv2
from skimage import data, filters   # pip install scikit-image
 
# Open Video
cap = cv2.VideoCapture('input/Background estimation/cars.mp4')
 
# Randomly select 25 frames
frameIds = cap.get(cv2.CAP_PROP_FRAME_COUNT) * np.random.uniform(size=25)
 
# Store selected frames in an array
frames = []
for fid in frameIds:
    cap.set(cv2.CAP_PROP_POS_FRAMES, fid)
    ret, frame = cap.read()
    frames.append(frame)
 
# Calculate the median along the time axis
medianFrame = np.median(frames, axis=0).astype(dtype=np.uint8)    
 
# Display median frame
cv2.imshow('Background estimation', medianFrame)
cv2.imwrite("output/Background estimation/Background estimation.jpg", medianFrame)
cv2.waitKey(0)