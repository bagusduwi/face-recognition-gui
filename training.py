from textwrap import wrap
from tkinter import *
import partial.nav as nav
import partial.train_func as train_func

def btn_clicked():
    print("Button Clicked")

def showTrain():
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

    background_img = PhotoImage(file = f"assets/training/background.png")
    background = canvas.create_image(
        550.0, 308.5,
        image=background_img)

    entry0_img = PhotoImage(file = f"assets/training/img_textBox0.png")
    entry0_bg = canvas.create_image(
        374.5, 542.5,
        image = entry0_img)

    entry0 = Entry(
        bd = 0,
        bg = "#ffffff",
        highlightthickness = 0)

    entry0.place(
        x = 199.0, y = 526,
        width = 351.0,
        height = 31)

    img0 = PhotoImage(file = f"assets/training/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(0),
        relief = "flat")

    b0.place(
        x = 0, y = 0,
        width = 250,
        height = 250)

    img1 = PhotoImage(file = f"assets/training/img1.png")
    b1 = Button(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(1),
        relief = "flat")

    b1.place(
        x = 250, y = 0,
        width = 250,
        height = 250)

    img2 = PhotoImage(file = f"assets/training/img2.png")
    b2 = Button(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(2),
        relief = "flat")

    b2.place(
        x = 500, y = 0,
        width = 250,
        height = 250)

    img3 = PhotoImage(file = f"assets/training/img3.png")
    b3 = Button(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(3),
        relief = "flat")

    b3.place(
        x = 0, y = 250,
        width = 250,
        height = 250)

    img4 = PhotoImage(file = f"assets/training/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(4),
        relief = "flat")

    b4.place(
        x = 250, y = 250,
        width = 250,
        height = 250)

    img5 = PhotoImage(file = f"assets/training/img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.uploadImage(5),
        relief = "flat")

    b5.place(
        x = 500, y = 250,
        width = 250,
        height = 250)

    img6 = PhotoImage(file = f"assets/training/img6.png")
    b6 = Button(
        image = img6,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda: train_func.createDir(entry0.get()),
        relief = "flat")

    b6.place(
        x = 189, y = 567,
        width = 371,
        height = 33)

    img7 = PhotoImage(file = f"assets/training/img7.png")
    b7 = Button(
        image = img7,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : nav.back(window),
        relief = "flat")

    b7.place(
        x = 757, y = 225,
        width = 335,
        height = 33)

    result = Label(
    background='#ffffff',
    font=('Chakra Petch', '12'),
    wraplength=300,
    justify='left'
    )
    result.place(
            x = 781, y = 374,
            # width=339,
            # height=231
        )

    img8 = PhotoImage(file = f"assets/training/img8.png")
    b8 = Button(
        image = img8,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : train_func.train_all(result),
        relief = "flat")

    b8.place(
        x = 758, y = 265,
        width = 335,
        height = 33)

   

    window.resizable(False, False)
    window.mainloop()