import cv2
import numpy as np


src_img = cv2.imread("Excess CuSO4 4.jpeg")
img_rgb = cv2.cvtColor(src_img, cv2.COLOR_BGR2RGB)
img_hsv = cv2.cvtColor(src_img, cv2.COLOR_BGR2HSV)


average_color_row_rgb = np.average(img_rgb, axis=0)
average_color_rgb = np.average(average_color_row_rgb, axis=0)
average_color_row_hsv = np.average(img_hsv, axis=0)
average_color_hsv = np.average(average_color_row_hsv, axis=0)
print("Average RGB:",average_color_rgb, "Average HSV:",average_color_hsv)