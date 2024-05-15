from lib.user_repository import UserRepository

from lib.user import User

"""
when io call #all
i get all the artists in the artists table
"""

def test_all(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    assert repository.all() == [
        User(1, "Mark Lovejoy", "lovejoy01", 'marklovejoy@gmail.com', 'Test123')
    ]
    
"""
when i call create
i create an album in the database
and i can see it back in all
"""


def test_create(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = UserRepository(db_connection)
    user = User(2, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    repository.create(user)
    assert repository.all() == [
        User(1, "Mark Lovejoy", "lovejoy01", 'marklovejoy@gmail.com', 'Test123'),
        User(2, "Mark", "mark01", 'mark@gmail.com', 'Test123')
    ]