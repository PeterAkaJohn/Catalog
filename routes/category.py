from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User
from flask import session as login_session
import random
import string
# Connect to Database and create database session
engine = create_engine('postgresql://catalog:catalog@localhost:5432/catalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

category = Blueprint('category', __name__,
                    template_folder='templates',
                    static_folder='static')

# Show all categories
@category.route('/')
@category.route('/categories/')
def showCategories():
    popularItems = session.query(Item).order_by(Item.upvote.desc()).limit(4).all()
    categories = session.query(Category).order_by(asc(Category.name)).all()
    state = ''.join(random.choice(string.ascii_uppercase + string.digits)
                    for x in xrange(32))
    login_session['state'] = state
    # return "The current session state is %s" % login_session['state']
    if 'username' not in login_session:
        return render_template('catalog.html', categories=categories, popularItems=popularItems, STATE=state)
    else:
        return render_template('catalog.html', categories=categories, popularItems=popularItems, STATE=state)

# Create a new category

@category.route('/categories/new/', methods=['GET', 'POST'])
def newCategory():
    if 'username' not in login_session:
        return redirect('/login')
    if request.method == 'POST':
        newCategory = Category(
            name=request.form['name'], user_id=login_session['user_id'])
        session.add(newCategory)
        flash('New Category %s Successfully Created' % newCategory.name)
        session.commit()
        return redirect(url_for('category.showCategories'))
    else:
        return render_template('newCategory.html')

# Edit a category

@category.route('/categories/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if editedCategory.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to edit this category. Please create your own category in order to edit.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            session.add(editedCategory)
            session.commit()
            flash('Category Successfully Edited %s' % editedCategory.name)
            return redirect(url_for('category.showCategories'))
    else:
        return render_template('editCategory.html', category=editedCategory)

# Delete a category

@category.route('/categories/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(Category).filter_by(id=category_id).one()
    if 'username' not in login_session:
        return redirect('/login')
    if categoryToDelete.user_id != login_session['user_id']:
        return "<script>function myFunction() {alert('You are not authorized to delete this restaurant. Please create your own restaurant in order to delete.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        category_items = session.query(Item).filter_by(category_id=category_id).all()
        for item in category_items:
            session.delete(item)
        session.delete(categoryToDelete)
        flash('%s Successfully Deleted' % categoryToDelete.name)
        session.commit()
        return redirect(url_for('category.showCategories', category_id=category_id))
    else:
        return render_template('deleteCategory.html', category=categoryToDelete)
