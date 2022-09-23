import cv2
import cv2 as cv
import numpy as np

cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, im = cap.read()
    #cv2.imshow('im',im)

    img = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    #cv2.imshow('img',img)

    imgb = cv.GaussianBlur(img,(3,3),0)
    #cv2.imshow('imgb',imgb)

    edges = cv.Canny(imgb,10,20)
    #cv2.imshow('edges',edges)

    kernel = np.ones((5,5),np.uint8)
    kernel2 = np.ones((7,7),np.uint8)
    closed = cv.morphologyEx(edges, cv.MORPH_CLOSE, kernel)
    #cv2.imshow('closed',closed)

    contours, hierarchy = cv2.findContours(closed,
                        cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)

    selected_cnt = []
    for cnt in contours:
        x,y,w,h = cv.boundingRect(cnt)
        if w > int(0.3*im.shape[1]) and w < int(0.7*im.shape[1]) and w in range(int(0.2*h),int(2.2*h)):
            area = cv2.contourArea(cnt)
            hull = cv2.convexHull(cnt)
            hull_area = cv2.contourArea(hull)
            solidity = float(area)/hull_area
            if solidity > 0.7:
                selected_cnt.append(cnt)
                #print(solidity,area,hull_area,x,y,w,h,im.shape)    
        cv2.drawContours(edges,[cnt],0,100,2)
    #cv2.imshow('edges',edges)

    if len(selected_cnt):
        if len(selected_cnt) > 1:
            selected_cnt = sorted(selected_cnt,key=lambda x: cv2.contourArea(x))[0]
        else:
            selected_cnt = selected_cnt[0]
        x,y,w,h = cv.boundingRect(selected_cnt)
        mask = np.zeros(img.shape,np.uint8)
        cv2.drawContours(mask,[selected_cnt],-1,255,-1)
        #cv2.imshow('msk_final',mask)
        mask = cv.erode(mask, kernel)
        mean = cv2.mean(im,mask=mask)
        #print(mean)
        cv2.rectangle(im,(x,y),(x+w,y+h),(50,255,50),2)
        rgb_txt = 'B:{},G:{},R:{}'.format(round(mean[0]),round(mean[1]),round(mean[2]))
        cv2.putText(im,rgb_txt,(x,y-20),1,1.2,(255,50,50),2)
    cv2.imshow('output',im)
    key=cv2.waitKey(30)
    if key == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()

