


import vlc
import time
import requests
import threading
import json
from datetime import datetime
from queue import Queue
from videoPlayer import VideoPlayerApp
from test1 import getTime

# def get_schedule(machine_id):
#     # Replace with your API endpoint to get schedule data
#     api_url = f"http://localhost:8080/api/get_video_data?machine_id={machine_id}"
    
#     try:
#         response = requests.get(api_url)
#         if response.status_code == 200:
#             schedule_data = json.loads(response.text)
#             return schedule_data
#         else:
#             return None
#     except Exception as e:
#         print(f"Error fetching schedule data: {e}")
#         return None
import requests
import json

def get_schedule(machine_id):
    # Replace with your API endpoint to get schedule data
    api_url = "http://localhost:8080/0v2/index.php/Get_schedule"
    current_time = datetime.now().strftime('%H:%M:%S')
    current_date = datetime.now().strftime('%Y-%m-%d')


    try:
        data = {
            'machine_id': machine_id,
            'current_time': current_time,
            'date': current_date
        }

        response = requests.post(api_url, data=data)

        if response.status_code == 200:
            schedule_data = response.json()
            return schedule_data
        else:
            print(f"Error: {response.status_code}")
            return None
    except Exception as e:
        print(f"Error fetching schedule data: {e}")
        return None

#def play_scheduled_videos(machine_id):
   # schedule_data = getTime(machine_id)
   # if schedule_data:
      #  current_time = datetime.now().time()
     #   instance = vlc.Instance('--no-xlib --fullscreen')  # Use '--no-xlib' for headless environments
      #  player = instance.media_player_new()

        #for entry in schedule_data:
          #  start_time = datetime.strptime(entry['start_time'], "%H:%M:%S").time()
           # if current_time < start_time:
                # Calculate the time difference in seconds
              #  time_diff = (datetime.combine(datetime.today(), start_time) - datetime.now()).total_seconds()
              #  if time_diff > 0:


                    ## Vendy Advertisement #####


                    # video_path = f"{entry['video_id']}.mp4"  # Replace with the actual path to your videos      
                    # media = instance.media_new(video_path)
                    # player.set_media(media)
                    # player.play()
                    # time.sleep(time_diff-2)
                    # player.stop()
    

                  #  print(f"Waiting for {time_diff} seconds until the scheduled start time.")
                  #  time.sleep(time_diff)
#

                
               # video_path = f"/home/pi/Desktop/AddCasting/videos/{entry['video_id']}.mp4"  # Replace with the actual path to your videos
               # print(video_path)
               # media = instance.media_new(video_path)
                #player.set_media(media)
               # player.play()



        #player.stop()   


         
    #else:
       # print("No schedule data found or error fetching data.")
import subprocess
import time
from datetime import datetime

def play_scheduled_videos(machine_id):
    schedule_data = getTime(machine_id)

    if schedule_data:
        current_time = datetime.now().time()

        for entry in schedule_data:
            start_time = datetime.strptime(entry['start_time'], "%H:%M:%S").time()

            if current_time < start_time:
                # Calculate the time difference in seconds
                time_diff = (datetime.combine(datetime.today(), start_time) - datetime.now()).total_seconds()

                if time_diff > 0:
                    print(f"Waiting for {time_diff} seconds until the scheduled start time.")
                    time.sleep(time_diff)

                video_path = f"/home/pi/Desktop/AddCasting/videos/{entry['video_id']}.mp4"
                print(video_path)

                # Terminate the previous instance of VLC
                subprocess.run(["pkill", "vlc"])

                # Launch VLC player to play the video
                subprocess.Popen(["vlc", "--fullscreen", video_path])

                # Wait for the video to finish playing
                time.sleep(5)  # Adjust this delay as needed

    else:
        print("No schedule data found or error fetching data.")
