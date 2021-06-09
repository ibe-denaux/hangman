import random

alphabet = 'abcdefghijklmnopqrstuvwxyz'
possible_words = ['becode', 'learning', 'mathematics', 'sessions']
word_to_find = random.choice(possible_words)
list_word_to_find = list(word_to_find)
lives = 5
correctly_guessed_letters = ["_"] * len(word_to_find)
wrongly_guessed_letters = []
already_guessed_letters = []
turn_count = 0
error_count = 0

#print(correctly_guessed_letters)
#print(word_to_find)

#Start of the game
print("Hi, welcome to Hangman!You have to guess a word but only 5 mistakes are allowed. Good luck!")
while lives != 0 and correctly_guessed_letters != list_word_to_find:
    print(f"You have {lives} lives left.\nThis was your guess #{turn_count} and you have made {error_count} mistakes so far.")

    # Check if valid input
    while True:
        letter = input("Give me one letter: ").lower()
        if len(letter) != 1:
            print("Please enter one letter exactly")
            continue
        elif letter not in alphabet:
            print("Please enter a valid letter.")
            continue
        elif letter in already_guessed_letters:
            print("You have already tried this letter, try another one.")
            continue
        else:
            break

    # Check if letter in secret word or not
    if letter in list_word_to_find:
        for index, value in enumerate(list_word_to_find):
            if value == letter:
                correctly_guessed_letters[index] = letter
        print(f"///\n'{letter}' is in the secret word!\nSo far, the secret word is {correctly_guessed_letters}\nYour incorrect letters are: {wrongly_guessed_letters}")
    elif letter not in word_to_find:
        wrongly_guessed_letters.append(letter)
        lives -= 1
        error_count += 1
        print(f"///\n'{letter}' is not in the secret word!\nSo far, the secret word is {correctly_guessed_letters}\nYour incorrect letters are: {wrongly_guessed_letters}")
    already_guessed_letters.append(letter)
    turn_count += 1

if correctly_guessed_letters == list_word_to_find:
    print(f"Congrats!, you have guess the word '{word_to_find}'.")
else:
    print(f"Game over! The secret word was '{word_to_find}'.")


