import os, sys, shutil, logging, argparse, subprocess
from time import sleep

#Configures subprocess to not open terminal window
si = subprocess.STARTUPINFO()
si.dwFlags |= subprocess.STARTF_USESHOWWINDOW


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


libraries = ['pydub', 'youtube-dl', 'mutagen', 'pafy',
            'elevate', 'progressbar', 'httplib2', 'bs4',
            'google_auth_oauthlib', 'google-api-python-client',
            'google', 'python-magic', 'python-magic-bin']
proceed = True


#install required libraries, catching exceptions to not proceed with install
try:
    subprocess.call("pip install --upgrade -q -q %s"%(" ".join(libraries)), startupinfo=si)
    dependenciesAvailable = True
except Exception as e:
    print("error")
    logging.error("The following exception occurred:\n", e)
    dependenciesAvailable = False

globalFolder = ""
execDir = "\\".join( ( __file__ ).split('\\')[:-1] )

def Install():
    # from elevate import elevate
    # elevate()   #Ask for root permission to add to PATH
    globalFolder = os.path.abspath(execDir)

    try:
        #This part retrieves the latest FFmpeg upload link from Github
        import httplib2
        from bs4 import BeautifulSoup, SoupStrainer
        import urllib.request as urllib
        http = httplib2.Http()
        ffmpegLink = ""
        status, response = http.request('https://github.com/BtbN/FFmpeg-Builds/releases/')
        for link in BeautifulSoup(response, parse_only=SoupStrainer('a'), features="html.parser"):
            if link.has_attr('href'):
                if 'win64' in link['href'] and link['href'].split('.')[-1] == 'zip' and 'shared' in link['href']:
                    ffmpegLink = "https://github.com/"+link['href']
                    break


        #Downloads the FFmpeg '.zip' file and extracts it
        os.mkdir(os.path.join(globalFolder, "ffmpeg"))
        ffmpeg = os.path.join(globalFolder, "ffmpeg.zip")
        urllib.urlretrieve(ffmpegLink, ffmpeg)
        subprocess.call("tar -xf %s -C %s"%(ffmpeg, os.path.join(globalFolder, "ffmpeg")), startupinfo=si, shell=True)
        subprocess.call(f"del {ffmpeg}", startupinfo=si, shell=True)
        print('1')
        zipFolder = os.path.join(os.path.join(globalFolder, "ffmpeg"), os.listdir(os.path.join(globalFolder, "ffmpeg"))[0])
        print('2')
        for file in os.listdir(zipFolder):
            shutil.move(os.path.join(zipFolder, file), os.path.join(globalFolder, "ffmpeg"))

        #Adds the ffmpeg executable to system environment variables
        ffmpegFolder = os.path.join(os.path.join(globalFolder, "ffmpeg"), "bin")
        subprocess.call(fr"""setx /M PATH "%PATH%;{ffmpegFolder}" """, stdout=subprocess.DEVNULL, startupinfo=si, stderr=subprocess.STDOUT, shell=True)     #Add to PATH without output

        proceed = True


    except Exception as e:
        logging.error(e)
        proceed = False

def copyFiles(dstFolder):
    #Makes sure path is written in the right format
    destinationFolder = os.path.join(os.path.abspath(dstFolder), "Autour")

    #Copies folder structure to chosen destination
    shutil.copytree(execDir, destinationFolder)
    proceed = True
    #Removes ffmpeg folder from origin
    # subprocess.call(f"del {ffmpegFolder}", startupinfo=si)
