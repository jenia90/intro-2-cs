import sys
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from operator import add
from math import sqrt
from random import randint  # Add this to README: https://docs.python.org/3/library/random.html

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    HIT_TITLE, HIT_MSG = "Uh-oh", "You got hit by an asteroid!"
    WON_TITLE, WON_MSG = "The force is strong with you!", \
                         "Congrats! you've won, exiting now."
    LOST_TITLE, LOST_MSG = "Better luck next time!", \
                           "You've lost, exiting now."
    QUIT_TITLE, QUIT_MSG = "Afraid of space?", \
                           "You've decided to cowardly quit, exiting now."
    X, Y = 0, 1
    INIT_SHIP_POS, INIT_SHIP_VELOCITY = (-100, 0), (1, 0)
    VELOCITY_MAX, VELOCITY_MIN = 5, 1
    ROTATE_LEFT, ROTATE_RIGHT = 7, -7
    TORPEDO_LIFESPAN = 200
    MAX_TORPEDOS_AT_ONCE = 15
    SCORE_OPTIONS = 100, 50, 20  # Depends on the size of the hit asteroid
    MAX_SHIP_LIVES = 3

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

        self.score = 0
        self.torpedo_lives = []
        self.torpedo_count = 0
        self.torpedos = []
        self.ship_lives = self.MAX_SHIP_LIVES

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def get_new_coords(self, velocity, old_coords):
        """
        Calculates the new coordinates of a ship, asteroid or torpedo
        :param velocity: Velocity of the object
        :type velocity: 2D floats tuple
        :param old_coords: Old coordinates of the object
        :type old_coords: 2D integers tuple
        :return: The new coordinates
        """
        min_coord_x, min_coord_y = self.screen_min

        return ((velocity[self.X] + old_coords[self.X] - min_coord_x) %
                self.screen_dist[self.X] + min_coord_x,
                (velocity[self.Y] + old_coords[self.Y] - min_coord_y) %
                self.screen_dist[self.Y] + min_coord_y)

    def exit_game(self, title, msg):
        """
        Exits the game with an alert message
        :param title: The message's title
        :param msg: A message
        """
        self._screen.show_message(title, msg)
        self._screen.end_game()
        sys.exit()

    def _game_loop(self):
        ship_x, ship_y = self.ship.get_position()
        self._screen.draw_ship(ship_x, ship_y, self.ship.get_heading())
        ship_vel = self.ship.get_velocity()

        # Move ship
        self.ship.set_position(self.get_new_coords(ship_vel, (ship_x, ship_y)))

        # Rotate ship to the left
        if self._screen.is_left_pressed():
            self.ship.set_heading(self.ship.get_heading() + self.ROTATE_LEFT)

        # Rotate ship to the right
        if self._screen.is_right_pressed():
            self.ship.set_heading(self.ship.get_heading() + self.ROTATE_RIGHT)

        # Accelerate ship
        if self._screen.is_up_pressed():
            self.ship.accelerate()

        # Fire torpedo
        elif self._screen.is_space_pressed():
            if self.torpedo_count != self.MAX_TORPEDOS_AT_ONCE:
                torpedo = Torpedo((ship_x, ship_y), ship_vel,
                                  self.ship.get_heading())
                self._screen.register_torpedo(torpedo)
                self.torpedo_lives.append(self.TORPEDO_LIFESPAN)
                self.torpedo_count += 1
                self.torpedos.append(torpedo)

        for asteroid in self.asteroids:
            ast_x, ast_y = asteroid.get_position()
            self._screen.draw_asteroid(asteroid, ast_x, ast_y)
            ast_vel = asteroid.get_velocity()

            # Move asteroid
            asteroid.set_position(self.get_new_coords(ast_vel, (ast_x, ast_y)))

            # From here till the end of the loop, the code handles
            # intersections (if any) of the asteroid with the ship or with a
            # torpedo
            if asteroid.has_intersection(self.ship):
                self._screen.remove_life()
                self.ship_lives -= 1
                self._screen.show_message(self.HIT_TITLE, self.HIT_MSG)
                self._screen.unregister_asteroid(asteroid)
                self.asteroids.remove(asteroid)

            ast_size = asteroid.get_size()

            for torpedo in self.torpedos:
                if asteroid.has_intersection(torpedo):
                    for i in range(len(self.SCORE_OPTIONS)):
                        if ast_size == i + 1:
                            self.score += self.SCORE_OPTIONS[i]
                            self._screen.set_score(self.score)

                        if i != 0:
                            # Split the asteroid into 2 smaller asteroids
                            # Calculate new velocity
                            den = sqrt(ast_vel[self.X] ** 2 +
                                       ast_vel[self.Y] ** 2)
                            nom = map(add, ast_vel, torpedo.get_velocity())
                            new_vel = tuple(v / den for v in nom)
                            # Create new asteroids
                            ast_1 = Asteroid((ast_x, ast_y), new_vel, i)
                            self._screen.register_asteroid(ast_1, i)
                            self.asteroids.append(ast_1)
                            # Second asteroid with the opposing velocity
                            ast_2 = Asteroid((ast_x, ast_y),
                                             tuple(v * -1 for v in new_vel), i)
                            self._screen.register_asteroid(ast_2, i)
                            self.asteroids.append(ast_2)

                        else:
                            # Remove smallest asteroid
                            self._screen.unregister_asteroid(asteroid)
                            self.asteroids.remove(asteroid)

                    self._screen.unregister_torpedo(torpedo)
                    del self.torpedo_lives[self.torpedos.index(torpedo)]
                    self.torpedo_count -= 1
                    self.torpedos.remove(torpedo)

        for torpedo in self.torpedos:
            torp_x, torp_y = torpedo.get_position()
            self._screen.draw_torpedo(torpedo, torp_x, torp_y,
                                      torpedo.get_heading())

            # Move torpedo
            torpedo.set_position(self.get_new_coords(torpedo.get_velocity(),
                                                     (torp_x, torp_y)))

            # Decrease lifespan of the torpedo
            torp_index = self.torpedos.index(torpedo)
            self.torpedo_lives[torp_index] -= 1

            if self.torpedo_lives[torp_index] == 0:
                self._screen.unregister_torpedo(torpedo)
                del self.torpedo_lives[torp_index]
                self.torpedo_count -= 1
                self.torpedos.remove(torpedo)

        if not self.asteroids:
            self.exit_game(self.WON_TITLE, self.WON_MSG)

        if self.ship_lives == 0:
            self.exit_game(self.LOST_TITLE, self.LOST_MSG)

        if self._screen.should_end():
            self.exit_game(self.QUIT_TITLE, self.QUIT_MSG)


def main(amnt):
    """
    Runs the game
    :param amnt: The desired amount of asteroids
    :return:
    """
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
