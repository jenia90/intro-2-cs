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
    :return:
    """
    word = get_random_word(words_list)
    pattern = '_' * len(word)
    error_count = 0
    wrong_guess_lst = []
    user_msg = DEFAULT_MSG

    while error_count < MAX_ERRORS:
        display_state(pattern, error_count, wrong_guess_lst, user_msg)
        user_input = get_input()

        if user_input[0] == LETTER:
            if len(user_input[1]) > 1 or not user_input[1].islower():
                user_msg = NON_VALID_MSG

            elif user_input[1] in wrong_guess_lst:
                user_msg = ALREADY_CHOSEN_MSG + user_input[1]

            elif user_input[1] in word:
                pattern = update_word_pattern(word, pattern, user_input[1])
                user_msg = DEFAULT_MSG

            else:
                wrong_guess_lst.append(user_input[1])
                error_count += 1
                user_msg = DEFAULT_MSG

        elif user_input[0] == HINT:
            pass
            # TODO

        elif user_input[0] == PLAY_AGAIN:
            pass
            # TODO

    display_state(pattern, error_count, wrong_guess_lst, user_msg, True)


def main():
    words_lst = open("words.txt")
    load_words(words_lst)
    run_single_game(load_words())
    user_input = get_input()
    if user_input[0] == PLAY_AGAIN and user_input[1] == True:
        run_single_game(load_words(words_lst))


if __name__ == "__main__":
    start_gui_and_call_main(main)
    close_gui()
