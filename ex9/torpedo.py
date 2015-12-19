###############################################################################
# FILE: torpedo.py                                                            #
# WRITERS: Yevgeni Dysin, jenia90, 320884216; Ben Faingold, ben_f, 208482604  #
# EXERCISE: intro2cs ex9 2015-2016                                            #
# DESCRIPTION: Contains the Torpedo object class implementation               #
###############################################################################
from math import pi, cos, sin


class Torpedo:
    """
    Torpedo object class definition
    """
    DEG_TO_RAD = pi / 180
    THRUST_COEFFICIENT = 2
    RADIUS = 4

    def __init__(self, position, ship_velocity, heading):
        """
        Initializes a Torpedo object
        :param position: Init position
        :type position: 2D integers tuple
        :param ship_velocity: Ship's velocity which will be used to calculate
                              the torpedo's velocity
        :type ship_velocity: 2D integers tuple
        :param heading: Init heading in degrees
        :type heading: float
        """
        self.position = position

        s_vel_x, s_vel_y = ship_velocity
        heading_rad = heading * self.DEG_TO_RAD
        self.velocity = s_vel_x + self.THRUST_COEFFICIENT * cos(heading_rad), \
                        s_vel_y + self.THRUST_COEFFICIENT * sin(heading_rad)

        self.heading = heading

    def get_position(self):
        """
        Gets torpedo's position
        :return: tuple containing (x, y) position coordinates
        """
        return self.position

    def get_velocity(self):
        """
        Gets torpedo's velocity
        :return: tuple containing the velocity on each axis (x, y)
        """
        return self.velocity

    def get_heading(self):
        """
        Gets torpedo's heading
        :return: int representing the angle to X axis (in degrees)
        """
        return self.heading

    def set_position(self, position):
        """
        Sets torpedo's position
        :param position: tuple containing the (x, y) coordinates
        """
        self.position = position
