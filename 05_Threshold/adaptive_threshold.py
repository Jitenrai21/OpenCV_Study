import os, cv2

img = cv2.imread(os.path.join('.','data','letter.png'))

img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

adaptive_thresh = cv2.adaptiveThreshold(img_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 21, 30) #30 is the size of the regions that has different thresholds and 21 should be an odd number
ret, simple_thresh = cv2.threshold(img_gray, 80, 255, cv2.THRESH_BINARY)

cv2.imshow('img', img)
cv2.imshow('thresh', adaptive_thresh)
cv2.imshow('simp', simple_thresh)
cv2.waitKey(0)