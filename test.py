from tkinter import *
from tkinter import messagebox
from tkinter.font import Font
import database as db
import re


def login(**kwargs):
    x = Tk()
    x.state('zoomed')
    x.configure(background="light green")
    x.title("Login Form")
    fontFamilyy = StringVar(value="Verdana")
    fontSizze = IntVar(value=12)
    fontSizze2 = IntVar(value=8)
    appfont = Font(family=fontFamilyy.get(), size=fontSizze.get(), weight='normal')

    er = StringVar(value="Verdana")
    eri = IntVar(value=8)

    fontconfi = Font(family=er.get(), size=eri.get(), weight='normal')
    mylabel = Label(x, text="LOGIN", font=appfont, bg="light green", fg="dark green", padx=10, pady=50)
    mylabel.grid(row=0, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(x, text="Enter your username", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=2, column=4, columnspan=5)

    q = Entry(x, width=90, bg="light blue", justify="center")
    q.grid(row=3, column=4, columnspan=5, padx=10, pady=10)

    abel = Label(x, text="Enter your password", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=4, column=4, columnspan=5)

    s = Entry(x, width=90, bg="light blue", justify="center")

    s.grid(row=5, column=4, columnspan=5, padx=10, pady=10)

    ut = Checkbutton(x, text="Remember Me!!", bg="light green")
    ut.grid(row=6, column=4, padx=10, pady=10)

    bi = Button(x, text="LOGIN", fg="white", bg="black", command=lambda: [login_back(q.get(), s.get()), x.destroy()])
    bi.grid(row=7, column=4, columnspan=5, padx=30, pady=20)

    fontFamily12 = StringVar(value="Arial")
    fontSize15 = IntVar(value=7)

    tFont = Font(family=fontFamily12.get(), size=fontSize15.get(), weight='normal')

    ylabel = Button(x, text="Not yet registered??", font=tFont, bg="forest green",  command=lambda: [x.destroy(), register()])

    ylabel.grid(row=8, column=5)
    x.mainloop()


def register():
    global root
    root = Tk()
    root.state('zoomed')
    root.configure(background="light green")
    root.title("Sign-up Form")
    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=12)
    fontSize2 = IntVar(value=8)
    fontcon = Font(family=fontFamily.get(), size=fontSize.get(), weight='normal')

    qw = StringVar(value="Verdana")
    qi = IntVar(value=8)

    fontconf = Font(family=qw.get(), size=qi.get(), weight='normal')

    myLabel = Label(root, text="SIGN-UP TODAY!!", font=fontcon, bg="light green", fg="dark green", padx=20, pady=50)
    myLabel.grid(row=0, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(root, text="Enter your Username", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=1, column=4, columnspan=5)

    e = Entry(root, width=90, bg="light blue", justify="center")

    e.grid(row=2, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(root, text="Enter your email-id:", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=3, column=4, columnspan=5)

    f = Entry(root, width=90, bg="light blue", justify="center")

    f.grid(row=4, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(root, text="Enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=5, column=4, columnspan=5)

    h = Entry(root, show="*",width=90, bg="light blue", justify="center")

    h.grid(row=6, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(root, text="Re-enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=7, column=4, columnspan=5)

    g = Entry(root, width=90, bg="light blue", justify="center")

    g.grid(row=8, column=4, columnspan=5, padx=20, pady=20)

    b = Button(root, text="SUBMIT", fg="white", bg="black", command=lambda: [register_back(e.get(), f.get(), h.get(), g.get()), root.destroy()])
    b.grid(row=9, column=4, columnspan=5, padx=20, pady=20)

    fontFamily2 = StringVar(value="Arial")
    fontSize5 = IntVar(value=7)
    WFont = Font(family=fontFamily2.get(), size=fontSize5.get(), weight='normal')

    yLabel = Button(root,text="Already registered??", font=WFont, bg="forest green", command=lambda: [root.destroy(), login()], justify="center")
    yLabel.grid(row=10,column=6)

    root.mainloop()


def chat_page():
    y = Tk()
    y.configure(background="light green")
    y.title("Chat page")


regex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'


def register_back(username, email, password, repeat_password):
    for x in [username, email, password, repeat_password]:
        if x == '':
            messagebox.showerror("Error", "Please fill in all the fields")
            return
    else:
        if not (re.search(regex, email)):
            messagebox.showerror("Error", "invalid Email")
            return
        else:
            if db.get_user(username):
                messagebox.showerror("Error", "You already have an account")
                return
            else:
                if password != repeat_password:
                    messagebox.showerror("Error", "The passwords do not match")
                    return
                else:
                    db.add_user(username, email, password)
                    chat_page()


def login_back(username, password):

    data = db.get_user(username)
    if not data:
        messagebox.showerror("Error", "Please fill in all the fields")
    else:
        if data['Password'] != password:
            messagebox.showerror("Error", "Invalid username or password")
        else:
            chat_page()


login()
