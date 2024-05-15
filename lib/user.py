class User:
    def __init__(self, id, name, username, email, password):
        self.id = id
        self.name = name
        self.username = username
        self.email = email
        self.password = password
        
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"User({self.id}, {self.name}, {self.username}, {self.email}, {self.password})"
    
    def is_valid(self):
        if self.name == None or self.name == "":
            return False
        if self.username == None or self.username == "":
            return False
        if self.email == None or self.email == "":
            return False
        if self.password == None or self.password == "":
            return False
        return True

    def generate_errors(self):
        errors = []
        if self.name == "" or self.name is None:
            errors.append("Name can't be blank")
        if self.username == "" or self.username is None:
            errors.append("Username can't be blank")
        if self.email == "" or self.email is None:
            errors.append("Email can't be blank")
        if self.password == "" or self.password is None:
            errors.append("Password can't be blank")

        if len(errors) == 0:
            return None
        else:
            return ", ".join(errors)