import random
import os
from ord import ord
os.system("title Hangman")

def hangman():
    word = random.choice(ord)
    os.system("cls")
    word_letters = set(word)
    alphabet = set('abcdefghijklmnopqrstuvwxyzæøå')
    used_letters = set()
    global lives
    lives = 6

    while len(word_letters) > 0 and lives > 0:
        print(f'Du har {lives} liv igjen. Bokstavene du har brukt:', ''.join(used_letters))
        hangmandrawing()

        word_list = [letter if letter in used_letters else '_' for letter in word]
        print('Gjeldene ord: ', ''.join(word_list))

        user_letter = input('Gjett en bokstav: ').lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print(f'Bokstaven {user_letter} er ikke i ordet. Prøv igjen!')
            
        elif user_letter in used_letters:
            print('Du har allerede skrevet denne bokstaven! Prøv igjen.')
        else:
            print('Ugyldig bokstav, prøv igjen!')
    if lives == 0:
        print(f'Du tapte! Ordet var {word}.')
        hangmandrawing()
    else:
        print(f'Du har gjettet ordet {word}!')
        hangmandrawing()
    input('Trykk enter for å prøve igjen.')

def hangmandrawing():
    if lives == 6 :
        print("  |------------| ")
        print("  |            | ")
        print("  |")
        print("  |")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 5:
        print("  |------------| ")
        print("  |            O ")
        print("  |            |")
        print("  |")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 4:
        print("  |------------| ")
        print("  |            O ")
        print("  |            |/")
        print("  |")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 3:
        print("  |------------| ")
        print("  |            O ")
        print("  |           \\|/")
        print("  |")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 2:
        print("  |------------| ")
        print("  |            O ")
        print("  |           \\|/")
        print("  |            |")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 1 :
        print("  |------------| ")
        print("  |            O ")
        print("  |           \\|/")
        print("  |           /")
        print("  |")
        print("  |")
        print(" ###\n")
    elif lives == 0 :
        print("  |------------| ")
        print("  |            O ")
        print("  |           \\|/")
        print("  |           / \\")
        print("  |")
        print("  |")
        print(" ###\n")

while True:
    hangman()