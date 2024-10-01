
import vlc ,time
import tkinter as tk
import requests
import threading
import json
from datetime import datetime
from test1 import play_video, VideoPlayerApp


def get_schedule(machine_id):
    # Replace with your API endpoint to get schedule data
    api_url = f"http://localhost:8080/api/get_video_data?machine_id={machine_id}"
    
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            schedule_data = json.loads(response.text)
            return schedule_data
        else:
            return None
    except Exception as e:
        print(f"Error fetching schedule data: {e}")
        return None

def play_scheduled_video(machine_id):
    schedule_data = get_schedule(machine_id)
    if schedule_data:
        current_time = datetime.now().time()
        video_app = None  # To hold the VideoPlayerApp instance
        
        for entry in schedule_data:
            start_time = datetime.strptime(entry['start_time'], "%H:%M:%S").time()
            if current_time < start_time:
                # Calculate the time difference in seconds
                time_diff = (datetime.combine(datetime.today(), start_time) - datetime.now()).total_seconds()
                if time_diff > 0:
                    print(f"Waiting for {time_diff} seconds until the scheduled start time.")
                    time.sleep(time_diff)
                
                video_path = f"{entry['video_id']}.mp4"  # Replace with the actual path to your videos
                
                if video_app is not None:
                    video_app.stop_video()  # Stop the previous video and set the window background to black
                
                play = tk.Tk()
                play.attributes('-fullscreen', True)
                video_app = VideoPlayerApp(play, video_path)
                play.mainloop()
                
    else:
        print("No schedule data found or error fetching data.")

if __name__ == "__main__":
     machine_id = input("Enter the machine ID: ")
     play_scheduled_video(machine_id)
     
