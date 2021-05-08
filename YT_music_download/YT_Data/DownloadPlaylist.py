import dependencies

if dependencies.proceed:
    from downloadFunctions import *
    import os, sys
    import DownloadVideo
    import DownloadAudio
    from time import sleep
    import pafy

    pafy.set_api_key("AIzaSyBFhNzsCk8YhXsTacBxKm-_Jd9rKhSvrsc")   #API key can be found at Google Cloud Platform,
                                         #after creating a project and enabling YouTube Data API v3

    def DownloadPlaylist(url):

        with open(os.path.join(dependencies.globalFolder, 'config.txt'), 'r') as f:
            cont = f.read().split('\n')

        location = os.path.abspath(cont[0])
        t = str(cont[1])

        #Initializing variables and retrieving playlist data
        playlist = pafy.get_playlist2(url)
        index = 0
        state = dependencies.proceed

        logging.info("\n" + "*" + "-"*80 + "*" + "\n" + " "*5 + "-"*72 +"\n")  #Aesthetic spacer for command outputs

        while state:
            if index > (len(playlist)-1):    #Check if there videos left to download
                logging.info("\tProcess finished successfully.\n")
                logging.info("\n" + " "*5 + "-"*72 + "\n" + "*" + "-"*80 + "*" + "\n")
                state = False
                continue
            try:
                if t == '1':        #Download as video
                    try:
                        vid = playlist[index]
                        logging.info("\n\tCurrently in number %i and music name is: %s"%(index, vid.title))
                        DownloadVideo.download(vid, location)

                    except Exception as e:
                        logging.error(e)
                        sleep(0.5)


                elif t == '0':    #Download as audio
                    try:
                        aud = playlist[index]
                        logging.info("\n\tCurrently in number %i and music name is: %s"%(index, aud.title))
                        DownloadAudio.download(aud, location)

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
