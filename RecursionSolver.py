import sys, os, argparse, cv2
from PIL import Image
import numpy as np

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)


# check if there is entrance on top or left side
def getEntrance(image):
    for x in range(1, image.size[0] - 1):
        if image.getpixel((x, 1)) == white:
            return x, 1
    for y in range(1, image.size[1] - 1):
        if image.getpixel((1, y)) == white:
            return 1, y


# check if there is entrance on top or left side
def getExit(image):
    for x in range(1, image.size[0] - 1):
        if image.getpixel((x, image.size[1] - 2)) == white:
            return x, image.size[1] - 2
    for y in range(1, image.size[1] - 1):
        if image.getpixel((image.size[0] - 2, y)) == white:
            return image.size[0] - 2, y


# check if we are still on the picture and we are not on the wall
def isOnPath(image, x, y):
    if image.size[0] > x >= 0 and image.size[1] > y >= 0:
        if image.getpixel((x, y)) == white:
            return True
    return False


"""
finaly solultion with recursion, where we check:
have we meet exit?
if not check if on path?
if on path - add red pixel, and check other pixels?
if first met is ok, set as red and go next until met exit, if no exit go back to the loop
"""

#TODO add backtracking

def solveMaze(image, x, y):
    successful = False
    if (x, y) == getExit(image):
        successful = True
    elif isOnPath(image, x, y):
        # visited
        image.putpixel((x, y), red)

        # if (solveMaze(image, x + 1, y) or solveMaze(image, x, y - 1) or solveMaze(image, x - 11, y) or solveMaze(image,x,y + 1)):
        #     successful = image.putpixel((x, y), red)

        # then check if neighbours are viable to visit them
        successful = solveMaze(image, x + 1, y)
        if not successful:
            successful = solveMaze(image, x, y - 1)
        if not successful:
            successful = solveMaze(image, x - 1, y)
        if not successful:
            successful = solveMaze(image, x, y + 1)

    # set proper track to green if successful
    if successful:
        image.putpixel((x, y), green)

    return successful


def main(options):
    solved = False
    sys.setrecursionlimit(7000)

    # thicken the walls
    image1 = cv2.imread(options.filename)
    gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    canny_output = cv2.Canny(gray, 100, 255)
    contours, hierarchy = cv2.findContours(canny_output, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    drawing = np.zeros((canny_output.shape[0], canny_output.shape[1], 4), dtype=np.uint8)
    for i in range(len(contours)):
        cv2.drawContours(drawing, contours, i, (255, 255, 255), options.thickness, cv2.LINE_8, hierarchy, 0)
    cv2.imshow('Contours', drawing)
    ret, threshold = cv2.threshold(drawing, 200, 255, cv2.THRESH_BINARY_INV)
    filename = os.path.splitext(options.filename)[0] + "_v2.png"
    cv2.imwrite(filename, threshold)
    cv2.imshow('threshold', threshold)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

    #final solution
    imagePli = Image.open(filename)

    imagePli = imagePli.convert('RGB')
    x, y = getEntrance(imagePli)
    print('Entrance at x = %d, y = %d' % (x, y))
    solved = solveMaze(imagePli, x, y)
    if not solved:
        print('No solution exists.')
    else:
        print('Solved maze.')
        basename = os.path.splitext(options.filename)[0]
        imagePli.save(basename + '_solution' + '.png', 'PNG')

    return 0 if solved else 1


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-th',
        dest='thickness',
        default=4,
        type=int,
        help='Change thickness of walls if the maze is unsolvable, 7-10 when walls thin, and 3-5 when walls are thicker')
    parser.add_argument(
        'filename',
        help='Image containing the maze.')
    options = parser.parse_args()
    sys.exit(main(options))
