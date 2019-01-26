from __future__ import print_function
import sys, functools, json

from flask import (
    Blueprint, flash, redirect, request, render_template, url_for, session, Response
)
from werkzeug.security import check_password_hash, generate_password_hash

from .database import db_session
from .models import User

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register new user and add information to db
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None

        if not username or not password:
            error = 'username and password are required'
            flash(error)

        # check db for existing user
        # if they exist, redirect to login page
        for user in User.query.all():
            if username == user.username:
                error = "Username already in use!"
                flash(error)
                return render_template('auth/register.html')

        user = User(username, generate_password_hash(password))
        db_session.add(user)
        db_session.commit()

        return redirect(url_for('auth.login'))
    return render_template('auth/register.html')

# Give existing users access to site
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        error = None
        user  = None

        if not username or not password:
            error = 'username and password are required'
            flash(error)

        # get db handle
        # if user exists, validate username and hash of password
        error = 'Wrong username or password'
        for user in User.query.all():
            if username == user.username and generate_password_hash(password) == user.password:
                error = None

                break


        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('index'))

        flash(error)

    return render_template('auth/login.html')


# Allow users to log out of current session
@bp.route('/logout')
def logout():
    session.clear()
    return "ok"
    # return redirect(url_for('index'))

@bp.route('/users', methods=['GET'])
def get_users():
    return Response(json.dumps([{
        'username'       : query.username,
        'password'       : query.password,
        'rank'           : query.rank}
        for query in User.query.all()]), mimetype='application/json')

