import image_processing
import analyze
import sys

movie = sys.argv[1]
imgdir = 'frames'
times = image_processing.make_list(movie)
temp_times = []

for time in times:
    path = image_processing.extract_frames(movie, time, imgdir)

    match = analyze.analyzation("./target.png", path)

    if match:
        temp_times.append(time)

    if image_processing.check_folder(imgdir):
        image_processing.clear_folder(imgdir)

analyze.parse_list(times)
