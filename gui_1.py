import tkinter as tk
from module_1 import compress_file,decompress_file

def compression(i,o):
    compress_file(i,o)

def decompression(i,o):
    decompress_file(i,o)

window=tk.Tk()
window.title("compressor")
window.geometry("600x600")

#lable for input
input_label_compress=tk.Label(window,text="Input file name ")
input_label_compress.grid(row=0,column=0)
#entry 1 input
input_entry_compress = tk.Entry(window)
input_entry_compress.grid(row=0,column=1)

#lable for output
output_label_compress=tk.Label(window,text="Output file name ")
output_label_compress.grid(row=1,column=0)
#entry 2 output
output_entry_compress = tk.Entry(window)
output_entry_compress.grid(row=1,column=1)

#button to compress
compress_button=tk.Button(window,text="Compress",command=lambda: compression(input_entry_compress.get(),output_entry_compress.get()))
compress_button.grid(row=2,column=1)


#decompress

#lable for input
input_label_decompress=tk.Label(window,text="Input file name ")
input_label_decompress.grid(row=3,column=0)
#entry 1 input
input_entry_decompress = tk.Entry(window)
input_entry_decompress.grid(row=3,column=1)

#lable for output
output_label_decompress=tk.Label(window,text="Output file name ")
output_label_decompress.grid(row=4,column=0)
#entry 2 output
output_entry_decompress = tk.Entry(window)
output_entry_decompress.grid(row=4,column=1)

#button to compress
decompress_button=tk.Button(window,text="decompress",command=lambda: decompression(input_entry_decompress.get(),output_entry_decompress.get()))
decompress_button.grid(row=5,column=1)
window.mainloop()