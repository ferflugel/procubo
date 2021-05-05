import os, sys, shutil
from time import sleep

libraries = ['pydub', 'youtube-dl', 'simple-image-download', 'mutagen', 'pafy']
proceed=True

try:
    os.system("pip install --upgrade -q -q %s"%(" ".join(libraries)))
except Exception as e:
    print("The following exception occurred:\n", e)
    proceed = False



#Creating folder for data handling
rootDir = os.getcwd().split('\\')[0]
globalFolder = os.path.join(rootDir, "\\YT_Data")
ffmpegFolder = ""

if os.getcwd() != globalFolder:
    try:
        shutil.copytree(os.getcwd(), globalFolder)
        proceed = False
        print(f"\n\tFinal destination folder created at '{globalFolder}'\n")

    except FileExistsError:
        shutil.rmtree(globalFolder)
        shutil.copytree(os.getcwd(), globalFolder)
        proceed = False
        print(f"\n\tFinal destination folder created at '{globalFolder}'\n")

    try:
        os.mkdir(os.path.join(globalFolder, "ffmpeg"))
        ffmpeg = os.path.join(globalFolder, "ffmpeg.zip")
        os.system("curl -L https://github.com/BtbN/FFmpeg-Builds/releases/download/autobuild-2021-05-04-12-33/ffmpeg-N-102349-ge27e80edcd-win64-gpl-shared.zip -o %s"%ffmpeg)
        os.system("tar -xf %s -C %s"%(ffmpeg, os.path.join(globalFolder, "ffmpeg")))
        zipFolder = os.path.join(os.path.join(globalFolder, "ffmpeg"), os.listdir(os.path.join(globalFolder, "ffmpeg"))[0])
        for file in os.listdir(zipFolder):
            shutil.move(os.path.join(zipFolder, file), os.path.join(globalFolder, "ffmpeg"))

        ffmpegFolder = '/'.join((os.path.join(os.path.join(globalFolder, "ffmpeg"), "bin")).split('\\'))
        ffmpegDisplay = os.path.join(os.path.join(globalFolder, "ffmpeg"), "bin")
        print(f"\n\tThis folder must be added to system PATH: \t{ffmpegDisplay}\n")
    except Exception as e:
        print(e)
        proceed = False


if not os.path.exists(os.path.join(globalFolder, 'config.txt')):
    destinationFolder = input("""\n\tWhere do you want the downloaded files to be stored? (In Windows, e.g. "C:\\Users\\~root~\\Music\\")\n\n\t\t>>> """)
    type = input("\n\n\tDo you want the videos to be downloaded as videos or audio? (type '0' for audio and '1' for video) \n\n\t\t>>> ")
    f = open(os.path.join(globalFolder, 'config.txt'), 'w')
    f.write(destinationFolder + '\n' + type + '\n' + ffmpegFolder + '\n' + globalFolder)
    f.close()

    g = open(os.path.join(globalFolder, 'runProgram.bat'), 'w')
    #exec = sys.executable
    quietExec = sys.executable.split('.')
    quietExec[0] = quietExec[0]+'w'
    quietExec = '.'.join(quietExec)
    g.write(""" "%s" "%s" """%(quietExec, os.path.join(globalFolder, 'DownloadPlaylist.py')))
    g.close()

    print("\n\t Continue reading the README.txt file for the next steps in automating the process...")
    sleep(3)
    end = input("\n\nPress 'enter' to conclude this process after taking note of the information presented.")
    os.system("start %s"%globalFolder)
