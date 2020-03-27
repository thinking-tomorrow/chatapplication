from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import database_local as db

user = ''


def load_function(func):
    global add_contact_backend
    add_contact_backend = func


def login(login_backend, register_backend):
    x = Tk()
    x.state('zoomed')
    # x.geometry(f"570x{x.winfo_screenheight()}")
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
    mylabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    abel = Label(x, text="Enter your username", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.2, anchor=CENTER)

    q = Entry(x, width=90, bg="#BEFAFA", relief="sunken", justify="center", highlightcolor = "blue")
    q.place(relx=0.5, rely=0.3, anchor=CENTER)

    abel = Label(x, text="Enter your password", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.4, anchor=CENTER)

    s = Entry(x, show="*", width=90, justify="center", bg="#BEFAFA", relief="sunken")

    s.place(relx=0.5, rely=0.5, anchor=CENTER)

    remember = IntVar()

    ut = Checkbutton(x, text="Remember Me!!", bg="light green", variable=remember)
    ut.place(relx=0.5, rely=0.6, anchor=CENTER)

    bi = Button(x, text="LOGIN", fg="white", bg="black", width=12, command=lambda: [login_backend(q.get(), s.get(), x, remember)])
    bi.place(relx=0.5, rely=0.7, anchor=CENTER)

    fontFamily12 = StringVar(value="Arial")
    fontSize15 = IntVar(value=7)

    tFont = Font(family=fontFamily12.get(), size=fontSize15.get(), weight='normal')

    ylabel = Button(x, text="Not yet registered??", font=tFont, bg="forest green",
                    command=lambda: [x.destroy(), register(register_backend, login_backend)])

    ylabel.place(relx=0.5, rely=0.8, anchor=CENTER)

    Button(x, text="EXIT", fg="red", command=x.destroy).place(relx=0.1, rely=0.1)

    x.mainloop()


