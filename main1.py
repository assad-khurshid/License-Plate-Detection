import cv2
import pandas as pd
from ultralytics import YOLO
import cvzone
import numpy as np
import pytesseract
from datetime import datetime

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

model = YOLO('best.pt')

def RGB(event, x, y, flags, param):
    if event == cv2.EVENT_MOUSEMOVE:
        point = [x, y]
        print(point)

cv2.namedWindow('RGB')
cv2.setMouseCallback('RGB', RGB)

#---------------for video input from file-------------------------------
cap = cv2.VideoCapture('mycarplate.mp4')


#--------------for video input from camera------------------------------
# cap = cv2.VideoCapture(0)
# width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

my_file = open("classes.txt", "r")
data = my_file.read()
class_list = data.split("\n") 

area = [(40,400), (10, 456), (1015, 451), (980, 400)]

count = 0
list1 = []
processed_numbers = set()

# Open file for writing car plate data
with open("license_plate_data.txt", "a") as file:
    file.write("NumberPlate\t\tDate\t\tTime\n")  # Writing column headers

while True:    
    ret, frame = cap.read()
    count += 1
    if count % 3 != 0:
        continue
    if not ret:
       break
   
    frame = cv2.resize(frame, (1020, 500))
    results = model.predict(frame)
    a = results[0].boxes.data
    px = pd.DataFrame(a).astype("float")
   
    for index, row in px.iterrows():
        x1 = int(row[0])
        y1 = int(row[1])
        x2 = int(row[2])
        y2 = int(row[3])
        
        d = int(row[5])
        c = class_list[d]
        cx = int(x1 + x2) // 2
        cy = int(y1 + y2) // 2
        result = cv2.pointPolygonTest(np.array(area, np.int32), ((cx, cy)), False)
        if result >= 0:
           crop = frame[y1:y2, x1:x2]
           gray = cv2.cvtColor(crop, cv2.COLOR_BGR2GRAY)
           gray = cv2.bilateralFilter(gray, 10, 20, 20)

           text = pytesseract.image_to_string(gray).strip()
           text = text.replace('(', '').replace('"', '').replace('\'', '').replace(')', '').replace(',', '').replace(']','')
           if text not in processed_numbers:
              processed_numbers.add(text) 
              list1.append(text)
              current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
              with open("license_plate_data.txt", "a") as file:
                   file.write(f"{text}\t{current_datetime}\n")
                   cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 1)
                   cv2.imshow('crop', crop)

      
    cv2.polylines(frame, [np.array(area, np.int32)], True, (255, 0, 0), 2)
    cv2.imshow("RGB", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

cap.release()    
cv2.destroyAllWindows()
