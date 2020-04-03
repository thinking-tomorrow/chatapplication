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
        view.click(contact)
    else:
        now = datetime.datetime.now()
        server_local.send_message(message, contact[1], now, database_local.get_setting('username'))
        database_local.add_message(message, contact[1], now)
        view.click(contact)


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

                    database_local.create_and_drop_table()
                    database_local.set_setting('username', username)
                    database_local.set_setting('profile_image', 'default_profile_image.png')

                    view.default()


def login(username, password, window, remember):
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
                if database_local.get_setting('username') != username:
                    try:
                        database_local.create_and_drop_table()
                        database_local.set_setting('username', username)
                    except Exception as e:
                        pass

                if remember.get() == 1:
                    database_local.set_setting('remember', 'True')
                else:
                    database_local.set_setting('remember', 'False')

                window.destroy()
                view.default()


def add_contact(contact, window):
    if str(contact).strip() == '':
        messagebox.showerror("Error", "Please enter a username or email")
    else:
        if contact == database_local.get_setting('username'):
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
                    view.default()


def change_password(password, retype_password):
    if password != retype_password:
        messagebox.showerror("Error", "Password and re-type password does not match")
    else:
        if len(password) < 6:
            messagebox.showerror("Error", "Password should be atleast six characters long")
        else:
            if server_local.change_password(database_local.get_setting('username'), password):
                messagebox.showinfo("Success", "Successfully Changed Your Password")
            else:
                messagebox.showerror("Failed", "Sorry! Failed to change your password, Please try again")


def uploadprofilepicture(username, profilepicture):
    pass
    # server_local.change_image(username, profilepicture)


view.load_function(login, register, add_contact, send_message, uploadprofilepicture, change_password)
view.homepage()
