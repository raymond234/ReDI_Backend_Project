import requests
import json
from pantry import HANGMAN_PICS
root_url = "http://127.0.0.1:5000"

class Game:
    def __init__(self, username, result=None):
        if result is None:
            requests.post(root_url + '/User/' + username + '/Game')
            result = json.loads(requests.get(root_url + '/User/' + username + '/Game').text)
            secret_word = result["secret_word"]
            hint = result["hint"]
            self.secret_word = secret_word
            self.hint = hint
            self.got_hint = False
            self.missed_letters = ""
            self.correct_letters = ""
            self.game_score = 0
            self.is_done = False
            self.is_won = False
            self.username = username
        else:
            self.secret_word = result["secret_word"]
            self.hint = result["hint"]
            self.got_hint = result["got_hint"]
            self.missed_letters = result["missed_letters"]
            self.correct_letters = result["correct_letters"]
            self.game_score = result["game_score"]
            self.is_done = result["is_done"]
            self.is_won = result["is_won"]
            self.username = username

    def get_hint(self):
        print("Would you like a hint? (y)es or (n)o")
        print("Getting a hint will cost you 2 points!")
        reply = input("").lower()
        if reply.startswith('y'):
            self.got_hint = True
        elif reply.startswith('n'):
            self.got_hint = False

    def update_fields_intermediate(self, got_hint, missed_letters, correct_letters, is_done):
        fields = {"got_hint": got_hint, "missed_letters": missed_letters, "correct_letters": correct_letters, "is_done": is_done}
        requests.patch(root_url+'/User/' + self.username + '/Game/' + self.secret_word, json=fields)

    def update_fields_end(self, got_hint, missed_letters, correct_letters, game_score, is_done, is_won):
        fields = {"got_hint": got_hint, "missed_letters": missed_letters, "correct_letters": correct_letters, "game_score": game_score,
                  "is_done": is_done, "is_won": is_won}
        requests.patch(root_url+'/User/' + self.username + '/Game/' + self.secret_word, json=fields)

    def update_special_char(self):
        if self.got_hint:
            return "#"

    def update_game_score(self):
        perfect_guess = len(HANGMAN_PICS)-1
        if self.got_hint:
            perfect_guess -= 2
        number_of_trials = len(self.missed_letters)
        trials_score = perfect_guess - number_of_trials
        length_score = len(self.secret_word)
        final_score = trials_score + length_score
        self.game_score = final_score
