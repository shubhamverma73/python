import mysql.connector


class user_model():
    def __init__(self):
        try:
            self.connection = self.connection = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="python"
            )
            self.cursor = self.connection.cursor(dictionary=True)
            self.connection.autocommit = True
        except mysql.connector.Error as err:
            print(f"Error: {err}")
            self.connection = None

    def get_users_data(self):
        if not self.connection:
            return "Database connection error", 500

        self.cursor.execute("SELECT name, email, password FROM users")
        users = self.cursor.fetchall()
        print(f"Users: {users}")
        if len(users) > 0:
            return users, 200
        else:
            return "No users found", 404
        
    def create_users_data(self, data):
        if not self.connection:
            return "Database connection error", 500

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        try:
            self.cursor.execute(
                "INSERT INTO users (name, email, password) VALUES (%s, %s, %s)",
                (name, email, password)
            )
            #self.connection.commit()
            return "User created successfully", 201

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Error occurred while creating user", 500
        
    def update_user(self, user_id, data):
        if not self.connection:
            return "Database connection error", 500

        name = data.get("name")
        email = data.get("email")
        password = data.get("password")

        try:
            self.cursor.execute(
                "UPDATE users SET name=%s, email=%s, password=%s WHERE user_id=%s",
                (name, email, password, user_id)
            )

            if self.cursor.rowcount == 0:
                return "User not found", 404
            # self.connection.commit()
            return "User updated successfully", 200

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Error occurred while updating user", 500
        
    def patch_user(self, user_id, data):

        fields = []
        values = []

        if "name" in data:
            fields.append("name=%s")
            values.append(data["name"])

        if "email" in data:
            fields.append("email=%s")
            values.append(data["email"])

        if "password" in data:
            fields.append("password=%s")
            values.append(data["password"])

        if not fields:
            return "Nothing to update", 400

        query = f""" UPDATE users SET {", ".join(fields)} WHERE user_id=%s """
        values.append(user_id)

        self.cursor.execute(query, values)

        if self.cursor.rowcount == 0:
            return "User not found", 404

        return "User updated successfully", 200
        
    def delete_user(self, user_id):
        if not self.connection:
            return "Database connection error", 500

        try:
            self.cursor.execute(
                "DELETE FROM users WHERE user_id=%s",
                (user_id,)
            )

            if self.cursor.rowcount == 0:
                return "User not found", 404
            return "User deleted successfully", 200

        except mysql.connector.Error as err:
            print(f"Error: {err}")
            return "Error occurred while deleting user", 500