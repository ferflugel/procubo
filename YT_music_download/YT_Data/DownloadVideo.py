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

    def DownloadVideo(videoId):
        with open(os.path.join(dependencies.globalFolder, 'config.txt'), 'r') as f:
            cont = f.read().split('\n')     #Reads the data from 'config.txt', as created in dependencies.py
        #
        location = os.path.abspath(cont[0])     #Folder to save downloaded videos
        t = str(cont[1])    #Type of download, Audio|Video
        #
        #Initializing variables and retrieving playlist data
        video = pafy.new(videoId)
        state = dependencies.proceed    #If the code runs for the 1st time, it will not download, just resolve the creation of folders and definition of destination folders, etc.
        #
        try:
            if t == '1':        #Download as video
                    Video_handler.download(video, location)

            elif t == '0':    #Download as audio
                    Audio_handler.download(video, location)

            logging.info("\tProcess finished successfully.\n")
        except Exception as e:
            logging.error("Process couldn't be concluded!\n", e)


if __name__ == "__main__":
  if dependencies.proceed:
      logging.info("Dependencies already set up...\n")
