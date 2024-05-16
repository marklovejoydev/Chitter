
class Peep:
    def __init__(self, id, title, content, time, user_id, name=None, username=None):
        self.id = id
        self.title = title
        self.content = content
        self.time = time
        self.user_id = user_id
        self.name = name
        self.username = username
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Peep({self.id}, {self.title}, {self.content}, {self.time}, {self.user_id})"
    
    def is_valid(self):
        if self.title == None or self.title == "":
            return False
        if self.content == None or self.content == "":
            return False
        if self.time == None or self.time == "":
            return False
        if self.user_id == None:
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.title == "" or self.title is None:
            errors.append("Title can't be blank")
        if self.content == "" or self.content is None:
            errors.append("Content can't be blank")
        if self.time == "" or self.time is None:
            errors.append("Time can't be blank")
        if self.user_id is None:
            errors.append("User ID can't be None")

        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)