import image_processing
import analyze
import sys

movie = sys.argv[1]
imgdir = 'frames'
times = [0, 1, 1.25, 1.5, 1.75, 2, 2.25, 2.5, 2.75, 3, 3.5, 4, 4.25, 4.5, 4.75, 5, 5.25]
temp_times = []

result = analyze.parse_list(times)
print(result)