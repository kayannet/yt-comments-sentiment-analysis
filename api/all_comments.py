import csv
from googleapiclient.discovery import build
from googleapiclient import errors
import pandas as pd
import random
'''
Parameters: developer_key, channel_id, csv_file, max_num

pulls max_num of comments from specified channel id, will pull different
set of comments everytime it's ran for the same channel_id
'''

class Comments():
    def __init__(self, developer_key, channel_id, csv_file, max_num = 100):
        self.channel_id = channel_id
        self.developer_key = developer_key
        self.max_num = max_num
        self.csv_file = csv_file
        # self.videos = []
        # print("intialized successfully")

    # def get_videos(self, max_results_per_page, max_total_results):
    #     api_key = self.developer_key
    #     channel_id = self.channel_id
    #     youtube = build("youtube", "v3", developerKey = api_key)

    #     # Get the channel's uploads playlist ID
    #     channels_response = youtube.channels().list(part="contentDetails", id=channel_id).execute()
    #     playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

    #     # Retrieve all video IDs from the channel's uploads playlist
    #     videos = []
    #     next_page_token = None 
                
    #     while len(videos) < max_total_results:
    #         playlist_response = youtube.playlistItems().list(
    #             part="contentDetails",
    #             playlistId=playlist_id,
    #             maxResults = max_results_per_page,
    #             order = 'time',
    #             pageToken=next_page_token
    #         ).execute()

    #         self.videos.extend(playlist_response["items"])
    #         next_page_token = playlist_response.get("nextPageToken")

    #         if not next_page_token or len(videos) >= max_total_results:
    #             break

    def get_comments(self):
        # if len(self.videos) == 0:
        #     print('There are no videos compiled, run get_videos() first.')
        #     return False
        
        # # Set up the YouTube Data API client
        api_key = self.developer_key
        channel_id = self.channel_id
        youtube = build("youtube", "v3", developerKey = api_key)

        # Get the channel's uploads playlist ID
        channels_response = youtube.channels().list(part="contentDetails", id=channel_id).execute()
        playlist_id = channels_response["items"][0]["contentDetails"]["relatedPlaylists"]["uploads"]

        # Retrieve all video IDs from the channel's uploads playlist
        videos = []
        next_page_token = None                 

        while True:
            playlist_response = youtube.playlistItems().list(
                part="contentDetails",
                playlistId=playlist_id,
                maxResults=50,
                #order = 'date',
                pageToken=next_page_token
            ).execute()

            videos.extend(playlist_response["items"])
            next_page_token = playlist_response.get("nextPageToken")

            if not next_page_token:
                break
        

        # Randomize the order of videos
        random.shuffle(videos)

        # Retrieve all comments from each video
        comments = []
        dates = []

        # Make an API request to retrieve channel details
        channel_request = youtube.channels().list(
            part="snippet",
            id=channel_id
        )
        channel_response = channel_request.execute()

        # Extract the channel name from the API response
        channel_name = channel_response['items'][0]['snippet']['title']

        # List to store the channel names
        channel_names = []

        for video in videos:
            video_id = video["contentDetails"]["videoId"]
            try:
                comment_threads_response = youtube.commentThreads().list(
                    part="snippet",
                    videoId=video_id,
                    maxResults=50,
                    order="relevance"
                ).execute()

                for item in comment_threads_response["items"]:
                    if len(comments) >= self.max_num:
                        break
                    comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
                    comments.append(comment)
                    channel_names.append(channel_name)
                    dates.append(item["snippet"]["topLevelComment"]["snippet"]["publishedAt"])
                    print("comment successfully added: ", channel_name)

                if len(comments) >= self.max_num:
                    break 

            except errors.HttpError as e:
                error_details = e.content.decode("utf-8")
                if "commentsDisabled" in error_details:
                    print("Comments are disabled for video: ", channel_name, ' ' , video_id)
                else:
                    print("An error occurred while retrieving comments:", error_details)

        # Save the comments in a CSV file
        with open(self.csv_file, "a", encoding="utf-8", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Youtuber", "Comments", 'Date'])

            for i in range(len(comments)):
                writer.writerow([channel_names[i], comments[i], dates[i]])


        print("Comments have been saved to", self.csv_file)


'''#given list of channel ids, get n comments from each
api_key = 'AIzaSyDQgVDKL4m1DtWTfee5wEY2rF8iR_JgXRM'
channel_ids = ["UC7_YxT-KID8kRbqZo7MyscQ", "UCTkXRDQl0luXxVQrRQvWS6w"] # markiplier
for i in channel_ids:
    obj = Comments(api_key, i, "test_csv", 5)
    obj.get_comments()
# test = Comments(api_key, channel_ids, "test_csv", 5)
# test.get_comments()'''