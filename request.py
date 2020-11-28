import logging
from datetime import datetime
from sqlalchemy import exc
import sqlalchemy
from flask import jsonify, request, make_response, g
from init import app
import function
# import utils
from models import User
import json
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


@app.route("/")
def index():
    return "Welcome to Hangman!"


@app.route("/User", methods=['POST'])
def create_user():
    user_info = request.json
    if request.method == 'POST':
        try:
            username = user_info["username"]
            password = user_info["password"]
            if User.query.filter_by(username=username).first() is not None:
                return make_response(jsonify(response="Welcome " + username + ". "
                                                      + "Please press 1 to login with your password as an existing user."), 402)
            if username is None or password is None:
                return make_response(jsonify(response="Please enter a valid username or password"), 405)

            function.create_user(username=username, password=password)  # Don't know yet whether it is json.get or json
            return make_response(jsonify(response='OK'), 201)
        except sqlalchemy.exc.InvalidRequestError:
            return make_response(jsonify(error='Bad request'), 400)


@auth.verify_password
def verify_password(username, password):
    user = function.get_user(username)
    if not user or not user.verify_password(password):
        return False
    g.user = user
    return True


# Scared I didn't use a get request. Hope this works.
@app.route('/User/<username>')
@auth.login_required
def get_resource():
    return jsonify({'data': 'Hello, %s!' % g.user.username})


@app.route('/User/<username>/Game', methods=['POST', 'GET'])
def create_game(username):
    logging.info(f"User logged in as: {username}")
    if request.method == 'POST':
        try:
            function.create_new_game(username=username)  # How is this parameter supposed to be set?
            return make_response(jsonify(response='OK'), 201)
        except sqlalchemy.exc.InvalidRequestError:
            return make_response(jsonify(error='Bad request'), 400)
    if request.method == 'GET':
        new_game = function.get_new_game(username=username)
        return jsonify(new_game.serialize())


@app.route('/User/<username>/Game/<secret_word>/<is_done>', methods=['GET', 'PATCH'])
def update_retrieve_game(username, secret_word, is_done):
    logging.info(f'User has given input secret_word as: {secret_word}')
    logging.info(f'User has given input username as: {username}')
    game_result = function.get_game(username, secret_word)
    if request.method == 'GET':
        return jsonify(game_result.serialize())  # I don't know if I need to present them serialized to my gameplay..

    if request.method == 'PATCH':
        data = request.json
        print(data)
        print(data["missed_letters"])

        if is_done:
            try:
                fields = {'missed_letters': data["missed_letters"], 'correct_letters': data["correct_letters"],
                          'game_score': data["game_score"], 'is_done': data["is_done"],
                          'is_won': data["is_won"], 'last_saved': datetime.now()}
                logging.info(fields)
                function.update_game(username, secret_word, fields)
                return jsonify(response='OK')
            except (sqlalchemy.exc.InvalidRequestError, KeyError):
                return make_response(jsonify(error='Bad request'), 400)
        else:
            try:
                fields = {'missed_letters': data['missed_letters'],
                          'correct_letters': data['correct_letters'], 'last_saved': datetime.now()}
                logging.info(fields)
                function.update_game(username, secret_word, fields)
                return jsonify(response='OK')
            except (sqlalchemy.exc.InvalidRequestError, KeyError):
                return make_response(jsonify(error='Bad request'), 400)


@app.route('/User/<username>/rankings', methods=['GET'])
def get_all_time_rankings(username):
    logging.info(f'User with username {username} is checking rankings.')
    return jsonify(function.get_rankings())


@app.route('/User/<username>/last_ten', methods=['GET'])
def get_last_ten_game_scores(username):
    return jsonify(function.last_ten_scores(username))


@app.route('/User/<username>/top_ten', methods=['GET'])
def get_top_ten_game_scores(username):
    return jsonify(function.top_ten_game_scores(username))


@app.route('/User/<username>/last_game_score', methods=['GET'])
def get_last_game_score(username):
    logging.info(print(function.last_score(username)))
    return jsonify(function.last_score(username))


@app.route('/User/<username>/win_percentage', methods=['GET'])
def get_win_percentage(username):
    result = function.win_percentage(username)
    return jsonify(result)
