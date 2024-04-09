import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Marks(SqlAlchemyBase):
    __tablename__ = 'marks'

    owner_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("users.id"), primary_key=True)

    rus = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    math = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    bio = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    geo = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    hist = sqlalchemy.Column(sqlalchemy.String, nullable=True)

    user = orm.relationship("User")

    def __repr__(self):
        return f"<Job> {self.job}"
