import pytesseract
import cv2

pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

img = cv2.imread('temp.jpg')
"""
cv2.rectangle(img, (218, 531), (807, 577), (0, 255, 0))
cv2.rectangle(img, (1563, 578), (1378, 526), (0, 255, 0))
cv2.rectangle(img, (1566, 626), (1381, 574), (0, 255, 0))
cv2.imshow('image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
"""
#[y1:y2,x1:x2]

name = img[531:577, 218:807]
#cv2.imshow('image',name)
#cv2.waitKey(0)
print("Starting OCR")
Name = pytesseract.image_to_string(name)
print("Name : "+ Name)


invoice = img[526:578,1378:1563]
#cv2.imshow('image',invoice)
#cv2.waitKey(0)
Invoice = pytesseract.image_to_string(invoice)
print("Invoice: "+ Invoice)

date = img[575:626,1381:1566]
#cv2.imshow('image',date)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
Date = pytesseract.image_to_string(date)
print("Date: "+ Date)

print("Ended")





