from lib.peep import Peep

"""
Peep constructs with an id, title, content, time, and user_id
"""
def test_peep_constructs():
    peep = Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1)
    assert peep.id == 1
    assert peep.title == "My First Peep"
    assert peep.content == "This is the content of my first peep."
    assert peep.time == '12:34'
    assert peep.user_id == 1


"""
We can compare two identical peeps and have them be equal
"""
def test_peeps_are_equal():
    peep1 = Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1)
    peep2 = Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1)
    assert peep1 == peep2
    
"""
We can format peeps to strings nicely
"""
def test_peep_format_nicely():
    peep = Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1)
    assert str(peep) == "Peep(1, My First Peep, This is the content of my first peep., 12:34, 1)"
    
"""
We can assess a peep for validity
"""
def test_peep_validity():
    assert Peep(1, "", "", '', None).is_valid() == False
    assert Peep(1, "", "This is the content of my first peep.", '12:34', 1).is_valid() == False
    assert Peep(1, "My First Peep", "", '12:34', 1).is_valid() == False
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '', 1).is_valid() == False
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', None).is_valid() == False
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1).is_valid() == True

"""
We can generate errors for an invalid Peep
"""
def test_peep_errors():
    assert Peep(1, "", "", '', None).generate_errors() == "Title can't be blank, Content can't be blank, Time can't be blank, User ID can't be None"
    assert Peep(1, "", "This is the content of my first peep.", '12:34', 1).generate_errors() == "Title can't be blank"
    assert Peep(1, "My First Peep", "", '12:34', 1).generate_errors() == "Content can't be blank"
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '', 1).generate_errors() == "Time can't be blank"
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', None).generate_errors() == "User ID can't be None"
    assert Peep(1, "My First Peep", "This is the content of my first peep.", '12:34', 1).generate_errors() == None