import os
import getpass
import hangman_art
clear = lambda: os.system('cls')

class Hangman:
    secret_word = None
    used_letters = None
    wrong_choices = None
    in_progress = False

    def __init__(this, word):
        this.secret_word = word
        this.used_letters = []
        this.wrong_choices = 0
        this.in_progress = True
    
    def start(this):
        while this.in_progress:
            this.__draw_ui()

    def __draw_ui(this):
        clear()
        # determine if user won on last turn
        # draws the current hangman board
        print(hangman_art.HANGMANPICS[this.wrong_choices])
        print("")
        patterned_word = this.__draw_secret_word()
        print(patterned_word)
        print("")
        this.__draw_used_letters()
        print()
        print()
        this.__determine_winner(patterned_word)
        this.__get_next_letter()

    def __determine_winner(this, patterned_word):
        if '-' not in patterned_word:
            clear()
            print(hangman_art.VICTORY)
            exit()
        
        if this.wrong_choices >= 7:
            clear()
            print(hangman_art.GAME_OVER)
            exit()

    def __get_next_letter(this):
        print("Please choose a letter:")
        letter = input()
        this.used_letters.append(letter)
        # Perform validation to make sure they typed 1 character
        if letter not in this.secret_word:
            this.wrong_choices += 1

    def __draw_used_letters(this):
        print("Used Letters:")
        print(this.used_letters)

    def __draw_secret_word(this):
        patterned_word = ''
        # how should we handle the spaces in the word?
        for char in this.secret_word:
            if char in this.used_letters:
                patterned_word += char
            elif char == ' ':
                patterned_word += ' '
            else:
                patterned_word += '-'
        return patterned_word

# Use this to collect the starting phrase ensuring that its spelled correctly
def get_game_phrase():
    valid_phrase = ''
    while len(valid_phrase) <= 0:
        phrase = getpass.getpass("Please provide a word or phrase to get started:\n")
        verify = getpass.getpass("Please verify your word or phrase:\n")
        if phrase == verify:
            valid_phrase = verify
        else:
            print("The word or phrase did not match...")
    return valid_phrase

clear()
# Setup some game instructions
# draw_instructions()
game_phrase = get_game_phrase()
game = Hangman(game_phrase)
game.start()