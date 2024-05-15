import os
from flask import Flask, request, render_template, redirect
from lib.database_connection import get_flask_database_connection
from lib.user_repository import UserRepository
from lib.user import User
# Create a new Flask app
app = Flask(__name__)


@app.route('/')
def get_index():
    return render_template('chitter/index.html')

@app.route('/sign-up')
def get_signup():
    return render_template('chitter/sign-up.html')

@app.route('/home')
def home():
    return render_template('chitter/home.html')

@app.route('/sign-up', methods=['POST'])
def post_artist():
    if has_invalid_user_parameters(request.form):
        return "You need to submit a name, username, email and password", 400
    connection = get_flask_database_connection(app)
    repository = UserRepository(connection)
    
    existing_user = repository.get_by_email(request.form["email"])
    if existing_user:
        return "Email is already in use", 400
    
    user = User(
                None,
                request.form["name"],
                request.form["username"],
                request.form["email"],
                request.form["password"])
    repository.create(user)
    return redirect(f"/")

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

    if user and user.password == password:
        # Login successful, redirect user to a dashboard or profile page
        return redirect('/home')
    else:
        # Login failed, return an error message
        return "Invalid email or password", 401





if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5001)))
