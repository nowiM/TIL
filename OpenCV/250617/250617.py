# 예제 1----------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('../images/wheat.jpg', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
#
# sobel = cv2.Sobel(gray, cv2.CV_8U, 1, 0, 3)
# laplacian = cv2.Laplacian(gray, cv2.CV_8U, ksize = 3)
# canny = cv2.Canny(src, 100, 255)
#
# src = cv2.resize(src, dsize=(800, 600), interpolation=cv2.INTER_AREA)
# sobel = cv2.resize(sobel, dsize=(800, 600), interpolation=cv2.INTER_AREA)
# laplacian = cv2.resize(sobel, dsize=(800, 600), interpolation=cv2.INTER_AREA)
# canny = cv2.resize(sobel, dsize=(800, 600), interpolation=cv2.INTER_AREA)
#
# cv2.imshow('src', src)
# cv2.imshow('sobel', sobel)
# cv2.imshow('laplacian', laplacian)
# cv2.imshow('canny', canny)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 2----------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('../images/tomato.jpg', cv2.IMREAD_COLOR)
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv) # h: blue, s: green, v: red
#
# src = cv2.resize(src, dsize=(0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# hsv = cv2.resize(hsv, dsize=(0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# h = cv2.resize(h, dsize=(0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# s = cv2.resize(s, dsize=(0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# v = cv2.resize(v, dsize=(0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
#
# cv2.imshow('src', src)
# cv2.imshow('hsv', hsv)
# cv2.imshow('h', h)
# cv2.imshow('s', s)
# cv2.imshow('v', v)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 3----------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('../images/tomato.jpg', cv2.IMREAD_COLOR)
# hsv = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
# h, s, v = cv2.split(hsv) # h: blue, s: green, v: red
#
# lower_red = cv2.inRange(hsv, (0, 100, 100), (5, 255, 255))
# upper_red = cv2.inRange(hsv, (170, 100, 100), (100, 255 ,255))
#
# added_red = cv2.addWeighted(lower_red, 1.0, upper_red, 1.0, 0.0)
#
# red = cv2.bitwise_and(hsv, hsv, mask=added_red)
# red = cv2.cvtColor(red, cv2.COLOR_HSV2BGR)
#
# src = cv2.resize(src, dsize=(0,0), fx=0.5, fy=0.5, interpolation=cv2.INTER_LINEAR)
# red = cv2.resize(red, dsize=(0,0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
#
# cv2.imshow('src', src)
# cv2.imshow('red', red)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 4----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# src = np.zeros((768, 1366, 3), dtype=np.uint8)
#
# src = cv2.line(src, (100, 100), (1200, 100), (0, 0, 255), 3, cv2.LINE_AA)
# src = cv2.circle(src, (300, 300), 50, (0, 255, 0), cv2.FILLED, cv2.LINE_4)
# src = cv2.rectangle(src, (500, 500), (1000, 400), (255, 0, 0), 5, cv2.LINE_8)
# src = cv2.ellipse(src, (1200, 300), (100, 50), 0, 90, 100, (255, 255, 0), 2)
#
# pts1 = np.array([[100, 500], [300, 500], [200, 600]])
# pts2 = np.array([[600, 500], [800, 500], [700, 600]])
# src = cv2.polylines(src, [pts1], True, (0, 255, 255), 2)
# src = cv2.fillPoly(src, [pts2], (255, 0, 255), cv2.LINE_AA)
#
# src = cv2.putText(src, 'Ryan', (900, 600), cv2.FONT_HERSHEY_COMPLEX, 2, (255, 255, 255))
#
# cv2.imshow('src', src)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 5----------------------------------------------------------------------
# import cv2
#
# img = cv2.imread('../images/sunset.jpg')
# x = 320; y = 150; w = 50; h = 50
# roi = img[y:y+h, x:x+w]
# print(roi.shape)
# cv2.rectangle(roi, (0,0), (h-1, w-1), (0, 255, 0))
# cv2.imshow('img', img)
#
# key = cv2.waitKey(0)
# print(key)
# cv2.destroyAllWindows()

