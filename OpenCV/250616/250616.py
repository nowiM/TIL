# 예제 1--------------------------------------------------------------------
import cv2
#
# capture = cv2.VideoCapture(0) # 사용할 카메라 지정
# # 객체 설정
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640) # 가로 640
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480) # 세로 480
#
# while cv2.waitKey(33) < 0: # waitKey 시간 설정
#     ret, frame = capture.read() # ret(읽었는지 못읽었는지 boolan 타입으로 저장), frame(읽으면 이미지 저장)
#     cv2.imshow('VideoFrame', frame) # 읽어드린 이미지 보여줌.
#
# capture.release() # 메모리 해제
# cv2.destroyAllWindows() # 카메라 윈도우창 제거
#
# # 예제 2--------------------------------------------------------------------
# import cv2
#
# cap = cv2.VideoCapture(0)
#
# if cap.isOpened():
#     while True:
#         ret, frame = cap.read()
#
#         if ret:
#             cv2.imshow('camera', frame)
#             if cv2.waitKey(1) != -1:
#                 cv2.imwrite('images/photo.jpg', frame)
#                 break
#             else:
#                 print('no frame')
#                 break
#         else:
#             print('no camera!')
# else:
#     print('no camera!')
#
# cap.release()
# cv2.destroyAllWindows()

# 예제 3--------------------------------------------------------------------
# cap = cv2.VideoCapture(0)
#
# if cap.isOpened:
#     file_path = 'images/record.avi'
#     fps = 30.0
#     fourcc = cv2.VideoWriter_fourcc(*'DIVX')
#     width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
#     height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
#     size = (int(width), int(height))
#     out = cv2.VideoWriter(file_path, fourcc, fps, size)
#
#     while True:
#         ret, frame = cap.read()
#         if ret:
#             cv2.imshow('camera-recording', frame)
#             out.write(frame)
#             if cv2.waitKey(int(1000 / fps)) != -1:
#                 break
#         else:
#             print('no frame')
#             break
#         out.release()
# else:
#     print("can't open camera!")
#
# cap.release()
# cv2.destroyAllWindows()

# 예제 4--------------------------------------------------------------------
# img_file = 'images/yeosu.jpg'
#
# # 원본: IMREAD_UNCHANGED 흑백:IMREAD_GRAYSCALE  컬러: IMREAD_COLOR
# img = cv2.imread(img_file, cv2.IMREAD_UNCHANGED)
#
# if img is not None:
#     cv2.imshow('IMG', img)
#     cv2.waitKey()
#     cv2.destroyAllWindows()
# else:
#     print('No image file.')

# 예제 5--------------------------------------------------------------------
# import cv2
#
# capture = cv2.VideoCapture('./images/youquiz4.mp4')
# print(capture.get(cv2.CAP_PROP_POS_FRAMES))
# print(capture.get(cv2.CAP_PROP_FRAME_COUNT))  # ← 수정
#
# while cv2.waitKey(33) < 0:
#     if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
#         capture.set(cv2.CAP_PROP_POS_FRAMES, 0)
#
#     ret, frame = capture.read()
#     if not ret:
#         break  # 파일 끝에 도달했을 때 안전하게 종료
#
#     cv2.imshow('wildlife', frame)
#
# capture.release()
# cv2.destroyAllWindows()

# 예제 6--------------------------------------------------------------------
# from datetime import datetime
#
# capture = cv2.VideoCapture('./images/youquiz4.mp4')
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# record = False
#
# while True:
#     if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
#         capture.open('./images/youquiz4.mp4')
#
#     ret, frame = capture.read()
#     cv2.imshow('VideoFrame', frame)
#     now = datetime.now().strftime('%d_%H-%M_%S')
#     key = cv2.waitKey(33)
#     print('key => ', key)
#
#     if key == 27: # esc
#         break
#     elif key == 49: # 숫자 1
#         print('캡쳐')
#         cv2.imwrite('./capture' + str(now) + '.png', frame)
#
#     elif key == 50:  # 숫자 2
#         print('녹화 시작')
#         record = True
#         height, width = frame.shape[:2]
#         video = cv2.VideoWriter('./capture/' + str(now) + '.avi', fourcc, 20.0, (width, height))
#
#     elif key == 51: # 숫자 3
#         print('녹화 중지')
#         record = False
#         video.release()
#
#     if record == True:
#         print('녹화 중...')
#         video.write(frame)

