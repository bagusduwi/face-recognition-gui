from tkinter import *
import partial.nav as nav
import partial.test_func as testing

def btn_clicked():
    print("Button Clicked")

def showTesting():
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

    background_img = PhotoImage(file = f"assets/testing/background.png")
    background = canvas.create_image(
        912.0, 308.5,
        image=background_img)

    img0 = PhotoImage(file = f"assets/testing/img0.png")
    b0 = Button(
        image = img0,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : testing.openFile(b0, b1, b2, b3, result, same_data),
        relief = "flat")

    b0.place(
        x = 2, y = 0,
        width = 716,
        height = 400)

    img1 = PhotoImage(file = f"assets/testing/img1.png")
    b1 = Label(
        image = img1,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b1.place(
        x = 49, y = 406,
        width = 200,
        height = 200)

    img2 = PhotoImage(file = f"assets/testing/img2.png")
    b2 = Label(
        image = img2,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b2.place(
        x = 258, y = 405,
        width = 200,
        height = 200)

    img3 = PhotoImage(file = f"assets/testing/img3.png")
    b3 = Label(
        image = img3,
        borderwidth = 0,
        highlightthickness = 0,
        relief = "flat")

    b3.place(
        x = 467, y = 406,
        width = 200,
        height = 200)

    img4 = PhotoImage(file = f"assets/testing/img4.png")
    b4 = Button(
        image = img4,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : nav.back(window),
        relief = "flat")

    b4.place(
        x = 744, y = 236,
        width = 335,
        height = 33)

    img5 = PhotoImage(file = f"assets/testing/img5.png")
    b5 = Button(
        image = img5,
        borderwidth = 0,
        highlightthickness = 0,
        command = lambda : testing.recognize(result, same_data),
        relief = "flat")

    b5.place(
        x = 745, y = 276,
        width = 335,
        height = 33)

    result = Label(
        text='',
        background='#ffffff',
        font=('Chakra Petch', '12'),
        wraplength=400,
        justify='left'
    )
    result.place(
            x = 750, y = 374,
            # width=339,
            # height=231
        )
    same_data = Label(
        background='#ffffff',
    )
    same_data.place(
        x = 850, y = 525,
        width=60,
        height=60
    )

    window.resizable(False, False)
    window.mainloop()
