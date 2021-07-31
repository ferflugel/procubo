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


rootDir = os.getcwd().split('\\')[0]
globalFolder = os.path.join(rootDir, "\\YT_Data")

#Find if 'file' is in the 'path' provided
def find(file, path, ext):
    contains = False
    nm = ""
    for root, dirs, files in os.walk(path):
        for name in files:
            if (name == file or ".".join(name.split('.')[:-1]) == file) and name.split('.')[-1] == ext:
                contains = True
                nm = name
                break
            else:
                contains = False
                nm = name
    return contains, nm

#Convert .webm file to .mp3
def Cvt2Mp3(loc, f_name):
    file_name = ".".join(f_name.split('.')[:-1]) if len(f_name.split('.')) > 1 else f_name
    file_type = f_name.split('.')[-1]

    file = os.path.join(loc, file_name)

    aud_file = audio.from_file("%s"%(file+"."+file_type), format=file_type)          #Converting .webm file to .mp3
    os.remove((file+"."+file_type))
    aud_file.export("%s"%(file+".mp3"), format="mp3")

def standardizeTitle(title):
    forbidden = ['/', '?', '<', '>', "|", ',']
    T = ""
    for ind in range(len(title)):
        if title[ind].lower() in forbidden:
            T += "_"
        else:
            T += title[ind]

    return T

def folderTitlteStandardization(title):
    forbidden = ['/', '?', '<', '>', ' ', ',', '|', ' ']
    T = ""
    for ind in range(len(title)):
        if title[ind].lower() in forbidden:
            T += "_"
        else:
            T += title[ind]

    return T


def GetMetadata(file, aud):
    path = os.path.abspath(file)
    pivotFile = os.path.join(globalFolder, "pivotFile.mp3")  #"~~YOU MIGHT NEED TO CREATE A PIVOT FILE YOURSELF~~"
    simpleImagesFolder = os.path.join(globalFolder, "simple_images")
    thumbnailFolder = os.path.join(simpleImagesFolder, folderTitlteStandardization(aud.title))    #"~~THE USED LIBRARY AUTOMATICALLY CREATES A FOLDER CALLED 'simple_images'"

    response = simp.simple_image_download()
    response.download(standardizeTitle(aud.title), 5)
    shutil.move(path, pivotFile)

    images = [i for g, h, i in os.walk(thumbnailFolder)]
    thumbnail = os.path.join(thumbnailFolder, choice(os.listdir(thumbnailFolder)))

    os.system("""ffmpeg -loglevel warning -i "%s" -i "%s" -map_metadata 0 -map 0:0 -map 1:0 -c copy -id3v2_version 3 -metadata:s:v comment="Cover (front)" "%s" """%(pivotFile, thumbnail, path))

    audio = EasyID3(str(path))
    audio['artist'] = aud.author
    audio['performer'] = aud.author
    audio['composer'] = aud.author
    audio['title'] = aud.title
    audio['date'] = aud.published.split('-')[0]
    audio['originaldate'] = aud.published.split('-')[0]

    audio.save()

    for f in os.listdir(thumbnailFolder):
        if file.lower() != "thumbnail.jpg":
            os.remove((os.path.join(thumbnailFolder, f)))
    os.system("""rmdir "%s" """%thumbnailFolder)
    os.system("""rmdir "%s" """%simpleImagesFolder)
    os.remove(pivotFile)
