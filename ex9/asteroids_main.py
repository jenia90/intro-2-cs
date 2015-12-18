import sys
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from math import cos, sin
from random import \
    randint  # Add this to README: https://docs.python.org/3/library/random.html

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    X, Y = 0, 1
    INIT_SHIP_POS, INIT_SHIP_VELOCITY = (-100, 0), (1, 0)
    VELOCITY_MAX, VELOCITY_MIN = 5, 1
    ROTATE_LEFT, ROTATE_RIGHT = 7, -7
    HIT_TITLE, HIT_MSG = 'Uh-oh', 'You got hit by an asteroid!'

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max = Screen.SCREEN_MAX_X, Screen.SCREEN_MAX_Y
        self.screen_min = Screen.SCREEN_MIN_X, Screen.SCREEN_MIN_Y

        self.screen_dist = self.screen_max[self.X] - self.screen_min[self.X], \
                           self.screen_max[self.Y] - self.screen_min[self.Y]

        self.ship = Ship(self.INIT_SHIP_POS, self.INIT_SHIP_VELOCITY)

        self.asteroids = []

        for i in range(asteroids_amnt):
            asteroid_pos = randint(self.screen_min[self.X],
                                   self.screen_max[self.X]), \
                           randint(self.screen_min[self.Y],
                                   self.screen_max[self.Y]),

            # Asteroid's position shouldn't be the same as the ship's
            while asteroid_pos == self.INIT_SHIP_POS:
                asteroid_pos = randint(self.screen_min[self.X],
                                       self.screen_max[self.X]), \
                               randint(self.screen_min[self.Y],
                                       self.screen_max[self.Y])

            asteroid_vel = randint(self.VELOCITY_MIN, self.VELOCITY_MAX), \
                           randint(self.VELOCITY_MIN, self.VELOCITY_MAX)

            asteroid = Asteroid(asteroid_pos, asteroid_vel)
            self._screen.register_asteroid(asteroid, Asteroid.INIT_SIZE)
            self.asteroids.append(asteroid)

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
        ship_x, ship_y = self.ship.get_position()
        self._screen.draw_ship(ship_x, ship_y, self.ship.get_heading())

        # Move ship
        self.ship.set_position(self.get_new_coords(self.ship.get_velocity(),
                                                   (ship_x, ship_y)))

        # Rotate ship
        if self._screen.is_left_pressed():
            self.ship.set_heading(self.ship.get_heading() + self.ROTATE_LEFT)

        elif self._screen.is_right_pressed():
            self.ship.set_heading(self.ship.get_heading() + self.ROTATE_RIGHT)

        # Accelerate ship
        elif self._screen.is_up_pressed():
            vel_x, vel_y = self.ship.get_velocity()
            heading_rad = self.ship.get_heading_in_rad()
            self.ship.set_velocity((vel_x + cos(heading_rad),
                                    vel_y + sin(heading_rad)))

        for asteroid in self.asteroids:
            ast_x, ast_y = asteroid.get_position()
            self._screen.draw_asteroid(asteroid, ast_x, ast_y)

            # Move asteroid
            asteroid.set_position(self.get_new_coords(asteroid.get_velocity(),
                                                      (ast_x, ast_y)))

            if asteroid.has_intersection(self.ship):
                self._screen.remove_life()
                self._screen.show_message(self.HIT_TITLE, self.HIT_MSG)
                self._screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
