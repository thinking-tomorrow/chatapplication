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
                ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name           VARCHAR(256) NOT NULL,
                message             VARCHAR(256) NOT NULL,
                date                VARCHAR(256) NOT NULL,
                time                VARCHAR(256) NOT NULL,
                received            BOOLEAN NOT NULL
            );'''
    cursor.execute(sql)
    db.commit()


def get_all_contacts():
    sql = "SELECT * FROM contacts"
    cursor.execute(sql)
    db.commit()

    contacts = [contact for contact in cursor]
    return contacts


def get_contact(username):
    sql = f"SELECT * FROM contacts WHERE user_name=={username}"
    cursor.execute()
    db.commit()

    if cursor.rowcount > 0:
        return cursor.fetchone()
    else:
        return False


def get_chats(username):
    sql = f"SELECT * FROM chats WHERE user_name=='{username}'"
    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()


try:
    create_table()
except Exception:
    if __name__ == '__main__':
        # sql = "INSERT INTO contacts(user_name, email, status, profile_picture) VALUES('aritra', 'aritra@gmail.com', 'Hi', 'test4.jpg')"
        sql2 = "INSERT INTO chats(user_name, message, date, time, received) VALUES('ayush', 'ok no problem.', '20-03-2020', '14:12', 'True')"

        # cursor.execute(sql)
        cursor.execute(sql2)
        db.commit()
        # print(cursor.fetchone())
        print("done")
    pass
