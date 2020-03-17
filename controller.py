from tkinter import messagebox
import database as db
import view
import re

regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def register(username, email, password, repeat_password, window):
    for x in [username, email, password, repeat_password]:
        if x == '':
            messagebox.showerror("Error", "Please fill in all the fields")
    else:
        if not (re.search(regex, email)):
            messagebox.showerror("Error", "invalid Email")
        else:
            if db.get_user(username):
                messagebox.showerror("Error", "You already have an account")
            else:
                if password != repeat_password:
                    messagebox.showerror("Error", "The passwords do not match")
                else:
                    db.add_user(username, email, password)
                    window.destroy()
                    view.chat_page()


def login(username, password, window):

    if username == '' or password == '':
        messagebox.showerror("Error", "Please fill in all the fields")
    else:
        data = db.get_user(username)

        if not data:
            messagebox.showerror("Error", "Invalid username or password")
        else:
            if data['Password'] != password:
                messagebox.showerror("Error", "Invalid username or password")
            else:
                print(True)
                window.destroy()
                view.chat_page()


view.login(login, register)
