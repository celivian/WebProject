import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Events(SqlAlchemyBase):
    __tablename__ = 'events'

    owner_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("users.id"), primary_key=True)
    month = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    day = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    year = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    discription = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    user = orm.relationship("User")
