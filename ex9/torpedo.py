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
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_heading(self):
        return self.heading

    def set_position(self, position):
        self.position = position
