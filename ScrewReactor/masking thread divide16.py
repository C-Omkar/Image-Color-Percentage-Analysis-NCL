from re import L
import cv2
import numpy as np

imagePath = "D:\OneDrive - Indian Institute of Technology Guwahati\Work Related\Image Analysis Color Percentage\ScrewReactor/"
img = cv2.imread(imagePath+"Screw Red.jpeg")

mask = np.zeros(img.shape[:2], dtype="uint8")
pts = np.array([[50,80],[70,200],[410,120],[390,00]]) # points go anticlockwise, first is the top left one
lengthinc = pts[3][0]-pts[0][0]
lengthinc = lengthinc/4
hinc = pts[0][1]-pts[3][1]
hinc = hinc/4
heightinc = pts[1][1]-pts[0][1]
heightinc = heightinc/4
linc = pts[1][0]-pts[0][0]
linc = linc/4

# points = np.array([[pts[0][0], pts[0][1]],[pts[0][0]+linc, pts[0][1]+heightinc],[pts[0][0]+linc+lengthinc, pts[0][1]+heightinc-hinc],[pts[0][0] + lengthinc, pts[0][1]-hinc]])

# print(points)
red_area = []
for i in range(4):
    for j in range(4):
        
        firstptx = pts[0][0] + j*lengthinc + i*linc
        firstpty = pts[0][1] + i*heightinc - j*hinc
        points = np.array([[firstptx, firstpty], [firstptx + linc, firstpty + heightinc], [firstptx + linc + lengthinc, firstpty + heightinc - hinc], [firstptx + lengthinc, firstpty - hinc]])
        mask = np.zeros(img.shape[:2], dtype="uint8")
        cv2.fillPoly(mask, pts = np.int32([points]), color=(255,255,255))
        # areapixel = cv2.contourArea(pts)
        area = ((360-235)/0.7)**2
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
        red_area.append(area_red)
        print('Red pixel area:', np.round(area_red, 2), "cm2")
        cv2.imshow("ANDed mask", labOutput)


red_area = np.array(red_area)
mean = np.mean(red_area)
std = np.std(red_area)
print('Red pixel area mean:', np.round(mean, 2), "cm2")
print('Red pixel area std:', np.round(std, 2), "cm2")

cv2.waitKey(0)
cv2.destroyAllWindows()