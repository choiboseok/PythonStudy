import cv2
import easyocr

reader = easyocr.Reader(['en'], gpu=False)
results = reader.readtext('eng.jpg')
for result in results:
    print(result)

car_img = cv2.imread('car1.JPG')
car_reader = easyocr.Reader(['ko'])
car_results = car_reader.readtext(car_img)
for bbox, text, prob in car_results:
    print(bbox, text, prob)
