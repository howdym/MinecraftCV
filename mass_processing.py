import video_processing
import os

directory_start = "./"

for filename in os.listdir(directory_start):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        video = os.path.join(directory_start, filename)
        logname = filename[0:len(filename) - 4]
        name = logname + "_ci-instances.txt"
        video_processing.process_video(video, name)
