from math import pi


class Ship:
    """
    Ship object class definition
    """
    INIT_HEADING = 0  # Parallel to the X axis
    DEG_TO_RAD = pi / 180

    def __init__(self, pos, vel):
        """
        Initializes a Ship object
        :param pos: Init position
        :type pos: 2D integers tuple
        :param vel: Init velocity
        :type vel: 2D integers tuple
        """
        self.pos = pos
        self.vel = vel
        self.heading = self.INIT_HEADING

    def get_position(self):
        return self.pos

    def get_velocity(self):
        return self.vel

    def get_heading(self):
        return self.heading

    def get_heading_in_rad(self):
        return self.heading * self.DEG_TO_RAD

    def set_position(self, pos):
        self.pos = pos

    def set_velocity(self, vel):
        self.vel = vel

    def set_heading(self, heading):
        self.heading = heading
