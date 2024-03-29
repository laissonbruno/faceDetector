# -*- coding: utf-8 -*-
"""deteccaoFace.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1dg7VYOTVFJGeYjuEVwLI0A8sR0J8L5Va
"""

import numpy as np
import cv2 as cv

face_classifier = cv.CascadeClassifier('/content/haarcascade_frontalface_default.xml')

image = cv.imread('/content/imagem1.jpg')
image_gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

faces = face_classifier.detectMultiScale(image_gray, 1.3, 5)

for (x,y,w,h) in faces:
  cv.rectangle(image, (x,y), (x+w,y+h), (255,0,0),2)

cv.imshow('imagem', image)
cv.waitKey(0)
cv.destroyAllWindows()