from tkinter import messagebox
import server_local
import database_local
import datetime
import view
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def send_message(message, contact, page):
    page.destroy()
    if str(message).strip() == '':
        view.click(contact, send_message)
    else:
        now = datetime.datetime.now()
        server_local.send_message(message, contact[1], now, database_local.get_current_user())
        database_local.add_message(message, contact[1], now)
        view.click(contact, send_message)


def register(username, email, password, repeat_password, window):

    for x in [username, email, password, repeat_password]:
        if x == '':
            messagebox.showerror("Error", "Please fill in all the fields")
            break
    else:
        if not (re.search(regex, email)):
            messagebox.showerror("Error", "invalid Email")
        else:
            if server_local.get_user(username):
                messagebox.showerror("Error", "This username has already been taken!")
            else:
                if password != repeat_password:
                    messagebox.showerror("Error", "The passwords do not match")
                else:
                    server_local.add_user(username, email, password)
                    window.destroy()
                    view.default(username, send_message)

                    database_local.create_and_drop_table()
                    database_local.set_current_user(username)


def login(username, password, window):
    if username == '' or password == '':
        messagebox.showerror("Error", "Please fill in all the fields")
    else:
        data = server_local.get_user(username)
        if not data:
            messagebox.showerror("Error", "Invalid username or password")
        else:
            if data['Password'] != password:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                if database_local.get_current_user() != username:
                    # database_local.drop_db()
                    try:
                        database_local.create_and_drop_table()
                        database_local.set_current_user(username)
                    except Exception as e:
                        pass

                window.destroy()
                view.default(data['Username'], send_message)


def add_contact(contact, window, username):
    if str(contact).strip() == '':
        messagebox.showerror("Error", "Please enter a username or email")
    else:
        if contact == database_local.get_current_user():
            messagebox.showerror("Error", "You cannot add yourself")
        else:
            if database_local.get_user(contact):
                messagebox.showerror("Error", "User already in contacts")
            else:
                if not server_local.get_contact(contact):
                    messagebox.showerror("Error", "No such user")
                else:
                    user = server_local.get_contact(contact)[0]
                    database_local.add_user((user[0], user[1], user[2], user[3], user[5]))

                    window.destroy()
                    view.default(username, send_message)


view.load_function(add_contact)
view.login(login, register)
