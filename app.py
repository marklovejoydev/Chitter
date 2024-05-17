import os
import re
from flask import Flask, request, render_template, redirect, session
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
from lib.peep_repository import PeepRepository
from lib.peep import Peep
from datetime import datetime
import bcrypt

app = Flask(__name__)
app.secret_key = "enigma"

@app.route('/')
def get_home():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    peeps = repository.all()
    user = None
    if 'user_id' in session:
        user_repository = UserRepository(connection)
        user = user_repository.get_by_id(session['user_id'])
    
    return render_template('chitter/home.html', peeps=peeps, user=user)

@app.route('/create')
def create_form():
    return render_template('chitter/new_peep.html')

@app.route('/create', methods=['POST'])
def create_peep():
    connection = get_flask_database_connection(app)
    repository = PeepRepository(connection)
    
    title = request.form['title']
    content = request.form['content']
    user_id = session.get('user_id')
    time = datetime.now().strftime('%H:%M')
    
    peep = Peep(id=user_id, title=title, content=content, time=time, user_id=user_id)
    repository.create(peep)
    
    return redirect('/')


@app.route('/sign-up')
def get_signup():
    return render_template('chitter/sign-up.html')

@app.route('/sign-in')
def sign_in():
    return render_template('chitter/index.html')

@app.route('/sign-up', methods=['POST'])
def post_signup():
    if has_invalid_user_parameters(request.form):
        return "You need to submit a name, username, email and password", 400
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    
    existing_user = repository.get_by_email(request.form["email"])
    if existing_user:
        return "Email is already in use", 400
    
    password = request.form["password"]
    if not is_valid_password(password):
        return "Password must have at least 1 capital letter, 1 number, and be greater than 4 in length", 400
    
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    hashed_password_str = hashed_password.decode('utf-8')  # Store the hash as a string
    print(f"Hashed password: {hashed_password_str}")  # Debugging line
    
    user = User(
        None,
        request.form["name"],
        request.form["username"],
        request.form["email"],
        hashed_password_str
    )
    repository.create(user)
    return redirect(f"/sign-in")

def has_invalid_user_parameters(form):
    return 'name' not in request.form or 'username' not in request.form or 'email' not in request.form or 'password' not in request.form 

@app.route('/login', methods=['POST'])
def login():
    email = request.form.get('email')
    password = request.form.get('password')

    if not email or not password:
        return "Email and password are required", 400

    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)

    user = repository.get_by_email(email)
    
    if user:
        stored_password_hash = user.password
        print(f"Stored password hash: {stored_password_hash}")  # Debugging line
        if bcrypt.checkpw(password.encode('utf-8'), stored_password_hash.encode('utf-8')):
            session['user_id'] = user.id
            return redirect('/')
    
    return "Invalid email or password", 401


def is_valid_password(password):
    if len(password) < 5:
        return False
    if not re.search("[A-Z]", password):
        return False
    if not re.search("[0-9]", password):
        return False
    return True

@app.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return redirect('/')


if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
