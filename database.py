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

    query = "INSERT INTO clients (Username, Email, Status, Password, ProfilePicture) VALUES(%s, %s, %s, %s, %s)"
    params = (username, email, f'Hey there! I am {username}', password, 'default_profile_image.png')

    cursor.execute(query, params)
    my_db.commit()
    return True


def send_message(message, contact, now):
    print("sent")


def get_contact(details):
    sql = f"SELECT * FROM clients WHERE Username='{details}' OR Email='{details}'"
    cursor.execute(sql)
    my_db.commit()

    return cursor.fetchall()
