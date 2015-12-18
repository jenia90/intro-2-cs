from screen import Screen
import sys

DEFAULT_ASTEROIDS_NUM = 5


class GameRunner:
    X = 0
    Y = 1

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max = Screen.SCREEN_MAX_X, Screen.SCREEN_MAX_Y
        self.screen_min = Screen.SCREEN_MIN_X, Screen.SCREEN_MIN_Y

        self.screen_dist = self.screen_max[self.X] - self.screen_min[self.X], \
                           self.screen_max[self.Y] - self.screen_min[self.Y]

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop, 5)

    def get_new_coord_on_axis(self, axis, speed, old_coord):
        """
        Calculates the new coordinate of a ship, asteroid or torpedo
        :param axis: The axis on which the calculation will be based (X or Y)
        :type axis: int
        :param speed: Speed on the desired axis
        :type speed: float
        :param old_coord: Old coordinate on the desired axis
        :type old_coord: int
        :return: The new coordinate
        """
        min_coord = self.screen_min[axis]

        return (speed + old_coord - min_coord) % \
               self.screen_dist[axis] + min_coord

    def _game_loop(self):
        '''
        Your code goes here!
        '''
        pass


def main(amnt):
    runner = GameRunner(amnt)
    runner.run()


if __name__ == "__main__":
    if len(sys.argv) > 1:
        main(int(sys.argv[1]))
    else:
        main(DEFAULT_ASTEROIDS_NUM)
