###############################################################################
#  FILE: ex6.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex6 2015-2016
#  DESCRIPTION : Program to create a photo mosaic from different smaller images
#
###############################################################################

import math
import sys
import copy
from mosaic import *

RED_INDEX = 0
GREEN_INDEX = 1
BLUE_INDEX = 2

HEIGHT = 0
WIDTH = 1

SOURCE_IMAGE_INDEX = 1
SOURCE_TILES_INDEX = 2
OUTPUT_IMAGE_INDEX = 3
TILE_HEIGHT_INDEX = 4
NUM_CANDIDATES_INDEX = 5

NUMBER_OF_ARGS = 6
ARGS_LENGTH_ERROR = "Wrong number of parameters. The correct usage is:" \
                    "\nex6.py <image_source> <images_dir> <output_name> " \
                    "<tile_height> <num_candidates>"


def get_image_size(image):
    """
    Gets the image size as tuple (height, width)
    :param image: image to process
    :return: tuple containing the measurements (height, width)
    """
    return len(image), len(image[HEIGHT])


def compare_pixel(pixel1, pixel2):
    """
    compares color RGB values of 2 pixels
    :param pixel1: tuple containing the RGB value of the first pixel
    :param pixel2: tuple containing the RGB value of the second pixel
    :return: returns the color difference of the pixels
    """
    result = 0

    for color in range(3):
        result += math.fabs(pixel1[color] - pixel2[color])

    return result


def compare(image1, image2):
    """
    compares two images and their pixel RGB values
    :param image1: first image
    :param image2: second image
    :return: returns the RGB distance between the 2 images
    """
    distance = 0
    height1, width1 = get_image_size(image1)  # gets the size of the 1st image
    height2, width2 = get_image_size(image2)  # gets the size of the 2nd image

    # iterates through rows and columns of the smaller image and compares
    # each of the pixels from both images
    for row in range(min(height1, height2)):
        for column in range(min(width1, width2)):
            distance += compare_pixel(image1[row][column], image2[row][column])

    return distance


def get_piece(image, upper_left, size):
    """
    Gets a slice of the original image at a specific position from the upper
    left corner
    :param image: the original image
    :param upper_left: the upper left corner position to measure from
    :param size: size of the slice
    :return: returns the slice as list of lists of pixels (height, width)
    """
    height, width = get_image_size(image)  # gets the size of the image

    # slices the original image at specific position and creates a piece of
    # desired size
    return [column[min(width, upper_left[WIDTH]):min(width, upper_left[WIDTH]+
                                                     size[WIDTH])]
            for column
            in image[min(height, upper_left[HEIGHT]):min(height,
                                                         upper_left[HEIGHT] +
                                                         size[HEIGHT])]]


def set_piece(image, upper_left, piece):
    """
    replaces part of the original image with a smaller image piece matching
    by color
    :param image: original image as list of lists (height,width)
    :param upper_left: position of the upper left corner of the new image piece
    :param piece: the piece that would be placed inside the original image
    """
    image_height, image_width = get_image_size(image)
    piece_height, piece_width = get_image_size(piece)

    # gets the beginning and the end of each row and column by
    # taking the one that doesn't exceed the size of the image
    row_start, row_end = min(image_height, upper_left[HEIGHT]), \
                         min(image_height, upper_left[HEIGHT] + piece_height)
    column_start, column_end = min(image_width, upper_left[WIDTH]), \
                               min(image_width, upper_left[WIDTH] + piece_width)

    # iterates the rows and columns of the image and replaces the portion
    # of the original image
    for row in range(row_start, row_end):
        for column in range(column_start, column_end):
            image[row][column] = piece[row - row_start][column - column_start]


def average(image):
    """
    calculates the average each color in the RGB color scheme of the image
    :param image: image to process
    :return: returns a tuple of the average RGB values (red, green, blue)
    """
    red_amount = 0
    green_amount = 0
    blue_amount = 0

    height, width = get_image_size(image)
    resolution = height * width  # calculates the resolution of the image

    # iterates through rows and columns and calculates the combined
    # amount of each of the RGB colors
    for row in range(height):
        for column in range(width):
            red_amount += image[row][column][RED_INDEX]
            green_amount += image[row][column][GREEN_INDEX]
            blue_amount += image[row][column][BLUE_INDEX]

    # devides each combined amount by the image resolution to
    # get the average of each color.
    # (returned value is RGB tuple)
    return red_amount / resolution, \
           green_amount / resolution, \
           blue_amount / resolution


