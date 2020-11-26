import datetime
from init import db
from passlib.apps import custom_app_context as pwd_context
from sqlalchemy.inspection import inspect
from sqlalchemy.orm import deferred


class Serializer(object):
    """Class for serializing SQLAlchemy objects into dicts."""

    @staticmethod
    def is_primitive(obj):
        return type(obj) in (int, float, str, bool)

    def serialize(self):
        fields = inspect(self).attrs.keys()
        return {c: getattr(self, c) for c in fields if Serializer.is_primitive(getattr(self, c))}

    @staticmethod
    def serialize_list(list_obj):
        return [m.serialize() for m in list_obj]


class Game(db.Model, Serializer):
    __tablename__ = "games_table"
    __table_args__ = (
        db.CheckConstraint("games_table.is_done IN (0, 1)", name='check1'),
        db.CheckConstraint("games_table.game_won IN (0, 1)", name='check2'),
        db.CheckConstraint("games_table.got_hint IN (0, 1)", name='check3'),
        {"extend_existing": True}
    )

    id = db.Column(db.Integer, primary_key=True)
    secret_word = db.Column(db.String(128), nullable=False)
    hint = db.Column(db.String(1024), nullable=False)
    got_hint = db.Column(db.SMALLINT)
    missed_letters = db.Column(db.String(128))
    correct_letters = db.Column(db.String(128))
    game_score = db.Column(db.Integer)
    is_done = db.Column(db.SMALLINT)
    game_won = db.Column(db.SMALLINT)
    last_saved = db.Column(db.DateTime(timezone=True), default=datetime.datetime.utcnow)
    username = db.Column(db.String(32), db.ForeignKey('users_table.username'), nullable=False)

    def __repr__(self):
        return f'Secret Word: {self.secret_word} Game Score: {self.game_score} Game Status: {self.game_won}'


class User(db.Model, Serializer):
    __tablename__ = "users_table"
    __table_args__ = {"extend_existing": True}
    username = db.Column(db.String(32), primary_key=True, nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)
    games = db.relationship('Game', backref='game', lazy=True)
    total_played = db.column_property(db.select([db.func.count(Game.id)]).where(Game.username == username))
    total_won = db.column_property(db.select([db.func.count(Game.id)]).where(db.and_(Game.username == username, Game.game_won == 1)))
    total_game_scores = db.column_property(db.select([db.func.sum(Game.game_score)]).where(Game.username == username))
    win_percentage = db.column_property(((total_won.expression * 1.0) / total_played.expression) * 100.0)

    def hash_password(self, password):
        self.hashed_password = pwd_context.encrypt(password)

    def verify_password(self, password):
        return pwd_context.verify(password, self.hashed_password)

    def __repr__(self):
        return f'Username: {self.username}'


if __name__ == '__main__':
    # db.create_all()
    # db.session.commit()
    Game.__table__.drop(db.engine)
    Game.__table__.create(db.engine)

