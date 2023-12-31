# Imports
import cv2
import numpy as np
from scipy.fftpack import sc_diff

# Read image
imagePath = "D:\OneDrive - Indian Institute of Technology Guwahati\Work Related\Image Analysis Color Percentage/"
img = cv2.imread(imagePath+"Test 2.jpeg")

# # Here, you define your target color as
# # a tuple of three values: RGB
# green = [130, 158, 0]

# # You define an interval that covers the values
# # in the tuple and are below and above them by 20
# diff = 20
scale = 0.7

# Calculate the new dimensions
width = int(img.shape[1]* scale)
height = int(img.shape[0]* scale)
newSize = (width, height)

# Resize the image:
img = cv2.resize(img, newSize, None, None, None, cv2.INTER_AREA)
print("img shape: ", img.shape)

# check out the image resized:
cv2.imshow("img resized", img)
cv2.waitKey(0)
# The HSV mask values, defined for the green color:
# lowerValues = np.array([29, 89, 70])
# upperValues = np.array([179, 255, 255])

lowerValues = np.array([40, 0, 185])
upperValues = np.array([190, 98, 250])

# Convert the image to HSV:
labImage = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)

# Create the HSV mask
labMask = cv2.inRange(labImage, lowerValues, upperValues)

# AND mask & input image:
labOutput = cv2.bitwise_and(img, img, mask=labMask)

cv2.imshow("ANDed mask", labOutput)
cv2.waitKey(0)

    # You can use the mask to count the number of white pixels.
    # Remember that the white pixels in the mask are those that
    # fall in your defined range, that is, every white pixel corresponds
    # to a green pixel. Divide by the image size and you got the
    # percentage of green pixels in the original image:
ratio_green = cv2.countNonZero(labMask)/(img.size/3)
print(labMask.size)
print(img.size)
    # This is the color percent calculation, considering the resize I did earlier.
colorPercent = (ratio_green * 100) 

    # Print the color percent, use 2 figures past the decimal point
print('green pixel percentage:', np.round(colorPercent, 2))

    # numpy's hstack is used to stack two images horizontally,
    # so you see the various images generated in one figure:
cv2.imshow("images", np.hstack([img, labOutput]))
cv2.waitKey(0)

# Be aware that opencv loads image in BGR format,
# that's why the color values have been adjusted here:
# boundaries = [([green[2], green[1]-diff, green[0]-diff],
#            [green[2]+diff, green[1]+diff, green[0]+diff])]

# Scale your BIG image into a small one:



# for each range in your boundary list:
# for (lower, upper) in boundaries:

#     # You get the lower and upper part of the interval:
#     lower = np.array(lower, dtype=np.uint8)
#     upper = np.array(upper, dtype=np.uint8)

#     # cv2.inRange is used to binarize (i.e., render in white/black) an image
#     # All the pixels that fall inside your interval [lower, uipper] will be white
#     # All the pixels that do not fall inside this interval will
#     # be rendered in black, for all three channels:
#     mask = cv2.inRange(img, lower, upper)

#     # Check out the binary mask:
#     cv2.imshow("binary mask", mask)
#     cv2.waitKey(0)

#     # Now, you AND the mask and the input image
#     # All the pixels that are white in the mask will
#     # survive the AND operation, all the black pixels
#     # will remain black
#     output = cv2.bitwise_and(img, img, mask=mask)

#     # Check out the ANDed mask:
#     cv2.imshow("ANDed mask", output)
#     cv2.waitKey(0)

#     # You can use the mask to count the number of white pixels.
#     # Remember that the white pixels in the mask are those that
#     # fall in your defined range, that is, every white pixel corresponds
#     # to a green pixel. Divide by the image size and you got the
#     # percentage of green pixels in the original image:
#     ratio_green = cv2.countNonZero(mask)/(img.size/3)

#     # This is the color percent calculation, considering the resize I did earlier.
#     colorPercent = (ratio_green * 100)  / scalePercent

#     # Print the color percent, use 2 figures past the decimal point
#     print('green pixel percentage:', np.round(colorPercent, 2))

#     # numpy's hstack is used to stack two images horizontally,
#     # so you see the various images generated in one figure:
#     cv2.imshow("images", np.hstack([img, output]))
#     cv2.waitKey(0)