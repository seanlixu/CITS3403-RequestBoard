# where rate user function should go
from app import app
from flask import Flask
import sqlite3
from config import db
from models import User
from flask import jsonify, render_template, redirect, request
from flask_login import LoginManager, current_user, login_required

# User rating function
@app.route('/rate_user/<username>', methods=['POST'])
@login_required
def rate_user(username):

    if current_user.is_authenticated:
        
        if current_user is None:
            return redirect('/login')
        # Get data from database and rating

        rating_value = request.form.get('rating')

        # if rating doesnt exist, prompt jsonify error
        if not rating_value:
            return jsonify(error="Missing value"), 400

        try:
        # Fetch user being rated, and prompt check
            rated_user = db.session.query(User).filter_by(username=username).first()
            if not rated_user:
                return jsonify(error='User not found'), 400
        
            # Check if user already rated this user

            # Update rating
            # So first try if it has 0 ratings then just set
            if rated_user.rating_count == 0:
                new_rating = rating_value
            # Else, update count first then calculate new average
            else:
                rated_user.count_ratings += 1
                new_rating = (rated_user.rating * (rated_user.count_ratings - 1) + rating_value) / rated_user.count_ratings
                rated_user.rating = new_rating
            db.session.add(rated_user)
            db.session.commit()

        except sqlite3.OperationalError  as err:
            print(f"An error occurred: {err}")
            db.session.rollback()
            new_rating = None

        return jsonify({'new_rating': new_rating})