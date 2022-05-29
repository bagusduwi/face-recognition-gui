from tkinter import Label, messagebox, filedialog, PhotoImage
from tensorflow.keras.models import load_model
from PIL import Image, ImageTk
import numpy as np
from random import randint
import pickle
import os
import cv2

path = 'datasets'

def createDir(name):
    global arr_image

    if name == '' or len(name) < 5:
        messagebox.showwarning(title='Warning', message='Label must be entered at least 5 characters!')

    else:
        print(len(arr_image))
        if len(arr_image) != 6:
            return messagebox.showwarning(title='Warning', message='Please add all images!')
        
        os.mkdir(f'{path}/{name}')
        for im in arr_image:
            if not isinstance(im, int):
                cv2.imwrite(f'{path}/{name}/{name}{randint(0, 100)}.jpg', cv2.cvtColor(np.array(im), cv2.COLOR_BGR2RGB))

        messagebox.showinfo(title='Success', message='Image has been uploaded!')

arr_image = [0,1,2,3,4,5]

def uploadImage(num):
    global arr_image

    positionImage = [
        [
            55, 55
        ],
        [
            305, 55
        ],
        [
            555, 55
        ],
        [
            55, 305
        ],
        [
            305, 305
        ],
        [
            555, 305
        ],
    ]

    filename = filedialog.askopenfilename(initialdir='D:/programming/python/skripsi/face-recognition')
    
    if filename != '':
        rgb = cv2.cvtColor(cv2.imread(filename), cv2.COLOR_BGR2RGB)
        from menu import detector
        detect = detector()
        faces = detect.detect_faces(rgb)
        if len(faces) < 1:
            return messagebox.showwarning(title='Warning', message='Face not detected!')
        
        face = faces[0]
        x,y,w,h = face['box']
        w = x + w
        h = y + h

        crop = Image.fromarray(rgb)
        crop = np.asarray(crop)
        crop = crop[y:h, x:w]

        resize = Image.fromarray(crop)
        resize = resize.resize((160,160))

        image = ImageTk.PhotoImage(resize)
        lb = Label(image = image)
        lb.image = image
        lb.place(
            x=positionImage[num][0],y=positionImage[num][1],
            height=139,
            width=139
        )

        arr_image[num] = resize

encodings = {}
def train_all(result):
    global encodings
    model = load_model('model/facenet.h5')

    path = 'datasets'

    
    arrimgname = []
    for filename in os.listdir(path):
        for index, imagename in enumerate(os.listdir(os.path.join(path, filename))):
            if len(arrimgname)  > 10:
                arrimgname = []
            arrimgname.append(imagename + ' trained!')
            image = cv2.imread(os.path.join(path, filename, imagename))
            rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            image = Image.fromarray(rgb)
            
            image = image.resize((160,160))
            image = np.asarray(image)

            # normalization
            image = image.astype('float32')
            mean, std = image.mean(), image.std()
            image = (image - mean) / std

            # expand dimension
            image = np.expand_dims(image, axis=0)

            signature = model.predict(image)

            encodings[f'{filename}_{index}'] = [os.path.join(path, filename, imagename), signature]
            
            result.configure(text='\n'.join(x for x in arrimgname) + '\m All images have been successfully trained!')
            result.update()

    result.configure(text='\n'.join(x for x in arrimgname))
    result.update()
    with open('encodings/datatrain.pkl', 'wb') as f:
        pickle.dump(encodings, f)

    messagebox.showinfo(title='Success', message='Training data has been done!')
    