def register(register_backend, login_backend):
    global root
    root = Tk()
    root.state('zoomed')

    root.configure(background="light green")
    root.title("Sign-up Form")
    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=12)

    fontcon = Font(family=fontFamily.get(), size=fontSize.get(), weight='normal')

    qw = StringVar(value="Verdana")
    qi = IntVar(value=8)

    fontconf = Font(family=qw.get(), size=qi.get(), weight='normal')

    myLabel = Label(root, text="SIGN-UP TODAY!!", font=fontcon, bg="light green", fg="dark green", padx=20, pady=50)
    myLabel.place(relx=0.5, rely=0.1, anchor=CENTER)

    abel = Label(root, text="Enter your Username", bg = "light green", font=fontconf, fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.2, anchor=CENTER)

    e = Entry(root, width=90, bg="#BEFAFA", relief="sunken", justify="center")

    e.place(relx=0.5, rely=0.25, anchor=CENTER)

    abel = Label(root, text="Enter your email-id:", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.3, anchor=CENTER)

    f = Entry(root, width=90, bg="#BEFAFA", relief="sunken", justify="center")

    f.place(relx=0.5, rely=0.35, anchor=CENTER)

    abel = Label(root, text="Enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.4, anchor=CENTER)

    h = Entry(root, width=90, show="*", bg="#BEFAFA", relief="sunken", justify="center")

    h.place(relx=0.5, rely=0.45, anchor=CENTER)

    abel = Label(root, text="Re-enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10,
                 pady=10)
    abel.place(relx=0.5, rely=0.5, anchor=CENTER)

    g = Entry(root, show="*", width=90, bg="#BEFAFA", relief="sunken", justify="center")

    g.place(relx=0.5, rely=0.55, anchor=CENTER)

    b = Button(root, text="SUBMIT", fg="white", width=12, bg="black",
               command=lambda: [register_backend(e.get(), f.get(), h.get(), g.get(), root)])
    b.place(relx=0.5, rely=0.6, anchor=CENTER)

    fontFamily2 = StringVar(value="Arial")
    fontSize5 = IntVar(value=7)
    WFont = Font(family=fontFamily2.get(), size=fontSize5.get(), weight='normal')

    yLabel = Button(root, text="Already registered??", font=WFont, bg="forest green",
                    command=lambda: [root.destroy(), login(login_backend, register_backend)], justify="center")
    yLabel.place(relx=0.5, rely=0.7, anchor=CENTER)

    root.mainloop()


def add_contact(send):

    a = Tk()
    a.state('zoomed')
    a.configure(background="light green")
    a.title('Add Contacts')

    Button(a, text=" <- Back ", font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
           command=lambda: [a.destroy(), default(user, send)]).place(relx=0.1, rely=0.1)

    Label(a, text="ADD CONTACTS", font=('Verdana', 20, 'bold'), bg="light green", fg='dark green').place(relx=0.375, rely=0.1)

    Label(a, text="Enter the Contact-Name or Contact Email-ID", font=('Verdana', 10, 'bold'), bg="light green", fg='dark green').place(relx=0.35, rely=0.3)

    contact = Entry(a, bg="#BEFAFA", relief="sunken", width=90)
    contact.place(relx=0.3, rely=0.4)

    Button(a, text="Add Contact", bg="black", fg="white", command=lambda: [add_contact_backend(contact.get(), a, user)]).place(relx=0.45, rely=0.9)

    a.mainloop()


def click(contact, send_function):
    chat_page = Tk()
    chat_page.state('zoomed')
    chat_page.configure(background="light blue")
    chat_page.title(contact[1])

    chats = db.get_chats(contact[1])

    Button(chat_page, text=" <- Back ", font=("Courier", 8, "bold"), padx=20, bg="white", fg="red",
           command=lambda: [chat_page.destroy(), default(user, send_function)]).grid(row=0, column=0)

    contact_details = Frame(chat_page, bg="light blue", pady=20, padx=300)
    contact_details.grid(row=0, column=1, columnspan=2)

    profileimg = Image.open(f'images/profile_image/{contact[4]}')
    profileimage = profileimg.resize((30, 30), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage,master=chat_page)
    buttonforprofileimage = Button(contact_details, image=openprofileimage)
    buttonforprofileimage.grid(row=0, column=1)
    buttonforprofileimage.image = openprofileimage

    Button(contact_details, text=contact[1], font=("Courier", 12, "bold"), bg="light green", fg="red").grid(
        row=0, column=2)

    if not chats:
        messagebox = Frame(chat_page, bg="pink")
        messagebox.grid(row=1, column=2)

        Label(messagebox, text="No chat history!!", bg="pink", fg="black").grid(row=1, column=0)

    else:

        mainframe = Frame(chat_page, bg="light blue")
        mainframe.grid(row=1, column=0, rowspan=200, columnspan=20)
        canvas = Canvas(mainframe, height=400, width=1250, bg="light blue")

        frame = Frame(canvas, bg="light blue")

        scroll_y = Scrollbar(mainframe, orient="vertical", command=canvas.yview)

        row_number = 2
        for chat in chats:
            if chat[5] == 'True':
                messagebox = Frame(frame, bg="pink")
                messagebox.grid(row=row_number, column=0)

                Label(messagebox, text=chat[2], bg="pink", fg="black").grid(row=row_number, column=0)
                Label(messagebox, text=chat[4], bg="pink", font=("Arial", 6, 'roman'), padx=5, pady=10).grid(row=row_number, column=1)
                row_number += 2

            else:
                messagebox2 = Frame(frame, bg="light blue", padx=800)
                messagebox2.grid(row=row_number, column=13, columnspan=3)

                Label(messagebox2, text=chat[2], bg="snow", fg="black").grid(row=row_number, column=15)
                Label(messagebox2, text=chat[4], bg="light blue", fg="red", font=("Arial", 6, 'roman')).grid(row=row_number+1, column=16)

                row_number += 2

        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
        canvas.yview_scroll(1,"page")
        canvas.yview_moveto(1)
        canvas.grid(row=0, column=0, columnspan=20, rowspan=200)
        scroll_y.grid(row=0, column=21, rowspan=300, sticky='ns')

    entryforchatbox = Entry(chat_page, borderwidth=5, bg="yellow", justify="center")
    entryforchatbox.place(relx=0.4, rely=0.9)

    send = Image.open('images/send.png')
    imageforsend = send.resize((20, 20), Image.ANTIALIAS)
    openimageforsend = ImageTk.PhotoImage(imageforsend,master=chat_page)
    buttonforsend = Button(chat_page, image=openimageforsend, command=lambda: [send_function(entryforchatbox.get(), contact, chat_page)])

    buttonforsend.place(relx=0.5, rely=0.9)
    buttonforsend.image = openimageforsend

    chat_page.mainloop()


def on_keypress(username, send, char, window, test):
    window.destroy()
    if ord(char) == 8:
        test = test[:-1]
    else:
        test = test+char
    default(username, send, test)

def settings(username,send):
    s = Tk()
    s.state('zoomed')
    s.title('Settings')
    s.configure(background='#ECE5DD')


    frame = Frame(s,bg="#25D366",width=2000,height=100)
    frame.place(relx=0.00001,rely=0.0000001)

    Label(frame,text="SETTINGS",bg="#25D366",fg="white",font=('Helvetica',15,'bold')).place(relx=0.32,rely=0.25)

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=frame)

    backbutton = Button(frame, image=openbackimage,command=lambda: [s.destroy(), default(user, send)] )

    backbutton["border"] = "0"
    backbutton["bg"] = "#25D366"
    backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
    backbutton.image = openbackimage

    userimg = Image.open('images/default_profile_image.png')
    userimage = userimg.resize((50, 50), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage, master=s)

    buttonforuserimage = Button(s, image=openuserimage )

    buttonforuserimage["border"] = "0"
    buttonforuserimage["bg"] = "#ECE5DD"
    buttonforuserimage.place(relx=0.5, rely=0.24, anchor=CENTER)
    buttonforuserimage.image = openuserimage

    Label(s, text= f"{username}",bg='#ECE5DD',fg='#075E54', font=('Kalpurush', 20, 'bold')).place(relx=0.45,rely=0.3)

    b = Button(s,text='Change your Password',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w')
    b.place(relx=0.00001,rely=0.4)

    Label(b,text='Change your Password if u want to...',bg="#ECE5DD",fg='#25D366',font=('Helvetica',10,'normal')).place(relx=0.7,rely=0.4)

    s.mainloop()


def default(username, send, query=''):
    global user
    user = username
    root = Tk()
    root.state("zoomed")
    root.title("Chat Page")
    root.configure(background="light green")

    if query != '':
        Button(root, text=" <- Back ", font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
               command=lambda: [root.destroy(), default(user, send)]).grid(row=0, column=0)
    else:
        pass

    username = Label(root, font=('Kalpurush', 20, 'bold'), text=f"{username}", bg="light green", fg="red")
    username.place(relx=0.5, rely=0.1, anchor=N)

    userimg = Image.open('images/default_profile_image.png')
    userimage = userimg.resize((50, 50), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage, master=root)

    buttonforuserimage = Button(root, image=openuserimage, bg="light green")

    buttonforuserimage["border"] = "0"
    buttonforuserimage["bg"] = "light green"
    buttonforuserimage.place(relx=0.5, rely=0.04, anchor=CENTER)
    buttonforuserimage.image = openuserimage

    pathVar = StringVar()
    searchbar = Entry(root, bg="pink", fg="blue", justify="center", borderwidth=3, textvariable=pathVar)
    searchbar.place(relx=0.5, rely=0.2, width=250, anchor=CENTER)
    searchbar.bind('<KeyPress>', lambda event: [on_keypress(user, send, event.char, root, searchbar.get())])
    searchbar.focus()

    mainframe = Frame(root, bg="light green")

    if query != '':
        mainframe.grid(row=10, column=10, rowspan=20, columnspan=5, padx=400, pady=140)
        searchbar.delete(0, END)
        searchbar.insert(0, query)
    else:
        mainframe.grid(row=10, column=10, rowspan=20, columnspan=5, padx=500, pady=160)
    canvas = Canvas(mainframe, height=500, bg="light green")

    frame = Frame(canvas, bg="light green")

    scroll_y = Scrollbar(mainframe, orient="vertical", command=canvas.yview)

    row = 5

    contacts_image = Image.open('images/add_contacts.png')
    add_contacts_image = contacts_image.resize((80, 80), Image.ANTIALIAS)
    open_add_contacts_image = ImageTk.PhotoImage(add_contacts_image, master=root)

    buttonadd_contact = Button(root, image=open_add_contacts_image, bg="light green", command=lambda: [root.destroy(), add_contact(send)])

    buttonadd_contact["border"] = "0"
    buttonadd_contact["bg"] = "light green"
    buttonadd_contact.place(relx=0.7, rely=0.9, anchor=CENTER)
    buttonadd_contact.image = open_add_contacts_image

    contactcount = 0

    if query == '':

        contacts = db.get_all_contacts()
    else:
        contacts = db.search_user(query)

    for contact in contacts:

        Button(frame, bg="yellow", text=f"{contact[1]}\t\t {contact[3]}", width=48, height=2,
               anchor="center", justify="center", command=lambda c=contact: [root.destroy(), click(c, send)]).grid(row=row, column=4)

        img = Image.open(f'images/profile_image/{contact[4]}')

        image = img.resize((30, 30), Image.ANTIALIAS)
        openimg = ImageTk.PhotoImage(image, master=root)

        conbi = Button(frame, image=openimg)

        conbi.grid(row=row, column=3)
        conbi.image = openimg
        contactcount += 1
        row += 1

    if len(contacts) == 0:
        Button(frame, text="No results found !!", bg='yellow', width=60, justify='center').grid(row=5, column=4)

    searchimage = Image.open('images/search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen, master=root)

    button1 = Button(root, image=opensearchimage, command=lambda: [default(user, send, pathVar.get())])
    button1.place(relx=0.6, rely=0.2, anchor=CENTER)
    button1.image = opensearchimage

    menuimg = Image.open('images/menu.webp')
    menuimageopen = menuimg.resize((20, 20), Image.ANTIALIAS)
    openmenuimage = ImageTk.PhotoImage(menuimageopen, master=root)

    button1 = Button(root,bg='light green', image=openmenuimage, command=lambda: [root.destroy(),settings(user,send)])
    button1.place(relx=0.95, rely=0.05, anchor=CENTER)
    button1.image = openmenuimage

    button1['border'] = 0

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)

    canvas.grid(row=12, column=12, columnspan=2, rowspan=2)
    scroll_y.grid(row=12, column=14, rowspan=5, sticky='ns')

    root.mainloop()
