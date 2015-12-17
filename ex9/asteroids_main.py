from screen import Screen
import sys

DEFAULT_ASTEROIDS_NUM = 5

class GameRunner:

    def __init__(self, asteroids_amnt):
        self._screen = Screen()

        self.screen_max_x = Screen.SCREEN_MAX_X
        self.screen_max_y = Screen.SCREEN_MAX_Y
        self.screen_min_x = Screen.SCREEN_MIN_X
        self.screen_min_y = Screen.SCREEN_MIN_Y

    def run(self):
        self._do_loop()
        self._screen.start_screen()

    def _do_loop(self):
        # You don't need to change this method!
        self._game_loop()

        # Set the timer to go off again
        self._screen.update()
        self._screen.ontimer(self._do_loop,5)

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
        main( int( sys.argv[1] ) )
    else:
        main( DEFAULT_ASTEROIDS_NUM )
