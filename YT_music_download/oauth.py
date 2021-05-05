# ORIGINAL CODE BY COREY SCHAFER

import os
import pickle 
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.discovery import build

credentials = None

if os.path.exists('token.pickle'):
    print('Loading Credentials From File...')
    with open('token.pickle', 'rb') as token:
        credentials = pickle.load(token)

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


youtube = build("youtube", "v3", credentials = credentials)
request = youtube.playlistItems().list(
    part = "status", playlistId ="LLoYJm-CazxEVhojC9S6cH-g"
)

response = request.execute()

print(response)