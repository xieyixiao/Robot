#-*- coding: utf-8 -*-
import cv2
import numpy as np
from naoqi import ALProxy


class MyClass(GeneratedClass):
    def __init__(self):
        GeneratedClass.__init__(self)

    def onLoad(self):
        self.path = r"./Pic/Pic1.jpg"
        #put initialization code here
        pass

    def onUnload(self):
        #put clean-up code here
        pass

    def onInput_onStart(self):
        x = 0
        y = 0
        image = cv2.imread(self.path)
        len_x = image.shape[1]
        len_y = image.shape[0]
        # 矩形掩膜
        mask = np.zeros((image.shape[0:2]), np.uint8)
        cv2.rectangle(mask, (int(len_x / 2 - 80), int(len_y / 2 - 50)),
                      (int(len_x / 2 + 80), int(len_y)), 255, -1)
        mask = cv2.bitwise_not(mask)
        # 加掩膜后图像
        # 灰度处理
        #im_1 = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        (im_1, u, v) = cv2.split(image)
        # 直方图均匀化
        im_2 = cv2.equalizeHist(im_1)
        # 自适应阈值处理
        # im_3 = cv2.adaptiveThreshold(im_2, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 3)
        ret, im_ex = cv2.threshold(im_2, 225, 255, cv2.THRESH_BINARY)
        im_ex = cv2.bitwise_and(im_ex, mask)
        # 形态学处理
        kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (15, 15))
        masked_draw = cv2.morphologyEx(im_ex, cv2.MORPH_CLOSE, kernel, iterations=0)
        # masked_draw2 = cv2.morphologyEx(im_ex, cv2.MORPH_OPEN, kernel, iterations=0)
        minLineLength = 100
        maxLineGap = 10
        lines = cv2.HoughLinesP(masked_draw, 1, np.pi / 180, 50, minLineLength, maxLineGap)
        # P1 = False
        # P2 = False
        for i in range(0, len(lines)):
            for x1, y1, x2, y2 in lines[i]:
                x = x + x1 + x2
                y = y + y1 + y2
        x = x / len(lines) / 2
        y = y / len(lines) / 2
        if x > 200:
            self.Left()
        elif x > 100:
            self.Right()
        # elif x == 0:
        #   self.onStoped()
        else:
            self.Straight()

        #self.onStopped() #activate the output of the box
        pass

    def onInput_onStop(self):
        self.onUnload() #it is recommended to reuse the clean-up as the box is stopped
        self.onStopped() #activate the output of the box