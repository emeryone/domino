import datetime
import sqlalchemy
from sqlalchemy import orm
from sqlalchemy_serializer import SerializerMixin

from .db_session import SqlAlchemyBase


problems_to_tournament = sqlalchemy.Table(
    'problems_to_tournament',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('problems', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('problems.id')),
    sqlalchemy.Column('tournament', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tournament.id')),
    sqlalchemy.Column('number', sqlalchemy.String),
    sqlalchemy.Column('state', sqlalchemy.Integer)
)


users_to_tournament = sqlalchemy.Table(
    'users_to_tournament',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('tournament', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tournament.id'))
)

tournament_to_problems_to_users = sqlalchemy.Table(
    'tournament_to_problems_to_users',
    SqlAlchemyBase.metadata,
    sqlalchemy.Column('tournament', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('tournament.id')),
    sqlalchemy.Column('problems', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('problems.id')),
    sqlalchemy.Column('users', sqlalchemy.Integer,
                      sqlalchemy.ForeignKey('users.id')),
    sqlalchemy.Column('result', sqlalchemy.Integer)
)


class Tournament(SqlAlchemyBase, SerializerMixin):
    __tablename__ = 'tournament'

    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True, autoincrement=True)
    title = sqlalchemy.Column(sqlalchemy.String)
    owner = sqlalchemy.Column(sqlalchemy.Integer, sqlalchemy.ForeignKey("users.id"))
    level = sqlalchemy.Column(sqlalchemy.Integer)
    modified_date = sqlalchemy.Column(sqlalchemy.DateTime, default=datetime.datetime.now)
    enable = sqlalchemy.Column(sqlalchemy.Boolean, default=False)