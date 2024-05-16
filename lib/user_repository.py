from lib.user import User

class UserRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        rows = self.connection.execute("SELECT * FROM users")
        return [
            User(row["id"], row["name"], row["username"], row["email"], row["password"])
            for row in rows
        ]
    
    
    def create(self, user):
        rows = self.connection.execute(
            "INSERT INTO users (name, username, email, password) VALUES (%s, %s, %s, %s) RETURNING id",
            [user.name, user.username, user.email, user.password]
        )
        row = rows[0]
        user.id = row["id"]
        return user
    
    def get_by_email(self, email):
        rows = self.connection.execute(
            "SELECT * FROM users WHERE email = %s", [email]
        )
        for row in rows:
            return User(row["id"], row["name"], row["username"], row["email"], row["password"])
        return None
    
    def get_by_id(self, user_id):
        rows = self.connection.execute(
            "SELECT * FROM users WHERE id = %s", [user_id]
        )
        for row in rows:
            return User(row["id"], row["name"], row["username"], row["email"], row["password"])
        return None