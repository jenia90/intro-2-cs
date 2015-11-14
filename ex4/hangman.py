#######################################################################
#  FILE: hangman.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex4 2015-2016
#  DESCRIPTION : Simple Hangman game where a user has to guess a word
#
#######################################################################

from ex4.hangman_helper import *

UNDERSCORE = '_'


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

    for word in words:  # this block of code goes through all the words and creates a dictionary
        for l in word:      # of all the letters in them
            if l not in pattern and len(word) == len(pattern):
                if l in letter_dict.keys():
                    letter_dict[l] += 1
                else:
                    letter_dict[l] = 0

    return find_letter_with_most_occurances(letter_dict)


def find_letter_with_most_occurances(letter_dict):
    """
    Helper function to find the letter that appears the most.
    :param letter_dict: dictionary containing letters as keys and number of their appearances as values
    :return: returns most common letter in the dictionary
    """
    chosen_letter_value = 0  # temporary variable to hold the maximum amount of times a letter appears
    chosen_letter = ''  # hold the letter which will be returned to the player

    for l in letter_dict.keys():
        if letter_dict[l] > chosen_letter_value:
            chosen_letter_value = letter_dict[l]
            chosen_letter = l

        elif letter_dict[l] == chosen_letter_value == 0:  # this condition is for the special case when each letter
            chosen_letter = l                                   # appears once

    return chosen_letter


def run_single_game(words_list):
    """
    Runs single instance of Hangman: The Game
    :param words_list: list of words from which a random one will be chosen for the game
    """
    word = get_random_word(words_list)
    pattern = UNDERSCORE * len(word)
    error_count = 0
    wrong_guess_lst = []
    user_msg = DEFAULT_MSG

    display_state(pattern, error_count, wrong_guess_lst, user_msg)

    while UNDERSCORE in pattern and error_count < MAX_ERRORS:
        user_input = get_input()

        if user_input[0] == LETTER:
            if len(user_input[1]) > 1 or not user_input[1].islower():
                user_msg = NON_VALID_MSG

            elif user_input[1] in wrong_guess_lst or user_input[1] in pattern:
                user_msg = ALREADY_CHOSEN_MSG + user_input[1]

            elif user_input[1] in word:
                pattern = update_word_pattern(word, pattern, user_input[1])
                user_msg = DEFAULT_MSG
                if pattern == word:
                    break

            else:
                wrong_guess_lst.append(user_input[1])
                error_count += 1
                user_msg = DEFAULT_MSG

            display_state(pattern, error_count, wrong_guess_lst, user_msg)

        elif user_input[0] == HINT:
            hint_letter = choose_letter(filter_words_list(words_list, pattern, wrong_guess_lst), pattern)
            display_state(pattern, error_count, wrong_guess_lst, HINT_MSG + hint_letter)

    if pattern != word:
        display_state(pattern, error_count, wrong_guess_lst, LOSS_MSG + word, True)

    else:
        display_state(pattern, error_count, wrong_guess_lst, WIN_MSG, True)

    if get_input()[0] == PLAY_AGAIN:
        run_single_game(load_words())


def main():
    """
    Function that is called when we run the script.
    It initiates the game and passes the word list to the game engine.
    """
    run_single_game(load_words())


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
