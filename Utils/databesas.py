# bot  databesas 
import sqlite3, json, os


class Databesas:
    
    def __init__(self):
        self.PAT = './data/databesas.db' # Databesas File PAth 
        if not os.path.isfile(self.PAT):
            with sqlite3.connect(self.PAT) as client:
                cursor = client.cursor()
                cursor.execute("""CREATE TABLE IF NOT EXISTS sessions (
                               id INTEGER, phone_number TEXT,first_name TEXT, username TEXT, sessions_string TEXT
                )
                """)
                
                client.commit()

    def ADD_NEW_SESSIONS(self, user_id: int, phone_number: str, first_name: str, username: str, session_string: str):
        # ADD NEW SESSION 
        with sqlite3.connect(self.PAT) as client:
            cursor = client.cursor()
            cursor.execute(""" INSERT INTO sessions VALUES (? ,? ,? ,?, ?);""", (
                     user_id, phone_number, first_name, username, session_string
            ))
            client.commit()

    def GET_ALL_SESSIONS(self):
        Obj  = {} # Databeasa Obj
        # GEt All Session 
        with sqlite3.connect(self.PAT) as client:
            cursor = client.cursor()
            data = cursor.execute("""SELECT * from sessions""").fetchall()
            for session in data:
                Obj.update({session[0]:{'id':session[0], 'phone_number':session[1], 'first_name':session[2], 'username':session[3], 'session_string':session[4]}})
        return Obj
    
    def GET_SESSIONS_COUNT(self):
        return len(self.GET_ALL_SESSIONS())
    
    def DELETE_SESSION(self, session_id: int):
        with sqlite3.connect(self.PAT) as client:
            cursor = client.cursor()
            cursor.execute(f"DELETE from sessions WHERE id = {session_id}")
            client.commit()


