import requests
root_url = "http://127.0.0.1:5000"


class User:
    def __init__(self):
        self.username = input("Enter username: ")
        self.password = input("Enter password: ")

    def create_user(self):
        user_info = {"username": self.username, "password": self.password}
        requests.post(root_url+"/User", json=user_info)

    def get_user(self):
        pass

    def get_saved_games(self):
        pass
