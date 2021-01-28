import requests
import json
from pprint import pprint
root_url = "http://127.0.0.1:5000"


class User:
    def __init__(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter password: ")

    def create_user(self):
        user_info = {"username": self.username, "password": self.password}
        requests.post(root_url+"/User", json=user_info)

    def get_user(self):
        user_exists = json.loads(requests.get(root_url + '/User/' + self.username + '/' + self.password).text)
        return user_exists

    def get_saved_game(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/Game/unfinished_games').text)
        print("Enter the game_id of the game you want to continue playing.")
        pprint(result)
        game_id = int(input("Input game id: "))
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/Game/' + str(game_id)).text)
        return result

    def get_last_score(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/last_game_score').text)
        pprint(result)

    def get_all_time_rankings(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/rankings').text)
        pprint(result)

    def get_last_ten_scores(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/last_ten').text)
        pprint(result)

    def get_top_ten_scores(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/top_ten').text)
        pprint(result)

    def get_win_percentage(self):
        result = json.loads(requests.get(root_url + '/User/' + self.username + '/win_percentage').text)
        pprint(result)