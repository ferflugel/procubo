import os, sys, shutil

libraries = ['pydub', 'youtube-dl', 'simple-image-download', 'mutagen', 'pafy']
proceed=True

try:
    os.system("pip install --upgrade -q %s"%(" ".join(libraries)))
except Exception as e:
    print("The following exception occurred:\n", e)
    proceed = False

#Creating folder for data handling
try:
    os.mkdir("C:\\YT_Data")
except FileExistsError:
    pass

if os.getcwd() != "C:\\YT_Data":
    shutil.copytree(os.getcwd(), "C:\\YT_Data")

if not os.path.exists('C:\\YT_Data\\dstFolder.txt'):
    destinationFolder = input("""Where do you want the downloaded files to be stored? (In Windows, e.g. "C:\\Users\\~root~\\Music\\")\n        >>> """)
    type = input("\nDo you want the videos to be downloaded as videos or audio? (0-audio and 1-video) >>> ")
    f = open('C:\\YT_Data\\dstFolder.txt', 'w')
    f.write(destinationFolder+'\n'+type)
    f.close()
