import datetime
import sqlalchemy
from sqlalchemy import orm
from .db_session import SqlAlchemyBase


class Ads(SqlAlchemyBase):
    __tablename__ = 'ads'
    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)

    owner_id = sqlalchemy.Column(sqlalchemy.Integer,
                                 sqlalchemy.ForeignKey("users.id"))


    ad_name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    discription = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    date = sqlalchemy.Column(sqlalchemy.DateTime,
                                      default=datetime.datetime.now)

    user = orm.relationship("User")
