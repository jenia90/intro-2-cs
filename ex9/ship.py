###############################################################################
# FILE: ship.py                                                               #
# WRITERS: Yevgeni Dysin, jenia90, 320884216; Ben Faingold, ben_f, 208482604  #
# EXERCISE: intro2cs ex9 2015-2016                                            #
# DESCRIPTION: Contains the Ship object class implementation                  #
###############################################################################
from math import pi, cos, sin


class Ship:
    """
    Ship object class definition
    """
    INIT_HEADING = 0  # Parallel to the X axis
    DEG_TO_RAD = pi / 180
    RADIUS = 1

    def __init__(self, position, velocity):
        """
        Initializes a Ship object
        :param position: Init position
        :type position: 2D integers tuple
        :param velocity: Init velocity
        :type velocity: 2D integers tuple
        """
        self.position = position
        self.velocity = velocity
        self.heading = self.INIT_HEADING

    def get_position(self):
        """
        Gets the position of the Ship object
        :return: tuple containing (x, y) coordinates of the ship
        """
        return self.position

    def get_velocity(self):
        """
        Gets the velocity of the Ship object
        :return: tuple containing the speed on each axis (x, y)
        """
        return self.velocity

    def get_heading(self):
        """
        Gets the heading (angle) of the Ship object
        :return: int of ship heading angle
        """
        return self.heading

    def set_position(self, position):
        """
        Sets ship's position
        :param position: tuple containing the (x, y) coordinates of the ship
        """
        self.position = position

    def accelerate(self):
        """
        Accelerates the ship (updates it's velocity)
        """
        vel_x, vel_y = self.velocity
        heading_rad = self.heading * self.DEG_TO_RAD
        self.velocity = vel_x + cos(heading_rad), vel_y + sin(heading_rad)

    def set_heading(self, heading):
        """
        Sets ship's heading (angle to the X axis)
        :param heading: angle in degrees (int)
        """
        self.heading = heading
