import dependenciesInstaller

if dependenciesInstaller.proceed:
    from functions import *
    import os, sys
    import Video_handler
    import Audio_handler
    from time import sleep
    import pafy

    pafy.set_api_key("AIzaSyBFhNzsCk8YhXsTacBxKm-_Jd9rKhSvrsc")   #API key can be found at Google Cloud Platform,
                           #after creating a project and enabling YouTube Data API v3

    def DownloadVideo(videoId, location, t):
        #Creates a new instance of the video in pafy
        video = pafy.new(videoId)
        try:
            if t == '1':        #Download as video
                    Video_handler.download(video, location)

            elif t == '0':    #Download as audio
                    Audio_handler.download(video, location)

            logging.info("\tProcess finished successfully.\n")
        except Exception as e:
            logging.error("Process couldn't be concluded!\n", e)


if __name__ == "__main__":
  if dependenciesInstaller.proceed:
      logging.info("Dependencies already set up...\n")
