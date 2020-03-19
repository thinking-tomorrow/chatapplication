import sqlite3

db = sqlite3.connect('chat_application_local.db')
cursor = db.cursor()


def create_table():
    sql = '''CREATE TABLE contacts (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name           VARCHAR(256) NOT NULL,
                email               VARCHAR(256) NOT NULL,
                status              VARCHAR(256),
                profile_picture     VARCHAR(256)
            );    
        '''

    cursor.execute(sql)
    db.commit()

    sql = '''CREATE TABLE chats (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name           VARCHAR(256) NOT NULL,
                message             VARCHAR(256) NOT NULL,
                time                VARCHAR(256) NOT NULL
            );'''
    cursor.execute(sql)
    db.commit()


def get_all_contacts():
    sql = "SELECT * FROM contacts"
    cursor.execute(sql)
    db.commit()

    contacts = [contact for contact in cursor]
    return contacts


create_table()

sql = "INSERT INTO contacts(user_name, email, status, profile_picture) VALUES('sajjad', 'sajjad@gmail.com', 'hello', 'test.png')"
cursor.execute(sql)

sql = "SELECT * FROM contacts"
cursor.execute(sql)

print(cursor.fetchall())