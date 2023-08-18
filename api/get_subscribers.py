import csv
from googleapiclient.discovery import build
from googleapiclient import errors
import pandas as pd

# Set up the YouTube Data API client
class Stats():
    def __init__(self, developer_key, channel_id):
        self.channel_id = channel_id
        self.developer_key = developer_key
    
    def get_sub_count(self):
        youtube = build("youtube", "v3", developerKey = self.developer_key)

        channel_id = self.channel_id 

        request = youtube.channels().list(
                part="statistics",
                id= channel_id
            )
        response = request.execute()

        sub_count = response["items"][0]["statistics"]["subscriberCount"]

        return sub_count
    
    def get_view_count(self):
        youtube = build("youtube", "v3", developerKey = self.developer_key)

        channel_id = self.channel_id 

        request = youtube.channels().list(
                part="statistics",
                id= channel_id
            )
        response = request.execute()

        view_count = response["items"][0]["statistics"]["viewCount"]

        return view_count
    
    def get_video_count(self):
        youtube = build("youtube", "v3", developerKey = self.developer_key)

        channel_id = self.channel_id 

        request = youtube.channels().list(
                part="statistics",
                id= channel_id
            )
        response = request.execute()

        video_count = response["items"][0]["statistics"]["videoCount"]

        return video_count
