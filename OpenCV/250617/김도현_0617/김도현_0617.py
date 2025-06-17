import cv2
import numpy as np


img = cv2.imread('./cat.jpg', cv2.IMREAD_COLOR)
if img is None:
    print("cat.jpg 파일을 찾을 수 없습니다.")
    exit()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

sobel_x = cv2.Sobel(gray, cv2.CV_64F, 1, 0, ksize=3)
sobel_y = cv2.Sobel(gray, cv2.CV_64F, 0, 1, ksize=3)
sobel = cv2.magnitude(sobel_x, sobel_y)
sobel = np.uint8(np.absolute(sobel))

laplacian = cv2.Laplacian(gray, cv2.CV_64F)
laplacian = np.uint8(np.absolute(laplacian))

canny = cv2.Canny(gray, 100, 200)

cv2.imshow('Original', img)
cv2.imshow('Sobel Edge', sobel)
cv2.imshow('Laplacian Edge', laplacian)
cv2.imshow('Canny Edge', canny)

cv2.imwrite('sobel_cat.jpg', sobel)
cv2.imwrite('laplacian_cat.jpg', laplacian)
cv2.imwrite('canny_cat.jpg', canny)

cv2.waitKey(0)
cv2.destroyAllWindows()
