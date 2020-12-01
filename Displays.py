from pantry import HANGMAN_PICS

def display_board_game(missed_letters, correct_letters, hint, special_char, secret_word):
    if "0" in special_char:
        print()
        print
    if '*' in special_char:
        print("Thank you for playing Hangman.")
        print("See you next time.")
        print("Updating game.")
        exit()
    if '#' in special_char:
        print()
        print(HANGMAN_PICS[len(missed_letters)])

        print()
        print(hint)
        print('Missed letters: ', end=' ')
        for letter in missed_letters:
            print(letter, end=' ')

        print()
        blanks = '_' * len(secret_word)
        for i in range(len(secret_word)):
            if secret_word[i] in correct_letters:
                blanks = blanks[:i] + secret_word[i] + blanks[i + 1:]
        # Display the secret word with spaces between the letters:
        for letter in blanks:
            print(letter, end=' ')
        print()

    else:
        print()
        print(HANGMAN_PICS[len(missed_letters)])

        print()
        print('Missed letters: ', end=' ')
        for letter in missed_letters:
            print(letter, end=' ')

        print()
        blanks = '_' * len(secret_word)
        for i in range(len(secret_word)):
            if secret_word[i] in correct_letters:
                blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
        # Display the secret word with spaces between the letters:
        for letter in blanks:
            print(letter, end=' ')
        print()

def display_board_user(special_char):
    pass