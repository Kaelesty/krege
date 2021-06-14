import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Word(SqlAlchemyBase):
    __tablename__ = 'words'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    string = sqlalchemy.Column(sqlalchemy.String)
    accent = sqlalchemy.Column(sqlalchemy.Integer)
    score = sqlalchemy.Column(sqlalchemy.Integer)