def preprocess_tiles(tiles):
    """
    converts list of tiles (images) into a list containing tuple of their RGB
    value averages
    :param tiles: list of tiles (images)
    :return: list of tuples in (red, green, blue) format
    """
    return [average(tile) for tile in tiles]


def get_best_tiles(objective, tiles, averages , num_candidates):
    """
    creates a list size of num_candidates of best tile matches to the original image
    :param objective: the original image
    :param tiles: list of tiles to check
    :param averages: list of tile color averages as tuple (red, green, blue)
    :param num_candidates: number of tiles to choose
    :return: returns a list of matched tiles
    """
    candidate_tiles = []  # creates a place holder for the returned list
    original_average = average(objective)  # gets the average of the original image
    init_deviation = compare_pixel(original_average, averages[0])

    # keeps looping until the length of the list matches the desired number
    while len(candidate_tiles) < num_candidates:
        min_deviation = init_deviation
        last_index = 0

        # iterates through the list of tiles and checks each if
        # it's average color is the closest to the
        # image\piece of image we want to replace
        for i in range(len(averages)):
            # checks if the tile is not in the list already
            if tiles[i] not in candidate_tiles:
                # compares the average pixel values of 2 tiles
                deviation = compare_pixel(original_average, averages[i])

                # checks if the new deviation is smaller then the
                # initial one (which means better match) and assigns
                # the index of the associated tile to the variable which will
                # later help us find the said tile. also sets the minimum
                # deviation to the smaller value
                if deviation < min_deviation:
                    min_deviation = deviation
                    last_index = i

        # adds the best matching tile to the list
        candidate_tiles.append(tiles[last_index])

    return candidate_tiles


def choose_tile(piece, tiles):
    """
    Gets the best matching tile for the original image piece
    :param piece: piece of the original image that will be replaces
    :param tiles: list of tiles to chose from
    :return: returns best matching tile
    """
    distance = compare(tiles[0], piece)
    index = 0

    # iterates through the list of tiles and checks which one is the best
    # match by pixel value to the piece of the original image
    for i in range(len(tiles)):
        temp_dist = compare(tiles[i], piece)

        if temp_dist < distance:
            distance = temp_dist
            index = i

    return tiles[index]


def make_mosaic(image, tiles, num_candidates):
    """
    Creates the mosaic image from the tiles list
    :param image: original image
    :param tiles: list of tiles to process and replace regions of the image with
    :param num_candidates: number of tiles to choose that will be shown in the mosaic
    :return: returns the mosaic image
    """
    height_tile, width_tile = get_image_size(tiles[0])
    height_image, width_image = get_image_size(image)
    last_position = [0, 0]
    mosaic = copy.deepcopy(image)
    averages = preprocess_tiles(tiles)

    # divides the image into squares which size is the size of the tiles
    # and then iterates through the rows and columns and finds
    # best matches for each piece of the original image from the list of tiles
    for row in range(0, height_image, height_tile):
        for column in range(0, width_image, width_tile):
            piece = get_piece(image, last_position, [height_tile, width_tile])
            best_tiles = get_best_tiles(piece, tiles, averages, num_candidates)
            best_tile = choose_tile(piece, best_tiles)
            set_piece(mosaic, last_position, best_tile)
            last_position = row, column
    return mosaic


def main(args):
    """
    Gets the environment arguments passed to the script and assigns them to variables.
    Then calls the appropriate functions to create the mosaic image
    :param args: list of environment arguments
    """
    # checks if number of system arguments passed to the script is correct
    if len(args) == NUMBER_OF_ARGS:
        # these next few lines create variables holding the values
        # of the environmental arguments passed tot the script
        source_image = args[SOURCE_IMAGE_INDEX]
        source_tiles = args[SOURCE_TILES_INDEX]
        output_image = args[OUTPUT_IMAGE_INDEX]
        tile_height = int(args[TILE_HEIGHT_INDEX])
        num_candidates = int(args[NUM_CANDIDATES_INDEX])

        save(
            make_mosaic(
                load_image(source_image),
                build_tile_base(source_tiles, tile_height),
                num_candidates),
            output_image)
    else:
        print(ARGS_LENGTH_ERROR)

# calls the main function whenever the script is executed and passes args to it
if __name__ == '__main__':
    main(sys.argv)
