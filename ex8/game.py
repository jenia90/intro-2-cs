############################################################
# Imports
############################################################
import game_helper as gh

############################################################
# Class definition
############################################################


class Game:
    """
    A class representing a battleship game.
    A game is composed of ships that are moving on a square board and a user
    which tries to guess the locations of the ships by guessing their
    coordinates.
    """

    def __init__(self, board_size, ships):
        """
        Initialize a new Game object.
        :param board_size: Length of the side of the game-board
        :param ships: A list of ships that participate in the game.
        :return: A new Game object.
        """
        self.board_size = board_size
        # self.ships = ships  /// PRODUCTION
        self.ships = gh.initialize_ship_list(self.board_size - 1, 3)
        self.bombs = {}
        self.hits = []
        self.hit_ships = []

    def __play_one_round(self):
        """
        Note - this function is here to guide you and it is *not mandatory*
        to implement it. The logic defined by this function must be implemented
        but if you wish to do so in another function (or some other functions)
        it is ok.

        Te function runs one round of the game :
            1. Get user coordinate choice for bombing.
            2. Move all game's ships.
            3. Update all ships and bombs.
            4. Report to the user the result of current round (number of hits and
             terminated ships)
        :return:
            (some constant you may want implement which represents) Game status :
            GAME_STATUS_ONGOING if there are still ships on the board or
            GAME_STATUS_ENDED otherwise.
        """
        usr_inpt = gh.get_target(self.board_size)

        self.bombs[usr_inpt] = 3

        for ship in self.ships:
            ship.move()

            for bomb in self.bombs.keys():
                if bomb in ship.coordinates():
                    ship.hit(bomb)
                    del self.bombs[bomb]
                    self.hits.append(bomb)
                    self.hit_ships.append(ship.pos)
                    if ship.terminated():
                        self.ships.remove(ship)

        for bomb in self.bombs.keys():
            if self.bombs[bomb] <= 0:
                del self.bombs[bomb]
            else:
                self.bombs[bomb] -= 1

        gh.board_to_string(self.board_size,
                           self.hits,
                           self.bombs,
                           self.hit_ships,
                           lambda ships: [ship for ship in self.ships
                                          if ship not in self.hit_ships])
        # TODO: Continue this fucking crappy function implementation!!!! FUUUU

    def __repr__(self):
        """
        Return a string representation of the board's game
        :return: A tuple converted to string. The tuple should contain (maintain
        the following order):
            1. Board's size.
            2. A dictionary of the bombs found on the board
                 {(pos_x, pos_y) : remaining turns}
                For example :
                 {(0, 1) : 2, (3, 2) : 1}
            3. A list of the ships found on the board (each ship should be
                represented by its __repr__ string).
        """
        pass

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        completion.
        :return: None
        """
        print(gh.report_legend())  # prints game legend

        while len(self.ships) > 0:
            self.__play_one_round()

        gh.report_gameover()

############################################################
# An example usage of the game
############################################################
if __name__=="__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
