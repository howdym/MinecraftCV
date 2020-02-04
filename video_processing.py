from __future__ import print_function
import cv2 as cv
import os
import util
import moviepy.editor

# "C:\\Users\\marcj\\Desktop\\Github Projects\\MinecraftCV\\mc07.mp4"


def process_video(mov, situation):
    print(mov)
    cap = cv.VideoCapture(mov)
    frame_counter = 0
    snip = False
    running = 0
    begin = 0
    end = 0
    clip = moviepy.editor.VideoFileClip(mov)
    os.mkdir("Yes_" + mov[:-4])
    os.mkdir("No_" + mov[:-4])
    os.mkdir("Videos_" + mov[:-4])

    while cap.isOpened():
        ret, frame = cap.read()
        if ret:

            total = False
            if situation == "code_builder":
                tr = util.confirm_top_bar(frame)
                tr1 = util.confirm_lower_bar(frame)
                tr2 = util.confirm_side_bar(frame)
                total = tr or tr1 or tr2
            elif situation == "portfolio":
                total = util.confirm_portfolio(frame)

            if total:
                imgpath = os.path.join("Yes_" + mov[:-4], '{}.png'.format(frame_counter))
                cv.imwrite(imgpath, frame)
                if snip:
                    end += 0.2
                else:
                    snip = True
                    begin = running
                    end = begin
            else:
                imgpath = os.path.join("No_" + mov[:-4], '{}.png'.format(frame_counter))
                cv.imwrite(imgpath, frame)
                if snip:
                    temp = clip.subclip(begin, end)
                    temp.write_videofile(os.path.join("Videos_" + mov[:-4], "_{}_{}.mp4".format(round(begin),
                                                                                               int(end + 1))))
                    snip = False
            running += 0.2
            running = round(running, 1)
            print(frame_counter)
            frame_counter += 1
            continue

        else:
            if snip:
                temp = clip.subclip(begin, end)
                temp.write_videofile(os.path.join("Videos_" + mov[:-4], "_{}_{}.mp4".format(round(begin),
                                                                                           int(end + 1))))
            break
