import sqlite3
import os

db = sqlite3.connect(f'chat_application_local.db')
cursor = db.cursor()


def drop_db():
    db.close()
    os.remove("chat_application_local.db")


def create_table():
    sql = f'''
            CREATE TABLE contacts (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name           VARCHAR(256) NOT NULL,
                email               VARCHAR(256) NOT NULL,
                status              VARCHAR(256),
                profile_picture     VARCHAR(256)
            );'''

    cursor.execute(sql)
    db.commit()

    sql = ''' CREATE TABLE chats (
                ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
                user_name           VARCHAR(256) NOT NULL,
                message             VARCHAR(256) NOT NULL,
                date                VARCHAR(256) NOT NULL,
                time                VARCHAR(256) NOT NULL,
                received            BOOLEAN NOT NULL
            );
        '''

    cursor.execute(sql)
    db.commit()

    sql = ''' CREATE TABLE settings (
                ID                  INTEGER PRIMARY KEY AUTOINCREMENT,
                key                 VARCHAR(256) NOT NULL,
                value               VARCHAR(256) NOT NULL                  
            );
        '''
    cursor.execute(sql)
    db.commit()


def create_and_drop_table():
    drop_db()

    global db, cursor

    db = sqlite3.connect('chat_application_local.db')
    cursor = db.cursor()

    create_table()


def get_all_contacts():
    sql = "SELECT * FROM contacts"
    cursor.execute(sql)
    db.commit()

    contacts = [contact for contact in cursor]
    return contacts


def get_contact(username):
    sql = f"SELECT * FROM contacts WHERE user_name=='{username}'"
    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()


def get_user(detail):
    sql = f"SELECT * FROM contacts WHERE user_name=='{detail}' OR email=='{detail}'"
    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()


def get_chats(username):
    sql = f"SELECT * FROM chats WHERE user_name=='{username}'"
    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()


def add_message(message, contact, now):
    date = now.date()
    time = str(now.time()).split('.')[0]
    sql = f"INSERT INTO chats(user_name, message, date, time, received) VALUES('{contact}', '{message}', '{date}', '{time}', 'False')"
    cursor.execute(sql)
    db.commit()
    return True


def search_user(search_query):
    sql = f"SELECT * FROM contacts WHERE user_name LIKE '{search_query}%'"
    cursor.execute(sql)
    db.commit()

    return cursor.fetchall()


def add_user(user):
    sql = f"INSERT INTO contacts(user_name, email, status, profile_picture) VALUES('{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}')"

    cursor.execute(sql)
    db.commit()
    return True


def get_current_user():
    sql = "SELECT * FROM settings WHERE key='user'"
    try:
        cursor.execute(sql)
        return cursor.fetchone()[2]
    except:
        return False
    finally:
        db.commit()


def set_current_user(username):
    sql = f"INSERT INTO settings(key, value) VALUES('user', '{username}')"
    cursor.execute(sql)
    db.commit()

    return True


def get_settings(key):
    sql = "SELECT * FROM settings WHERE key='{key}'"
    try:
        cursor.execute(sql)
        return cursor.fetchone()[2]
    except:
        return False
    finally:
        db.commit()


def set_setting(key, value):
    sql = f"INSERT INTO settings(key, value) VALUES('{key}', '{value}')"
    cursor.execute(sql)
    db.commit()

    return True
