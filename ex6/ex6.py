import math
import sys
from mosaic import *
import logging

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


def get_image_size(image):
    return len(image), len(image[WIDTH])


def compare_pixel(pixel1, pixel2):
    """
    compares color RGB values of 2 pixels
    :param pixel1: tuple containing the RGB value of the first pixel
    :param pixel2: tuple containing the RGB value of the second pixel
    :return: returns the color difference of the pixels
    """
    '''
    result = 0

    for color in range(3):
        result += math.fabs(pixel1[color] - pixel2[color])
    '''
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
    height, width = get_image_size(image1)

    for row in range(height):
        if image2[row]:
            for column in range(width):
                if image2[row][column]:
                    logging.warning(str(image1[row][column]) + '\t' + str(image2[row][column]))
                    distance += compare_pixel(image1[row][column], image2[row][column])
                    logging.warning(distance)
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
    piece = []
    height, width = get_image_size(image)

    for row in range(size[HEIGHT]):
        if image[row]:
            for column in range(size[WIDTH]):
                if image[row][column]:
                    piece.append(image[row + upper_left[HEIGHT]][column + upper_left[WIDTH]])

    return piece


def set_piece(image, upper_left, piece):
    """
    replaces part of the original image with a smaller image piece matching by color
    :param image: original image as list of lists (height,width)
    :param upper_left: starting position of the upper left corner of the new image piece
    :param piece: the piece that would be placed inside the original image
    """
    height, width = get_image_size(piece)

    for row in range(height):
        if image[row]:
            for column in range(width):
                if image[row][column]:
                    image[upper_left[HEIGHT] + row][upper_left[WIDTH] + column] = piece[HEIGHT][WIDTH]
                else:
                    break
        else:
            break


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
    resolution = height * width

    for row in range(height):
        if image[row]:
            for column in range(width):
                if image[row][column]:
                    red_amount += image[row][column][RED_INDEX]
                    green_amount += image[row][column][GREEN_INDEX]
                    blue_amount += image[row][column][BLUE_INDEX]

    return red_amount / resolution, green_amount / resolution, blue_amount / resolution


def preprocess_tiles(tiles):
    """
    converts list of tiles (images) into a list containing tuple of their RGB value averages
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
    candidate_tiles = []
    original_average = average(objective)
    init_deviation = compare_pixel(original_average, averages[0])

    while len(candidate_tiles) < num_candidates:
        deviation = init_deviation

        for i in range(len(tiles)):
            if tiles[i] not in candidate_tiles:
                deviation = compare_pixel(original_average, averages[i])

                if deviation < init_deviation:
                    candidate_tiles.append(tiles[i])

    return candidate_tiles


def choose_tile(piece, tiles):
    return min([compare(tile, piece) for tile in tiles])


def make_mosaic(image, tiles, num_candidates):
    height_tile, width_tile = get_image_size(tiles[0])
    height_image, width_image = get_image_size(image)
    last_position = [0, 0]
    mosaic = image
    best_tiles = get_best_tiles(image, tiles, preprocess_tiles(tiles), num_candidates)

    for row in range(int(height_image / height_tile)):
        for column in range(int(width_image / width_tile)):
            best_tile = choose_tile(get_piece(image, last_position, [height_tile, width_tile]), best_tiles)
            set_piece(mosaic, last_position, best_tile)
            last_position += height_tile, width_tile
    return mosaic


def main(args):
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


if __name__ == '__main__':
    main(sys.argv)
