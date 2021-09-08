# ORIGINAL CODE BY COREY SCHAFER, ADAPTED BY PROCUBO

import os, pickle
from time import sleep
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build
import DownloadVideo
from functions import *

#Stops program if it is not configured correctly
if not DownloadVideo.dependenciesInstaller.proceed:
    raise SystemExit(0)

with open('memory.txt', 'w') as f:
    pass

#Setting variables
# with open('config.txt', 'r') as f:
#     playlist_id = f.read().split('\n')[3]
playlist_id = "PLLcpBVEQD-Czy_ykXnqiY0O2tN4EYzh6j"
location = "M:\\"
t = '0'
credentials = None


# If credentials were saved before
if os.path.exists('token.pickle'):
    logging.info('Loading Credentials From File...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

# If we don't have any valid credentials
if not credentials or not credentials.valid:
    if credentials and credentials.expired and credentials.refresh_token:
        logging.info('Refreshing Access Token...')
        credentials.refresh(Request())
    else:
        logging.info('Fetching New Tokens...')
        flow = InstalledAppFlow.from_client_secrets_file(
            'client_secrets.json',
            scopes=[
                'https://www.googleapis.com/auth/youtube.readonly'
            ]
        )
        flow.run_local_server(port=8080, prompt='consent',
                            authorization_prompt_message='')
        credentials = flow.credentials

        # Save the credentials for the next run
        with open('token.pickle', 'wb') as f:
            logging.info('Saving Credentials for Future Use...')
            pickle.dump(credentials, f)

# Gets the YouTube data
youtube = build("youtube", "v3", credentials = credentials)
request = youtube.playlistItems().list(
    part = "snippet", playlistId = playlist_id, maxResults = 50
)

#Loop to check for additions to playlist
while True:
    sleep(5)
    response = request.execute()

    IDs = ""
    itemsIds = getAllPlaylistItems(response, youtube, playlist_id)
    mem = open('memory.txt', 'r')
    memory = mem.read().split('\n')
    mem.close()

    for id in itemsIds:
        #save to memory
        IDs += id+"\n"

        if id not in memory:
            DownloadVideo.DownloadVideo(id, location, t)

    logging.info("Nothing new, continuing...")

    with open('memory.txt', 'w') as f:
        f.write(IDs)
