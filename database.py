import mysql.connector as db

my_db = db.connect(host="localhost", user="root", passwd="", database="chat_application")
cursor = my_db.cursor(buffered=True)


def get_user(username):

    sql = f"SELECT * FROM clients WHERE Username='{username}'"
    cursor.execute(sql)
    my_db.commit()
    if cursor.rowcount > 0:
        data = dict(zip(cursor.column_names, cursor.fetchone()))
        return data
    else:
        return False


def add_user(username, email, password):

    query = "INSERT INTO clients (Username, Email, Password, ProfilePicture) VALUES(%s, %s, %s, %s)"
    params = (username, email, password, 'default_profile_image.png')

    cursor.execute(query, params)
    my_db.commit()
    return True


def send_message(message, contact, now, sender):
    datetime = str(now).split(' ')
    date = datetime[0]
    time = datetime[1].split('.')[0]
    print(date)
    sql = "INSERT INTO chats (message, date, time, sent_from, sent_to) VALUES(%s, %s, %s, %s, %s)"
    params = (message, date, time, sender, contact)

    cursor.execute(sql, params)
    print(cursor.statement)
    my_db.commit()
    return True


def get_contact(details):
    sql = f"SELECT * FROM clients WHERE Username='{details}' OR Email='{details}'"
    cursor.execute(sql)
    my_db.commit()

    return cursor.fetchall()