# 예제 7--------------------------------------------------------------------
# img_file = 'images/yeosu.jpg'
# save_file = 'images/yeosu_gray.jpg'
#
# # 원본: IMREAD_UNCHANGED 흑백:IMREAD_GRAYSCALE  컬러: IMREAD_COLOR
# img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)
# cv2.imshow(img_file, img)
# cv2.imwrite(save_file, img)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 8--------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
# dst = cv2.flip(src, 0)
# dst1 = cv2.flip(src, 1)
# dst2 = cv2.flip(src, -1)
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 9--------------------------------------------------------------------
# 회전함수
# import cv2
# import matplotlib.pyplot as plt
#
# def img_show(title = 'image', img = None, figsize = (8, 5)):
#     plt.figure(figsize = figsize)
#     if type(title) == list:
#         titles = title
#     else:
#         titles = []
#         for i in range(len(img)):
#             titles.append(title)
#
#     for i in range(len(img)):
#         if len(img[i].shape) <= 2:
#             # 이미지의 색상 공간을 반환하는데 사용
#             # src : 입력 이미지
#             # code : 변환하려는 색상 공간을 지정하는 플래그
#             # dst : 출력 이미지
#             # dstCn : 출력 이미지의 채널 수
#             rgbImg = cv2.cvtColor(img[i], cv2.COLOR_GRAY2BGR)
#         else:
#             rgbImg = cv2.cvtColor(img[i], cv2.COLOR_BGR2RGB)
#
#         plt.subplot(1, len(img), i + 1), plt.imshow(rgbImg)
#         plt.title(titles[i])
#         plt.xticks([]), plt.yticks([])
#
#     plt.show()
#
# src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
# height, width, channel = src.shape
# matrix = cv2.getRotationMatrix2D((width / 2, height / 2), 90, 1)
# dst = cv2.warpAffine(src, matrix, (width, height))
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# img_show(['Original', 'rotate_90'], [src, dst])
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 10--------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('./images/song_1.jpg', cv2.IMREAD_COLOR)
# height, width, channel = src.shape
# dst_pyrUp = cv2.pyrUp(src, dstsize=(width * 2, height * 2),
#                       borderType=cv2.BORDER_DEFAULT)
# dst_pyrDown = cv2.pyrDown(src)
#
# cv2.imshow('src', src)
# cv2.imshow('pyrUp', dst_pyrUp)
# cv2.imshow('pyrDown', dst_pyrDown)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 11--------------------------------------------------------------------
# import cv2
# import numpy as np
# img = cv2.imread('./images/cat.jpg')
# smaller = cv2.pyrDown(img)
# bigger = cv2.pyrUp(smaller)
#
# laplacian = cv2.subtract(img, bigger)
# restored = bigger + laplacian
#
# merged = np.hstack((img, laplacian, bigger, restored))
# merged = cv2.resize(merged, None, fx=1/2, fy = 1/2, interpolation=cv2.INTER_AREA)
# cv2.imshow('Laplacian Pyramid', merged)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# 예제 12--------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
# dst = cv2.resize(src, dsize=(800, 600), interpolation=cv2.INTER_AREA)
# # fx=0.3, fy=0.3 비율 설정하면 사이즈는 0으로
# dst2 = cv2.resize(src, dsize=(0, 0), fx=0.3, fy=0.3, interpolation=cv2.INTER_LINEAR)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 13--------------------------------------------------------------------
# 자르기
# import cv2
#
# src = cv2.imread('./images/chess.jpg', cv2.IMREAD_COLOR)
# print(src.shape)
# dst = src[100:600, 200:700].copy()
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 14--------------------------------------------------------------------
# import cv2
#
# src = cv2.imread('./images/chess.jpg', cv2.IMREAD_COLOR)
# print(src.shape)
# roi = src[100:600, 200:700]
# dst = roi
#
# src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
# dst = cv2.resize(dst, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 15--------------------------------------------------------------------
# 색상 공간 변환
# import cv2
#
# src = cv2.imread('./images/chess.jpg', cv2.IMREAD_COLOR)
# dst = cv2.cvtColor(src, cv2.COLOR_BGR2RGB)
#
# src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
# dst = cv2.resize(dst, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 15--------------------------------------------------------------------
# 역상(영상이나 이미지를 반전 된 색상으로 변환)
# import cv2
#
# src = cv2.imread('./images/bird.jpg', cv2.IMREAD_COLOR)
# dst = cv2.bitwise_not(src)
#
# src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
# dst = cv2.resize(dst, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
#
# cv2.imshow('sec', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 16--------------------------------------------------------------------
# 이진화, 패턴 찾는데 유리(자동차 번호판)
'''
파라미터
– src : 입력 이미지. 단일 채널 이미지(그레이스케일)을 입력해 사용
– thresh : 임계값
– maxval : 최대값
– type : 임계값 형식. 임계값을 초과한 값은 최댓값으로 변경하고 임계값 이하의 값은 0으로 바꾸는 등의
연산을 적용한다.
알고리즘
cv2.THRESH_OTSH 오츠 알고리즘 적용
'''
# import cv2
#
# src = cv2.imread('./images/duck.jpg', cv2.IMREAD_COLOR)
# gray = cv2.cvtColor(src, cv2.COLOR_BGR2GRAY)
# ret, dst = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
#
#
# src = cv2.resize(src, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
# dst = cv2.resize(dst, None, fx=1/2, fy=1/2, interpolation=cv2.INTER_AREA)
#
# cv2.imshow('src', src)
# cv2.imshow('dst', dst)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 16--------------------------------------------------------------------
# import cv2
# import numpy as np
# import matplotlib.pylab as plt
#
# img = cv2.imread('images/gray_gradient.jpg', cv2.IMREAD_GRAYSCALE)
# thresh_np = np.zeros_like(img)
# thresh_np[img > 127] = 255
#
# ret, thresh_cv = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
# print(ret)
#
# imgs = {'Original': img, 'NumPy API': thresh_np, 'cv2.threshold': thresh_cv}
# for i, (key, value) in enumerate(imgs.items()):
#     plt.subplot(1, 3, i + 1)
#     plt.title(key)
#     plt.imshow(value, cmap='gray')
#     plt.xticks([])
#     plt.yticks([])
#
# plt.show()

