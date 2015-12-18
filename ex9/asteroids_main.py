from screen import Screen
import sys
from ship import Ship
from math import cos, sin

DEFAULT_ASTEROIDS_NUM = 5
ROTATE_LEFT, ROTATE_RIGHT = 7, -7


class GameRunner:
    X = 0
    Y = 1

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max = Screen.SCREEN_MAX_X, Screen.SCREEN_MAX_Y
        self.screen_min = Screen.SCREEN_MIN_X, Screen.SCREEN_MIN_Y

        self.screen_dist = self.screen_max[self.X] - self.screen_min[self.X], \
                           self.screen_max[self.Y] - self.screen_min[self.Y]

        self.ship = Ship((0, 0), (0, 0.5))

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def get_new_coords(self, velocity, old_coord):
        """
        Calculates the new coordinate of a ship, asteroid or torpedo
        :param velocity: Velocity of the object
        :type velocity: 2D floats tuple
        :param old_coord: Old coordinate of the object
        :type old_coord: 2D integers tuple
        :return: The new coordinates
        """
        min_coord_x, min_coord_y = self.screen_min

        return ((velocity[self.X] + old_coord[self.X] - min_coord_x) %
                self.screen_dist[self.X] + min_coord_x,
                (velocity[self.Y] + old_coord[self.Y] - min_coord_y) %
                self.screen_dist[self.Y] + min_coord_y)

    def _game_loop(self):
        pos_x, pos_y = self.ship.get_position()
        self._screen.draw_ship(pos_x, pos_y, self.ship.get_heading())

        # Move ship
        self.ship.set_position(self.get_new_coords(self.ship.get_velocity(),
                                                   (pos_x, pos_y)))

        # Rotate ship
        if self._screen.is_left_pressed():
            self.ship.set_heading(self.ship.get_heading() + ROTATE_LEFT)

        elif self._screen.is_right_pressed():
            self.ship.set_heading(self.ship.get_heading() + ROTATE_RIGHT)

        # Accelerate ship
        elif self._screen.is_up_pressed():
            vel_x, vel_y = self.ship.get_velocity()
            heading_rad = self.ship.get_heading_in_rad()
            self.ship.set_velocity((vel_x + cos(heading_rad),
                                    vel_y + sin(heading_rad)))


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
