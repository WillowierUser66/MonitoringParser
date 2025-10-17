def pre(data):
    import tkinter
    from tkinter import Toplevel
    from tkinter import LabelFrame, Button, Entry, Label
    import matplotlib.pyplot as plt
    from matplotlib import figure
    from matplotlib.backends.backend_tkagg import (
        FigureCanvasTkAgg, NavigationToolbar2Tk)
    from matplotlib.backend_bases import key_press_handler
    from PIL import ImageTk, Image

    lay_num = 1

    top = Toplevel()
    top.title = "Layer ROI Preview"
    top.iconbitmap('Images/i.ico')

    fig = plt.figure(figsize=(5, 4), dpi=100)
    fig.add_subplot(111).plot(data[2][lay_num - 1], data[3][lay_num - 1], 'ro', data[0][lay_num - 1],
                              data[1][lay_num - 1])

    canvas = FigureCanvasTkAgg(fig, master=top)
    canvas.draw()
    canvas.get_tk_widget().grid(row=0, column=1)

    status_frame = LabelFrame(top, width=10, relief="flat")
    status_frame.grid(row=1, column=1)
    status_lay = Label(status_frame, text="layer ")
    status_lay.grid(row=0, column=0)
    status_ent = Entry(status_frame)
    status_ent.grid(row=0, column=1)
    status_no = Label(status_frame, text=" of " + str(len(data[0])))
    status_no.grid(row=0, column=2)

    status_ent.insert(0, lay_num)
    number = int(status_ent.get())

    def back(num):
        global f_b
        global b_b

        fig.add_subplot(111).plot(data[2][num - 1], data[3][num - 1], 'ro', data[0][num - 1], data[1][num - 1])
        canvas.draw()

        f_b = Button(top, text=">>", command=lambda: forward(num + 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))
        b_b = Button(top, text="<<", command=lambda: back(num - 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))

        status_ent.delete(0, "end")
        status_ent.insert(0, num)

        if num == 1:
            b_b = Button(top, text="<<", state="disabled", padx=5, bg="#FFFFFF", fg="#0D1D41",
                         font=('Calibri', 12, 'bold'))

        f_b.grid(row=1, column=2)
        b_b.grid(row=1, column=0)

    def forward(num):
        global f_b
        global b_b

        fig.add_subplot(111).plot(data[2][num - 1], data[3][num - 1], 'ro', data[0][num - 1], data[1][num - 1])
        canvas.draw()

        f_b = Button(top, text=">>", command=lambda: forward(num + 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))
        b_b = Button(top, text="<<", command=lambda: back(num - 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))

        status_ent.delete(0, "end")
        status_ent.insert(0, num)

        if num == len(data[0]):
            f_b = Button(top, text=">>", state="disabled", padx=5, bg="#FFFFFF", fg="#0D1D41",
                         font=('Calibri', 12, 'bold'))

        f_b.grid(row=1, column=2)
        b_b.grid(row=1, column=0)

    def go(num):
        global f_b
        global b_b

        fig.add_subplot(111).plot(data[2][num - 1], data[3][num - 1], 'ro', data[0][num - 1], data[1][num - 1])
        canvas.draw()

        f_b = Button(top, text=">>", command=lambda: forward(num + 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))
        b_b = Button(top, text="<<", command=lambda: back(num - 1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                     font=('Calibri', 12, 'bold'))

        status_ent.delete(0, "end")
        status_ent.insert(0, num)

        if num == 1:
            b_b = Button(top, text="<<", state="disabled", padx=5, bg="#FFFFFF", fg="#0D1D41",
                         font=('Calibri', 12, 'bold'))
        elif num == len(data[0]):
            f_b = Button(top, text=">>", state="disabled", padx=5, bg="#FFFFFF", fg="#0D1D41",
                         font=('Calibri', 12, 'bold'))

        f_b.grid(row=1, column=2)
        b_b.grid(row=1, column=0)

    b_b = Button(top, text="<<", command=lambda: back(1), padx=5, bg="#FFFFFF", fg="#0D1D41",
                 font=('Calibri', 12, 'bold'))
    b_b.grid(row=1, column=0)

    f_b = Button(top, text=">>", command=lambda: forward(2), padx=5, bg="#FFFFFF", fg="#0D1D41",
                 font=('Calibri', 12, 'bold'))
    f_b.grid(row=1, column=2)

    go_b = Button(status_frame, text="GO", command=lambda: go(number))
    go_b.grid(row=0, column=3)