# 예제 6----------------------------------------------------------------------
# import cv2
#
# img = cv2.imread('../images/sunset.jpg')
#
# x, y, w, h = cv2.selectROI('img', img, False)
# print(x, y, w, h)
# if w and h:
#     roi = img[y:y + h, x:x + w]
#     cv2.imshow('cropped', roi)
#     cv2.moveWindow('cropped', 0, 0)
#     cv2.imwrite('./cropped2.jpg', roi)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 7----------------------------------------------------------------------
# import cv2
#
# isDragging = False
# x0, y0, w, h = -1, -1, -1, -1
# blue, red = (255, 0, 0), (0, 0, 255)
#
# def onMouse(event, x, y, flags, param):
#     global isDragging, x0, y0, img
#     if event == cv2.EVENT_LBUTTONDOWN:
#         isDragging = True
#         x0 = x
#         y0 = y
#     elif event == cv2.EVENT_MOUSEMOVE:
#         if isDragging:
#             img_draw = img.copy()
#             cv2.rectangle(img_draw, (x0, y0), (x, y), blue, 2)
#             cv2.imshow('img', img_draw)
#     elif event == cv2.EVENT_LBUTTONUP:
#         if isDragging:
#             isDragging = False
#             w = x - x0
#             h = y - y0
#             print('x: %d, y: %d, w: %d, h: %d' % (x0, y0, w, h))
#             if w > 0 and h > 0:
#                 img_draw = img.copy()
#                 cv2.rectangle(img_draw, (x0, y0), (x, y), red, 2)
#                 cv2.imshow('img', img_draw)
#                 roi = img[y0: y0 + h, x0: x0 + w]
#                 cv2.imshow('croppend', roi)
#                 cv2.moveWindow('croppend', 0, 0)
#                 cv2.imwrite('../images/cropped1212.jpg', roi)
#                 print('croped.')
#             else:
#                 cv2.imshow('img', img)
#                 print('좌측 상단에서 우측 하락으로 영역을 드래그 하세요.')
#
# img = cv2.imread('../images/sunset.jpg')
# cv2.imshow('img', img)
# cv2.setMouseCallback('img', onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 8----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# win_name = 'scanning'
# img = cv2.imread('../images/paper.jpg')
# rows, cols = img.shape[:2]
# draw = img.copy()
# pts_cnt = 0
# pts = np.zeros((4, 2), dtype=np.float32)
#
# def onMouse(event, x, y, flags, param):
#     global pts_cnt
#
#     if event == cv2.EVENT_LBUTTONDOWN:
#         cv2.circle(draw, (x, y), 10, (0, 255, 0), -1)
#         cv2.imshow(win_name, draw)
#         pts[pts_cnt] = [x, y]
#         pts_cnt += 1
#
#         if pts_cnt == 4:
#             print(pts)
#             sm = pts.sum(axis=1)
#             print(sm)
#             diff = np.diff(pts, axis=1)
#             print(diff)
#
#             topLeft = pts[np.argmin(sm)]
#             bottomRight = pts[np.argmax(sm)]
#             topRight = pts[np.argmin(diff)]
#             bottomLeft = pts[np.argmax(diff)]
#
#             pts1 = np.float32([topLeft, topRight, bottomRight, bottomLeft])
#             w1 = abs(bottomRight[0] - bottomLeft[0])
#             w2 = abs(topRight[0] - topLeft[0])
#             h1 = abs(topRight[1] -  bottomRight[1])
#             h2 = abs(topLeft[1] - bottomLeft[1])
#
#             width = int(max([w1, w2]))
#             height = int(max([h1, h2]))
#             pts2 = np.float32([[0, 0], [width - 1, 0], [width - 1, height - 1], [0, height - 1]])
#             mtrx = cv2.getPerspectiveTransform(pts1, pts2)
#             result = cv2.warpPerspective(img, mtrx, (width, height))
#             cv2.imshow('scanned', result)
#
# cv2.imshow(win_name, img)
# cv2.setMouseCallback(win_name, onMouse)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 9----------------------------------------------------------------------
# import cv2
#
# target = cv2.imread('../images/4star.jpg')
# shapes = cv2.imread('../images/shapestomatch.jpg')
#
# targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
# shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)
#
# ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
# ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)
#
# cntrs_target, _ = cv2.findContours(targetTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
# cntrs_shapes, _ = cv2.findContours(shapesTh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
#
# matchs = []
#
# for contr in cntrs_shapes:
#     match = cv2.matchShapes(cntrs_target[0], contr, cv2.CONTOURS_MATCH_I2, 0.0)
#     matchs.append((match, contr))
#     cv2.putText(shapes, '%.2f' % match, tuple(contr[0][0]), cv2.FONT_HERSHEY_PLAIN, 1,
#                                               (0, 0, 255), 1)
#
# matchs.sort(key=lambda x : x[0])
# cv2.drawContours(shapes, [matchs[0][1]], -1, (0, 255, 0), 3) # -1 모든 컨투어를 다 표시해라.
# cv2.imshow('target', target)
# cv2.imshow('Match Shape', shapes)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 10-----------------------------------------------------------------------
# 시와 토마시 코너
# import cv2
# import numpy as np
#
# img = cv2.imread('../images/coffee.jpg')
# gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# print(gray.shape)
#
# corner = cv2.cornerHarris(gray, 2, 3, 0.04)
# print(corner.shape)
#
# coord = np.where(corner > 0.1 * corner.max())
# print(len(coord))
# print(coord)
# coord = np.stack((coord[1], coord[0]), axis=1)
# print(coord)
#
# for x, y in coord:
#     cv2.circle(img, (x, y), 5, (0, 0, 255), 1, cv2.LINE_AA)
#
# corner_norm = cv2.normalize(corner, None, 0, 255, cv2.NORM_MINMAX, cv2.CV_8U)
# corner_norm = cv2.cvtColor(corner_norm, cv2.COLOR_GRAY2BGR)
# merged = np.hstack((corner_norm, img))
#
# merged_re = cv2.resize(merged, dsize=(0, 0), fx = 0.3, fy = 0.3, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('Harris Corner', merged_re)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 10-----------------------------------------------------------------------
# 블록 선체
# import cv2
#
# src = cv2.imread('../images/convex.png')
# dst = src.copy()
#
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ret, binary = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
#
# contours, hierarchy = cv2.findContours(binary, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_NONE)
#
# for i in contours:
#     hull = cv2.convexHull(i, clockwise = True)
#     cv2.drawContours(dst, [hull], 0, (0, 0, 255), 2)
#
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 11-----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# img = cv2.imread('../images/morph_hole.png')
# k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
#
# rect = cv2.dilate(img, k1, iterations=3)
# cross = cv2.dilate(img, k2, iterations=3)
# ellipse = cv2.dilate(img, k3, iterations=3)
#
# merged = np.hstack((img, rect, cross, ellipse))
#
# cv2.imshow('Dilation', merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 12-----------------------------------------------------------------------

