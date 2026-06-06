#accessing local directory
import tkinter as tk
from module_2 import compress_file,decompress_file
from tkinter import filedialog

def open_file():
    filename=filedialog.askopenfilename(initialdir='/',title="select a file to compress") #setting initial directory
    return filename

def compression(i,o):
    b=compress_file(i,o)
    return b

def decompression(i,o):
    decompress_file(i,o)

#wrapper function

def process():
    print("Button is clicked ")
    a=compression(open_file(),'middle_file')
    decompression(a,'final.text')

window=tk.Tk()
window.title("compressor")
window.geometry("600x600")


#button to compress
compress_button=tk.Button(window,text="compressed file",command=lambda: process())
compress_button.grid(row=5,column=1)
window.mainloop()