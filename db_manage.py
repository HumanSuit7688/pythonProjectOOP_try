import sqlite3 as sql3


class DataBase:

    def __init__(self, path):
        self.path = path

    def connect(self):
        conn = sql3.connect(self.path)
        return conn

# c.execute("CREATE TABLE users ("
#           "id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,"
#           "username TEXT,"
#           "user_id TEXT"
#           ")"
# )

# c.execute("INSERT INTO users VALUES (?, ?, ?)", (0, 'тест', 'тест'))

#'OOPmain.db'

# def sign_up_db(username, user_id):
#     c.execute("SELECT * FROM users WHERE user_id = ?", (user_id,))
#     row = c.fetchall()
#     if not row:
#         c.execute("INSERT INTO users(username,user_id) VALUES(?, ?)", (username, user_id))
#         conn.commit()


class User:

    def __init__(self, username, user_id):
        self.username = username
        self.user_id = user_id

    def return_all_options(self):
        print(self.username)
        print(self.user_id)

    def load_into_db(self, db):
        con = db.connect()
        c = con.cursor()
        c.execute("SELECT * FROM users WHERE user_id = ?", (self.user_id,))
        row = c.fetchall()
        if not row:
            c.execute("INSERT INTO users(username,user_id) VALUES(?, ?)", (self.username, self.user_id))
            con.commit()
