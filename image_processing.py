import os
from moviepy.editor import *
import numpy


def close_clip(clip):
    clip.reader.close()
    clip.close()
    del clip.reader
    if clip.audio is not None:
        clip.audio.reader.close_proc()
        clip.audio.close()
        del clip.audio
    del clip


def extract_frames(movie, time, imgdir):
    clip = VideoFileClip(movie)
    imgpath = os.path.join(imgdir, '{}.png'.format(time))
    clip.save_frame(imgpath, time)
    close_clip(clip)
    return imgpath


def make_list(movie):
    clip = VideoFileClip(movie)
    length = clip.duration
    frame_list = numpy.arange(0,length, 0.25)
    close_clip(clip)
    return frame_list


def check_folder(imgdir):
    return len(os.listdir(imgdir)) >= 5


def clear_folder(imgdir):
    for filename in os.listdir(imgdir):
        os.system("del /f " + os.path.join(imgdir, filename))