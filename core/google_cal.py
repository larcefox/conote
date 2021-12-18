#!./env/bin/python

"""calendar.py: modual for add events to google calendar."""

__author__ = "Bac9l Xyer"
__copyright__ = "GPLv3"

# from __future__ import print_function
import datetime
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials


PATH = os.path.abspath("..")
CLIENT_SECRET = "".join([PATH, "/credentials/creds.json"])
CLIENT_TOKEN = "".join([PATH, "/credentials/token.json"])
API_NAME = "calendar"
API_VERSION = "v3"
SCOPES = ["https://www.googleapis.com/auth/calendar"]
# If modifying these scopes, delete the file token.json.


def main():
    """Shows basic usage of the Google Calendar API.
    Prints the start and name of the next 10 events on the user's calendar.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists(CLIENT_TOKEN):
        creds = Credentials.from_authorized_user_file(CLIENT_TOKEN, SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(CLIENT_SECRET, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open(CLIENT_TOKEN, "w") as token:
            token.write(creds.to_json())

    service = build(API_NAME, API_VERSION, credentials=creds)

    # Call the Calendar API
    now = datetime.datetime.utcnow().isoformat() + "Z"  # 'Z' indicates UTC time
    print("Getting the upcoming 10 events")
    calendar_result = service.calendar.list()
    calendar_items = calendar_result.get("items", [])
    print(calendar_items)
    events_result = (
        service.events()
        .list(
            calendarId="primary",
            timeMin=now,
            maxResults=10,
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
        print(start, event["summary"])


if __name__ == "__main__":
    main()
