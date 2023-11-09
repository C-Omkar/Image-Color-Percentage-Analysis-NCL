import cv2
import numpy as np

imagePath = "D:\OneDrive - Indian Institute of Technology Guwahati\Work Related\Image Analysis Color Percentage\ScrewReactor/"
img = cv2.imread(imagePath+"Screw Red.jpeg")

mask = np.zeros(img.shape[:2], dtype="uint8")
pts = np.array([[50,80],[70,200],[410,120],[390,00]]) # points go anticlockwise, first is the top left one

cv2.fillPoly(mask, pts = [pts], color=(255,255,255))
# areapixel = cv2.contourArea(pts)

area = ((360-235)/7)**2
# print(area)

masked = cv2.bitwise_and(img, img, mask=mask)
cv2.imshow("masked", masked)
# pixels = cv2.countNonZero(mask)
# print("pixels: ", pixels)

# Lab Color Space
lowerValues = np.array([0, 155, 130])
upperValues = np.array([255, 223, 226])
labImage = cv2.cvtColor(masked, cv2.COLOR_BGR2LAB)
labMask = cv2.inRange(labImage, lowerValues, upperValues)

labOutput = cv2.bitwise_and(masked, masked, mask=labMask)

area_red = cv2.countNonZero(labMask)/area
print('Red pixel area:', np.round(area_red, 2), "cm2")

cv2.imshow("ANDed mask", labOutput)

cv2.waitKey(0)
cv2.destroyAllWindows()