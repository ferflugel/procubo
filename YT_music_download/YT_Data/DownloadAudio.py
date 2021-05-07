from downloadFunctions import *
from time import sleep
import pafy

def download(aud, location):
    title = standardizeTitle(aud.title)

    existence = find(title, location, 'mp3')

    if existence[0] == False:
        aud.getbestaudio().download(filepath=location, quiet=True)
        logging.info("\tSuccesfully downloaded %s!"%(aud.title))

        Cvt2Mp3(location, find(title, location, 'webm')[1])    #Audio files usually come in .webm format, which some players cannot reproduce, so
                                    #PyDub is used to convert them to .mp3
        logging.info("\tFile converted to mp3!")

        GetMetadata(os.path.join(location, title+".mp3"), aud)    #Use other video metadata from Youtube to add to the file's metadata
        logging.info("\tMetadata updated!")

    else:
        if existence[1].split('.')[-1] != 'mp3':    #File exists, but is in a format other than .mp3
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
