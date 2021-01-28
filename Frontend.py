from pantry import HANGMAN_PICS


def display_board_game(missed_letters, correct_letters, hint, special_char, secret_word):
    if "0" in special_char:
        print()
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
                blanks = blanks[:i] + secret_word[i] + blanks[i+1:]
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


def display_board_user_game(name):
    print("Welcome " + name)
    print("Press " + str(1) + " to start a new game.")
    print("Press " + str(2) + " to view your profile.")


def display_board_landing():
    print()
    print()
    print("WELCOME TO HANGMAN!!")
    print("Press " + str(1) + " to create a profile")
    print("Press " + str(2) + " to login into your profile.")


def display_user_profile(username):
    print()
    print("Hello " + username + "! and welcome to your profile.")
    print("Press " + str(1) + " to start a new game.")
    print("Press " + str(2) + " to view your unfinished games.")
    print("Press " + str(3) + " to view your get your last game score.")
    print("Press " + str(4) + " to view the game's all time rankings.")
    print("Press " + str(5) + " to view the scores from your last " + str(10) + "games.")
    print("Press " + str(6) + " to view your win percentage.")
    print("Press " + str(7) + " to view your top " + str(10) + " game scores.")