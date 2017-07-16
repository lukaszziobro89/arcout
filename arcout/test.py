from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter.filedialog import askopenfilename
import os

def test():
    messagebox.showinfo(title="Greetings", message="Hello World!")

def openfile():
    try:
        filename = askopenfilename(initialdir="C:/Users/Batman/Documents/Programming/tkinter/",
                   filetypes=(("Text File", "*.txt"), ("All Files", "*.*")),
                   title="Choose a file."
                   )
        arc_file = open(filename)
        directory = str(os.getcwd())
        print(directory)
        arc_file.read()
    except FileNotFoundError:
        pass

root = Tk()
menubar = Menu(root)
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Open", command=openfile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
menubar.add_cascade(label="File", menu=filemenu)

root.config(menu=menubar)
root.mainloop()

