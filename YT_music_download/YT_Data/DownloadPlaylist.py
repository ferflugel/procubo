import dependencies

if dependencies.proceed:
    from functions import *
    import os, sys
    import Video_handler
    import Audio_handler
    from time import sleep
    import pafy


    pafy.set_api_key("AIzaSyBFhNzsCk8YhXsTacBxKm-_Jd9rKhSvrsc")   #API key can be found at Google Cloud Platform,
                           #after creating a project and enabling YouTube Data API v3

    def DownloadPlaylist():
        url = "https://www.youtube.com/playlist?list=PLLcpBVEQD-CwpLaJzjFbKhBbAn2Wz4lle"    #The url of the playlist to be used

        with open(os.path.join(dependencies.globalFolder, 'config.txt'), 'r') as f:
            cont = f.read().split('\n')     #Reads the data from 'config.txt', as created in dependencies.py

        location = os.path.abspath(cont[0])     #Folder to save downloaded videos
        t = str(cont[1])    #Type of download, Audio|Video

        #Initializing variables and retrieving playlist data
        playlist = pafy.get_playlist2(url)
        index = 0
        state = dependencies.proceed    #If the code runs for the 1st time, it will not download, just resolve the creation of folders and definition of destination folders, etc.

        logging.info("\n" + "*" + "-"*80 + "*" + "\n" + " "*5 + "-"*72 +"\n")  #Aesthetic spacer for command outputs

        while state:
            if index > (len(playlist)-1):    #Checks if there are videos left to download
                logging.info("\tProcess finished successfully.\n")
                logging.info("\n" + " "*5 + "-"*72 + "\n" + "*" + "-"*80 + "*" + "\n")
                state = False
                continue
            try:
                if t == '1':        #Download as video
                    try:
                        vid = playlist[index]
                        logging.info("\n\tCurrently in number %i and music name is: %s"%(index, vid.title))
                        Video_handler.download(vid, location)

                    except Exception as e:
                        logging.error(e)
                        sleep(0.5)


                elif t == '0':    #Download as audio
                    try:
                        aud = playlist[index]
                        logging.info("\n\tCurrently in number %i and music name is: %s"%(index, aud.title))
                        Audio_handler.download(aud, location)

                    except Exception as e:
                        logging.error(e)
                        sleep(0.5)

            except Exception as e:
                logging.error("Process couldn't be concluded!\n", e)

            index += 1    #Go to the next item in the playlist
            logging.info("\n"+"-"*80+"\n")    #Aesthetic spacer for command outputs


if __name__ == "__main__":
  if dependencies.proceed:
      DownloadPlaylist()
