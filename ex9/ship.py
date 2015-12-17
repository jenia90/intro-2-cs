INIT_HEADING = 0  # Parallel to the X axis


class Ship:
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
        self.heading = INIT_HEADING
