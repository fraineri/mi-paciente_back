class UserRepository:
    def __init__(self, db):
        self.db = db

    def get_user_by_id(self, user_id):
        return self.db.query("SELECT * FROM users WHERE id = ?", (user_id,)).fetchone()

    def create_user(self, user_data):
        self.db.execute(
            "INSERT INTO users (name, email) VALUES (?, ?)",
            (user_data["name"], user_data["email"]),
        )
        self.db.commit()

    def update_user(self, user_id, user_data):
        self.db.execute(
            "UPDATE users SET name = ?, email = ? WHERE id = ?",
            (user_data["name"], user_data["email"], user_id),
        )
        self.db.commit()

    def delete_user(self, user_id):
        self.db.execute("DELETE FROM users WHERE id = ?", (user_id,))
        self.db.commit()