# 예제 17--------------------------------------------------------------------
# import cv2
# import matplotlib.pylab as plt
#
# img = cv2.imread('images/scaned_paper.jpg', cv2.IMREAD_GRAYSCALE)
# _, t_130 = cv2.threshold(img, 130, 255, cv2.THRESH_BINARY)
# t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
# print('otsu threshold:', t)
#
# imgs = {'Original': img, 't:130':t_130, 'otsu: %d'%t: t_otsu}
# plt.figure(figsize = (12, 5))
#
# for i, (key, value) in enumerate(imgs.items()):
#     plt.subplot(1, 3, i + 1)
#     plt.title(key)
#     plt.imshow(value, cmap = 'gray')
#     plt.xticks([]); plt.yticks([])
#
# plt.show()
# 예제 17--------------------------------------------------------------------
# 적응형 이진화
# import cv2
# import matplotlib.pylab as plt
#
# blk_size = 9
# C = 5
# img = cv2.imread('images/sudoku.jpg', cv2.IMREAD_GRAYSCALE)
# ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
#
# th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
#                             cv2.THRESH_BINARY, blk_size, C)
# th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
#                             cv2.THRESH_BINARY, blk_size, C)
#
# imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1,
#         'Adapted-Mean':th2, 'Adapted-Gaussian': th3}
#
# for i, (key, value) in enumerate(imgs.items()):
#     plt.subplot(2, 2, i + 1)
#     plt.title(key)
#     plt.imshow(value, cmap = 'gray')
#     plt.xticks([]); plt.yticks([])
#
# plt.show()

# 예제 18--------------------------------------------------------------------
# 흐림 효과
# import cv2
#
# src = cv2.imread('./images/cat.jpg', cv2.IMREAD_COLOR)
# dst1 = cv2.blur(src, (3, 3), anchor = (-1, -1), borderType=cv2.BORDER_DEFAULT)
# dst2 = cv2.blur(src, (9, 9), anchor = (-1, -1), borderType=cv2.BORDER_DEFAULT)
# cv2.imshow('src', src)
# cv2.imshow('dst1', dst1)
# cv2.imshow('dst2', dst2)
# cv2.waitKey()
# cv2.destroyAllWindows()

# 예제 19--------------------------------------------------------------------
import cv2

# cv2.GaussianBlur(src, ksize, sigmaX, dst = None, sigmaY = None, borderType = None) -> dst
# src : 입력 이미지
# dst : 출력 이미지
# ksize : 커널 사이즈 (0, 0)을 지정하면 sigma 값에 의해 자동 결정
# sigmaX : x방향 시그마
# sigmaY : y방향 시그마
# borderType : 가장자리 픽셀 확장 방식
src = cv2.imread('../images/cat.jpg', cv2.IMREAD_COLOR)
dst = cv2.GaussianBlur(src, (9, 9), 0)

cv2.imshow('src', src)
cv2.imshow('dst', dst)
cv2.waitKey()
cv2.destroyAllWindows()

# 예제 20--------------------------------------------------------------------
import cv2

src = cv2.imread('../images/cat.jpg', cv2.IMREAD_COLOR)

for ksize in (3, 5, 7, 11):
    dst = cv2.GaussianBlur(src, (ksize, ksize), 0)
    desc = 'Mean: {}x{}'.format(ksize,ksize)
    cv2.putText(dst, desc, (10, 30), cv2.FONT_HERSHEY_SIMPLEX,
                1.0, 255, 1, cv2.LINE_AA)
    cv2.imshow('src', src)
    cv2.imshow('dst', dst)
    cv2.waitKey()

cv2.destroyAllWindows()
