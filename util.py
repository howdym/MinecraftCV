import cv2
import numpy as np
from moviepy.editor import *

# Generate test videos
# mov = "C:\\Users\\marcj\\Desktop\\Github Projects\\MinecraftCV\\mc07.mp4"
# clip = VideoFileClip(mov)
# temp = clip.subclip((26 * 60 + 20), (27 * 60 + 6))
# temp.write_videofile("test_video_no_beginning.mp4")

def template_helper(img, target):
    h = target.shape[0]
    w = target.shape[1]
    res = cv2.matchTemplate(img[:, :, 0], target[:, :, 0], cv2.TM_SQDIFF_NORMED)
    res += cv2.matchTemplate(img[:, :, 1], target[:, :, 1], cv2.TM_SQDIFF_NORMED)
    res += cv2.matchTemplate(img[:, :, 2], target[:, :, 2], cv2.TM_SQDIFF_NORMED)
    threshold = 0.0075
    loc = np.where(res <= threshold)
    img_rgb = img.copy()

    for pt in zip(*loc[::-1]):
        cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0, 0, 255), 2)

    # This is for debugging purposes because we can see if the computer detected the image or not
    # because it will show with a highlighted box
    # img_rgb = cv2.resize(img_rgb, (800, 450))
    # cv2.imshow('Frame', img_rgb)
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()

    return len(loc[0]) == 1 and len(loc[1]) == 1


# Find out if person is on the page of interest
def confirm_top_bar(img):
    img2 = cv2.imread("target_images\\tc.png")
    target = img2[0:45, 0:120, :]
    target1 = img2[0:45, 220:400, :]
    target2 = img2[0:45, 508:628, :]
    return template_helper(img, target) or template_helper(img, target1) or template_helper(img, target2)

# Find out if person is on the page of interest
def confirm_lower_bar(img):
    img2 = cv2.imread("target_images\\tc.png")
    target = img2[45:, 0:120, :]
    target1 = img2[45:, 250:370, :]
    target2 = img2[45:, 508:628, :]

    # Confirm that we cropped the image correctly 
    # img1 = cv2.imread("C:\\Users\\marcj\\Desktop\\Github Projects\\MinecraftCV\\target_code_top.png")
    # img1 = img1[0:37, :, :]
    # cv2.imshow("target", target)
    # if cv2.waitKey(0) & 0xFF == ord('q'):
    #     cv2.destroyAllWindows()
    
    return template_helper(img, target) or template_helper(img, target1) or template_helper(img, target2)

# Find out if person is on the page of interest
def confirm_side_bar(img):
    target = cv2.imread("target_images\\target_code_side.png")
    target1 = target[0:45, :, :]
    target2 = target[45:100, :, :]
    target3 = target[99:154, :, :]
    target4 = target[153:153 + 58, :, :]
    target5 = target[153 + 56:153 + 54 + 58, :, :]
    target6 = target[153 + 54 + 57:153 + 54 + 58 + 55, :, :]
    target7 = target[153 + 54 + 111:153 + 54 + 113 + 55, :, :]
    target8 = target[153 + 54 + 113 + 54:153 + 54 + 113 + 110, :, :]
    target9 = target[153 + 54 + 113 + 108:153 + 54 + 113 + 166, :, :]
    return template_helper(img, target1) or template_helper(img, target2) or template_helper(img, target3) or \
           template_helper(img, target4) or template_helper(img, target5) or template_helper(img, target6) or \
           template_helper(img, target7) or template_helper(img, target8) or template_helper(img, target9)

def confirm_portfolio(img):
    target = cv2.imread("target_images\\portfolio.png")
    target1 = target[65:95, 260:380, :]
    target2 = target[575:595, 342:360, :]
    target3 = target[637:677, 520:760, :]
    return template_helper(img, target1) or template_helper(img, target2) or template_helper(img, target3)
