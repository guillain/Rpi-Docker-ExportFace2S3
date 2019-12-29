'''
Haar Cascade Face detection with OpenCV  
    Based on tutorial by pythonprogramming.net
    Visit original post: https://pythonprogramming.net/haar-cascade-face-eye-detection-python-opencv-tutorial/  
Adapted by Marcelo Rovai - MJRoBot.org @ 7Feb2018 
'''

my_region='eu-central-1'
my_bucket='facialreco'

import os
import glob
import numpy as np
import cv2
import boto3

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades
faceCascade = cv2.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
cap.set(3,640) # set Width
cap.set(4,480) # set Height

s3r = boto3.resource('s3', region_name=my_region)
s3c = boto3.client('s3')
get_last_modified = lambda obj: int(obj['LastModified'].strftime('%s'))

try:
    objs = s3c.list_objects_v2(Bucket=my_bucket)['Contents']
    last_added = [obj['Key'] for obj in sorted(objs, key=get_last_modified)][0]
    i_image = int(latest_added.split('.')[0]) + 1 
except:
    i_image = 1

while True:
    ret, img = cap.read()
    img = cv2.flip(img, -1)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        
        scaleFactor=1.2,
        minNeighbors=5
        ,     
        minSize=(20, 20)
    )

    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]

        filename = '{}.jpg'.format(i_image)
        cv2.imwrite(filename, roi_color)
        s3r.Bucket(my_bucket).upload_file(Filename=filename, Key=filename)
        os.remove(filename)

        i_image = i_image + 1

    cv2.imshow('video',img)

    k = cv2.waitKey(30) & 0xff
    if k == 27: # press 'ESC' to quit
        break

cap.release()
cv2.destroyAllWindows()
