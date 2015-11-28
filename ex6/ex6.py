import math
import sys
from mosaic import *
import logging

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
    height, width = len(image1[HEIGHT]), len(image1[WIDTH])

    for row in range(height):
        if image2[row]:
            for column in range(width):
                if image2[row, column]:
                    distance += compare_pixel(image1[row, column], image2[row, column])
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
    piece = [2]
    height, width = len(image[HEIGHT]), len(image[WIDTH])

    for row in range(size[HEIGHT]):
        if image[row]:
            for column in range(size[WIDTH]):
                if image[row][column]:
                    piece[HEIGHT].append(height + size[HEIGHT] - 1)
                else:
                    break
            piece[WIDTH].append(width + size[WIDTH] - 1)
        else:
            break

    return piece


def set_piece(image, upper_left, piece):
    """
    replaces part of the original image with a smaller image piece matching by color
    :param image: original image as list of lists (height,width)
    :param upper_left: starting position of the upper left corner of the new image piece
    :param piece: the piece that would be placed inside the original image
    """
    height, width = len(piece[HEIGHT]), len(piece[WIDTH])

    for row in range(height):
        if image[row]:
            for column in range(width):
                if image[row][column]:
                    image[upper_left[HEIGHT] + row][upper_left[WIDTH] + column] = piece[HEIGHT][WIDTH]
                else:
                    break
        else:
            break

    logging.warning('SET PIECE!')


def average(image):
    """
    calculates the average each color in the RGB color scheme of the image
    :param image: image to process
    :return: returns a tuple of the average RGB values (red, green, blue)
    """
    red_amount = 0
    green_amount = 0
    blue_amount = 0

    height, width = len(image), len(image[WIDTH])
    resolution = height * width

    for row in range(height):
        if image[row]:
            for column in range(width):
                if image[row][column]:
                    red_amount += image[row][column][RED_INDEX]
                    green_amount += image[row][column][GREEN_INDEX]
                    blue_amount += image[row][column][BLUE_INDEX]
    logging.warning('GOT AVERAGE')
    return red_amount / resolution, green_amount / resolution, blue_amount / resolution


def preprocess_tiles(tiles):
    """
    converts list of tiles (images) into a list containing tuple of their RGB value averages
    :param tiles: list of tiles (images)
    :return: list of tuples in (red, green, blue) format
    """
    logging.warning('PROCESSED TILES')
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
                deviation = compare_pixel(original_average, tiles[i])

                if deviation < init_deviation:
                    candidate_tiles.append(tiles[i])

    return candidate_tiles


def choose_tile(piece, tiles):
    return min([compare(tile, piece) for tile in tiles])


def make_mosaic(image, tiles, num_candidates):
    height_tile, width_tile = len(tiles[HEIGHT]), len(tiles[WIDTH])
    height_image, width_image = len(image[HEIGHT]), len(image[WIDTH])
    last_position = [0, 0]
    mosaic = image
    best_tiles = get_best_tiles(image, tiles, preprocess_tiles(tiles), num_candidates)

    for row in range(int(height_image / height_tile)):
        for column in range(int(width_image / width_tile)):
            best_tile = choose_tile(get_piece(image, last_position, [height_tile, width_tile]), best_tiles)
            set_piece(mosaic, last_position, best_tile)
            last_position += height_tile, width_tile
    logging.warning('CHOSE TILE')
    return mosaic


def main(args):
    source_image = args[1]
    source_tiles = args[2]
    output_image = args[3]
    tile_height = int(args[4])
    num_candidates = int(args[5])
    save(make_mosaic(load_image(source_image), build_tile_base(source_tiles, tile_height), num_candidates), output_image)


if __name__ == '__main__':
    main(sys.argv)
