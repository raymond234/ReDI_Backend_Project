HANGMAN_PICS = ['''




           ''', '''
    +---+
         |
         |
         |
        ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +---+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''']


def user_greeting(username):
    print()
    print("Hello " + username + "! and welcome to your profile.")
    print("Press " + str(1) + " to start a new game.")
    print("Press " + str(2) + " to view your unfinished games.")
    print("Press " + str(3) + " to view your get your last game score.")
    print("Press " + str(4) + " to view the game's all time rankings.")
    print("Press " + str(5) + " to view the scores from your last " + str(10) + "games.")
    print("Press " + str(6) + " to view your win percentage.")
    print("Press " + str(7) + " to view your top " + str(10) + " game scores.")
    entry = input("Enter your option: ")

    if entry == 1:
        print("Create game sequence/route")
    elif entry == 2:
        print("Get unfinished games route.")
    elif entry == 3:
        print("Get last game score.")
    elif entry == 4:
        print("Get all time rankings route.")
    elif entry == 5:
        print("Get last ten games scores.")
    elif entry == 6:
        print("Get win percentage.")
    elif entry == 7:
        print("Get top ten games scores.")
    print()