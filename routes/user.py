from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session

# Connect to Database and create database session
engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

user = Blueprint('user', __name__,
                    template_folder='templates',
                    static_folder='static')

@user.route('/user/<int:user_id>')
def getUser(user_id):
    user = session.query(User).filter_by(id=user_id).one()
    categories = session.query(Category).filter_by(user_id=user_id).all()
    items = session.query(Item).filter_by(user_id=user_id).all()
    return render_template('userpage.html', user=user, categories=categories, items=items)
