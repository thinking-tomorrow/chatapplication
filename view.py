from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font


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
    mylabel.grid(row=0, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(x, text="Enter your username", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=1, column=4, columnspan=5)

    q = Entry(x, width=90, bg="light blue", justify="center")
    q.grid(row=2, column=4, columnspan=5, padx=10, pady=10)

    abel = Label(x, text="Enter your password", font=fontconfi, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=3, column=4, columnspan=5)

    s = Entry(x, show="*", width=90, bg="light blue", justify="center")
    s.grid(row=4, column=4, columnspan=5, padx=10, pady=10)

    ut = Checkbutton(x, text="Remember Me!!", bg="light green")
    ut.grid(row=5, column=4, padx=10, pady=10)

    bi = Button(x, text="LOGIN", fg="white", bg="black", command=lambda: [login_backend(q.get(), s.get(), x)])
    bi.grid(row=6, column=4, columnspan=5, padx=30, pady=20)

    fontFamily12 = StringVar(value="Arial")
    fontSize15 = IntVar(value=7)

    tFont = Font(family=fontFamily12.get(), size=fontSize15.get(), weight='normal')

    ylabel = Button(x, text="Not yet registered??", font=tFont, bg="forest green",  command=lambda: [x.destroy(), register(register_backend, login_backend)])

    ylabel.grid(row=7, column=5)
    x.mainloop()


def register(register_backend, login_backend):
    global root
    root = Tk()
    root.state('zoomed')
    # root.geometry(f"570x{root.winfo_screenheight()}")
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

    h = Entry(root, width=90, show="*", bg="light blue", justify="center")

    h.grid(row=6, column=4, columnspan=5, padx=20, pady=20)

    abel = Label(root, text="Re-enter your Password", font=fontconf, bg="light green", fg="slate blue", padx=10, pady=10)
    abel.grid(row=7, column=4, columnspan=5)

    g = Entry(root, show="*", width=90, bg="light blue", justify="center")

    g.grid(row=8, column=4, columnspan=5, padx=20, pady=20)

    b = Button(root, text="SUBMIT", fg="white", bg="black", command=lambda: [register_backend(e.get(), f.get(), h.get(), g.get(), root)])
    b.grid(row=9, column=4, columnspan=5, padx=20, pady=20)

    fontFamily2 = StringVar(value="Arial")
    fontSize5 = IntVar(value=7)
    WFont = Font(family=fontFamily2.get(), size=fontSize5.get(), weight='normal')

    yLabel = Button(root,text="Already registered??", font=WFont, bg="forest green", command=lambda: [root.destroy(), login(login_backend, register_backend)], justify="center")
    yLabel.grid(row=10,column=6)

    root.mainloop()


def click(num=1):
    chat_page = Tk()
    chat_page.state('zoomed')
    chat_page.configure(background="light blue")
    chat_page.title("Contact  " + str(num) + " Chat Page")
    Button(chat_page, text=" <- Back ", font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
           command=lambda: [chat_page.destroy(), default()]).grid(row=0, column=0)
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
    root = Tk()
    root.state('zoomed')
    root.title("Chat Page")
    root.configure(background="light green")

    userdetails = Frame(root, bg="light green")
    userdetails.grid(row=0, column=5, pady=20, padx=100)

    fontfamily = StringVar(value="Kalpurush")
    font_size = IntVar(value=14)
    app_font = Font(family=fontfamily.get(), size=font_size.get(), weight='bold')

    username = Label(userdetails, font=app_font, text=f"{username}", bg="light green", fg="red", padx=10)
    username.grid(row=1, column=4, columnspan=3)

    userimg = Image.open('images/default_profile_image.png')
    userimage = userimg.resize((100, 100), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage)

    buttonforuserimage = Button(userdetails, image=openuserimage, bg="light green")
    buttonforuserimage.grid(row=0, column=4)
    buttonforuserimage.image = openuserimage

    # fontfamily = StringVar(value="Magneto")
    # font_size = IntVar(value=14)
    # app_font = Font(family=fontfamily.get(), size=font_size.get(), weight='normal')

    frame = Frame(root, bg="light green")
    frame.grid(row=1, column=5, padx=100)

    searchimage = Image.open('images/search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen)

    searchbar = Entry(frame, font=app_font, bg="pink", fg="blue", justify="center", borderwidth=0)

    searchbar.grid(row=1, column=0, columnspan=4)

    button1 = Button(frame, image=opensearchimage, bg='white', command=click)
    button1.grid(row=1, column=5)
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
           anchor="center", justify="center").grid(row=(3), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(1 + 1), width=48,
           anchor="center", justify="center").grid(row=(2 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(2 + 1), width=48,
           anchor="center", justify="center").grid(row=(3 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(3 + 1), width=48,
           anchor="center", justify="center").grid(row=(4 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(4 + 1), width=48,
           anchor="center", justify="center").grid(row=(5 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(5 + 1), width=48,
           anchor="center", justify="center").grid(row=(6 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(6 + 1), width=48,
           anchor="center", justify="center").grid(row=(7 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(7 + 1), width=48,
           anchor="center", justify="center").grid(row=(8 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(8 + 1), width=48,
           anchor="center", justify="center").grid(row=(9 + 2), column=(5))

    Button(frame, bg="yellow", command=lambda: [root.destroy(), click()], text="Contact " + str(9 + 1), width=48,
           anchor="center", justify="center").grid(row=(10 + 2), column=(5))

    for i in range(10):
        conbi = Button(frame, image=openimg)
        conbi.grid(row=(i + 3), column=0)
        conbi.image = openimg

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canvas.grid(row=2, column=5, rowspan=20, padx=100)
    scroll_y.grid(row=2, column=6, rowspan=20, sticky="ns")

    root.mainloop()
