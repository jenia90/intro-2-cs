import math

RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2


def compare_pixel(pixel1, pixel2):
    """
    compares color RGB values of 2 pixels
    :param pixel1: tuple containing the RGB value of the first pixel
    :param pixel2: tuple containing the RGB value of the second pixel
    :return: returns the color difference of the pixels
    """
    return math.fabs(pixel1[RED_INDEX] - pixel2[RED_INDEX]) + math.fabs(pixel1[GREEN_INDEX] - pixel2[GREEN_INDEX]) + \
           math.fabs(pixel1[BLUE_INDEX] - pixel2[BLUE_INDEX])


def compare(image1, image2):
    pass


def get_piece(image, upper_left, size):
    pass


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