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
        return self.position

    def get_velocity(self):
        return self.velocity

    def get_heading(self):
        return self.heading

    def set_position(self, position):
        self.position = position

    def accelerate(self):
        vel_x, vel_y = self.velocity
        heading_rad = self.heading * self.DEG_TO_RAD
        self.velocity = vel_x + cos(heading_rad), vel_y + sin(heading_rad)

    def set_heading(self, heading):
        self.heading = heading
