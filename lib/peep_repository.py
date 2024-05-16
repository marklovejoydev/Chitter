from lib.peep import Peep
from lib.user import User
from datetime import datetime

class PeepRepository:
    def __init__(self, connection):
        self.connection = connection
    
    def all(self):
        query = """
                SELECT peeps.id, peeps.title, peeps.content, to_char(peeps.time, 'HH24:MI') AS time, peeps.user_id, users.name, users.username
                FROM peeps
                JOIN users ON peeps.user_id = users.id
                ORDER BY peeps.time DESC
                """
        rows = self.connection.execute(query)
        print(rows[0].keys())
            
        return [
            Peep(row["id"], row["title"], row["content"], row["time"], row["user_id"], row["name"], row["username"])
            for row in rows
        ]
    
    def create(self, peep):
        current_time = datetime.now().strftime('%H:%M')
        rows = self.connection.execute(
            "INSERT INTO peeps (title, content, time, user_id) VALUES (%s, %s, %s, %s) RETURNING id",
            [peep.title, peep.content, current_time, peep.user_id]
        )
        row = rows[0]
        peep.id = row["id"]
        return peep

    
    def get_user_details(self, user_id):
        rows = self.connection.execute(
            "SELECT name, username FROM users WHERE id = %s", [user_id]
        )
        row = rows[0]
        return {"name": row["name"], "username": row["username"]}