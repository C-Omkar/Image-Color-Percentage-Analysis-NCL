import cv2
import numpy as np

imagePath = "D:\OneDrive - Indian Institute of Technology Guwahati\Work Related\Image Analysis Color Percentage\ScrewReactor/"
img = cv2.imread(imagePath+"Screw Red.jpeg")
cv2.line(img, (250,235), (250,360), (0,0,0), 2)
cv2.imshow("img", img)
cv2.waitKey(0)
cv2.destroyAllWindows()