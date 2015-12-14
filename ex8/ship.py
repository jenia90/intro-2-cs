import ship_helper as SH

############################################################
# Helper class
############################################################


class Direction:
    """
    Class representing a direction in 2D world.
    You may not change the name of any of the constants (UP, DOWN, LEFT, RIGHT,
     NOT_MOVING, VERTICAL, HORIZONTAL, ALL_DIRECTIONS), but all other
     implementations are for you to carry out.
    """
    UP = (0, 1)  # Choose your own value
    DOWN = (0, -1)  # Choose your own value
    LEFT = (-1, 0)  # Choose your own value
    RIGHT = (1, 0)  # Choose your own value

    NOT_MOVING = (0, 0)  # Choose your own value

    VERTICAL = (UP, DOWN)
    HORIZONTAL = (LEFT, RIGHT)

    ALL_DIRECTIONS = (UP, DOWN, LEFT, RIGHT)

############################################################
# Class definition
############################################################


class Ship:
    """
    A class representing a ship in Battleship game.
    A ship is 1-dimensional object that could be laid in either horizontal or
    vertical alignment. A ship sails on its vertical\horizontal axis back and
    forth until reaching the board's boarders and then changes its direction to
    the opposite (left <--> right, up <--> down).
    If a ship is hit in one of its coordinates, it ceases its movement in all
    future turns.
    A ship that had all her coordinates hit is considered terminated.
    """
    X_AXIS = 0
    Y_AXIS = 1

    def __init__(self, pos, length, direction, board_size):
        """
        A constructor for a Ship object
        :param pos: A tuple representing The ship's head's (x, y) position
        :param length: Ship's length
        :param direction: Initial direction in which the ship is sailing
        :param board_size: Board size in which the ship is sailing
        """
        self.pos = pos
        self.length = length
        self.init_direction = direction
        self.board_size = board_size
        self.hits = []

    def __repr__(self):
        """
        Return a string representation of the ship.
        :return: A tuple converted to string. The tuple's content should be (in
        the exact following order):
            1. A list of all the ship's coordinates.
            2. A list of all the ship's hit coordinates.
            3. Last sailing direction.
            4. The size of the board in which the ship is located.
        """
        return str(self.coordinates()) + \
            str(self.damaged_cells()) + \
            SH.direction_repr_str(Direction, self.direction()) + \
            str(self.board_size)

    def move(self):
        """
        Make the ship move one board unit.
        Movement is in the current sailing direction, unless such movement would
        take it outside of the board in which case the shp switches direction
        and sails one board unit in the new direction.
        the ship
        :return: A direction object representing the current movement direction.
        """
        direct_x, direct_y = self.init_direction
        max_coordinate = max(self.coordinates())

        if len(self.damaged_cells()) == 0:
            if self.board_size == max(max_coordinate):
                if self.direction() == Direction.HORIZONTAL:
                    self.init_direction = (direct_x * -1, direct_y)
                elif self.direction() == Direction.VERTICAL:
                    self.init_direction = (direct_x, direct_y * -1)
                    
                self.pos = self.coordinates()[self.length]

            return self.direction()

        else:
            return Direction.NOT_MOVING

    def hit(self, pos):
        """
        Inform the ship that a bomb hit a specific coordinate. The ship updates
         its state accordingly.
        If one of the ship's body's coordinate is hit, the ship does not move
         in future turns. If all ship's body's coordinate are hit, the ship is
         terminated and removed from the board.
        :param pos: A tuple representing the (x, y) position of the hit.
        :return: True if the bomb generated a new hit in the ship, False
         otherwise.
        """
        if pos in self.coordinates() and pos not in self.damaged_cells():
            self.hits.append(pos)  # appends the hit position to the hits list
            return True  # returns True for confirmed hit

        else:
            return False  # returns False if missed

    def terminated(self):
        """
        :return: True if all ship's coordinates were hit in previous turns, False
        otherwise.
        """
        return len(self.coordinates()) == len(self.damaged_cells())

    def __contains__(self, pos):
        """
        Check whether the ship is found in a specific coordinate.
        :param pos: A tuple representing the coordinate for check.
        :return: True if one of the ship's coordinates is found in the given
        (x, y) coordinates, False otherwise.
        """
        return True if pos in self.coordinates() else False

    def coordinates(self):
        """
        Return ship's current positions on board.
        :return: A list of (x, y) tuples representing the ship's current
        position.
        """
        return [(abs(self.pos[self.X_AXIS] + self.direction()[self.X_AXIS] * i),
                 abs(self.pos[self.Y_AXIS] + self.direction()[self.Y_AXIS] * i))
                for i in range(self.length)]

    def damaged_cells(self):
        """
        Return the ship's hit positions.
        :return: A list of tuples representing the (x, y) coordinates of the
         ship which were hit in past turns (If there are no hit coordinates,
         return an empty list). There is no importance to the order of the
         values in the returned list.
        """
        return self.hits

    def direction(self):
        """
        Return the ship's current sailing direction.
        :return: One of the constants of Direction class :
         [UP, DOWN, LEFT, RIGHT] according to current
         sailing direction or NOT_MOVING if the ship is hit and not moving.
        """
        if self.init_direction == Direction.LEFT:
            return Direction.LEFT

        elif self.init_direction == Direction.RIGHT:
            return Direction.RIGHT

        elif self.init_direction == Direction.UP:
            return Direction.UP

        elif self.init_direction == Direction.DOWN:
            return Direction.DOWN
        else:
            return Direction.NOT_MOVING

    def cell_status(self, pos):
        """
        Return the state of the given coordinate (hit\not hit)
        :param pos: A tuple representing the coordinate to query.
        :return:
            if the given coordinate is not hit : False
            if the given coordinate is hit : True
            if the coordinate is not part of the ship's body : None 
        """
        if pos not in self.coordinates():
            return None

        return True if pos in self.damaged_cells() else False
