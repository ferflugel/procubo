from tkinter import *
from tkinter.filedialog import askdirectory

root = Tk()

root.resizable(False, False)
root.title("Autour Installer")
root.config(background="#000000")

canvas = Canvas(root, width=600, height=500);
canvas.grid(columnspan=10, rowspan=9)
dstFolder = StringVar()

DestinationFolder = Entry(root,
                            width=50,
                            textvariable=dstFolder)

DestinationFolder.grid(column=6,
                        row=3,
                        pady=10,
                        padx=5)

BrowseBtn = Button(root,
                    text="Browse",
                    width=10)

BrowseBtn.grid(column=7,
                row=3,
                pady=10)

AdvanceBtn = Button(root,
                    text="Avançar",
                    width=15)

AdvanceBtn.grid(column=8,
                row=8,
                pady=0,
                padx=10)

root.mainloop()
