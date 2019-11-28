import face_model
import argparse
import cv2
import sys
import numpy as np
from time import time
import os

parser = argparse.ArgumentParser(description='face model test')
# general
parser.add_argument('--image-size', default='112,112', help='')
parser.add_argument('--model', default='models/face-model-r100-ii/model,0', help='path to load model.')
parser.add_argument('--ga-model', default='models/gender-age-model/model,0', help='path to load model.')
parser.add_argument('--gpu', default=-1, type=int, help='gpu id')
parser.add_argument('--det', default=0, type=int, help='mtcnn option, 1 means using R+O, 0 means detect from begining')
parser.add_argument('--flip', default=0, type=int, help='whether do lr flip aug')
parser.add_argument('--threshold', default=1.24, type=float, help='ver dist threshold')
parser.add_argument('--img1_file', type=str, help='Image 1')    
parser.add_argument('--img2_file', type=str, help='Image 2')
args = parser.parse_args()

model_path,_ =  os.path.split(args.model)
if not os.path.exists(model_path):
    print('Please run "download_model.py" first')
    exit()

if args.img1_file == None or args.img2_file == None:
    print('Run : python compare.py --img1_file <img1_file> --img2_file <img2_file>')
    exit()

model = face_model.FaceModel(args)
img = cv2.imread(args.img1_file)
img = model.get_input(img)
f1 = model.get_feature(img)
#print(f1[0:10])
gender, age = model.get_ga(img)
#print(gender)
#print(age)

img = cv2.imread(args.img2_file)
img = model.get_input(img)
#print(img.shape)

t = time()
counter = 1

for _ in range(counter):
  f2 = model.get_feature(img)

#print((time()-t)/counter)

dist = np.sum(np.square(f1-f2))
print('Euclide diatance:', dist)
sim = np.dot(f1, f2.T)
print('Cosine simarlity:', sim)
