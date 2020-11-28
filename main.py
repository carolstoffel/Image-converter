from tkinter import *
from tkinter import filedialog
import convert_image

root = Tk()
root.title('Image Converter')
root.geometry('380x100')


def browse_button():
    global folder_path
    global filename
    filename = filedialog.askdirectory()
    e.insert(0, filename)


def ok_button(format):
    backup = var_backup.get()
    convert_image.main(filename, backup, format)


frame = LabelFrame(root)
frame.grid(row=10, column=3)

MODES = [("BMP", ".bmp"), ("JPG", ".jpg"), ("PNG", ".png")]
format = StringVar()
format.set(".jpg")

c = 0
for text, mode in MODES:
    Radiobutton(root, text=text, variable=format,
                value=mode).grid(row=0, column=c)
    c += 1

e = Entry(root, borderwidth=2, width=40, bg="white")
e.grid(row=2, column=1)


folder_path = StringVar()
lbl1 = Label(master=root, textvariable=folder_path)
lbl1.grid(row=2, column=0)
button1 = Button(root, text="Browse", command=browse_button, anchor=W)
button1.grid(row=2, column=2, padx=10)
button2 = Button(root, text="OK", command=lambda: ok_button(format.get()))
button2.grid(row=3, column=2, pady=10)

var_backup = BooleanVar()
c1 = Checkbutton(root, text='Fazer backup', variable=var_backup,
                 onvalue=True, offvalue=False, anchor=E)
c1.deselect()
c1.grid(row=3, column=0, columnspan=5)

root.mainloop()
