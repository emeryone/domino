import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


class Problems(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'problems'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    owner = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    text = sqlalchemy.Column(sqlalchemy.String)
    difficulty = sqlalchemy.Column(sqlalchemy.Integer)
    level = sqlalchemy.Column(sqlalchemy.Integer)
    answer = sqlalchemy.Column(sqlalchemy.String)
    comment = sqlalchemy.Column(sqlalchemy.String, default='')
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)

    tournaments = orm.relation("Tournament", secondary="problems_to_tournament", backref="problems")
    #tournament_users = orm.relation("Tournament", "Users", secondary="tournament_to_problems_to_users",
    #                              backref="problems")

