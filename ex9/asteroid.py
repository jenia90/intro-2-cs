from math import sqrt


class Asteroid:
    """
    Asteroid object class definition
    """
    INIT_SIZE = 3
    SIZE_COEFFICIENT = 10
    NORMAL_FACTOR = -5

    def __init__(self, position, velocity, size=INIT_SIZE):
        """
        Constructor for asteroid class
        :param position: position as coordinates tuple (x, y)
        :param velocity: velocity as coordinates tuple (x, y)
        :param size: size of the rock (int)
        """
        self.position = position
        self.velocity = velocity
        self.size = size

        self.radius = self.size * self.SIZE_COEFFICIENT + self.NORMAL_FACTOR

    def has_intersection(self, obj):
        """
        Checks if our asteroid has intersection with another object
        :param obj: the object that might intersect
        :return: True if distance smaller or equal to sum of radiuses else False
        """
        obj_x, obj_y = obj.get_position()
        pos_x, pos_y = self.position

        # calculates the distance between the asteroid and the other object
        distance = sqrt((obj_x - pos_x) ** 2 + (obj_y - pos_y) ** 2)

        return distance <= self.radius + obj.RADIUS

    def get_size(self):
        """
        Gets the size of an asteroid
        :return: Size of the asteroid as int between 1-3
        """
        return self.size

    def get_position(self):
        """
        Gets the current position of an asteroid
        :return: a tuple of its (x, y) coordinate
        """
        return self.position

    def set_position(self, position):
        """
        Sets the position of the asteroid
        :param position: position as (x, y) tuple
        """
        self.position = position

    def get_velocity(self):
        """
        Gets the current velocity of the asteroid
        :return: (speed_x, speed_y) tuple
        """
        return self.velocity

