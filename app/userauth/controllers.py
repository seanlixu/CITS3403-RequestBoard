# where rate user function should go
from app import app
import flask
from flask import Flask
import sqlite3
from flask import jsonify, render_template, redirect, request
from flask_login import LoginManager, current_user, login_required
# User rating function
@app.route('/rate_user/<username>', methods=['POST'])
@login_required
def rate_user(username):
    if current_user is None:
        return redirect('/login')
    # Get data from database and rating
    # Get data

    rating_value = request.form.get('rating')


    # if rating doesnt exist, prompt jsonify error
    if not rating_value:
        return jsonify(error="Missing value"), 400
    
    # Connec to db
    con = sqlite3.connect('users.db')
    cur = con.cursor()

    try:
    # Fetch user being rated, and prompt check
        cur.execute('SELECT id, rating FROM user WHERE username=?', (username,))
        rated_user = cur.fetchone()
        if not rated_user:
            con.close()
            return jsonify(error='User not found'), 400
        # Check if user already rated this user

        # Update rating
        # So first try if it has 0 ratings then just set
        count_ratings = rated_user[4]
        if count_ratings == 0:
            new_rating = rating_value
            cur.execute('UPDATE user SET rating_count=1 WHERE id=?', rated_user[0])
        # Else, update count first then calculate new average
        else:
            count_ratings += 1
            new_rating = (rated_user[3] * (count_ratings - 1) + rating_value) / count_ratings
            cur.execute('UPDATE user SET rating=?, rating_count=? WHERE id = ?', (new_rating, count_ratings, rated_user[0]))

        con.commit()

    except sqlite3.OperationalError  as err:
        print(f"An error occurred: {err}")
        new_rating = None

    return jsonify({'new_rating': new_rating})