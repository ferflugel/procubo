import os, sys, shutil, logging, argparse, subprocess
from time import sleep

libraries = ['pydub', 'youtube-dl', 'mutagen', 'pafy', 'elevate', 'progressbar', 'httplib2', 'bs4']
proceed = True

#Creating folder for data handling
execDir = "\\".join( ( __file__ ).split('\\')[:-1])
rootDir = execDir.split('\\')[0]
globalFolder = os.path.join(rootDir, "\\YT_Data")
ffmpegFolder = ""

if execDir != globalFolder:
    from elevate import elevate
    elevate()   #Ask for root permission to add to PATH

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

#install required libraries
try:
    os.system("pip install --upgrade -q -q %s"%(" ".join(libraries)))
except Exception as e:
    logging.error("The following exception occurred:\n", e)
    proceed = False


if execDir != globalFolder:
    try:
        shutil.copytree(execDir, globalFolder)
        proceed = False
        print(f"\n\tFinal destination folder created at '{globalFolder}'\n")

    except FileExistsError:
        logging.critical(f"Delete the folder {globalFolder} before continuing")

    try:
        import httplib2
        from bs4 import BeautifulSoup, SoupStrainer
        http = httplib2.Http()
        ffmpegLink = ""
        status, response = http.request('https://github.com/BtbN/FFmpeg-Builds/releases/')
        for link in BeautifulSoup(response, parse_only=SoupStrainer('a')):
            if link.has_attr('href'):
                if 'win64' link['href'] and link['href'].split('.')[-1] == 'zip':
                    ffmpegLink = "https://github.com/"+link['href']

        os.mkdir(os.path.join(globalFolder, "ffmpeg"))
        ffmpeg = os.path.join(globalFolder, "ffmpeg.zip")
        os.system("curl -L %s -o %s"%(ffmpegLink, ffmpeg))
        os.system("tar -xf %s -C %s"%(ffmpeg, os.path.join(globalFolder, "ffmpeg")))
        os.system(f"del {ffmpeg}")
        zipFolder = os.path.join(os.path.join(globalFolder, "ffmpeg"), os.listdir(os.path.join(globalFolder, "ffmpeg"))[0])
        for file in os.listdir(zipFolder):
            shutil.move(os.path.join(zipFolder, file), os.path.join(globalFolder, "ffmpeg"))

        ffmpegFolder = os.path.join(os.path.join(globalFolder, "ffmpeg"), "bin")
        subprocess.call(fr"""setx /M PATH "%PATH%;{ffmpegFolder}" """, stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT, shell=True)     #Add to PATH without output

    except Exception as e:
        logging.error(e)
        proceed = False


    print("\n\t Continue reading the README.txt file for the next steps in automating the process...")
    sleep(3)
    end = input("\n\nPress 'enter' to conclude this process after taking note of the information presented.")
    os.system("start %s"%globalFolder)
