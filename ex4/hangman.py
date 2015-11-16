#######################################################################
#  FILE: hangman.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex4 2015-2016
#  DESCRIPTION : Simple Hangman game where a user has to guess a word
#
#######################################################################

from hangman_helper import *

UNDERSCORE = '_'
INPUT_TYPE = 0
INPUT_VALUE = 1


def update_word_pattern(word, pattern, letter):
    """
    Updates the given pattern if the user chosen letter matches the original word
    :param word: The random word to guess
    :param pattern: Pattern of the word shown to the user
    :param letter: Guessed letter
    :return: Returns the updated pattern
    """
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + word[i] + pattern[i+1:]  # slices the pattern, replaces the letter and rejoins it.

    return pattern


def match_pattern_to_word(pattern, word):
    """
    Checks if the given word matches the pattern
    :param pattern: pattern as a string
    :param word: word as a string
    :return: returns True if the pattern matches and False if not
    """
    if len(pattern) == len(word):
        for i in range(len(pattern)):
            if pattern[i] != word[i] and pattern[i] != UNDERSCORE:
                return False

    return True


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Filters the word list to give more precise hints to the user
    :param wrong_guess_lst: list of wrong letters the user already tried
    :param words: list of words to filter through
    :param pattern: the word pattern string shown to the user
    :return: returns the filtered word list
    """
    filtered_lst = []

    # loops through word list and appends the relevant to the returned variable
    for word in words:
        if len(pattern) == len(word) and match_pattern_to_word(pattern, word) \
               and not is_in_wrong_guess_list_filter(word, wrong_guess_lst):
            filtered_lst.append(word)

    return filtered_lst


def is_in_wrong_guess_list_filter(word, wrong_guess_lst):
    """
    Checks if a word contains any of the letters in the wrong guess list
    :param word: word to check
    :param wrong_guess_lst: list of wrongly guessed letters
    :return: True if the word contains any of the letters and False if not
    """
    for letter in wrong_guess_lst:
        if letter in word:
            return True

    return False


def choose_letter(words, pattern):
    """
    Matches words to the pattern and chooses a single letter that has most appearances
    :param words: List of words to check
    :param pattern: the secret word pattern
    :return: Returns the single letter to be presented as a hint for the player
    """
    letter_dict = dict()    # creates a dictionary which will hold all the letters

    # this block of code goes through all the words and creates a dictionary of all the letters in them
    for word in words:
        for letter in word:
            if letter not in pattern and len(word) == len(pattern):
                if letter in letter_dict.keys():
                    letter_dict[letter] += 1
                else:
                    letter_dict[letter] = 0

    return find_letter_with_most_occurances(letter_dict)


def find_letter_with_most_occurances(letter_dict):
    """
    Helper function to find the letter that appears the most.
    :param letter_dict: dictionary containing letters as keys and number of their appearances as values
    :return: returns most common letter in the dictionary
    """
    chosen_letter_value = 0  # temporary variable to hold the maximum amount of times a letter appears
    chosen_letter = ''  # hold the letter which will be returned to the player

    # loops through all the letters in the dictionary and checks which appears the most
    for letter in letter_dict.keys():
        if letter_dict[letter] > chosen_letter_value:
            chosen_letter_value = letter_dict[letter]
            chosen_letter = letter

        # this condition is for the special case when each letter appears once
        elif letter_dict[letter] == chosen_letter_value == 0:
            chosen_letter = letter

    return chosen_letter


def run_single_game(words_list):
    """
    Runs single instance of Hangman: The Game
    :param words_list: list of words from which a random one will be chosen for the game
    """
    word = get_random_word(words_list)  # gets random word from the list
    pattern = UNDERSCORE * len(word)    # create the word pattern to be shown during the game
    error_count = 0  # initializes the error counter
    wrong_guess_lst = []  # creates a list to hold the wrong guessed letters
    user_msg = DEFAULT_MSG  # assigns the defaults message which will be shown to the user

    display_state(pattern, error_count, wrong_guess_lst, user_msg)

    # runs the game until the error counter reaches the maximum number of error (usually 7)
    while error_count < MAX_ERRORS:
        user_input = get_input()  # gets user input

        # block of code to check validity of user input
        if user_input[INPUT_TYPE] == LETTER:
            # checks if single lower case letter was inputted
            if len(user_input[INPUT_VALUE]) > 1 or not user_input[INPUT_VALUE].islower():
                user_msg = NON_VALID_MSG

            # checks if letter was inputted before
            elif user_input[INPUT_VALUE] in wrong_guess_lst or user_input[INPUT_VALUE] in pattern:
                user_msg = ALREADY_CHOSEN_MSG + user_input[INPUT_VALUE]

            # updates the pattern and in case the word was guessed completely stops the game and shows WIN_MSG
            elif user_input[INPUT_VALUE] in word:
                pattern = update_word_pattern(word, pattern, user_input[INPUT_VALUE])
                user_msg = DEFAULT_MSG
                if pattern == word:
                    break

            # if wrong guess adds the letter to the wrong guess list and increments the error counter
            else:
                wrong_guess_lst.append(user_input[INPUT_VALUE])
                error_count += 1
                if error_count == MAX_ERRORS:
                    break
                user_msg = DEFAULT_MSG

            display_state(pattern, error_count, wrong_guess_lst, user_msg)  # updates GUI

        # if asked for a hint gets the most common letter and shows it to the user
        elif user_input[INPUT_TYPE] == HINT:
            hint_letter = choose_letter(filter_words_list(words_list, pattern, wrong_guess_lst), pattern)
            display_state(pattern, error_count, wrong_guess_lst, HINT_MSG + hint_letter)

    if pattern != word:  # checks if the word wasn't guessed and shows lost game message
        display_state(pattern, error_count, wrong_guess_lst, LOSS_MSG + word, True)

    else:  # if game was won shows win message
        display_state(pattern, error_count, wrong_guess_lst, WIN_MSG, True)


def main():
    """
    Function that is called when we run the script.
    It initiates the game and passes the word list to the game engine.
    """
    words_list = load_words('words.txt')    # loads a list of words to be used during the game
    run_single_game(words_list)
    user_input = get_input()
    while user_input[INPUT_TYPE] == PLAY_AGAIN:

        if user_input[INPUT_VALUE]:
            run_single_game(words_list)
        else:
            break

        user_input = get_input()


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
