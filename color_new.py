# Python code for Multiple Color Detection

from scipy.spatial import KDTree
import numpy as np
import cv2
from webcolors import rgb_to_name
from webcolors import (
    css3_hex_to_names,
    hex_to_rgb,
)
# Capturing video through webcam
webcam = cv2.VideoCapture(0)
def convert_rgb_to_name(rgb_tuple):
    
    # a dictionary of all the hex and their respective names in css3
    css3_db = css3_hex_to_names
    names = []
    rgb_values = []
    for color_hex, color_name in css3_db.items():
        names.append(color_name)
        rgb_values.append(hex_to_rgb(color_hex))
    
    kdt_db = KDTree(rgb_values)
    distance, index = kdt_db.query(rgb_tuple)
    return  names[index]
# Start a while loop
while(1):
    
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()

    # Convert the imageFrame in
    # BGR(RGB color space) to
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
    ## mask of red color
    maskred = cv2.inRange(hsvFrame, (0, 0, 50), (50, 50,255))
    maskred = int(np.mean(maskred))
    print('mask red',maskred)
    maskblue = cv2.inRange(hsvFrame, (50, 0, 0), (250, 50,50))
    maskblue = int(np.mean(maskblue))
    print('mask blue',maskblue)
    maskgreen = cv2.inRange(hsvFrame, (0, 50, 0), (50, 250,50))
    maskgreen = int(np.mean(maskgreen))
    print('mask blue',maskgreen)
    # Set range for red color and
    # define mask
    red_lower = np.array([136, 87, 111], np.uint8)
    red_upper = np.array([180, 255, 255], np.uint8)
    red_mask = cv2.inRange(hsvFrame, red_lower, red_upper)

    # Set range for green color and
    # define mask
    green_lower = np.array([25, 52, 72], np.uint8)
    green_upper = np.array([102, 255, 255], np.uint8)
    green_mask = cv2.inRange(hsvFrame, green_lower, green_upper)

    # Set range for blue color and
    # define mask
    blue_lower = np.array([94, 80, 2], np.uint8)
    blue_upper = np.array([120, 255, 255], np.uint8)
    blue_mask = cv2.inRange(hsvFrame, blue_lower, blue_upper)
    
    
    
    
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernal = np.ones((5, 5), "uint8")
    
    # For red color
    red_mask = cv2.dilate(red_mask, kernal)
    res_red = cv2.bitwise_and(imageFrame, imageFrame,
                            mask = red_mask)
    
    # For green color
    green_mask = cv2.dilate(green_mask, kernal)
    res_green = cv2.bitwise_and(imageFrame, imageFrame,
                                mask = green_mask)
    
    # For blue color
    blue_mask = cv2.dilate(blue_mask, kernal)
    res_blue = cv2.bitwise_and(imageFrame, imageFrame,
                            mask = blue_mask)

    # Creating contour to track red color
    contours, hierarchy = cv2.findContours(red_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
   # setting values for base colors
    b = hsvFrame[:, :, :1]
    g = hsvFrame[:, :, 1:2]
    r = hsvFrame[:, :, 2:]

    # computing the mean
    b_mean = int(np.mean(b))
    g_mean = int(np.mean(g))
    r_mean = int(np.mean(r))
    print('red value :', r_mean)
    print('green value :', g_mean)
    print('blue value :', b_mean)
    named_color = str(convert_rgb_to_name((r_mean,g_mean,b_mean)))
    print(named_color)
    cv2.putText(imageFrame, named_color, (110, 110),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (r_mean,g_mean,b_mean))
    #time.sleep(1)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                    (x + w, y + h),
                                    (r_mean,g_mean,b_mean), 2)
            
            cv2.putText(imageFrame, named_color, (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX, 1.0,
                        (r_mean,g_mean,b_mean))    

    # Creating contour to track green color
    contours, hierarchy = cv2.findContours(green_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    '''    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 9000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                    (x + w, y + h),
                                    (0, 255, 0), 2)
            
            cv2.putText(imageFrame, "Green Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (0, 255, 0))

    # Creating contour to track blue color
    contours, hierarchy = cv2.findContours(blue_mask,
                                        cv2.RETR_TREE,
                                        cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 9000):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                    (x + w, y + h),
                                    (255, 0, 0), 2)
            
            cv2.putText(imageFrame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))
    '''            
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        cap.release()
        cv2.destroyAllWindows()
        break
