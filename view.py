from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font

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
    root.attributes("-fullscreen", True)

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


def click(num=1):
    chat_page = Tk()
    chat_page.state('zoomed')
    chat_page.configure(background="light blue")
    chat_page.title("Contact  " + str(num) + " Chat Page")
    Button(chat_page, text=" <- Back ", font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
           command=lambda: [chat_page.destroy(), default(user)]).grid(row=0, column=0)
    contact_details = Frame(chat_page, bg="light blue", pady=20, padx=50)
    contact_details.grid(row=0, column=1)
    profileimg = Image.open('images/pr.jpg')  # the location of the image would change according to every user
    profileimage = profileimg.resize((30, 30), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage)
    buttonforprofileimage = Button(contact_details, image=openprofileimage)
    buttonforprofileimage.grid(row=0, column=1)
    buttonforprofileimage.image = openprofileimage
    Button(contact_details, text="Contact  " + str(num), font=("Courier", 12, "bold"), bg="light green", fg="red").grid(
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
    Label(messagebox3, text="I am contact " + str(num), bg="pink", fg="black").grid(row=3, column=0)
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
    root.attributes('-fullscreen',True)
    root.title("Chat Page")
    root.configure(background="light green")

    userdetails = Frame(root, bg="light green")
    userdetails.place(relx=0.4,rely=0.1,width=20,anchor=CENTER)

    fontfamily = StringVar(value="Kalpurush")
    font_size = IntVar(value=14)
    app_font = Font(family=fontfamily.get(), size=font_size.get(), weight='bold')

    username = Label(userdetails, font=app_font, text=f"{username}", bg="light green", fg="red", padx=10)
    username.place(relx=0.5,rely=0.1,anchor=CENTER)

    userimg = Image.open('images/default_profile_image.png')
    userimage = userimg.resize((100, 100), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage)

    buttonforuserimage = Button(userdetails, image=openuserimage, bg="light green")
    buttonforuserimage.place(relx=0.4,rely=0.1,anchor=CENTER)
    buttonforuserimage.image = openuserimage



    frame = Frame(root, bg="light green")
    frame.place(relx=0.5,rely=0.2,width=20,anchor=CENTER)

    searchimage = Image.open('images/search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen)

    searchbar = Entry(frame, font=app_font, bg="pink", fg="blue", justify="center", borderwidth=0)

    searchbar.place(relx=0.5,rely=0.2,anchor=CENTER)

    button1 = Button(frame, image=opensearchimage, bg='white', command=click)
    button1.place(relx=0.6,rely=0.2,anchor=CENTER)
    button1.image = opensearchimage

    # fontstyle = StringVar(value="Courier")
    # font_size = IntVar(value=20)
    #
    # contactfont = Font(family=fontstyle.get(), size=font_size.get(), weight='normal')
    # scrollbar = Scrollbar(root, orient="vertical")

    canvas = Canvas(root, bg="light green")
    scroll_y = Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = Frame(canvas, bg="light green")

    img = Image.open('images/pr.jpg')  # the location of the image would change according to every user
    image = img.resize((30, 30), Image.ANTIALIAS)
    openimg = ImageTk.PhotoImage(image)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.3,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(1 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.35,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(2 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.4,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(3 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.45,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(4 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.5,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(5 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.55,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(6 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.6,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(7 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.65,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(8 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.7,anchor=CENTER)

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(9 + 1), width=48,
           anchor="center", justify="center").place(relx=0.5,rely=0.75,anchor=CENTER)

    rel_y = 0.25

    for i in range(10):
        conbi = Button(frame, image=openimg)
        rel_y += 0.05
        conbi.place(relx=0.5,rely=rel_y,anchor=CENTER)
        conbi.image = openimg

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canvas.place(relx=0.5, rely=0.3, width = 50 , height=100 ,anchor=CENTER)
    scroll_y.place(relx=0.6,rely=0.3 , height=100, width=10 ,anchor=CENTER)

    root.mainloop()
