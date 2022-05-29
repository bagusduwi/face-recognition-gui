from tkinter import *
from mtcnn.mtcnn import MTCNN

def detector():
    detect = MTCNN()
    return detect

def btn_clicked():
    print("Button Clicked")

def training():
    global window
    window.destroy()
    from training import showTrain
    showTrain()

def testing():
    global window
    window.destroy()
    from testing import showTesting
    showTesting()

def realtime():
    global window
    window.destroy()
    from realtime import showRealtime
    showRealtime()

def showMenu():
    global window
    
    window = Tk()
    
    window.geometry("1100x617")
    window.configure(bg = "#ffffff")
    
    canvas = Canvas(
        window,
        bg = "#ffffff",
        height = 617,
        width = 1100,
        bd = 0,
        highlightthickness = 0,
        relief = "ridge")
    canvas.place(x = 0, y = 0)

    background_img = PhotoImage(file = f"assets/home/background.png")
    background = canvas.create_image(
        545.5, 308.5,
        image=background_img)

    img0 = PhotoImage(file = f"assets/home/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = training,
        relief = "flat")

    b0.place(
        x = 596, y = 273,
        width = 259,
        height = 57)

    img1 = PhotoImage(file = f"assets/home/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = testing,
        relief = "flat")

    b1.place(
        x = 596, y = 356,
        width = 259,
        height = 57)

    img2 = PhotoImage(file = f"assets/home/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = realtime,
        relief = "flat")

    b2.place(
        x = 596, y = 439,
        width = 259,
        height = 57)

    window.resizable(False, False)
    window.mainloop()

