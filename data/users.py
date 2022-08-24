import datetime
import sqlalchemy
from flask_login import UserMixin
from .db_session import SqlAlchemyBase
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy import orm


class User(SqlAlchemyBase, UserMixin, SerializerMixin):
    __tablename__ = 'users'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    surname = sqlalchemy.Column(sqlalchemy.String)
    name = sqlalchemy.Column(sqlalchemy.String)
    email = sqlalchemy.Column(sqlalchemy.String, index=True, unique=True, nullable=True)
    hashed_password = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    role = sqlalchemy.Column(sqlalchemy.Integer, default=0)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    tournaments = orm.relation("Tournament", secondary="users_to_tournament", backref="users")
    #tournament_problems = orm.relation("Tournament", "Problems", secondary="tournament_to_problems_to_users",
    #                                 backref="users")

    def set_password(self, password):
        return generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.hashed_password, password)

