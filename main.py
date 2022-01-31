import os.path
import tkinter
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from os import path
import converter


def select_input_file():
    input_file = filedialog.askopenfilename(filetypes=(('Comma separated', '*.csv'), ("all files", "*.*")))
    io_dir.set(os.path.dirname(input_file))
    input_filename.set(os.path.basename(input_file))
    input_file_label.configure(text=input_filename.get())
    output_filename.set('.'.join([input_filename.get().split(sep='.')[0] + '_output', 'csv']))
    output_file_entry.configure(state='normal')
    output_file_entry.focus()


def convert_file():
    if input_filename.get() and output_filename.get():
        input_file = '//'.join([io_dir.get(), input_filename.get()])
        output_file = '//'.join([io_dir.get(), output_filename.get()])
        markers_filtered = converter.open_file(input_file)
        markers_translated = [converter.translate_snp(marker) for marker in markers_filtered]
        converter.save_file(output_file, markers_translated)
    else:
        pass


window = Tk()
window.title = 'SNP converter'
window.geometry('700x250')
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=5)
window.columnconfigure(2, weight=5)
window.columnconfigure(3, weight=1)

io_dir = tkinter.StringVar()
input_filename = tkinter.StringVar()
output_filename = tkinter.StringVar()

select_file_button = tkinter.Button(window, text='Select file', font=24, command=select_input_file)
select_file_button.grid(column=1, row=0, sticky=W+E, padx=5, pady=5)

input_file_label = tkinter.Label(window, text="Input file not selected", font=24)
input_file_label.grid(column=2, row=1, sticky=W+E, padx=5, pady=5)

convert_file_button = tkinter.Button(window, text='Convert file', font=24, command=convert_file)
convert_file_button.grid(column=1, row=2, sticky=W+E, padx=5, pady=5)

output_file_entry = tkinter.Entry(window, width=20, font=24, textvariable=output_filename, state='disabled')
output_file_entry.grid(column=2, row=4, sticky=W+E, padx=5, pady=5)

#converting_status_label = tkinter.Label(window, text="waiting...", font=24)
#converting_status_label.grid(column=1, row=5)

exit_button = tkinter.Button(window, text="Exit", command=window.destroy, font=24)
exit_button.grid(column=1, row=5, sticky=W+E, padx=5, pady=5)

window.mainloop()
