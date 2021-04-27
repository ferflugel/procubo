import os, sys
from downloadFunctions import *
from time import sleep

try:
    os.system("pip install --upgrade -q youtube-dl")
    proceed = True
    print("\nYoutube-dl is up to date...")
except Exception as e:
    print("The following exception occurred:\n", e)
    proceed = False

import pafy

pafy.set_api_key("")    #API key can be found at Google Cloud Platform,
                        #after creating a project and enabling YouTube Data API v3


def DownloadPlaylist(use_cmd=False):
    
    if use_cmd == False:
        url = input("URL of the video to download: ")
        location = input("Location to save the video (default goes to '~~YOUR DEST FOLDER~~'): ")
        t = input("Type 1 if you want the video to be downloaded with audio and 0 if just the audio: ")
    else:
        url = str(sys.argv[1])
        location = "~~YOUR DEST FOLDER~~"
        t = str(sys.argv[2])
        print("\nUsing url: %s\nUsing download type: %s"%(url, t))

    if location in ["", " "]:
        location = "~~YOUR DEST FOLDER~~"
        
    #Initializing variables and retrieving playlist data
    playlist = pafy.get_playlist2(url)
    i = 0
    state = True
    NotDownloaded = []
    
    while state:
        try:
            if i > (len(playlist)-1):    #Check if there videos left to download
                    state = False
                    
            if t == '1' and state == True:        #Download as video
                try:
                    vid = playlist[i]
                    print("Currently in number %i and music name is: %s"%(i, vid.title))

                    title = standardizeTitle(vid.title)    #Make title conform to acceptable system parameters,
                                                           #e.g. some videos have '\' and '?', which can mess up in certain systems

                    existence = find(title, location)    #Check if the video isn't already downloaded in the assigned destination folder to conserve data
                    
                    if existence[0] == False:
                        vid.getbest().download(filepath=location, quiet=True)    #Downloads video to folder
                        print("        Succesfully downloaded %s!"%(vid.title))
                    else:
                        print("%s already exists in %s\n" % (title, location))
                        sleep(1)
                    i += 1
                except Exception as e:
                    if e == "index out of range":
                        state = False
                        print("Exiting loop...")
                    print(e)
                    i += 1
                    sleep(0.5)
                    NotDownloaded.append(vid.title)    #I never got this thing to work :/

                    
            elif t == '0' and state == True:    #Download as audio
            
                try:
                    aud = playlist[i]
                    print("Currently in number %i and music name is: %s"%(i, aud.title))

                    title = standardizeTitle(aud.title)

                    existence = find(title, location)
                    
                    if existence[0] == False:
                        aud.getbestaudio().download(filepath=location, quiet=True)
                        print("        Succesfully downloaded %s!"%(aud.title))

                        Cvt2Mp3(location, title)    #Audio files usually come in .webm format, which some players cannot reproduce, so
                                                    #PyDub is used to convert them to .mp3
                        print("        File converted to mp3!")

                        GetMetadata(os.path.join(location, title+".mp3"), aud)    #Use other video metadata from Youtube to add to the file's metadata
                        print("        Metadata updated!")

                    else:
                        if existence[1].split('.')[-1] != 'mp3':
                            modify = input("File already exists in %s, however it is in the format '.webm'\n    Do you want me to convert it to '.mp3'? (Y/N)"%(location))
                            if modify.lower() == "y":
                                try:
                                    Cvt2Mp3(location, existence[1])
                                    print("        File converted to mp3!")

                                    GetMetadata(os.path.join(location, title+".mp3"), aud)
                                    print("        Metadata updated!\n")
                                    
                                except Exception as e:
                                    print("Something went wrong during conversion :/\nContinuing...")
                        else:
                            print("%s already exists in %s\n" % (title, location))
                            sleep(1)
                    i += 1
                    
                except Exception as e:
                    if e == "index out of range":
                        state = False
                        print("Exiting loop...")
                    print(e)
                    i += 1
                    sleep(0.5)
                    NotDownloaded.append(aud.title)
                    
                print("\n"+"-"*60+"\n")    #Aesthetic spacer for command outputs
                
        except Exception as e:
            print("Process couldn't be concluded!\n", e)
            i += 1

    if len(NotDownloaded) >= 1:
        ls = "".join("      "+i+"\n" for i in NotDownloaded)
        text = "Couldn't download the following files: \n" + ls
        #color.write(text, "COMMENT")
    else:
        print("Files downloaded to %s with total success" % location)

if __name__ == "__main__":
    if proceed == True:
        if sys.argv[1] != None:
            DownloadPlaylist(use_cmd=True)
        else:
            DownloadPlaylist()
