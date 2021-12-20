#!./env/bin/python

"""calendar.py: modual for add events to google calendar."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

# from __future__ import print_function
import os.path
from datetime import datetime
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from pathlib import Path
from loguru import logger


logger.add('loguru.log', format="{time} {level} {message}", filter="my_module", level="INFO")

class GoogleCalendarAPI:
    def __init__(self, message=None):
        self.Path = Path(__file__).parent.parent.absolute()
        self.CLIENT_SECRET = self.Path / "credentials/creds.json"
        self.CLIENT_TOKEN = self.Path / "credentials/token.json"
        self.API_NAME = "calendar"
        self.API_VERSION = "v3"
        self.SCOPES = ["https://www.googleapis.com/auth/calendar"]
        # If modifying these scopes, delete the file token.json.
        self.message = message
        self.get_creds()


    def get_creds(self):
        '''Inits service with given constants'''
        creds = None
        # The file token.json stores the user's access and refresh tokens, and is
        # created automatically when the authorization flow completes for the first
        # time.
        if os.path.exists(self.CLIENT_TOKEN):
            creds = Credentials.from_authorized_user_file(self.CLIENT_TOKEN, self.SCOPES)
        # If there are no (valid) credentials available, let the user log in.
        if not creds or not creds.valid:
            if creds and creds.expired and creds.refresh_token:
                creds.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file(self.CLIENT_SECRET, self.SCOPES)
                creds = flow.run_local_server(port=0)
            # Save the credentials for the next run
            with open(self.CLIENT_TOKEN, "w") as token:
                token.write(creds.to_json())
        self.service = build(self.API_NAME, self.API_VERSION, credentials=creds)


    def get_calendars_list(self):
        #List all calendars
        page_token = None
        while True:
            calendar_list = self.service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
                logger.info(f'{calendar_list_entry["id"]}')
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break

    def get_events(self):
        # Call the Calendar API
        now = datetime(datetime.now().year, 1, 1).isoformat() + "Z"  # 'Z' indicates UTC time
        print("Getting the upcoming 10 events")
        events_result = (
            self.service.events()
            .list(
                calendarId="primary",
                timeMin=now,
                maxResults=50,
                singleEvents=True,
                orderBy="startTime",
            )
            .execute()
        )
        events = events_result.get("items", [])

        if not events:
            print("No upcoming events found.")
        for event in events:
            start = event["start"].get("dateTime", event["start"].get("date"))
            try:
                print(start, event["summary"])
            except KeyError:
                print(event['id'])

    def quick_event_add(self):
        created_event = self.service.events().quickAdd(
        calendarId='primary',
        text=self.message).execute()


if __name__ == '__main__':
    calendar = GoogleCalendarAPI()
    calendar.get_events()
