import moviepy.editor


def close_clip(clip):
    clip.reader.close()
    clip.close()
    del clip.reader
    if clip.audio is not None:
        clip.audio.reader.close_proc()
        clip.audio.close()
        del clip.audio
    del clip

