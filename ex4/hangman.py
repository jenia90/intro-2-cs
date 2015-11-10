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
            hint_letter = choose_letter(filter_words_list(wrong_guess_lst, words_list, pattern), pattern)
            display_state(pattern, error_count, wrong_guess_lst, HINT_MSG + hint_letter)

    display_state(pattern, error_count, wrong_guess_lst, user_msg, True)


def filter_words_list(wrong_guess_lst, words, pattern):
    """
    Filters the word list to give more precise hints to the user
    :param wrong_guess_lst: list of wrong letters the user already tried
    :param words: list of words to filter through
    :param pattern: the pattern shown to the user
    :return: returns the update word list
    """
    filtered_word_lst = []  # creates an empty list to hold the filtered words

    for word in words:
        if len(word) == len(pattern):  # check if the word and pattern are the same length
            for l in word:  # these next few lines check if each of the letters are in the pattern or wrong guess list
                if l not in pattern and l not in wrong_guess_lst:
                    filtered_word_lst.append(word)  # appends the filtered words to the list

    return filtered_word_lst


def choose_letter(words, pattern):
    letter_dict = {}
    chosen_letter = ''
    count = 0
    for word in words:
        for l in word:
            if l not in pattern:
                if l not in letter_dict.keys():
                    letter_dict[l] = 0
                else:
                    letter_dict[l] += 1
    for item in letter_dict.keys():
        if count < letter_dict[item]:
            count = letter_dict[item]
            chosen_letter = item

    return chosen_letter


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
