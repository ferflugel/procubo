import os
from pydub import AudioSegment as audio
from random import choice
from mutagen.easyid3 import EasyID3
from simple_image_download import simple_image_download as simp
import shutil

#Find if 'file' is in the 'path' provided
def find(file, path):
    contains = False
    nm = ""
    for root, dirs, files in os.walk(path):
        for name in files:
            if name == file or ".".join(name.split('.')[:-1]) == file:
                contains = True
                nm = name
                break
            else:
                contains = False
                nm = name
    return contains, nm

#Convert .webm file to .mp3
def Cvt2Mp3(loc, f_name):
    file_name = ".".join(f_name.split('.')[:-1])
    file_type = f_name.split('.')[-1]
    
    file = os.path.join(loc, file_name)
    print("        Converting file to mp3!\n")
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
    forbidden = ['/', '?', '<', '>', ' ', ',', '|']
    T = ""
    for ind in range(len(title)):
        if title[ind].lower() in forbidden:
            T += "_"
        else:
            T += title[ind]

    return T


def GetMetadata(file, aud):
    path = os.path.abspath(file)
    pivotFile = "~~YOU MIGHT NEED TO CREATE A PIVOT FILE YOURSELF~~"
    thumbnailFolder = "~~THE USED LIBRARY AUTOMATICALLY CREATES A FOLDER CALLED 'simple_images'"+folderTitlteStandardization(aud.title)
    
    response = simp.simple_image_download()
    response.download(standardizeTitle(aud.title), 5)
    shutil.move(path, pivotFile)
    
    images = [i for g, h, i in os.walk(thumbnailFolder)]
    thumbnail = os.path.join(thumbnailFolder, choice(os.listdir(thumbnailFolder)))
    
    os.system("""ffmpeg -loglevel warning -i "%s" -i "%s" -map_metadata 0 -map 0 -map 1 "%s" """%(pivotFile, thumbnail, path))    

    audio = EasyID3(str(path))
    audio['artist'] = aud.author
    audio['title'] = aud.title
    
    audio.save()

    for f in os.listdir(thumbnailFolder):
        if file.lower() != "thumbnail.jpg":
            os.remove((os.path.join(thumbnailFolder, f)))
    os.system("""rmdir "%s" """%thumbnailFolder)
