from http.client import REQUESTED_RANGE_NOT_SATISFIABLE
from tensorflow.keras.models import load_model
from tkinter import Label
from PIL import Image, ImageTk
import numpy as np
from scipy.spatial.distance import cosine
import pickle
import cv2

cap= cv2.VideoCapture(0)
loops = 0
with open('encodings/datatrain.pkl', 'rb') as f:
    datatrain = pickle.load(f)

model = load_model('model/facenet.h5')
min_dist = 0.4
def show_frames(b0, b1, b2, b3, result, same_data):    
    global loops, model, datatrain, min_dist
    
    rgb= cv2.cvtColor(cap.read()[1],cv2.COLOR_BGR2RGB)
    rgb= cv2.flip(rgb, 1)

    from menu import detector
    detect = detector()

    faces = detect.detect_faces(rgb)

    if len(faces) > 0:
        face = faces[0]
        x,y,w,h = face['box']
        w = x + w
        h = y + h

        crop = Image.fromarray(rgb)
        crop = np.asarray(crop)
        crop = crop[y:h, x:w]

        resize = Image.fromarray(crop)
        resize = resize.resize((160,160))
        
        rgb = cv2.rectangle(rgb, (x,y), (w,h), (0,43,11), 4)
        face_point = rgb

        face_point = cv2.circle(face_point, face['keypoints']['left_eye'], radius=10, color=(0, 255, 0), thickness=-1)
        # face_point = cv2.circle(rgb, face['keypoints']['right_eye'], radius=10, color=(0, 255, 0), thickness=-1)
        # face_point = cv2.circle(rgb, face['keypoints']['nose'], radius=10, color=(0, 255, 0), thickness=-1)
        # face_point = cv2.circle(rgb, face['keypoints']['mouth_right'], radius=10, color=(0, 255, 0), thickness=-1)
        # face_point = cv2.circle(rgb, face['keypoints']['mouth_left'], radius=10, color=(0, 255, 0), thickness=-1)

        # face_point = np.asarray(Image.fromarray(face_point))
        # face_point = face_point[y:h, x:w]

        img_crop = ImageTk.PhotoImage(Image.fromarray(crop).resize((200,200)))
        b1.image = img_crop
        b1.configure(image=img_crop)
        b1.update()

        img_resize = ImageTk.PhotoImage(resize)
        b2.image = img_resize
        b2.configure(image=img_resize)
        b2.update()  

        img_point = ImageTk.PhotoImage(Image.fromarray(face_point))
        b3.image = img_point
        b3.configure(image=img_point)
        b3.update()

    else:
        img3 = ImageTk.PhotoImage(file = f"assets/realtime/img3.png")
        b1.image = img3
        b1.configure(image=img3)
        b1.update()

        b2.image = img3
        b2.configure(image=img3)
        b2.update()

        b3.image = img3
        b3.configure(image=img3)
        b3.update()
        
    imgtk = ImageTk.PhotoImage(Image.fromarray(rgb))
    b0.image = imgtk
    b0.configure(image=imgtk)
    b0.update()

        

        # loops = loops + 1

        # if loops == 5:
            
        #     image = np.asarray(resize)

        #     image = image.astype('float32')
        #     mean, std = image.mean(), image.std()
        #     image = (image - mean) / std
            
        #     image = np.expand_dims(image, axis=0)
        
        #     signature = model.predict(image)

        #     distance = float('inf')
        #     name = 'unknown'
        #     path = ''
        #     for key, value in datatrain.items():
        #         dist = cosine(signature, value[1])

        #         if dist < min_dist and dist < distance:
        #             distance = dist
        #             name = key.split('_')[0]
        #             path = value[0]

        #     confidence = face['confidence']
        #     left_eye = face['keypoints']['left_eye']
        #     right_eye = face['keypoints']['right_eye']
        #     nose = face['keypoints']['nose']
        #     mouth_left = face['keypoints']['mouth_left']
        #     mouth_right = face['keypoints']['mouth_right']
            
        #     result.configure(text=f'label : {name}\nDistance : {distance}\nConfidence : {confidence}\nRight Eye : {right_eye}\nLeft Eye : {left_eye}\nNose : {nose}\nMouth Right : {mouth_right}\nMouth Left : {mouth_left}\nSame Face : ')
        #     result.update()

        #     sameimage = ImageTk.PhotoImage(Image.open(path).resize((50,50)))
        #     same_data.image = sameimage
        #     same_data.configure(image = sameimage)

        #     loops = 0

    b0.after(100, lambda : show_frames(b0, b1, b2, b3, result, same_data))
