from  tkinter import *
from tkinter.filedialog import askdirectory
root = Tk()
root.directory = askdirectory()
print(root.directory)
