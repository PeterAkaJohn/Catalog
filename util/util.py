from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from functools import wraps
from flask import flash, redirect, url_for
from flask import session as login_session
# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

# User Helper Functions
class Util():
    def createUser(self, login_session):
        newUser = User(name=login_session['username'], email=login_session[
                       'email'], picture=login_session['picture'])
        session.add(newUser)
        session.commit()
        user = session.query(User).filter_by(email=login_session['email']).one()
        return user.id

    def getUserInfo(self, user_id):
        user = session.query(User).filter_by(id=user_id).one()
        return user

    def getUserID(self, email):
        try:
            user = session.query(User).filter_by(email=email).one()
            return user.id
        except:
            return None
