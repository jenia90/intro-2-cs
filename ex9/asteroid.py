import math

class Asteroid:
    """
    Asteroid object class definition
    """
    NORMAL_FACTOR = -5
    SIZE_COEFFICIENT = 10

    def __init__(self, position, velocity, size):
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
        Chekcs if our asteroid has intersection with another object
        :param obj: the object that might intersect
        :return:
        """
        obj_x, obj_y = obj
        pos_x, pos_y = self.position
        distance = math.sqrt((obj_x - pos_x) ** 2 + (obj_y - pos_y) ** 2)

        return True if distance <= (self.radius + obj.radius) else False

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

    def get_velocity(self):
        """
        Gets the current velocity of the asteroid
        :return: (speed_x, speed_y) tuple
        """
        return self.velocity

    def get_radius(self):
        """
        Gets the radius of an asteroid
        :return: asteroid radius as int
        """
        return self.radius


