import random
possible_words = ['becode', 'learning', 'mathematics', 'sessions']
alphabet = 'abcdefghijklmnopqrstuvwxyz'

class Hangman:
    """
    The hangman game class with his methods
    """

    def __init__(self):
        self.word_to_find = list(random.choice(possible_words))
        self.turn_count = 0
        self.error_count = 0
        self.lives = 5
        self.correctly_guessed_letters = ["_"] * len(self.word_to_find)
        self.wrongly_guessed_letters = []
        self.already_guessed_letters = []
        self.guessed = False

        # Init methods
        self.start_game(self.lives, self.guessed)
        self.game()

    # this method calls the play_game(), well_played() and game_over()
    def start_game(self, lives, guessed):
        if guessed is False and lives > 0:
            self.game()
        if guessed:
            self.well_played()
        if lives == 0:
            self.game_over()

    def well_played(self):
        # COACHES' NOTE: functions should be verbs 'inform_user' 'display_win_message'
        print(f"Good Job, Buddy! you've found the word {self.word_to_find} in {self.turn_count}, you made {self.error_count} mistakes and still had {self.lives} left.")

    def game_over(self):
        print("game over...")

    def game(self):
        # COACHES' NOTE: game? weird function name that says nothing. Use play or play_game.
        print(self.correctly_guessed_letters)
        while self.lives > 0 and self.guessed == False:
            print(
                f"You have {self.lives} lives left.\nThis was your guess #{self.turn_count} and you have made {self.error_count} mistakes so far.")
            
            # COACHES' NOTE: comment that could have been a function
            # Check if valid input
            # COACHES' NOTE: nested while loops? Should be avoided.
            while True:
                self.letter = input("Give me one letter: ").lower()
                if len(self.letter) != 1:
                    print("Please enter one letter exactly")
                    continue
                elif self.letter not in alphabet:
                    print("Please enter a valid letter.")
                    continue
                elif self.letter in self.already_guessed_letters:
                    print("You have already tried this letter, try another one.")
                    continue
                else:
                    break
            
            # COACHES' NOTE: comment that could have been a function
            # Check if letter in secret word or not
            if self.letter in self.word_to_find:
                for index, value in enumerate(self.word_to_find):
                    if value == self.letter:
                        self.correctly_guessed_letters[index] = self.letter
                print(f"///\n'{self.letter}' is in the secret word!\nSo far, the secret word is {self.correctly_guessed_letters}\nYour incorrect letters are: {self.wrongly_guessed_letters}")
            elif self.letter not in self.word_to_find:
                self.wrongly_guessed_letters.append(self.letter)
                self.lives -= 1
                self.error_count += 1
                print(f"///\n'{self.letter}' is not in the secret word!\nSo far, the secret word is {self.correctly_guessed_letters}\nYour incorrect letters are: {self.wrongly_guessed_letters}")
            self.already_guessed_letters.append(self.letter)
            self.turn_count += 1

# COACHES' NOTE: It works, but the implementation is sloppy. Not enough structure and functions, weird function naming...most likely caused by starting off non-OOP oriented and trying to make the code fit.
# COACHES' NOTE: Break up your problem into small subproblems and make functions out of those. Go bottom-up instead of top-down.

