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
        self.ships = ships
        self.bombs = dict()
        self.hits = []
        self.hit_ships = []

    def hit_confiramation(self, pos, ship):
        """
        Checks if a bomb in the given location hit any of the ships
        :param pos: coordinates (x,y) of a bomb
        :param ship: current ship
        :return: True if confirmed hit and False if not
        """
        pass # TODO: finish implementation


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
        intact_ships = []
        round_hits = 0
        round_terminations = 0

        usr_inpt = gh.get_target(self.board_size)

        self.bombs[usr_inpt] = 4

        for ship in self.ships:
            ship.move()

            for bomb in self.bombs.keys():
                if bomb in ship.coordinates():
                    round_hits += 1
                    ship.hit(bomb)
                    self.hits.append(bomb)
                    for coordinate in ship.coordinates():
                        if coordinate not in self.hit_ships:
                            self.hit_ships.append(coordinate)

                    if ship.terminated():
                        round_terminations += 1
                        self.ships.remove(ship)

        for ship in self.ships:
            if ship not in self.hit_ships:
                for coordinate in ship.coordinates():
                    intact_ships.append(coordinate)

        self.bombs = {bomb: (self.bombs[bomb] - 1)
                      for bomb in self.bombs.keys()
                      if self.bombs[bomb] > 0 and
                      self.bombs[bomb] not in self.hits}

        print(gh.board_to_string(self.board_size,
                                 self.hits,
                                 self.bombs,
                                 self.hit_ships,
                                 intact_ships))
        gh.report_turn(round_hits, round_terminations)

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
        ships_string = ''

        for ship in self.ships:
            ships_string += ship.__repr__()

        return str(self.board_size) + str(self.bombs) + ships_string

    def play(self):
        """
        The main driver of the Game. Manages the game until completion.
        completion.
        :return: None
        """
        gh.report_legend()  # prints game legend

        while len(self.ships) > 0:
            self.__play_one_round()

        gh.report_gameover()

############################################################
# An example usage of the game
############################################################
if __name__=="__main__":
    game = Game(5, gh.initialize_ship_list(4, 2))
    game.play()
