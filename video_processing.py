import image_processing
import analyze


def process_video(mov, name):
    movie = mov
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

    for time in times:
        image_processing.extract_frames(movie, time, imgdir)

    result = analyze.parse_list(times)
    analyze.write_results(result, name)
