import math
import sys

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
    height, width = image1.size

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
    height, width = image.size

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
    height, width = piece.size

    for row in range(height):
        if image[row]:
            for column in range(width):
                if image[row][column]:
                    image[upper_left[HEIGHT] + row][upper_left[WIDTH] + column] = piece[HEIGHT, WIDTH]
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

    height, width = image.size
    resolution =  height * width

    for row in range(height):
        for column in range(width):
            red_amount += image[row, column][RED_INDEX]
            green_amount += image[row, column][GREEN_INDEX]
            blue_amount += image[row, column][BLUE_INDEX]

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
    deviation = [0, 0, 0]
    original_average = average(objective)

    while len(candidate_tiles) < num_candidates:
        for i in range(len(averages)):
            if [int(original_average[color] - averages[i][color]) for color in range(3)] == deviation:
                candidate_tiles.append(tiles[i])

        deviation = [value + 1 for value in deviation]

    return candidate_tiles


def choose_tile(piece, tiles):
    return min([compare(tile, piece) for tile in tiles])


def make_mosaic(image, tiles, num_candidates):
    height_tile, width_tile = tiles[0].size
    height_image, width_image = image.size
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
    with open(args[3], 'w') as file:
        file = make_mosaic(args[1], args[2], int(args[4]))


if __name__ == '__main__':
    main(sys.argv)
