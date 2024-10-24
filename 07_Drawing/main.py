import os, cv2
img = cv2.imread(os.path.join('.','data','whiteboard.png'))
# print(img.shape) #(650, 982, 3)
#drawing a line
cv2.line(img, (100,150), (300, 450), (0, 255, 0), 3) #3 is for thickness
#rectangle
cv2.rectangle(img, (200,350), (450,600), (0,0,255), -1) #negative value for thickness gives filled output.
#circle
cv2.circle(img, (800, 200), 100, (255,0,0), 10)
#text
cv2.putText(img, 'Annyeoung!', (550, 450),cv2.FONT_HERSHEY_SIMPLEX,2,(0,0,0), 5)
cv2.imshow('img', img)
cv2.waitKey(0)