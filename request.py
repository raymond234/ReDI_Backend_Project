import logging
from datetime import datetime
from sqlalchemy import exc
import sqlalchemy
from flask import jsonify, request, make_response, g
from init import app
import function
# import utils
from models import User
from flask_httpauth import HTTPBasicAuth
auth = HTTPBasicAuth()


@app.route("/")
def index():
    return "Welcome to Hangman!"


@app.route("/User", methods=['POST'])
def create_user():
    if request.method == 'POST':
        try:
            username = request.json.get('username')
            password = request.json.get('password')
            if User.query.filter_by(username=username).first() is not None:
                return make_response(jsonify(response="Welcome " + username + ". "
                                                      + "Please login with your password as an existing user."), 400)
            if username is None or password is None:
                return make_response(jsonify(response="Please enter a valid username or password"), 400)

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


@app.route('/User/<username>/Game', methods=['POST'])
def create_game(username):
    if request.method == 'POST':
        try:
            function.create_new_game(username=username)  # How is this parameter supposed to be set?
            return make_response(jsonify(response='OK'), 201)
        except sqlalchemy.exc.InvalidRequestError:
            return make_response(jsonify(error='Bad request'), 400)


@app.route('/User/<username>/Game/<game_id>', methods=['GET', 'PATCH'])
def update_retrieve_game(username, game_id):
    logging.info(f'User has given input game as: {game_id}')
    logging.info(f'User has given input username as: {username}')
    game_result = function.get_game(game_id)
    if request.method == 'GET':
        return jsonify(game_result.serialize())  # I don't know if I need to present them serialized to my gameplay..

    if request.method == 'PATCH':
        try:
            fields = {'missed_letters': request.json.get('missed_letters'),
                      'correct_letters': request.json.get('correct_letters'),
                      'game_score': request.json.get('game_score'), 'is_done': request.json.get('is_done'),
                      'game_won': request.json.get('game_won'), 'last_saved': datetime.now()}
            logging.info(fields)
            function.update_game(game_id, fields)
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
