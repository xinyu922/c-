import cv2 as cv
import numpy as np


def extrace_object_demo():
    capture = cv.VideoCapture("/Users/xinyu/Movies/IMG_0597.mov")

    while(True):
        ret, frame = capture.read()
        if ret == False:
            break
        hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
        lower_hsv = np.array([78, 43, 46])
        upper_hsv = np.array([99, 255, 255])
        mask = cv.inRange(hsv, lower_hsv, upper_hsv)
        dst = cv.bitwise_and(frame, frame, mask = mask)         #添加逻辑与操作，保存与那图像的颜色
        cv.imshow("video", frame)
        cv.imshow("mask", dst)
        c = cv.waitKey(40)
        if c == 27:
            break


def color_space_demo(image):    #不同色彩空间的相互转换
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
    cv.imshow("gray", gray)
    hsv = cv.cvtColor(image, cv.COLOR_BGR2HSV)
    cv.imshow("hsv", hsv)
    yuv = cv.cvtColor(image, cv.COLOR_BGR2YUV)
    cv.imshow("yuv", yuv)
    ycrcb = cv.cvtColor(image, cv.COLOR_BGR2YCR_CB)
    cv.imshow("ycrcb", ycrcb)


# src = cv.imread("cat.jpg")
# cv.namedWindow("Cat", cv.WINDOW_AUTOSIZE)
# cv.imshow("Cat",src)
# color_space_demo(src)
extrace_object_demo()
cv.waitKey(0)

cv.destroyAllWindows()

