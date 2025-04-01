import easyocr
import cv2

img = cv2.imread('car1.JPG')

x, y, w, h = 350, 260, 300, 100
plate_img = img[y:y + h, x:x + w]

reader = easyocr.Reader(['ko'])
results = reader.readtext(plate_img)
for bbox, text, prob in results:
    print(f'번호판 인식 결과:{text}, 신뢰도:{prob:.2}')
    # 원본 이미지에 영역 표시
    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)
cv2.imshow('detection', img)
cv2.waitKey(0)
cv2.destroyAllWindows()