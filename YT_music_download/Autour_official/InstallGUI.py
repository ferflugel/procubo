from tkinter import *
from tkinter.filedialog import askdirectory

#This function enables browsing for the destination folder
def Browse():
    download_Path.set( askdirectory() )

def Installer():
    import dependenciesInstaller as depInst
    if depInst.dependenciesAvailable:
        depInst.Install(download_Path)

def Widgets():
    link_label = Label(root,
                       text="Install directory:",
                       bg="#cfcfcf")
    link_label.place(x=20, y=53)

    browse_B = Button(root,
                    text="Browse",
                    command=Browse,
                    # border = "0",
                    width=10,
                    bg="#ffffff")

    browse_B.place(x=400, y=51)

    root.linkText = Entry(root,
                          width=40,
                          textvariable=download_Path)
    root.linkText.place(x=125,y=55)

    browse_B = Button(root,
                    text="Install",
                    command=Installer,
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
    root.config(background="#cfcfcf")

    # Creating the tkinter Variables
    download_Path = StringVar()

    # Calling the Widgets() function
    Widgets()

    # Defining infinite loop to run
    # application
    root.mainloop()
else:
    print("This file must be run through the command line, and cannot be imported...")
