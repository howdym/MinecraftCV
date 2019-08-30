import numpy as np
import cv2 as cv
import matplotlib.pyplot as plt


def analyzation(image, background):

    MIN_MATCH_COUNT = 10

    img1 = cv.imread(image, 0)            # queryImage
    img2 = cv.imread(background, 0)       # trainImage

    # Initiate ORB detector
    orb = cv.ORB_create()
    # find the keypoints and descriptors with ORB
    kp1, des1 = orb.detectAndCompute(img1,None)
    kp2, des2 = orb.detectAndCompute(img2,None)

    # BFMatcher with default params
    bf = cv.BFMatcher()
    matches = bf.knnMatch(des1,des2,k=2)

    # Apply ratio test
    good = []
    for m, n in matches:
        if m.distance < 0.75*n.distance:
            good.append([m])
    # cv.drawMatchesKnn expects list of lists as matches.
    # img3 = cv.drawMatchesKnn(img1,kp1,img2,kp2,good,None,flags=cv.DrawMatchesFlags_NOT_DRAW_SINGLE_POINTS)
    # plt.imshow(img3),plt.show()

    if len(good) <= MIN_MATCH_COUNT:
        # print("Not enough matches are found - %d/%d" % (len(good), MIN_MATCH_COUNT))
        return False
    # print(len(good))
    return True


def parse_list(elot):
    keep = True
    lot = []
    focus = len(elot) - 1
    for entry in range(len(elot) - 1, -1, -1):
        pivot = entry - 1
        if entry == 0 and keep:
            temp = [elot[focus]]
            lot.insert(0, temp)
            keep = True
            focus = entry - 1
            continue
        elif keep and elot[focus] - elot[pivot] == 0.25:  # Set the focus
            keep = False
            continue
        elif entry == 0 or (not keep and elot[pivot + 1] - elot[pivot] != 0.25):  # Focus set and sequence ended
            temp = [elot[pivot + 1], elot[focus]]
            lot.insert(0, temp)
            keep = True
            focus = entry - 1
            continue
        elif not keep and elot[pivot + 1] - elot[pivot] == 0.25:  # Focus set and sequence is still ongoing
            continue
        else:  # If focus not set, then it is a lone point.
            temp = [elot[focus]]
            lot.insert(0, temp)
            keep = True
            focus = entry - 1
            continue
    return lot


def write_results(lolot):
    f = open("result.txt", "w+")
    for groups in lolot:
        writing = "["
        for its in groups:
            writing = writing + str(its) + ", "
        writing = writing[0:len(writing) - 2] + "]"
        f.write(writing)
    f.close()
