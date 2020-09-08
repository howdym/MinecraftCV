from __future__ import print_function
import cv2 as cv
import os
import util
import moviepy.editor

# "C:\\Users\\marcj\\Desktop\\Github Projects\\MinecraftCV\\mc07.mp4"

def sec_to_hms(seconds):
    hours = str(int(seconds / 3600))
    if len(hours) == 1:
        hours = "0" + hours
    seconds = seconds % 3600
    minutes = str(int(seconds / 60))
    if len(minutes) == 1:
        minutes = "0" + minutes
    seconds = seconds % 60
    seconds = str(seconds)
    if len(seconds) == 1:
        seconds = "0" + seconds
    ret = hours + ":" + minutes + ":" + seconds
    return ret
    
    

def process_video(mov, situation):
    print(mov)
    cap = cv.VideoCapture(mov)
    fps = cap.get(cv.CAP_PROP_FPS)
    increment = float(1 / fps)
    frame_counter = 0
    snip = False
    running = 0
    begin = 0
    end = 0
    os.mkdir("Videos_" + mov[:-4])

    show = False

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:

            if frame_counter % fps == 0:
                
                total = False
                if situation == "code_builder":
                    tr = util.confirm_top_bar(frame)
                    tr1 = util.confirm_lower_bar(frame)
                    tr2 = util.confirm_side_bar(frame)
                    total = tr or tr1 or tr2
                elif situation == "portfolio":
                    total = util.confirm_portfolio(frame)

                if total:
                    if snip:
                        end += 1
                    else:
                        snip = True
                        begin = running
                        end = begin
                else:
                    if snip: 
                        end = int(end + 1)
                        begin = round(begin)
                        path = os.path.join("Videos_" + mov[:-4], "_{}_{}.mp4".format(round(begin), end))
                        print("ffmpeg -ss {} -i {} -t {} -async 1 -c copy {}".format(sec_to_hms(begin), mov, sec_to_hms(end - begin), path))
                        os.system("ffmpeg -i {} -ss {} -to {} {}".format(mov, sec_to_hms(begin), sec_to_hms(end), path))
                        snip = False
            running += increment
            running = round(running, 1)
            print(frame_counter)
            frame_counter += 1
            continue

        else:
            if snip: 
                end = int(end + 1)
                begin = round(begin)
                path = os.path.join("Videos_" + mov[:-4], "_{}_{}.mp4".format(round(begin), end))
                os.system("ffmpeg -ss {} -i {} -to {} -c copy -copyts {}".format(sec_to_hms(begin), mov, sec_to_hms(end), path))
            cap.release()
            break
