import os, shutil, logging, argparse
from pydub import AudioSegment as audio
from random import choice
from mutagen.easyid3 import EasyID3
from simple_image_download import simple_image_download as simp

#Configuring argparser for command line inputs
parser = argparse.ArgumentParser()
parser.add_argument(
    "-log",
    "--log",
    default="warning",
    help=(
        "Provide logging level. "
        "Example --log debug', default='warning'"),
    )


options = parser.parse_args()
levels = {
    'critical': logging.CRITICAL,
    'error': logging.ERROR,
    'warn': logging.WARNING,
    'warning': logging.WARNING,
    'info': logging.INFO,
    'debug': logging.DEBUG
}
level = levels.get(options.log.lower())
if level is None:
    raise ValueError(
        f"log level given: {options.log}"
        f" -- must be one of: {' | '.join(levels.keys())}")

logging.basicConfig(level=level)
logger = logging.getLogger(__name__)


#Getting the user's root directory ('C:', 'D:', etc.) and
#assigning a global folder to contain all the files and data the code needs to run
rootDir = os.getcwd().split('\\')[0]
globalFolder = os.path.join(rootDir, "\\YT_Data")
forbiddenChr = ['\\',
            '/',
            '?',
            '<',
            '>',
            ',',
            '|',
            ':',
            '*',
            '"',]


def TitleStandardization(title, forbiddenChars, simpleImDown_folder=False):
    if simpleImDown_folder==True:
        forbiddenChars.append(' ')
    T = ""
    for ind in range(len(title)):
        char = title[ind]
        if ( ord(char) < 31 ) or ( ord(char) > 126 ) or ( char in forbiddenChars ):
            T += "_"
        elif ( ind == len(title)-1 ) and ( char in [' ', '.'] ):
            T += "_"
        else:
            T += title[ind]
    return T

#Find if 'file' is in the 'path' provided
def find(file, path, ext='webm'):
    contains = False
    nm = ""
    asExt = False
    for root, dirs, files in os.walk(path):
        for name in files:
            # if (name == file or ".".join(name.split('.')[:-1]) == file) and name.split('.')[-1] == ext:
            if ( name == file or ".".join(name.split('.')[:-1]) == file ):
                contains = True
                nm = name
                if name.split('.')[-1] == ext:      #If file exists, checks if the extension is the desired one
                    asExt = True
                break
            else:
                contains = False
                nm = name
    return contains, nm, asExt

#Convert .webm file to .mp3
def Cvt2Mp3(loc, f_name):
    file_name = ".".join(f_name.split('.')[:-1]) if len(f_name.split('.')) > 1 else f_name
    file_type = f_name.split('.')[-1]

    file = os.path.join(loc, file_name)
    renamed = TitleStandardization(file_name, forbiddenChr)
    print(renamed)
    rnmFile = os.path.join(loc, renamed)

    aud_file = audio.from_file("%s"%(file+"."+file_type), format=file_type)          #Converting .webm file to .mp3
    os.remove((file+"."+file_type))
    aud_file.export("%s"%(rnmFile+".mp3"), format="mp3")

def standardizeTitle(title):
    forbidden = ['/', '?', '<', '>', "|", ',']
    T = ""
    for ind in range(len(title)):
        if title[ind].lower() in forbidden:
            T += "_"
        else:
            T += title[ind]

    return T

def GetMetadata(file, aud):
    path = os.path.abspath(file)    #Get file's absolute path (as a string)
    pivotFile = os.path.join(globalFolder, "pivotFile.mp3") #Creates a pivotFile to manage copying, deleting and updating the original file
    simpleImagesFolder = os.path.join(globalFolder, "simple_images")    #Variable to contain the folder path of thumbnails
    thumbnailFolder = os.path.join(simpleImagesFolder, TitleStandardization(aud.title, forbiddenChr, simpleImDown_folder=True))    #"~~THE USED LIBRARY AUTOMATICALLY CREATES A FOLDER CALLED 'simple_images'"
    print('0')
    #These lines download the thumbnails from google using the title of the video
    # response = simp.simple_image_download()
    simp().download(TitleStandardization(aud.title, forbiddenChr, simpleImDown_folder=True), 5, progressBar=False)
    print('1')
    #Move original file to the temp. one
    shutil.move(path, pivotFile)
    print('2')
    #Randomly choses one of the 5 thumbails returned from google search engine
    images = [i for g, h, i in os.walk(thumbnailFolder)]
    thumbnail = os.path.join(thumbnailFolder, choice(os.listdir(thumbnailFolder)))
    print("Thumbnail: ", thumbnailFolder)
    print("Path: ", path)
    #Joins the thumbnail and the video
    os.system("""ffmpeg -loglevel warning -i "%s" -i "%s" -map_metadata 0 -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v comment="Cover (front)" "%s" """%(pivotFile, thumbnail, path))

    #Provides metadata properties to the file
    audio = EasyID3(str(path))
    audio['artist'] = aud.author
    audio['performer'] = aud.author
    audio['composer'] = aud.author
    audio['title'] = aud.title
    audio['date'] = aud.published.split('-')[0]
    audio['originaldate'] = aud.published.split('-')[0]
    audio.save()

    # Cleans directories and removes unnecessary files
    for f in os.listdir(thumbnailFolder):
        if file.lower() != "thumbnail.jpg":
            os.remove((os.path.join(thumbnailFolder, f)))
    os.system("""rmdir "%s" """%thumbnailFolder)
    os.system("""rmdir "%s" """%simpleImagesFolder)
    os.remove(pivotFile)
