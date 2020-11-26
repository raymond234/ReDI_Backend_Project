import requests
from User import User


class Game:
    def __init__(self, secretWord, hint):
        self.secretWord = secretWord
        self.hint = hint
        self.got_hint = False
        self.missedletters = ""
        self.correctletters = ""
        self.game_score = 0
        self.is_done = False
        self.is_won = False
        # self.player = User.

    def create_game(self):
        pass

    def get_game(self):
        pass

    def get_hint(self):
        print("Would you like a hint? (y)es or (n)o")
        print("Getting a hint will cost you 2 turns!")
        reply = input("").lower()
        if reply.startswith('y'):
            self.print_hint()
            self.got_hint = True
        elif reply.startswith('n'):
            return


    def update_fields(self):

        pass

    def print_hint(self):
        return f'{self.hint}'

    def update_special_char(self):
        if self.got_hint:
            return "#"
