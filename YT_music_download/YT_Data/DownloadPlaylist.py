from downloadFunctions import *
import os, sys
import DownloadVideo
import DownloadAudio
from time import sleep
import pafy

pafy.set_api_key("~PEGUE A API KEY do Google Cloud Platform~")   #API key can be found at Google Cloud Platform,
                        #after creating a project and enabling YouTube Data API v3

def DownloadPlaylist():
    url = "https://www.youtube.com/playlist?list=PLLcpBVEQD-CwpLaJzjFbKhBbAn2Wz4lle"
    
    with open('C:\\YT_Data\\dstFolder.txt', 'r') as f:
        cont = f.read().split('\n')

    location = os.path.abspath(cont[0])
    t = str(cont[1])

    #Initializing variables and retrieving playlist data
    playlist = pafy.get_playlist2(url)
    index = 0
    state = True

    while state:
        if index > (len(playlist)-1):    #Check if there videos left to download
            # print("Index over threshold: ", index)
            state = False
            continue
        try:
            if t == '1':        #Download as video
                try:
                    vid = playlist[index]
                    print("Currently in number %i and music name is: %s"%(index, vid.title))
                    DownloadVideo.download(vid, location)

                except Exception as e:
                    print(e)
                    sleep(0.5)


            elif t == '0':    #Download as audio
                try:
                    aud = playlist[index]
                    print("Currently in number %i and music name is: %s"%(index, aud.title))
                    DownloadAudio.download(aud, location)

                except Exception as e:
                    print(e)
                    sleep(0.5)

        except Exception as e:
            print("Process couldn't be concluded!\n", e)

        index += 1    #Go to the next item in the playlist
        print("\n"+"-"*60+"\n")    #Aesthetic spacer for command outputs

if __name__ == "__main__":
  if dependencies.proceed:
      DownloadPlaylist()
