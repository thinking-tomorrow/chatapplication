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

    query = "INSERT INTO clients (Username, Email, Password) VALUES(%s, %s, %s)"
    params = (username, email, password)

    cursor.execute(query, params)
    my_db.commit()
    return True


def send_message(message, contact, now):
    print("sent")