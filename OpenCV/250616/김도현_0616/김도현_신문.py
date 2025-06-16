import cv2
import matplotlib.pylab as plt

file_path = 'newspaper.jpg'

# 1. 이진화 : THRESH_BINARY, THRESH_OTSU 사용 시 최적의 thresh 값을 찾아라.
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
_, t_150 = cv2.threshold(img, 150, 255, cv2.THRESH_BINARY)
t, t_otsu = cv2.threshold(img, -1, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)
print('otsu threshold:', t)

imgs = {'Original': img, 't:130':t_150, 'otsu: %d'%t: t_otsu}
plt.figure(figsize = (12, 5))

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(1, 3, i + 1)
    plt.title(key)
    plt.imshow(value, cmap = 'gray')
    plt.xticks([]); plt.yticks([])

plt.show()

# 2. 적응적 이진화 : adaptiveMethod에서 cv2.ADAPTIVE_THRESH_MEAN_C과 cv2.ADAPTIVE_THRESH_GAUSSIAN_C를 적용한 결과 이미지를 출력
import cv2
import matplotlib.pylab as plt

blk_size = 9
C = 5
img = cv2.imread(file_path, cv2.IMREAD_GRAYSCALE)
ret, th1 = cv2.threshold(img, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

th2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C,
                            cv2.THRESH_BINARY, blk_size, C)
th3 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                            cv2.THRESH_BINARY, blk_size, C)

imgs = {'Original': img, 'Global-Otsu:%d'%ret:th1,
        'Adapted-Mean':th2, 'Adapted-Gaussian': th3}

for i, (key, value) in enumerate(imgs.items()):
    plt.subplot(2, 2, i + 1)
    plt.title(key)
    plt.imshow(value, cmap = 'gray')
    plt.xticks([]); plt.yticks([])

plt.show()