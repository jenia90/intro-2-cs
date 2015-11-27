import math

RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2
HEIGHT = 0
WIDTH = 1


def compare_pixel(pixel1, pixel2):
    """
    compares color RGB values of 2 pixels
    :param pixel1: tuple containing the RGB value of the first pixel
    :param pixel2: tuple containing the RGB value of the second pixel
    :return: returns the color difference of the pixels
    """
    return math.fabs(pixel1[RED_INDEX] - pixel2[RED_INDEX]) + \
           math.fabs(pixel1[GREEN_INDEX] - pixel2[GREEN_INDEX]) + \
           math.fabs(pixel1[BLUE_INDEX] - pixel2[BLUE_INDEX])


def compare(image1, image2):
    """
    compares two images and their pixel RGB values
    :param image1: first image
    :param image2: second image
    :return: returns the RGB distance between the 2 images
    """
    distance = 0

    for row in range(image1.size[0]):
        if image2[row]:
            for column in range(image1.size[1]):
                if image2[row][column]:
                    distance += compare_pixel(image1[row][column], image2[row][column])
                else:
                    break

    return distance


def get_piece(image, upper_left, size):
    """
    Gets a slice of the original image at a specific position from the upper left corner
    :param image: the original image
    :param upper_left: the upper left corner position to measure from
    :param size: size of the slice
    :return: returns the slice as list of lists of pixels (height, width)
    """
    new_img = [2]

    for row in range(size[0]):
        if image[row]:
            for column in range(size[1]):
                if image[row][column]:
                    new_img[HEIGHT].append(image.size[HEIGHT] + size[HEIGHT] - 1)
                else:
                    break
            new_img[WIDTH].append(image.size[WIDTH] + size[WIDTH] - 1)
        else:
            break

    return new_img


def set_piece(image, upper_left, piece):
    pass

def average(image):
    pass


def preprocess_tiles(tiles):
    pass


def get_best_tiles(objective, tiles, averages , num_candidates):
    pass


def choose_tile(piece, tiles):
    pass


def make_mosaic(image, tiles, num_candidates):
    pass