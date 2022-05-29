from tkinter import filedialog, messagebox, Label
from tensorflow.keras.models import load_model
from scipy.spatial.distance import cosine
from PIL import Image, ImageTk
import numpy as np
import pickle
import cv2

detected_face = ''
facebox = []
def openFile(btn, lb1, lb2, lb3, result, same_data):
    global detected_face, facebox
    filename = filedialog.askopenfilename(initialdir='D:/programming/python/skripsi/face-recognition')
    if filename != '':
        # destroy result
        result.configure(text='')
        result.update
        same_data.configure(image = '')
        same_data.image = ''

        rgb = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
        from menu import detector
        detect = detector()
        faces = detect.detect_faces(rgb)
        if len(faces) < 1:
            return messagebox.showwarning(title='Warning', message='Face not detected!')
        
        face = faces[0]
        facebox = face
        x,y,w,h = face['box']
        w = x + w
        h = y + h

        rgb = cv2.rectangle(rgb, (x,y), (w,h), (0,43,11), 4)

        crop = Image.fromarray(rgb)
        crop = np.asarray(crop)
        crop = crop[y:h, x:w]

        resize = Image.fromarray(crop)
        resize = resize.resize((160,160))

        ori_image = ImageTk.PhotoImage(Image.fromarray(rgb).resize((716,400)))
        btn.configure(image = ori_image)
        btn.image = ori_image

        crop_image = ImageTk.PhotoImage(Image.fromarray(crop).resize((200,200)))
        lb1.configure(image = crop_image)
        lb1.image = crop_image

        resize_image = ImageTk.PhotoImage(resize)
        lb2.configure(image = resize_image)
        lb2.image = resize_image

        face_point = cv2.circle(rgb, face['keypoints']['left_eye'], radius=10, color=(0, 255, 0), thickness=-1)
        face_point = cv2.circle(rgb, face['keypoints']['right_eye'], radius=10, color=(0, 255, 0), thickness=-1)
        face_point = cv2.circle(rgb, face['keypoints']['nose'], radius=10, color=(0, 255, 0), thickness=-1)
        face_point = cv2.circle(rgb, face['keypoints']['mouth_right'], radius=10, color=(0, 255, 0), thickness=-1)
        face_point = cv2.circle(rgb, face['keypoints']['mouth_left'], radius=10, color=(0, 255, 0), thickness=-1)

        face_point = np.asarray(Image.fromarray(face_point))
        face_point = face_point[y:h, x:w]

        point_image = ImageTk.PhotoImage(Image.fromarray(face_point).resize((160,160)))
        lb3.configure(image = point_image)
        lb3.image = point_image

        detected_face = resize

with open('encodings/datatrain.pkl', 'rb') as f:
    datatrain = pickle.load(f)

def recognize(result, same_data):
    global detected_face, datatrain, facebox
    min_dist = 0.4

    if detected_face == '':
        return messagebox.showwarning(title='Warning', message='Image not selected!')

    model = load_model('model/facenet.h5')
    
    # normalization
    image = np.asarray(detected_face)

    image = image.astype('float32')
    mean, std = image.mean(), image.std()
    image = (image - mean) / std
    
    face = np.expand_dims(image, axis=0)
    
    signature = model.predict(face)

    distance = float('inf')
    name = 'unknown'
    path = ''
    for key, value in datatrain.items():
        dist = cosine(signature, value[1])

        if dist < min_dist and dist < distance:
            distance = dist
            name = key.split('_')[0]
            path = value[0]

    confidence = facebox['confidence']
    left_eye = facebox['keypoints']['left_eye']
    right_eye = facebox['keypoints']['right_eye']
    nose = facebox['keypoints']['nose']
    mouth_left = facebox['keypoints']['mouth_left']
    mouth_right = facebox['keypoints']['mouth_right']
    
    # result 
    result.configure(text=f'label : {name}\nDistance : {distance}\nConfidence : {confidence}\nRight Eye : {right_eye}\nLeft Eye : {left_eye}\nNose : {nose}\nMouth Right : {mouth_right}\nMouth Left : {mouth_left}\nSame Face : ')

    sameimage = ImageTk.PhotoImage(Image.open(path).resize((50,50)))
    same_data.configure(image = sameimage)
    same_data.image = sameimage