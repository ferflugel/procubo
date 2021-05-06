# ORIGINAL CODE BY COREY SCHAFER, ADAPTED BY PROCUBO

import os
import pickle 
import time 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

while True:
    time.sleep(5)
    credentials = None

    # If credentials were saved before
    if os.path.exists('token.pickle'):
        print('Loading Credentials From File...')
        with open('token.pickle', 'rb') as token:
            credentials = pickle.load(token)

    # If we don't have any valid credentials
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            print('Refreshing Access Token...')
            credentials.refresh(Request())
        else:
            print('Fetching New Tokens...')
            flow = InstalledAppFlow.from_client_secrets_file(
                '/Users/fernando/projeto/YT_music_download/client_secrets.json',
                scopes=[
                    'https://www.googleapis.com/auth/youtube.readonly'
                ]
            )
            flow.run_local_server(port=8080, prompt='consent',
                                authorization_prompt_message='')
            credentials = flow.credentials

            # Save the credentials for the next run
            with open('token.pickle', 'wb') as f:
                print('Saving Credentials for Future Use...')
                pickle.dump(credentials, f)

    # Gets the YouTube data
    youtube = build("youtube", "v3", credentials = credentials)
    request = youtube.playlistItems().list(
        part = "status", playlistId ="LLoYJm-CazxEVhojC9S6cH-g", maxResults = 50
    )
    response = request.execute()

    # Check for new ids
    mem = open('memory.txt', 'r')
    memory = mem.read()
    for video in response['items']:
        if video['id'] not in memory:
            # print(video['id']) # What should we do with the id?
            download()

    # Update ids
    IDs = ""
    for video in response['items']:
        IDs += video['id']
        IDs += " \n"
    with open('memory.txt', 'w') as f:
        f.write(IDs)