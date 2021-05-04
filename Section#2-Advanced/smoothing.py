import cv2 as cv

img = cv.imread("./Resources/Photos/0003.jpeg")
cv.imshow('Weirdo', img)

# Averaging Blur
average = cv.blur(img, (7, 7))
cv.imshow('Average Blur', average)

# Gaussian Blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian Blur', gauss)

cv.waitKey(0)