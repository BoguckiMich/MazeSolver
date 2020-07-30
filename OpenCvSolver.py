import cv2, sys, argparse
import numpy as np


def main(options):
    filename = options.filename
    img = cv2.imread(filename)
    cv2.imshow('Maze', img)

    # to apply thresholding we need to convert picture to grayscale
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    cv2.imshow('Gray maze', gray)

    # thresholding allows us to see where the pixel is different from white background, and inverting the colors
    ret, threshold = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY_INV)

    # saving to file
    cv2.imshow('Threshold 1', threshold)

    # we are looking for contours from entry point to exit point
    contours, hierarchy = cv2.findContours(threshold, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
    drawnContours = cv2.drawContours(threshold, contours, 0, (255, 255, 255), 5)
    cv2.imshow('Contours1', drawnContours)

    # we are cleaning maze from unwanted contours
    drawnContours = cv2.drawContours(drawnContours, contours, 1, (0,0,0), 5)
    cv2.imshow('Contours2', drawnContours)

    # we are creating buffer from contours
    contourBuffer = np.ones((19,19), np.uint8)
    contourBufferRes = cv2.dilate(drawnContours, contourBuffer, iterations=1)
    cv2.imshow('Buffer', contourBufferRes)

    # by eroding we are creating same alement but smaller so we could later cut the line to the end
    thinBufferRes = cv2.erode(contourBufferRes, contourBuffer, iterations=1)
    cv2.imshow('Thin buffer', thinBufferRes)

    # difference of two similar elements
    difference = cv2.absdiff(contourBufferRes, thinBufferRes)
    cv2.imshow('Absolute difference', difference)

    #TODO find a way to draw it on picture

    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__=='__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filename',
        help='Image containing the maze.')
    options = parser.parse_args()
    sys.exit(main(options))