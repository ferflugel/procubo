import os, sys, shutil

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
    shutil.copytree(os.getcwd(), globalFolder)

if not os.path.exists(os.path.join(globalFolder, 'config.txt')):
    destinationFolder = input("""\n\tWhere do you want the downloaded files to be stored? (In Windows, e.g. "C:\\Users\\~root~\\Music\\")\n\n\t\t>>> """)
    type = input("\n\n\tDo you want the videos to be downloaded as videos or audio? (type '0' for audio and '1' for video) \n\n\t\t>>> ")
    f = open(os.path.join(globalFolder, 'config.txt'), 'w')
    f.write(destinationFolder+'\n'+type)
    f.close()
