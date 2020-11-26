from init import db
from models import Game, User
import datetime
from api_connector import ApiConnector

"""
    Functions that can be carried out by the User.
"""


def create_user(username, password):
    new_user = User(username=username)
    new_user.hash_password(password)
    db.session.add(new_user)
    db.session.commit()


def create_new_game(username):
    obj = ApiConnector()
    obj.get_entry()
    secret_word = obj.get_word()
    hint = obj.get_definition()
    new_game = Game(secret_word=secret_word, hint=hint, got_hint=0, missed_letters="", correct_letters="", game_score=0,
                    is_done=0, game_won=0, last_saved=datetime.datetime.now(), username=username)
    db.session.add(new_game)
    db.session.commit()
    return new_game


def get_user(username):  # return User.query.filter_by(username=username).first()  # That shit fit be flask cause am.
    result = db.session.query(User).filter_by(username=username).first()
    return result


def get_game(game_id):
    return db.session.query(Game).filter_by(id=game_id).first()


def update_game(game_id, fields):
    # Has to encompass situations involving loading a saved game and saving it back later without completing it.
    # And also encompass situations saving the game finally after it is completed.
    # All this will probably be coded in the client side.

    # Above covers the fields that will appear in the Flask app

    result = db.session.query(Game).filter_by(id=game_id).update(fields)
    db.session.commit()
    return result


def win_percentage(username):
    result = db.session.query(User.username.label("Username"), User.total_game_scores.label("Total Scores"),
                              User.win_percentage.label("Win Percentage")).filter(User.username == username).first()
    return result


def get_rankings():  # filter was here as parameter
    # Possible extension for when there are more than 50 players and the User is not in the top 50.
    result = db.session.query(User.username.label("Username"), User.total_game_scores.label("All_time"),
                              User.win_percentage.label("Win_Percentage")).order_by(User.total_game_scores.desc()).\
        limit(50).all()
    # case expression/+exists for that with possible union...
    return result


def last_ten_scores(username):
    result = db.session.query(User.username, Game.game_score).outerjoin(Game, User.username == Game.username)\
        .filter(User.username == username).order_by(Game.last_saved.desc()).limit(10).all()
    return result


def last_score(username):
    result = db.session.query(User.username, Game.game_score).outerjoin(Game, User.username == Game.username) \
        .filter(User.username == username).order_by(Game.last_saved.desc()).limit(1).all()
    return result


def top_ten_game_scores(username):
    result = db.session.query(User.username, Game.game_score).outerjoin(Game, User.username == Game.username) \
        .filter(User.username == username).order_by(Game.game_score.desc()).limit(10).all()
    return result

