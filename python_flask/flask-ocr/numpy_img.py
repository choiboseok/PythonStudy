# pip install opencv-python
# pip install easyOCR
import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('car1.JPG')
print('원본 이미지', img.shape)
print('픽셀[0,0]', img[0,0]) #[B, G, R]
mean_pixel = np.mean(img, axis=(0,1))
print('RGB 평균', mean_pixel)

# 원보 이미지(컬러)
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# gray 이미지로
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# cv2.imwrite('car_gray.jpg', gray)

# 크기 조정
resized = cv2.resize(img, (128, 128))

# 정규화(0~1 t스케일로)
normalized =  (resized/255.0).astype(np.float32)

# gaussian blur
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# edge detection
edges = cv2.Canny(gray, 100, 200)

# 회전
(h, w) = img.shape[:2]
center = (w//2, h//2)
M = cv2.getRotationMatrix2D(center, 15, 1.0)
rotated = cv2.warpAffine(img, M, (w, h))

# 좌우 반전
flipped = cv2.flip(img, 1)
images = [img_rgb, gray, resized, normalized, blurred, edges, rotated, flipped]
plt.figure(figsize=(15, 10))
for i in range(len(images)):
    plt.subplot(2, 4, i+1)
    if len(images[i].shape) == 2: # 흑백은 다르게 출력
        plt.imshow(images[i], cmap='gray')
    else:
        plt.imshow(cv2.cvtColor(images[i], cv2.COLOR_BGR2RGB))
    plt.axis("off")
plt.tight_layout()
plt.show()