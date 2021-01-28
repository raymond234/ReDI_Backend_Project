from User import User
from Game import Game
import json
import requests
root_url = "http://127.0.0.1:5000"


def user_registration_authentication(entry):
    if entry == 1:
        print("Choose a username and a password.")
        user = User()
        user.create_user()
        return user

    elif entry == 2:
        print("Authenticating user")
        print("Enter your username and password")
        user = User()
        success = user.get_user()["response"]
        if success:
            return user
        else:
            x = True
            while x:
                print("Wrong ID or password")
                print("Enter your username and password again.")
                print("Press exit() to terminate the program anytime if you have forgotten username or password and start a new profile.")
                user = User()
                success = user.get_user()["response"]
                if success:
                    x = False
            return user
    else:
        print("Please choose the correct letter")


def user_get_profile_or_game(user, entry):
    if entry == 1:
        game = Game(user.username)
        return game
    elif entry == 2:
        return entry
    else:
        print("Please enter the correct input")


def user_profile(user, entry):
    if entry == 1:
        game = Game(user.username)
        return game
    elif entry == 2:
        result = user.get_saved_game()
        game = Game(user.username, result=result)
        return game
        # How do I return a game that is not new..........
    elif entry == 3:
        user.get_last_score()
    elif entry == 4:
        user.get_all_time_rankings()
    elif entry == 5:
        user.get_last_ten_scores()
    elif entry == 6:
        user.get_win_percentage()
    elif entry == 7:
        user.get_top_ten_scores()
    print()


if __name__ == '__main__':
    pass