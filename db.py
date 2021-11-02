# -*- coding: utf-8 -*-
"""
Created on Mon Oct 25 14:06:37 2021

@author: Abraham
"""

import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
engine = sqlalchemy.create_engine("mariadb+mariadbconnector://root:1234@127.0.0.1:3306/Unnamed")
Base = declarative_base()
class Employee(Base):
    __tablename__ = 'employees'
    ids = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    first_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    last_name = sqlalchemy.Column(sqlalchemy.String(length=100))
    active = sqlalchemy.Column(sqlalchemy.Boolean, default=True)

Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
Session = Session()
employees = Session.query(Employee).all()
    