##################################################
#  FILE: hangman.py
#  WRITER : yevgeni, jenia90, 320884216
#  EXERCISE : intro2cs ex4 2015-2016
#  DESCRIPTION : 
#
##################################################

from ex4.hangman_helper import *


def update_word_pattern(word, pattern, letter):
    """
    Updates the given pattern if user chosen letter appears in the original word
    :param word: The random word to guess
    :param pattern: Pattern of the word shown to the user
    :param letter: Guessed letter
    :return: Returns the updated pattern
    """
    for i in range(len(word)):
        if word[i] == letter:
            pattern = pattern[:i] + word[i] + pattern[i+1:]  # slices the pattern, replaces the letter and rejoins it.

    return pattern


def run_single_game(words_list):
    """
    Runs single instance of Hangman: The Game
    :param words_list: list of words from which a random one will be chosen for the game
    """
    word = get_random_word(words_list)
    pattern = '_' * len(word)
    error_count = 0
    wrong_guess_lst = []
    user_msg = DEFAULT_MSG

    display_state(pattern, error_count, wrong_guess_lst, user_msg)

    while error_count < MAX_ERRORS:
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


def filter_words_list(words, pattern, wrong_guess_lst):
    """
    Filters the word list to give more precise hints to the user
    :param wrong_guess_lst: list of wrong letters the user already tried
    :param words: list of words to filter through
    :param pattern: the word pattern string shown to the user
    :return: returns the filtered word list
    """
    import re

    filtered_lst = []
    regex_pattern = pattern.replace('_', '\w')+'$'

    for word in words:
        if re.match(re.compile(regex_pattern), word) \
                and not is_in_wrong_guess_word_filter(word, wrong_guess_lst):
            filtered_lst.append(word)

    return filtered_lst


def is_in_wrong_guess_word_filter(word, wrong_guess_lst):
    for letter in wrong_guess_lst:
        if letter in word:
            return True

    return False


def choose_letter(words, pattern):
    letter_dict = dict()

    for word in words:
        for l in word:
            if l not in pattern and len(word) == len(pattern):
                if l in letter_dict.keys():
                    letter_dict[l] += 1
                else:
                    letter_dict[l] = 0

    chosen_letter = find_letter_with_most_occurances(letter_dict)

    return chosen_letter


def find_letter_with_most_occurances(letter_dict):
    chosen_letter_value = 0
    chosen_letter = ''

    for l in letter_dict.keys():
        if letter_dict[l] > chosen_letter_value:
            chosen_letter_value = letter_dict[l]
            chosen_letter = l

        elif letter_dict[l] == chosen_letter_value == 0:
            chosen_letter = l

    return chosen_letter


def main():
    run_single_game(load_words())
    user_input = get_input()
    if user_input[0] == PLAY_AGAIN and user_input[1] == True:
        run_single_game(load_words())


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