# import cv2
# import numpy as np
#
# img = cv2.imread('../images/morph_dot.png')
# k1 = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# k2 = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
# k3 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (3, 3))
#
# rect = cv2.erode(img, k1, iterations=3)
# cross = cv2.erode(img, k2, iterations=3)
# ellipse = cv2.erode(img, k3, iterations=3)
#
# merged = np.hstack((img, rect, cross, ellipse))
#
# cv2.imshow('Dilation', merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 13-----------------------------------------------------------------------
# 이미지 강조할 부분을 결정해서 opening, closing 둘 중 결정
# import cv2
# import numpy as np
#
# img1 = cv2.imread('../images/morph_dot.png', cv2.IMREAD_GRAYSCALE)
# img2 = cv2.imread('../images/morph_hole.png', cv2.IMREAD_GRAYSCALE)
#
# k = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
# opening = cv2.morphologyEx(img1, cv2.MORPH_OPEN, k)
# closing = cv2.morphologyEx(img2, cv2.MORPH_OPEN, k)
#
# merged1 = np.hstack((img1, opening))
# merged2 = np.hstack((img2, closing))
#
# cv2.imshow('opening', merged1)
# cv2.imshow('closing', merged2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 14-----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# img = cv2.imread('../images/morphological.png')
#
# k = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
# gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, k)
#
# merged = np.hstack((img, gradient))
# cv2.imshow('gradient', merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 15-----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# img = cv2.imread('../images/moon_gray.jpg')
# k = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))
#
# tophat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
# blackhat = cv2.morphologyEx(img, cv2.MORPH_BLACKHAT, k)
#
# merged = np.hstack((img, tophat, blackhat))
# cv2.imshow('tophat, blackhat', merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 16-----------------------------------------------------------------------
# import cv2
# import numpy as np
#
# src = cv2.imread('../images/pencils.jpg')
# number1 = np.ones_like(src) * 127
# number2 = np.ones_like(src) * 2
#
# add = cv2.add(src, number1)
# sub = cv2.subtract(src, number1)
# mul = cv2.multiply(src, number2)
# div = cv2.divide(src, number2)
#
# src = np.concatenate((src, src, src, src), axis=1)
# number = np.concatenate((number1, number1, number2, number2), axis=1)
# dst = np.concatenate((add, sub, mul, div), axis=1)
# dst = np.concatenate((src, number, dst), axis=0)
#
# dst = np.concatenate((src, number, dst), axis=0)
#
# dst_re = cv2.resize(dst, dsize=(0, 0), fx=0.2, fy=0.2, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('dst', dst_re)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 17-----------------------------------------------------------------------
# import cv2
# import matplotlib.pylab as plt
#
# img1 = cv2.imread('../images/wing_wall.jpg')
# img2 = cv2.imread('../images/yate.jpg')
#
# img3 = img1 + img2
# img4 = cv2.add(img1, img2)
#
# imgs = {'ima1': img1, 'img2': img2, 'img1+img2': img3, 'cv.add(img1, img2)': img4}
#
# for i, (k, v) in enumerate(imgs.items()):
#     plt.subplot(2, 2, i + 1)
#     plt.imshow(v[:, :, ::-1])
#     plt.title(k)
#     plt.xticks([]); plt.yticks([])
#
# plt.show()
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 18-----------------------------------------------------------------------
# 이미지 비트 연산
# import numpy as np
# import cv2
#
# src = cv2.imread('../images/analysis.jpg')
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# _, binary = cv2.threshold(gray, 127, 255, cv2.THRESH_BINARY)
#
# _and = cv2.bitwise_and(gray, binary)
# _or = cv2.bitwise_or(gray, binary)
# _xor = cv2.bitwise_xor(gray, binary)
# _not = cv2.bitwise_not(gray)
#
# src = np.concatenate((np.zeros_like(gray), gray, binary, np.zeros_like(gray)), axis=1)
# dst = np.concatenate((_and, _or, _xor, _not), axis = 1)
# dst = np.concatenate((src, dst), axis = 0)
#
# dst_re = cv2.resize(dst, dsize=(0, 0), fx = 0.2, fy = 0.2, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('dst', dst_re)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 19-----------------------------------------------------------------------
# 이미지 비트 연산 활용
# import cv2
# import numpy as np
#
# img = cv2.imread('../images/yeosu.jpg')
#
# mask = np.zeros_like(img)
# cv2.circle(mask, (500, 410), 100, (255, 255, 255), -1)
#
# masked = cv2.bitwise_and(img, mask)
#
# cv2.imshow('original', img)
# cv2.imshow('mask', mask)
# cv2.imshow('masked', masked)
#
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 19-----------------------------------------------------------------------
# 색상의 분포를 알기 위해 사용
# import cv2
# import numpy as np
#
# src = cv2.imread('../images/road.jpg')
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
# result = np.zeros((src.shape[0], 256), dtype = np.uint8)
#
# hist = cv2.calcHist([gray], [0], None, [256], [0, 256])
# cv2.normalize(hist, hist, 0, result.shape[0], cv2.NORM_MINMAX)
#
# for x, y in enumerate(hist):
#     cv2.line(result, (x, result.shape[0]), (x, result.shape[0] -  int(y)), 255)
#
# dst = np.hstack([gray, result])
# dst_re = cv2.resize(dst, disize = (0, 0), fx = 0.5, fy = 0.5, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('dst', dst_re)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 20-----------------------------------------------------------------------
import cv2
import matplotlib.pylab as plt

img = cv2.imread('../images/mountain.jpg')
cv2.imshow('img', img)

channels = cv2.split(img)
colors = ('b', 'g', 'r')

for (ch, color) in zip(channels, colors):
    hist = cv2.calcHist([ch], [0], None, [256], [0, 256])
    plt.plot(hist, color = color)

plt.show()



