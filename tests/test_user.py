from lib.user import User

"""
user constructs with an id, name, username, email and password
"""
def test_user_constructs():
    user = User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    assert user.id == 1
    assert user.name == "Mark"
    assert user.username == "mark01"
    assert user.email == "mark@gmail.com"
    assert user.password == "Test123"


"""
We can compare two identical users
And have them be equal
"""
def test_users_are_equal():
    user1 = User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    user2 = User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    assert user1 == user2
    
"""
We can format users to strings nicely
"""
def test_user_format_nicely():
    user = User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    assert str(user) == "User(1, Mark, mark01, mark@gmail.com, Test123)"
    
"""
We can assess a user for validity
"""
def test_user_validity():
    assert User(1, "", "", '', '').is_valid() == False
    assert User(1, "", "mark01", 'mark@gmail.com', 'Test123').is_valid() == False
    assert User(1, "Mark", "mark01", '', 'Test123').is_valid() == False
    assert User(1, "Mark", "", 'mark@gmail.com', 'Test123').is_valid() == False
    assert User(1, "Mark", "mark01", 'mark@gmail.com',"").is_valid() == False
    assert User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123').is_valid() == True
    assert User(None, "Mark", "mark01", 'mark@gmail.com', 'Test123').is_valid() == True

"""
We can generate errors for an invalid User
"""
def test_user_errors():
    assert User(1, "", "", '', '').generate_errors() == "Name can't be blank, Username can't be blank, Email can't be blank, Password can't be blank"
    assert User(1, "", "mark01", 'mark@gmail.com', 'Test123').generate_errors() == "Name can't be blank"
    assert User(1, "Mark", "mark01", '', 'Test123').generate_errors() == "Email can't be blank"
    assert User(1, "Mark", "", 'mark@gmail.com', 'Test123').generate_errors() == "Username can't be blank"
    assert User(1, "Mark", "mark01", 'mark@gmail.com',"").generate_errors() == "Password can't be blank"
    assert User(1, "Mark", "mark01", 'mark@gmail.com', 'Test123').generate_errors() == None
    assert User(None, "Mark", "mark01", 'mark@gmail.com', 'Test123').generate_errors() == None

