import os
import urllib.request
from bz2 import decompress

def decompress_bz2(fn):
    with open(fn, "rb") as f:
        data = f.read()

    data = decompress(data)

    with open(fn[:-4], "wb") as f:
        f.write(data)

print('Downloading dlib_face_recognition_resnet_model_v1.dat ...')
urllib.request.urlretrieve("https://raw.githubusercontent.com/ageitgey/face_recognition_models/master/face_recognition_models/models/dlib_face_recognition_resnet_model_v1.dat", "dlib_face_recognition_resnet_model_v1.dat")


print('Downloading shape_predictor_68_face_landmarks.dat.bz2 ...')
urllib.request.urlretrieve("https://raw.githubusercontent.com/davisking/dlib-models/master/shape_predictor_68_face_landmarks.dat.bz2", "shape_predictor_68_face_landmarks.dat.bz2")

print('Extracting shape_predictor_68_face_landmarks.dat ...')
decompress_bz2("shape_predictor_68_face_landmarks.dat.bz2")

os.remove("shape_predictor_68_face_landmarks.dat.bz2")
