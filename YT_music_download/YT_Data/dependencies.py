import os, sys, shutil
from time import sleep

libraries = ['pydub', 'youtube-dl', 'simple-image-download', 'mutagen', 'pafy']
proceed=True

try:
    os.system("pip install --upgrade -q %s"%(" ".join(libraries)))
except Exception as e:
    print("The following exception occurred:\n", e)
    proceed = False

#Creating folder for data handling
rootDir = os.getcwd().split('\\')[0]
globalFolder = os.path.join(rootDir, "\\YT_Data")

if os.getcwd() != globalFolder:
    try:
        shutil.copytree(os.getcwd(), globalFolder)
        proceed = False
        print("\n\tFinal destination folder created at '%s'"%globalFolder)
    except FileExistsError:
        if len(os.listdir(globalFolder)) != len(os.listdir(os.getcwd())):
            shutil.rmtree(globalFolder)
            shutil.copytree(os.getcwd(), globalFolder)
            proceed = False
            print("\n\tFinal destination folder created at '%s'"%globalFolder)

if not os.path.exists(os.path.join(globalFolder, 'config.txt')):
    destinationFolder = input("""\n\tWhere do you want the downloaded files to be stored? (In Windows, e.g. "C:\\Users\\~root~\\Music\\")\n\n\t\t>>> """)
    type = input("\n\n\tDo you want the videos to be downloaded as videos or audio? (type '0' for audio and '1' for video) \n\n\t\t>>> ")
    f = open(os.path.join(globalFolder, 'config.txt'), 'w')
    f.write(destinationFolder+'\n'+type)
    f.close()

    g = open(os.path.join(globalFolder, 'runProgram.bat'), 'w')
    g.write(""" "%s" "%s" """%(sys.executable, os.path.join(globalFolder, 'DownloadPlaylist.py')))
    g.close()

    print("\n\t Continue reading the README.txt file for the next steps in automating the process...")
    sleep(3)
    end = input("\n\nPress 'enter' to close this windows after taking note of the information presented.")
    os.system("start %s"%globalFolder)
