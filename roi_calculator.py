# JMJ
import os
import tkinter
import matplotlib.pyplot as plt
from matplotlib import figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog
from tkinter import messagebox
from functions.cst_p import cst_parser
from functions.ornl_p import ornl_parser
from functions.calc import c_roi
from functions.preview import pre
from functions.export import export

# import numpy
# import h5py

root = Tk()
root.title("ROI Calculator")
root.iconbitmap('Images/i.ico')
root.geometry("600x400")
root.configure(bg='#FFFFFF')

unit = IntVar()
unit.set("1")

clicked = StringVar()
clicked.set("ORNL")

# Logo
K_image = ImageTk.PhotoImage(Image.open('Images/KeckLogo.png'))
K_logo = Label(image=K_image)
K_logo.config(bg="#FFFFFF")
K_logo.place(anchor="nw")

# Path to file
path_frame = LabelFrame(root, text="Path to File", width=40, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 11, 'bold'),
                        relief=FLAT)
path_frame.place(x=135, y=108)
path = Entry(path_frame, width=40, borderwidth=2, font=('Calibri', 11))
path.pack()

# Parameters
frame = LabelFrame(root, text="Parameters", width=40, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 11, 'bold'))
frame.place(x=50, y=180)

# Threshold
thr_frame = LabelFrame(frame, text="Length Threshold", width=10, bg="#FFFFFF", fg="#0D1D41",
                       font=('Calibri', 11, 'bold'), relief=FLAT)
thr_frame.grid(row=0, column=0)
threshold = Entry(thr_frame, width=10, borderwidth=2, font=('Calibri', 11))
threshold.pack()

# Velocity
vel_frame = LabelFrame(frame, text="Extrusion Speed", width=10, bg="#FFFFFF", fg="#0D1D41",
                       font=('Calibri', 11, 'bold'), relief=FLAT)
vel_frame.grid(row=1, column=0)
velocity = Entry(vel_frame, width=10, borderwidth=2, font=('Calibri', 11))
velocity.pack()

# Units
unit_frame = LabelFrame(frame, text="Units", width=10, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 11, 'bold'),
                        relief=FLAT)
unit_frame.grid(row=2, column=0)
Radiobutton(unit_frame, text="Imperial (in,ft/s)", variable=unit, value=1, bg="#FFFFFF", fg="#0D1D41",
            font=('Calibri', 11, 'bold'), selectcolor="#FFFFFF", activebackground="#FFFFFF",
            activeforeground="#FFFFFF").pack()
Radiobutton(unit_frame, text="Metric (mm,m/s)", variable=unit, value=2, bg="#FFFFFF", fg="#0D1D41",
            font=('Calibri', 11, 'bold'), selectcolor="#FFFFFF", activebackground="#FFFFFF",
            activeforeground="#FFFFFF").pack()

# Slicer
slcr_frame = LabelFrame(root, text="Slicer", width=40, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 11, 'bold'),
                        relief=FLAT)
slcr_frame.place(x=427, y=104)
drop = OptionMenu(slcr_frame, clicked, "ORNL", "CST")
drop.config(bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 12, 'bold'), highlightbackground="#FFFFFF",
            activebackground="#FFFFFF", activeforeground="#0D1D41")
drop.pack()


def Browse():
    global file
    root.filename = filedialog.askopenfilename(initialdir="C:/", title="Select G-Code",
                                               filetypes=(("txt", "*.txt"), ("mpf", "*.mpf"), ("nc", "*.nc"),
                                                          ("all files", "*.*")))
    path.delete(0, END)
    path.insert(0, root.filename)


def parse():
    global par_click
    global lists
    global vel
    global thresh
    file = path.get()
    isFile = os.path.isfile(file)
    try:
        thresh = float(threshold.get())
        vel = float(velocity.get())
        if thresh == 0 or vel == 0:
            par_click = 0
            messagebox.showerror("Error", "No input value")
        else:
            if isFile == 1:
                par_click = 1
                slc = clicked.get()
                if slc == "CST":
                    lists = cst_parser(file)
                if slc == "ORNL":
                    lists = ornl_parser(file)
                    # print(lists[1])
                messagebox.showinfo("", "Parsing Completed")
            else:
                par_click = 0
                messagebox.showerror("Error", "No file selected")
    except ValueError:
        par_click = 0
        messagebox.showerror("Error", "Not valid input")


par_click = 0


def preview():
    global lay_num
    lay_num = 0

    if calc_click == 0:
        messagebox.showerror("Error", "Missing G_Code")
    else:
        pre(r_data[1])


def calc():
    global r_data
    global calc_click
    if par_click == 0:
        messagebox.showerror("Error", "Missing G_Code")
        calc_click = 0
    else:
        r_data = c_roi(vel, thresh, lists[0], lists[1], lists[2])
        calc_click = 1


calc_click = 0


def start():
    strt = messagebox.askyesno("", "Start Print?")
    if strt == 1:
        export(r_data[0])
        root.destroy()


Browse_B = Button(root, text="Browse", padx=30, command=Browse, bg="#FFFFFF", fg="#0D1D41",
                  font=('Calibri', 12, 'bold'))
Browse_B.place(x=10, y=124)
# root.filename = filedialog.askopenfilename(initialdir = "C:/", title = "Select G-Code", filetypes =(("txt","*.*"),("all files","*.*")))
# all files filetypes = (("all files","*.*"))

Parse_B = Button(root, text="Parse", width=10, command=parse, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 12, 'bold'))
Parse_B.place(x=300, y=200)

Pre_B = Button(root, text="Preview", width=10, command=preview, bg="#FFFFFF", fg="#0D1D41",
               font=('Calibri', 12, 'bold'))
Pre_B.place(x=300, y=300)

Calc_B = Button(root, text="Calculate", width=10, command=calc, bg="#FFFFFF", fg="#0D1D41",
                font=('Calibri', 12, ' bold'))
Calc_B.place(x=300, y=250)

start_b = Button(root, text="Start", width=10, command=start, bg="#FFFFFF", fg="#0D1D41", font=('Calibri', 12, 'bold'))
start_b.place(x=480, y=340)
# threshold.get()
# velocity.get()
# unit.get()

# canvas.create_window(105, 60, window = K_logo)
# canvas.create_window(150, 150, window = Browse_B)

root.mainloop()