import os
import cv2
import numpy as np
# import matplotlib.pyplot as plt
image_path='form.jpg'
image=cv2.imread(image_path)
gray_scale=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)

cv2.imwrite("dump/gray_scale.jpg",gray_scale)

th1,img_bin = cv2.threshold(gray_scale,150,225,cv2.THRESH_BINARY)
cv2.imwrite("dump/img_bin.jpg",img_bin)

img_bin=~img_bin
cv2.imwrite("dump/img_bin2.jpg",img_bin)

print(img_bin.shape)

line_min_width = 5
kernal_h = np.ones((1,line_min_width), np.uint8)
print(kernal_h)

kernal_v = np.ones((line_min_width,1), np.uint8)
print(kernal_v)

img_bin_h = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernal_h)
print(img_bin_h)

img_bin_v = cv2.morphologyEx(img_bin, cv2.MORPH_CLOSE, kernal_v)
print(img_bin_v)

img_bin_final=img_bin_h|img_bin_v
print(img_bin_final)

s_, labels, stats,y_ = cv2.connectedComponentsWithStats(~img_bin_final, connectivity=8, ltype=cv2.CV_32S)
print(labels,stats,s_,y_)
for x,y,w,h,area in stats:
    cv2.rectangle(image,(x,y),(x+w,y+h),(0,255,0),2)
cv2.imwrite("dump/image.jpg",image)

#print(s_, labels, stats,y_)