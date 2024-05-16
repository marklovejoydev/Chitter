from lib.peep_repository import PeepRepository
from lib.peep import Peep
from lib.user import User
from datetime import datetime

# Update test_all
def test_all(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    retrieved_peeps = repository.all()
    
    # Assert individual attributes of the retrieved peep with the expected peep
    assert len(retrieved_peeps) == 1  # Ensure only one peep is retrieved
    assert retrieved_peeps[0].id == 1
    assert retrieved_peeps[0].title == "My First Peep"
    assert retrieved_peeps[0].content == "This is the content of my first peep."
    assert retrieved_peeps[0].time == '12:34'
    assert retrieved_peeps[0].user_id == 1
    
# Update test_create
def test_create(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    current_time = datetime.now().strftime('%H:%M')
    peep = Peep(1, "My Second Peep", "This is the content of my second peep.", current_time, 1)
    created_peep = repository.create(peep)
    
    # Query the database to get the newly created peep
    new_peep_from_db = repository.all()[-1]  # Assuming the newly created peep is the last one
    
    # Compare the attributes of the created peep and the peep retrieved from the database
    assert created_peep.title == new_peep_from_db.title
    assert created_peep.content == new_peep_from_db.content
    assert created_peep.time == new_peep_from_db.time
    assert created_peep.user_id == new_peep_from_db.user_id
"""
when I call get_user_details
I get the user details (name and email) for the given user ID
"""
def test_get_user_details(db_connection):
    db_connection.seed("seeds/chitter.sql")
    repository = PeepRepository(db_connection)
    assert repository.get_user_details(1) == {
        "name": "Mark Lovejoy",
        "username": "lovejoy01"
    }