from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import database_local as db

user = ''


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

    q = Entry(x, width=90, bg="light blue", justify="center")
    q.place(relx=0.5, rely=0.3, anchor=CENTER)

    abel = Label(x, text="Enter your password", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.4, anchor=CENTER)

    s = Entry(x, show="*", width=90, bg="light blue", justify="center")

    s.place(relx=0.5, rely=0.5, anchor=CENTER)

    ut = Checkbutton(x, text="Remember Me!!", bg="light green")
    ut.place(relx=0.5, rely=0.6, anchor=CENTER)

    bi = Button(x, text="LOGIN", fg="white", bg="black", width=12, command=lambda: [login_backend(q.get(), s.get(), x)])
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

    abel = Label(root, text="Enter your Username", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.2, anchor=CENTER)

    e = Entry(root, width=90, bg="light blue", justify="center")

    e.place(relx=0.5, rely=0.25, anchor=CENTER)

    abel = Label(root, text="Enter your email-id:", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.3, anchor=CENTER)

    f = Entry(root, width=90, bg="light blue", justify="center")

    f.place(relx=0.5, rely=0.35, anchor=CENTER)

    abel = Label(root, text="Enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.4, anchor=CENTER)

    h = Entry(root, width=90, show="*", bg="light blue", justify="center")

    h.place(relx=0.5, rely=0.45, anchor=CENTER)

    abel = Label(root, text="Re-enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10,
                 pady=10)
    abel.place(relx=0.5, rely=0.5, anchor=CENTER)

    g = Entry(root, show="*", width=90, bg="light blue", justify="center")

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


def click(contact):
    chat_page = Tk()
    chat_page.state('zoomed')
    chat_page.configure(background="light blue")
    chat_page.title(contact[1])

    Button(chat_page, text=" <- Back ", font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
           command=lambda: [chat_page.destroy(), default(user)]).grid(row=0, column=0)

    contact_details = Frame(chat_page, bg="light blue", pady=20, padx=50)
    contact_details.grid(row=0, column=1)

    profileimg = Image.open(f'images/profile_image/{contact[4]}')  # the location of the image would change according to every user
    profileimage = profileimg.resize((30, 30), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage)
    buttonforprofileimage = Button(contact_details, image=openprofileimage)
    buttonforprofileimage.grid(row=0, column=1)
    buttonforprofileimage.image = openprofileimage

    Button(contact_details, text=contact[1], font=("Courier", 12, "bold"), bg="light green", fg="red").grid(
        row=0, column=2)

    messagebox = Frame(chat_page, bg="pink")
    messagebox.grid(row=1, column=0)

    Label(messagebox, text="Hello!!", bg="pink", fg="black").grid(row=1, column=0)
    Label(messagebox, text="14.08", bg="pink", font=("Arial", 6, 'roman'), padx=5).grid(row=1, column=1)
    Label(chat_page,
          text="                                                                                                                                                          ",
          bg="light blue", fg="black").grid(row=2, column=0)

    messagebox2 = Frame(chat_page, bg="snow")
    messagebox2.grid(row=2, column=3)

    Label(messagebox2, text="Who are you?", bg="snow", fg="black").grid(row=2, column=4)
    Label(messagebox2, text="14.08", bg="snow", font=("Arial", 6, 'roman')).grid(row=2, column=5)

    messagebox3 = Frame(chat_page, bg="pink")
    messagebox3.grid(row=3, column=0)

    Label(messagebox3, text="I am contact " + str(contact[1]), bg="pink", fg="black").grid(row=3, column=0)
    Label(messagebox3, text="14.08", bg="pink", font=("Arial", 6, 'roman')).grid(row=3, column=1)

    chatbox = Frame(chat_page, pady=300, bg="light blue")
    chatbox.grid(row=5, column=1)

    entryforchatbox = Entry(chatbox, borderwidth=5, bg="yellow", justify="center")
    entryforchatbox.grid(row=5, column=1)

    send = Image.open('images/send.png')
    imageforsend = send.resize((20, 20), Image.ANTIALIAS)
    openimageforsend = ImageTk.PhotoImage(imageforsend)
    buttonforsend = Button(chatbox, image=openimageforsend)
    buttonforsend.grid(row=5, column=3)
    buttonforsend.image = openimageforsend

    chat_page.mainloop()


def default(username):
    global user
    user = username
    root = Tk()
    root.state("zoomed")
    root.title("Chat Page")
    root.configure(background="light green")    



    username = Label(root, font=('Kalpurush', 20, 'bold'), text=f"{username}", bg="light green", fg="red")
    username.place(relx=0.5, rely=0.1, anchor=N)

    userimg = Image.open('images/default_profile_image.png')
    userimage = userimg.resize((50, 50), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage)

    buttonforuserimage = Button(root, image=openuserimage, bg="light green")
    buttonforuserimage.place(relx=0.5, rely=0.04, anchor=CENTER)
    buttonforuserimage.image = openuserimage

    searchimage = Image.open('images/search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen)

    searchbar = Entry(root, bg="pink", fg="blue", justify="center", borderwidth=3)

    searchbar.place(relx=0.5, rely=0.2, width=250, anchor=CENTER)

    button1 = Button(root, image=opensearchimage,width=50, bg='white')
    button1.place(relx=0.6, rely=0.2, anchor=CENTER)
    button1.image = opensearchimage

    mainframe = Frame(root,bg = "light green")
    mainframe.grid(row=10,column=10,rowspan=20,columnspan=5,padx=500,pady=160)
    canvas = Canvas(mainframe, height = 500 , bg="light green")


    frame = Frame(canvas, bg="light green")
    
    scroll_y = Scrollbar(mainframe, orient="vertical", command=canvas.yview)



    row = 5
    contacts = db.get_all_contacts()
    
    for contact in contacts:
        Button(frame, bg="yellow", text=f"{contact[1]}\t\t {contact[3]}", width=48, height=2,
               anchor="center", justify="center", command=lambda: [root.destroy(), click(contact)]).grid(row=row, column=4)

        img = Image.open(f'images/profile_image/{contact[4]}')  # the location of the image would change according to every user
        image = img.resize((30, 30), Image.ANTIALIAS)
        openimg = ImageTk.PhotoImage(image)

        conbi = Button(frame, image=openimg)

        conbi.grid(row=row, column=3)
        conbi.image = openimg
        row += 1



    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canvas.grid(row=12, column=12, columnspan = 2 ,rowspan=2 )
    scroll_y.grid(row=12,column=14,rowspan=5,sticky='ns')

    root.mainloop()
