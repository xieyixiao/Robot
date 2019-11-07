#-*- coding: utf-8 -*-
import cv2
import numpy as np

# 读取图像
path = r"./new.avi_20191104_212105.728.jpg"
image = cv2.imread(path)
len_x = image.shape[1]
len_y = image.shape[0]
# 矩形掩膜
mask = np.zeros((image.shape[0:2]), np.uint8)
cv2.rectangle(mask, (int(len_x / 2 - 80), int(len_y / 2 - 50)),
              (int(len_x / 2 + 80), int(len_y)), 255, -1)
mask = cv2.bitwise_not(mask)
# 加掩膜后图像
masked_ori = cv2.bitwise_and(image, image, mask=mask)
masked_dst = image.copy()
# 灰度处理
im_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 直方图均匀化
im_2 = cv2.equalizeHist(im_1)
# 自适应阈值处理
# im_3 = cv2.adaptiveThreshold(im_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
ret, im_ex = cv2.threshold(im_2, 225, 255, cv2.THRESH_BINARY)
im_ex = cv2.bitwise_and(im_ex, mask)
# 形态学处理
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
masked_draw = cv2.morphologyEx(im_ex, cv2.MORPH_CLOSE, kernel, iterations=0)
masked_draw2 = cv2.morphologyEx(im_ex, cv2.MORPH_OPEN, kernel, iterations=0)


minLineLength = 100
maxLineGap = 10
lines = cv2.HoughLinesP(masked_draw, 1, np.pi / 180, 50, minLineLength, maxLineGap)
P1 = False
P2 = False
for i in range(0, len(lines)):
    for x1, y1, x2, y2 in lines[i]:
        if not P1:
            if x1 < len_x * 0.4 and len_y * 0.4 < y1 < len_y * 0.7:
                x3, y3 = x1, y1
                P1 = True
        if not P2:
            if x1 > len_x * 0.8 and len_y * 0.3 < y1 < len_y*0.6:
                x4, y4 = x1, y1
                P2 = True
        if P1 and P2:
            cv2.line(masked_dst, (x3, y3), (x4, y4), (0, 255, 0), 5)
# 显示原始图像
cv2.namedWindow("masked_ori", 0)
cv2.imshow("masked_ori", image)
# 显示白线
cv2.namedWindow("dst", 0)
cv2.imshow("dst", masked_dst)
cv2.waitKey(0)
