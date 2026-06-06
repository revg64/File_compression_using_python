import tkinter as tk
from module_2 import compress_file,decompress_file
from tkinter import filedialog
def compression(i,o):
    b=compress_file(i,o)
    return b

def decompression(i,o):
    decompress_file(i,o)

#wrapper function

def process():
    print("Button is clicked ")
    a=compression(input_entry.get(),'middle_file')
    decompression(a,output_entry.get())
window=tk.Tk()
window.title("compressor")
window.geometry("600x600")

#lable for input
input_label=tk.Label(window,text="Input file name ")
input_label.grid(row=0,column=0)
#entry 1 input
input_entry = tk.Entry(window)
input_entry.grid(row=0,column=1)

#lable for input
output_label=tk.Label(window,text="Output file name ")
output_label.grid(row=1,column=0)
#entry 1 input
output_entry = tk.Entry(window)
output_entry.grid(row=1,column=1)



#button to compress
decompress_button=tk.Button(window,text="compressed file",command=lambda: process())
decompress_button.grid(row=5,column=1)
window.mainloop()