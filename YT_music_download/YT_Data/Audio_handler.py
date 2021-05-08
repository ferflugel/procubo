from functions import *
from time import sleep
import pafy

def download(aud, location):
    title = TitleStandardization(aud.title, forbiddenChr)     #Standardizes the video's title to be accepted as an actual file name

    existence = find(title, location, ext='mp3')    #Checks if file has already been downloaded,
                                                #to prevent going over all the playlist again

    if existence[0] == False:
        aud.getbestaudio().download(filepath=location, quiet=True)      #Downloads the file to the given location
        logging.info("\tSuccesfully downloaded %s!"%(aud.title))

        Cvt2Mp3(location, find(title, location)[1])    #Audio files usually come in .webm format, which some players cannot reproduce, so
                                    #PyDub is used to convert them to .mp3
        logging.info("\tFile converted to mp3!")

        GetMetadata(os.path.join(location, title+".mp3"), aud)    #Use Youtube video's metadata to add to the file's metadata
        logging.info("\tMetadata updated!")

    else:
        if existence[2] == False:    #File exists, but is in a format other than .mp3
            try:
                Cvt2Mp3(location, existence[1])
                logging.info("        File converted to mp3!")

                GetMetadata(os.path.join(location, title+".mp3"), aud)
                logging.info("        Metadata updated!\n")

            except Exception as e:
                logging.error("\tSomething went wrong during conversion :/\nContinuing...")
        else:
            logging.info("\n\t%s already exists in %s\n" % (title, location))
            sleep(1)
