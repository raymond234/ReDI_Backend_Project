import requests
from User import User
import json
root_url = "http://127.0.0.1:5000"


class Game:
    def __init__(self, username):
        requests.post(root_url + '/User/' + username + '/Game')
        result = json.loads(requests.get(root_url + '/User/' + username + '/Game').text)
        secret_word = result["secret_word"]
        hint = result["hint"]
        player = result["username"]
        self.secretWord = secret_word
        self.hint = hint
        self.got_hint = False
        self.missedletters = ""
        self.correctletters = ""
        self.game_score = 0
        self.is_done = False
        self.is_won = False
        self.username = username

    def get_game(self):
        requests.get(root_url)
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

    def update_fields_intermediate(self, missedLetters, correctLetters, is_done):
        fields = {"missed_letters": missedLetters, "correct_letters": correctLetters, "is_done": is_done}
        requests.patch(root_url+'/User/' + self.username + '/Game/' + self.secretWord + '/' + str.format(is_done), json=fields)

    def update_fields_end(self, missedLetters, correctLetters, game_score, is_done, is_won):
        fields = {"missed_letters": missedLetters, "correct_letters": correctLetters, "game_score": game_score,
                  "is_done": is_done, "is_won": is_won}
        requests.patch(root_url+'/User/' + self.username + '/Game/' + self.secretWord + '/' + str("{}").format(is_done), json=fields)

    def print_hint(self):
        return f'{self.hint}'

    def update_special_char(self):
        if self.got_hint:
            return "#"
