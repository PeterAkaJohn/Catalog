from flask import Flask, render_template, request, redirect, jsonify, url_for, flash, Blueprint
from sqlalchemy import create_engine, asc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item, User, Rating
from flask import session as login_session
from util import Util

Util = Util()

# Connect to Database and create database session
engine = create_engine('sqlite:///catalog.db')
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
session = DBSession()

item = Blueprint('item', __name__,
                    template_folder='templates',
                    static_folder='static')

# Show a category items

@item.route('/categories/<int:category_id>/index/')
@item.route('/categories/<int:category_id>/')
def showCategoryItems(category_id):
    category = session.query(Category).filter_by(id=category_id).one()
    creator = Util.getUserInfo(category.user_id)
    popularItems = session.query(Item).filter_by(category_id=category_id).order_by(Item.upvote.desc()).limit(3).all()
    items = session.query(Item).filter_by(category_id=category_id).all()
    for popular in popularItems:
        print popular.name
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('category.html', items=items, category=category, creator=creator, popularItems=popularItems)
    else:
        return render_template('category.html', items=items, category=category, creator=creator, popularItems=popularItems)

# Create a new category item
@item.route('/categories/<int:category_id>/new/', methods=['GET', 'POST'])
def newItem(category_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to add menu items to this restaurant. Please create your own restaurant in order to add items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        newItem = Item(name=request.form['name'], description=request.form['description'], price=request.form[
                           'price'], picture=request.form['image'], upvote=0, downvote=0, category_id=category_id, user_id=category.user_id)
        session.add(newItem)
        session.commit()
        flash('New %s Item Successfully Created' % (newItem.name))
        return redirect(url_for('item.showCategoryItems', category_id=category_id))
    else:
        return render_template('newitem.html', category=category)

#Show Item
@item.route('/categories/<int:category_id>/<int:item_id>/')
def showItem(category_id, item_id):
    category = session.query(Category).filter_by(id=category_id).one()
    creator = Util.getUserInfo(category.user_id)
    item = session.query(Item).filter_by(id=item_id).one()
    popularItems = session.query(Item).filter_by(category_id=category_id).order_by(Item.upvote.desc()).limit(3).all()
    if 'username' not in login_session or creator.id != login_session['user_id']:
        return render_template('item.html', item=item, category=category, creator=creator, popularItems=popularItems)
    else:
        return render_template('item.html', item=item, category=category, creator=creator, popularItems=popularItems)

# Edit a category item

@item.route('/categories/<int:category_id>/<int:item_id>/edit', methods=['GET', 'POST'])
def editItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    editedItem = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to edit menu items to this restaurant. Please create your own restaurant in order to edit items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
        if request.form['price']:
            editedItem.price = request.form['price']
        if request.form['image']:
            editedItem.picture = request.form['image']
        session.add(editedItem)
        session.commit()
        flash('Category Item Successfully Edited')
        return redirect(url_for('item.showItem', category_id=category_id, item_id=item_id))
    else:
        return render_template('edititem.html', category=category, item=editedItem)

#Upvote Item
@item.route('/categories/<int:category_id>/<int:item_id>/upvote', methods=['POST'])
def upvoteItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    upvoteItem = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    userVotedItemCount = session.query(Rating).filter(Rating.item_id==item_id, Rating.user_id==login_session['user_id']).count()
    if userVotedItemCount > 0:
        userVote = session.query(Rating).filter(Rating.item_id==item_id, Rating.user_id==login_session['user_id']).one()
        if userVote.result == "down":
            editRating(userVote, "up", upvoteItem)
            flash('You liked this Item.')
            return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
        flash('You already liked/disliked this Item.')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    if login_session['user_id'] == upvoteItem.user_id:
        flash('Error in the UpVote process')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    if request.method == 'POST':
        upvoteItem.upvote += 1
        session.add(upvoteItem)
        userRating = Rating(item_id = item_id, user_id = login_session['user_id'], result = "up")
        session.add(userRating)
        session.commit()
        flash('Item Successfully Liked')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    else:
        flash('Error in the Upvote process')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))

#DownVote Item
@item.route('/categories/<int:category_id>/<int:item_id>/downvote', methods=['POST'])
def downvoteItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    downvoteItem = session.query(Item).filter_by(id=item_id).one()
    category = session.query(Category).filter_by(id=category_id).one()
    userVotedItemCount = session.query(Rating).filter(Rating.item_id==item_id, Rating.user_id==login_session['user_id']).count()
    if userVotedItemCount > 0:
        userVote = session.query(Rating).filter(Rating.item_id==item_id, Rating.user_id==login_session['user_id']).one()
        if userVote.result == "up":
            editRating(userVote, "down", downvoteItem)
            flash('You disliked this Item.')
            return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
        flash('You already liked/disliked this Item.')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    if login_session['user_id'] == downvoteItem.user_id:
        flash('Error in the DownVote process')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    if request.method == 'POST':
        downvoteItem.downvote += 1
        session.add(downvoteItem)
        userRating = Rating(item_id = item_id, user_id = login_session['user_id'], result = "down")
        session.add(userRating)
        session.commit()
        flash('Item Successfully Disliked')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))
    else:
        flash('Error in the DownVOte process')
        return redirect(url_for('item.showItem', category_id = category_id, item_id=item_id))

# Edit Rating of an item for a user that already voted
def editRating(userVote, newVote, rateItem):
    userVote.result = newVote
    if newVote == "up":
        rateItem.upvote += 1
        rateItem.downvote -= 1
    else:
        rateItem.upvote -= 1
        rateItem.downvote += 1
    session.add(userVote)
    session.add(rateItem)
    session.commit()

# Delete a category item
@item.route('/categories/<int:category_id>/<int:item_id>/delete', methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    if 'username' not in login_session:
        return redirect('/login')
    category = session.query(Category).filter_by(id=category_id).one()
    itemToDelete = session.query(Item).filter_by(id=item_id).one()
    if login_session['user_id'] != category.user_id:
        return "<script>function myFunction() {alert('You are not authorized to delete menu items to this restaurant. Please create your own restaurant in order to delete items.');}</script><body onload='myFunction()''>"
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        flash('Category Item Successfully Deleted')
        return redirect(url_for('item.showCategoryItems', category_id=category_id))
    else:
        return render_template('deleteitem.html', item=itemToDelete, category=category)
