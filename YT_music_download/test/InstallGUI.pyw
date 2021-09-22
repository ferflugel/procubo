#Installing pre-dependencies
import os, subprocess
subprocess.call("pip install --upgrade -q -q %s"%(" ".join(["Pillow", "Tk", "elevate"])))

#Imports required libraries for GUI
from tkinter import *
from tkinter.filedialog import askdirectory

#This function enables browsing for the destination folder
def openWindow():
    
    
def Widgets():
    #Loads logo image
    load = Image.open(".\etc\LogoPro3.png").resize((215,100))
    render = ImageTk.PhotoImage(load)
    img_label = Label(image=render, borderwidth=0, highlightthickness=0)
    img_label.image = render
    img_label.place(x=142.5, y=20)

    #Text for the label to request install directory
    link_label = Label(root,
                       text="Install directory:",
                       bg="#18241c",
                       fg="#ffffff")
    link_label.place(x=20, y=133)

    #Button that opens search for folder
    browse_B = Button(root,
                    text="Browse",
                    command=Browse,
                    width=10,
                    bg="#ffffff")

    browse_B.place(x=390, y=131)

    #Option for manual input entry
    root.linkText = Entry(root,
                          width=40,
                          textvariable=download_Path)
    root.linkText.place(x=125,y=135)

    #Install button --> continues with program
    browse_B = Button(root,
                    text="Install",
                    command=openWindow,
                    width=10,
                    bg="#000000",
                    fg="#ffffff")

    browse_B.place(x=210, y=200)


if __name__=='__main__':
    # Creating object of tk class
    root = Tk()

    # Setting the title, background color
    # and size of the tkinter window and
    # disabling the resizing property

    root.resizable(False, False)
    root.title("Autour Installer")
    root.geometry('500x300')
    root.config(background="#18241c")

    # Creating the tkinter Variables
    download_Path = StringVar()

    # Calling the Widgets() function
    Widgets()

    # Defining infinite loop to run
    # application
    root.mainloop()
else:
    print("This file must be run through the command line, and cannot be imported...")
