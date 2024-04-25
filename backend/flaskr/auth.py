import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db
from flask_cors import CORS, cross_origin

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Initialize CORS object
cors = CORS()

# Initialize CORS policy
cors.init_app(bp)

@bp.route('/register', methods=('GET', 'POST'))
@cross_origin()
def register():
    if request.method == 'POST':
        data = request.get_json()
        email = data['email']
        username = data['username']
        password = data['password']
        db = get_db()
        error = None

        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'
        elif not email:
            error = 'Email is required.'

        if error is None:
            try:
                db.execute(
                    "INSERT INTO user (email, username, password) VALUES (?, ?, ?)",
                    (email, username, generate_password_hash(password)),
                )
                db.commit()
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                return jsonify({'message': 'User registered successfully'}), 201

        return jsonify({'error': error})

    return 'Sve super!'

@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))