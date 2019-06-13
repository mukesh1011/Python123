import cv2
import numpy

img = cv2.imread("smallgray.png", 0)
print(img)

# cv2.imwrite("newsmallgray.png", img)

print(img[0:2, 2:4])

print("=" * 100)
ims = numpy.hstack((img,img))
print(ims)

lst = numpy.hsplit(ims, 2)
print(lst)

