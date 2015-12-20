###############################################################################
# FILE: asteroids_main.py                                                     #
# WRITERS: Yevgeni Dysin, jenia90, 320884216; Ben Faingold, ben_f, 208482604  #
# EXERCISE: intro2cs ex9 2015-2016                                            #
# DESCRIPTION: Contains the main game logic                                   #
###############################################################################
import sys
from screen import Screen
from ship import Ship
from asteroid import Asteroid
from torpedo import Torpedo
from operator import add
from math import sqrt
from random import randint

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
    INIT_SHIP_VELOCITY = (1, 0)
    ROTATE_LEFT, ROTATE_RIGHT = 7, -7
    AST_VEL_MAX, AST_VEL_MIN = 5, 1
    INIT_AST_SIZE = 3
    TORPEDO_LIFESPAN = 200
    MAX_TORPEDOS_AT_ONCE = 15
    SCORE_OPTIONS = 100, 50, 20  # (Index + 1) is the size of the hit asteroid
    MAX_SHIP_LIVES = 3

    def __init__(self, asteroids_amnt):
        """
        Initializes the GameRunner class and all the game related parameters
        :param asteroids_amnt: int representing the amount of asteroids
        """
        self._screen = Screen()
        self.screen_max = Screen.SCREEN_MAX_X, Screen.SCREEN_MAX_Y
        self.screen_min = Screen.SCREEN_MIN_X, Screen.SCREEN_MIN_Y
        self.screen_dist = self.screen_max[self.X] - self.screen_min[self.X], \
                           self.screen_max[self.Y] - self.screen_min[self.Y]

        self.ship = Ship(self.get_random_position(), self.INIT_SHIP_VELOCITY)
        self.asteroids = []

        # This section of code creates a list of asteroid objects with random
        # location and velocity parameters
        for i in range(asteroids_amnt):
            # Generates random values for asteroid object location
            asteroid_pos = self.get_random_position()

            # Asteroid's position shouldn't be the same as the ship's
            while asteroid_pos == self.ship.get_position():
                asteroid_pos = self.get_random_position()

            # Generates random values for asteroid object speed on x and y axis
            asteroid_vel = randint(self.AST_VEL_MIN, self.AST_VEL_MAX), \
                           randint(self.AST_VEL_MIN, self.AST_VEL_MAX)

            self.add_asteroid(asteroid_pos, asteroid_vel, self.INIT_AST_SIZE)

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

    def get_random_position(self):
        """
        Generates random position based on screen's limits
        :return: Random position
        """
        return randint(self.screen_min[self.X], self.screen_max[self.X]), \
               randint(self.screen_min[self.Y], self.screen_max[self.Y])

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

    def add_asteroid(self, position, velocity, size):
        """
        Does all operations needed to add an asteroid
        :param position: position as coordinates tuple (x, y)
        :param velocity: velocity as coordinates tuple (x, y)
        :param size: size of the rock (int)
        """
        asteroid = Asteroid(position, velocity, size)
        self._screen.register_asteroid(asteroid, size)
        self.asteroids.append(asteroid)

    def remove_asteroid(self, asteroid):
        """
        Does all operations needed to remove an asteroid
        :param asteroid: Asteroid object instance about to be removed
        """
        self._screen.unregister_asteroid(asteroid)
        self.asteroids.remove(asteroid)

    def remove_torpedo(self, torpedo_index, torpedo):
        """
        Does all operations needed to remove a torpedo
        :param torpedo_index: Torpedo's index from every relevant list
        :type torpedo_index: int
        :param torpedo: Torpedo object instance about to be removed
        """
        self._screen.unregister_torpedo(torpedo)
        del self.torpedo_lives[torpedo_index]
        self.torpedo_count -= 1
        self.torpedos.remove(torpedo)

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
        """
        Main game logic method
        """
        ship_pos = self.ship.get_position()
        self._screen.draw_ship(ship_pos[self.X], ship_pos[self.Y],
                               self.ship.get_heading())
        ship_vel = self.ship.get_velocity()

        # Move ship
        self.ship.set_position(self.get_new_coords(ship_vel, ship_pos))

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
        if self._screen.is_space_pressed():
            if self.torpedo_count != self.MAX_TORPEDOS_AT_ONCE:
                torpedo = Torpedo(ship_pos, ship_vel, self.ship.get_heading())
                self._screen.register_torpedo(torpedo)
                self.torpedo_lives.append(self.TORPEDO_LIFESPAN)
                self.torpedo_count += 1
                self.torpedos.append(torpedo)

        # This section of code handles each asteroid objects parameter updates
        for asteroid in self.asteroids:
            ast_pos = asteroid.get_position()
            self._screen.draw_asteroid(asteroid,
                                       ast_pos[self.X], ast_pos[self.Y])
            ast_vel = asteroid.get_velocity()

            # Move asteroid
            asteroid.set_position(self.get_new_coords(ast_vel, ast_pos))

            # From here till the end of the loop, the code handles
            # intersections (if any) of the asteroid with the ship or with a
            # torpedo
            if asteroid.has_intersection(self.ship):
                self._screen.remove_life()
                self.ship_lives -= 1
                self._screen.show_message(self.HIT_TITLE, self.HIT_MSG)
                self.remove_asteroid(asteroid)
                continue

            ast_size = asteroid.get_size()

            for torpedo in self.torpedos:
                if asteroid.has_intersection(torpedo):
                    i = ast_size - 1  # Score option's index
                    self.score += self.SCORE_OPTIONS[i]
                    self._screen.set_score(self.score)
                    # Split the asteroid into 2 smaller ones
                    # Remove original asteroid
                    self.remove_asteroid(asteroid)
                    # Removes the torpedo after it hit the asteroid
                    self.remove_torpedo(self.torpedos.index(torpedo), torpedo)

                    if i == 0:
                        # Iteration can be terminated if the removed
                        # asteroid had the smallest size
                        break

                    # Calculate new velocity
                    nom = map(add, ast_vel, torpedo.get_velocity())
                    den = sqrt(ast_vel[self.X] ** 2 + ast_vel[self.Y] ** 2)
                    # Nominator / Denominator
                    n_vel = tuple(v / den for v in nom)
                    # Create new asteroids
                    self.add_asteroid(ast_pos, n_vel, i)
                    # Second asteroid with the opposing velocity
                    self.add_asteroid(ast_pos, tuple(v * -1 for v in n_vel), i)

        # This section of code updates torpedos parameters
        for torpedo in self.torpedos:
            t_pos = torpedo.get_position()
            self._screen.draw_torpedo(torpedo, t_pos[self.X], t_pos[self.Y],
                                      torpedo.get_heading())

            # Move torpedo
            torpedo.set_position(self.get_new_coords(torpedo.get_velocity(),
                                                     t_pos))

            # Decrease lifespan of the torpedo
            torp_index = self.torpedos.index(torpedo)
            self.torpedo_lives[torp_index] -= 1

            # Remove torpedo after its lifespan is depleted
            if self.torpedo_lives[torp_index] == 0:
                self.remove_torpedo(torp_index, torpedo)

        # Exit game and show win message when all asteroids are destroyed
        if not self.asteroids:
            self.exit_game(self.WON_TITLE, self.WON_MSG)

        # Exit game and show loss message when ship is out of lives
        if self.ship_lives == 0:
            self.exit_game(self.LOST_TITLE, self.LOST_MSG)

        # Exit game on request
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
