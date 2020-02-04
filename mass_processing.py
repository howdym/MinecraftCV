import video_processing
import os

directory_start = "./"
situation = input("What are you looking for (code_builder or portfolio): ")

for filename in os.listdir(directory_start):
    if filename.endswith(".mp4") or filename.endswith(".avi"):
        video_processing.process_video(filename, situation)
