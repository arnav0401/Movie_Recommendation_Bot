import sqlite3


class DBHelper:
    def __init__(self, dbname="todo.sqlite"):
        self.dbname = dbname
        self.conn = sqlite3.connect(dbname)

    def setup(self):
        stmt = '''CREATE TABLE IF NOT EXISTS userdata
    (
    id INTEGER NOT NULL PRIMARY KEY UNIQUE, 
    );'''
        self.conn.execute(stmt)
        self.conn.commit()

    def add_user(self, user_id):
        stmt = "INSERT INTO userdata (id) VALUES (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def delete_user(self, user_id):
        stmt = "DELETE FROM userdata WHERE id = (?)"
        args = (user_id, )
        self.conn.execute(stmt, args)
        self.conn.commit()

    def get_users(self):
        stmt = "SELECT description FROM userdata"
        return [x[0] for x in self.conn.execute(stmt)]

    def check_user(self, user_id):
        cur = self.conn.cursor()
        if len(cur.execute('''SELECT id FROM userdata WHERE id = ?''')).fetchall() > 0:
            print('Past user')
        else:
            cur.execute('''INSERT or IGNORE INTO userdata (id) VALUES (?)''')
            print('New user')
        self.conn.commit()