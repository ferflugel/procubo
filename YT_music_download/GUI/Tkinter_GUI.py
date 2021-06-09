from tkinter import *
from tkinter.filedialog import askdirectory

#This function enables browsing for the destination folder
def Browse():
    download_Path.set( askdirectory() )

#This function calls the other python file to download the playlist
def Download():


# Defining CreateWidgets() function
# to create necessary tkinter widgets
def Widgets():
    link_label = Label(root,
                       text="Playlist code :",
                       bg="#E8D579")
    link_label.grid(row=1,
                    column=0,
                    pady=10,
                    padx=0)

    root.linkText = Entry(root,
                          width=40,
                          textvariable=playlist_code)
    root.linkText.grid(row=1,
                       column=1,
                       pady=10,
                       padx=5,
                       )

    format_label = Label(root,
                       text="Download format :",
                       bg="#E8D579")
    format_label.grid(row=2,
                      column=0,
                      pady=10,
                      padx=10)

    root.formatmenu = OptionMenu(root,
                                 clicked,
                                 "Audio",
                                 "Video")
    root.formatmenu.grid(row=2,
                         column=1,
                         pady=10,
                         padx=10)

    root.formatmenu.config(width = 35,
                            height = 1)

    destination_label = Label(root,
                              text="Destination :",
                              bg="#E8D579")
    destination_label.grid(row=3,
                           column=0,
                           pady=10,
                           padx=10)

    root.destinationText = Entry(root,
                                 width=40,
                                 textvariable=download_Path)
    root.destinationText.grid(row=3,
                              column=1,
                              pady=10,
                              padx=10)

    browse_B = Button(root,
                      text="Browse",
                      command=Browse,
                      width=10,
                      bg="#05E8E0")
    browse_B.grid(row=3,
                  column=2,
                  pady=1,
                  padx=1)

    Download_B = Button(root,
                        text="Download",
                        #command=Download,
                        width=20,
                        bg="#05E8E0")
    Download_B.grid(row=4,
                    column=1,
                    pady=3,
                    padx=3)


# Creating object of tk class
root = Tk()

# Setting the title, background color
# and size of the tkinter window and
# disabling the resizing property

root.resizable(False, False)
root.title("Playlist_Downloader")
root.config(background="#000000")

# Creating the tkinter Variables
playlist_code = StringVar()
download_Path = StringVar()
clicked = StringVar()
clicked.set("Audio")

# Calling the Widgets() function
Widgets()

# Defining infinite loop to run
# application
root.mainloop()
