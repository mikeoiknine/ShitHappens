from __future__ import print_function
import sys
import functools

from flask import (
    Blueprint, flash, redirect, request, render_template, url_for, session, g
)

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Register new user and add information to db
@bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        # get db handle

        if not email or not password:
            error = 'email and password are required'
            flash(error)

        # check db for existing user
        # if they exist, redirect to login page
        if email == 'Mike' and password == '123':
            print("Welcome, Mike", file=sys.stderr)
            return redirect(url_for('auth.login'))
        else:
            print("Not Mike: User = ", email, " pass = ", password,  file=sys.stderr)
    return render_template('auth/register.html')

# Give existing users access to site
@bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        error = None
        user = None
        if not email or not password:
            error = 'email and password are required'
            flash(error)

        # get db handle
        # if user exists, validate email and hash of password
        if email == 'Mike' and password == '123':
            print("Welcome, Mike", file=sys.stderr)
            user = User("40024934", "Mike", "Fall")
        else:
            print("Not Mike: User = ", email, " pass = ", password,  file=sys.stderr)

        if error is None:
            session.clear()
            session['user_id'] = user.id
            return redirect(url_for('home'))
        flash(error)

    return render_template('auth/login.html')


# Allow users to log out of current session
@bp.route('/logout')
def logout():
    session.clear()
    return "ok"
    # return redirect(url_for('index'))

