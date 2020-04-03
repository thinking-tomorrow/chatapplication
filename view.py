from tkinter import *
from PIL import ImageTk, Image
import server_local
from tkinter.font import Font
import database_local as db
from tkinter import filedialog  as f

import webbrowser

import datetime

user = ''


def load_function(login_func, register_func, add_contact_func, send_message_func, upload_image_func, password_func):
    global add_contact_backend, login_backend, register_backend, send_message_backend, uploadimage_func, password_back
    add_contact_backend = add_contact_func
    login_backend = login_func
    register_backend = register_func
    send_message_backend = send_message_func
    uploadimage_func = upload_image_func
    password_back = password_func


def hello():
    if db.get_setting('remember') == 'True':
        default()
    else:
        login()


def homepage():
    root = Tk()
    root.title('Introductory Page')
    root.iconbitmap('images/logo.ico')
    root.configure(background = '#ECE5DD')

    root.state('zoomed')

    frame = Frame(root, bg="#25D366", width=2000, height=75)
    frame.place(relx=0.00001, rely=0.0000001)

    Label(frame,text='Welcome!',bg='#25D366',fg='white',font=('Helvetica',15,'bold')).place(relx=0.31,rely=0.25)

    logoimg = Image.open('images/logo.png')
    logoimage = logoimg.resize((500,500),Image.ANTIALIAS)
    openlogoimage = ImageTk.PhotoImage(logoimage,master=root)

    logoLabel = Label(root,image= openlogoimage)
    logoLabel.place(relx=0.3,rely=0.15)
    logoLabel['border'] = 0
    logoLabel['background'] = '#ECE5DD'

    Label(root,text='THINKING TOMORROW',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.35,rely=0.9)

    nextimg = Image.open('images/next.webp')
    nextimage = nextimg.resize((50,50),Image.ANTIALIAS)
    opennextimage = ImageTk.PhotoImage(nextimage,master=root)

    b = Button(root,image=opennextimage,command= lambda : [root.destroy(),hello()])

    b.place(relx=0.9,rely=0.9)
    b['border'] = 0
    b['background'] = '#ECE5DD'

    b.image = opennextimage

    root.mainloop()


def login():
    x = Tk()
    x.state('zoomed')
    # x.geometry(f"570x{x.winfo_screenheight()}")
    x.configure(background="#ECE5DD")
    x.title("Login Form")
    fontFamilyy = StringVar(value="Verdana")
    fontSizze = IntVar(value=12)
    fontSizze2 = IntVar(value=8)
    appfont = Font(family=fontFamilyy.get(), size=fontSizze.get(), weight='normal')

    x.iconbitmap('images/logo.ico')

    frame = Frame(x,bg="#25D366",width=2000,height=100)
    frame.place(relx=0.00001,rely=0.0000001)


    er = StringVar(value="Verdana")
    eri = IntVar(value=8)

    fontconfi = Font(family=er.get(), size=eri.get(), weight='normal')
    Label(frame, text="LOGIN", bg="#25D366", fg="white", font=('Helvetica', 25, 'bold')).place(relx=0.32, rely=0.3)

    loginimg = Image.open('images/login.webp')
    loginimage = loginimg.resize((50, 50), Image.ANTIALIAS)
    openloginimage = ImageTk.PhotoImage(loginimage, master=frame)

    l = Label(frame, bg = '#25D366',image=openloginimage)
    l.place(relx=0.4,rely=0.3)
    l.image = openloginimage

    abel = Label(x, text="Enter your username", font=('Helvetica', 15, 'bold'), bg="#ECE5DD", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.2, anchor=CENTER)

    q = Entry(x, width=90, bg="#BEFAFA", relief="sunken", justify="center", highlightcolor = "blue")
    q.place(relx=0.5, rely=0.3, anchor=CENTER)

    abel = Label(x, text="Enter your password", font=('Helvetica', 15, 'bold'), bg="#ECE5DD", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.4, anchor=CENTER)

    s = Entry(x, show="*", width=90, justify="center", bg="#BEFAFA", relief="sunken")

    s.place(relx=0.5, rely=0.5, anchor=CENTER)

    remember = IntVar()

    ut = Checkbutton(x, text="Remember Me!!", bg="#ECE5DD", variable=remember)
    ut.place(relx=0.5, rely=0.6, anchor=CENTER)

    bi = Button(x, text="LOGIN", fg="white", bg="black", width=12, command=lambda: [login_backend(q.get(), s.get(), x, remember)])
    bi.place(relx=0.5, rely=0.7, anchor=CENTER)

    fontFamily12 = StringVar(value="Arial")
    fontSize15 = IntVar(value=7)

    tFont = Font(family=fontFamily12.get(), size=fontSize15.get(), weight='normal')

    ylabel = Button(x, text="Not yet registered??", font=tFont, bg="#ECE5DD",
                    fg = "red",command=lambda: [x.destroy(), register()])

    ylabel['border'] = 0

    ylabel.place(relx=0.5, rely=0.9, anchor=CENTER)


    x.mainloop()


def register():
    global root
    root = Tk()
    root.state('zoomed')

    root.configure(background="#ECE5DD")
    root.title("Sign-up Form")
    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=12)

    root.iconbitmap('images/logo.ico')

    fontcon = Font(family=fontFamily.get(), size=fontSize.get(), weight='normal')

    qw = StringVar(value="Verdana")
    qi = IntVar(value=8)

    fontconf = Font(family=qw.get(), size=qi.get(), weight='normal')

    frame = Frame(root, bg="#25D366", width=2000, height=100)
    frame.place(relx=0.00001, rely=0.0000001)

    myLabel = Label(frame, text="SIGN-UP TODAY!!", font=('Helvetica',20,'bold'), bg="#25D366", fg="white")
    myLabel.place(relx=0.35, rely=0.5, anchor=CENTER)

    regimg = Image.open('images/register.webp')
    registerimage = regimg.resize((100, 100), Image.ANTIALIAS)
    openregisterimage = ImageTk.PhotoImage(registerimage, master=frame)

    l = Label(frame, bg='#25D366', image=openregisterimage)
    l.place(relx=0.4, rely=0.1)
    l.image = openregisterimage

    abel = Label(root, text="Enter your Username", bg = "#ECE5DD", font=('Helvetica',20,'bold'), fg="slate blue")
    abel.place(relx=0.5, rely=0.2, anchor=CENTER)

    e = Entry(root, width=90, bg="#BEFAFA", relief="sunken", justify="center")

    e.place(relx=0.5, rely=0.25, anchor=CENTER)

    abel = Label(root, text="Enter your email-id", font=('Helvetica',20,'bold'), bg="#ECE5DD", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.35, anchor=CENTER)

    f = Entry(root, width=90, bg="#BEFAFA", relief="sunken", justify="center")

    f.place(relx=0.5, rely=0.4, anchor=CENTER)

    abel = Label(root, text="Enter your Password", font=('Helvetica',20,'bold'), bg="#ECE5DD", fg="slate blue", padx=10, pady=10)
    abel.place(relx=0.5, rely=0.5, anchor=CENTER)

    h = Entry(root, width=90, show="*", bg="#BEFAFA", relief="sunken", justify="center")

    h.place(relx=0.5, rely=0.55, anchor=CENTER)

    abel = Label(root, text="Re-enter your Password", font=('Helvetica',20,'bold'), bg="#ECE5DD", fg="slate blue", padx=10,
                 pady=10)
    abel.place(relx=0.5, rely=0.65, anchor=CENTER)

    g = Entry(root, show="*", width=90, bg="#BEFAFA", relief="sunken", justify="center")

    g.place(relx=0.5, rely=0.7, anchor=CENTER)

    b = Button(root, text="SUBMIT", fg="white", width=12, bg="#25D366", relief='flat',
               command=lambda: [register_backend(e.get(), f.get(), h.get(), g.get(), root)])
    b.place(relx=0.5, rely=0.85, anchor=CENTER)

    fontFamily2 = StringVar(value="Arial")
    fontSize5 = IntVar(value=7)
    WFont = Font(family=fontFamily2.get(), size=fontSize5.get(), weight='normal')

    yLabel = Button(root, text="Already registered??", font=WFont, bg="#ECE5DD", relief='flat',  fg = 'red',
                    command=lambda: [root.destroy(), login()], justify="center")
    yLabel.place(relx=0.5, rely=0.9, anchor=CENTER)

    root.mainloop()


def add_contact():

    a = Tk()
    a.state('zoomed')
    a.configure(background="#ECE5DD")
    a.title('Add Contacts')

    a.iconbitmap('images/logo.ico')

    frame = Frame(a, bg="#25D366", width=2000, height=100)
    frame.place(relx=0.00001, rely=0.0000001)

    profileimg = Image.open('images/back.webp')
    profileimage = profileimg.resize((50, 50), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage, master=a)

    b = Button(frame, image=openprofileimage, font=("Courier", 8, "normal"), padx=20, bg="white", fg="red",
           command=lambda: [a.destroy(), default()])
    b.place(relx=0.001, rely=0.3)
    b['background'] = "#25D366"
    b['border'] = 0

    Label(frame, text="ADD CONTACTS", bg = "#25D366", font=('Helvetica', 20, 'bold'), fg='white').place(relx=0.25, rely=0.3)

    Label(a, text="Enter the Contact-Name or Contact Email-ID", font=('Helvetica', 20, 'bold'), bg="#ECE5DD", fg='slate blue').place(relx=0.275, rely=0.2)

    contact = Entry(a, bg="#BEFAFA", relief="sunken", width=90)
    contact.place(relx=0.275, rely=0.4)

    Button(a, text="Add Contact", font = ('Helvetica',10,'bold') , bg="#25D366", fg="white", relief='flat', command=lambda: [add_contact_backend(contact.get(), a)]).place(relx=0.45, rely=0.6)

    a.mainloop()


def contactinfo(contact):
    root = Tk()

    root.configure(background='#ECE5DD')
    root.state('zoomed')

    contactname = contact[1]

    root.iconbitmap('images/logo.ico')

    root.title(f'{contactname}')

    fra = Frame(root, bg="#25D366", width=1500, height=120)
    fra.place(relx=0.00001, rely=0.0000001)

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=fra)

    backbutton = Button(fra, image=openbackimage, command=lambda: [root.destroy(), click(contact)])

    backbutton["border"] = "0"
    backbutton["bg"] = "#25D366"
    backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
    backbutton.image = openbackimage

    Label(fra,text=contactname,bg='#25D366',fg='white',font=('Helvetica',30,'bold')).place(relx=0.42,rely=0.3)

    contactimg = Image.open(f'images/profile_image/{contact[4]}')
    contactimage = contactimg.resize((50, 50), Image.ANTIALIAS)
    opencontactimage = ImageTk.PhotoImage(contactimage, master=fra)

    imageLabel = Label(fra, image=opencontactimage)

    imageLabel["border"] = "0"
    imageLabel["bg"] = "#25D366"
    imageLabel.place(relx=0.4, rely=0.55, anchor=CENTER)
    imageLabel.image = opencontactimage

    bigcontactimage = contactimg.resize((250,250),Image.ANTIALIAS)
    openbigcontactimage = ImageTk.PhotoImage(bigcontactimage,master=root)

    bigimageLabel = Label(root,image=openbigcontactimage)

    bigimageLabel['border'] = 0
    bigimageLabel['background'] = '#ECE5DD'
    bigimageLabel.place(relx=0.35,rely=0.175)
    bigimageLabel.image = openbigcontactimage

    Label(root,text=contactname,bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.001,rely=0.59)

    Label(root,text='STATUS:',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.001,rely=0.69)

    status = contact[3]

    if status == '':
        status = 'No status'
    else:
        pass

    Label(root, text=f'{status}', bg='#ECE5DD', fg='#00ACEE', font=('Kalpurush', 20, 'bold')).place(relx=0.1, rely=0.69)

    Label(root,text='Last Seen today at : ',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.001,rely=0.79)

    now = datetime.datetime.now()

    current_time = now.strftime('%H:%M:%S')

    Label(root,text=f'{current_time}',bg='#ECE5DD',fg='#00ACEE',font=('Kalpurush',20,'bold')).place(relx=0.25,rely=0.79)


def click(contact):
    chat_page = Tk()
    chat_page.state('zoomed')
    chat_page.configure(background="#ECE5DD")
    chat_page.title(contact[1])

    chats = db.get_chats(contact[1])

    chat_page.iconbitmap('images/logo.ico')

    fra = Frame(chat_page, bg="#25D366", width=1500, height=120)
    fra.place(relx=0.00001, rely=0.0000001)

    profileimg = Image.open('images/back.webp')
    profileimage = profileimg.resize((50, 50), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage, master=fra)

    b = Button(fra, image=openprofileimage, bg="#25D366",
               command=lambda: [chat_page.destroy(), default()])
    b.place(relx=0.01, rely=0.3)
    b['background'] = "#25D366"
    b['border'] = 0

    contact_details = Frame(fra, bg="#25D366",width=1000)
    contact_details.place(relx=0.125,rely=0.35)

    video_callimg = Image.open('images/video_call.png')
    video_callimage = video_callimg.resize((50, 50), Image.ANTIALIAS)
    openvideo_callimage = ImageTk.PhotoImage(video_callimage, master=fra)

    buttonforvideoimage = Button(fra, image=openvideo_callimage,relief='flat')
    buttonforvideoimage.place(relx=0.7,rely=0.35)

    buttonforvideoimage['border'] = 0
    buttonforvideoimage['background'] = "#25D366"

    audio_callimg = Image.open('images/audio_call.webp')
    audio_callimage = audio_callimg.resize((50, 50), Image.ANTIALIAS)
    openaudio_callimage = ImageTk.PhotoImage(audio_callimage, master=fra)

    buttonforvideoimage = Button(fra, image=openaudio_callimage, relief='flat')
    buttonforvideoimage.place(relx=0.8, rely=0.35)

    buttonforvideoimage['border'] = 0
    buttonforvideoimage['background'] = "#25D366"

    Label(fra, text=contact[1], font=("Helvetica", 20, "bold"), bg="#25D366", fg="#075E54",relief='flat').place(relx=0.15,rely=0.375)


    menuimg = Image.open(f'images/profile_image/{contact[4]}')
    menuimage = menuimg.resize((50, 50), Image.ANTIALIAS)
    openmenuimage = ImageTk.PhotoImage(menuimage, master=fra)

    buttonfornewimage = Button(fra, image=openmenuimage, command = lambda :  [chat_page.destroy(),contactinfo(contact)])
    buttonfornewimage.place(relx=0.11,rely=0.35)


    buttonfornewimage['border'] = 0
    buttonfornewimage['background'] = "#25D366"




    if not chats:
        messagebox = Frame(chat_page, bg="pink")
        messagebox.place(relx=0.5,rely=0.5)

        Label(chat_page, text="No chat history!!", bg="pink", fg="black").place(relx=0.5,rely=0.5)

    else:

        mainframe = Frame(chat_page, bg="#ECE5DD",width=1000,height=500)
        mainframe.place(relx=0.01,rely=0.2)
        canvas = Canvas(mainframe, height=400, width=1250, bg="#ECE5DD")

        frame = Frame(canvas, bg="#ECE5DD")

        scroll_y = Scrollbar(mainframe, orient="vertical", command=canvas.yview)

        row_number = 4
        for chat in chats:
            if chat[5] == 'True':
                messagebox = Frame(frame, bg="pink")
                messagebox.grid(row=row_number, column=0)

                Label(messagebox, text=chat[2], bg="white", fg="black").grid(row=row_number, column=0)
                Label(messagebox, text=chat[4], bg="white", font=("Arial", 6, 'roman'), padx=5, pady=10).grid(row=row_number, column=1)
                row_number += 2

            else:
                messagebox2 = Frame(frame, bg="#ECE5DD", padx=1100)
                messagebox2.grid(row=row_number, column=13, columnspan=3)

                Label(messagebox2, text=chat[2], bg="#25D366", fg="black").grid(row=row_number, column=20)
                Label(messagebox2, text=chat[4], bg="#ECE5DD", fg="red", font=("Arial", 6, 'roman')).grid(row=row_number+1, column=20)

                row_number += 2

        canvas.create_window(0, 0, anchor='nw', window=frame)

        canvas.update_idletasks()

        canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)
        canvas.yview_scroll(1,"page")
        canvas.yview_moveto(1)
        canvas.grid(row=3, column=0, columnspan=20, rowspan=200)
        scroll_y.grid(row=3, column=21, rowspan=300, sticky='ns')

    entryforchatbox = Entry(chat_page, borderwidth=5, width=90, bg="#BEFAFA", justify="center")
    entryforchatbox.place(relx=0.3, rely=0.9)

    send = Image.open('images/send.png')
    imageforsend = send.resize((20, 20), Image.ANTIALIAS)
    openimageforsend = ImageTk.PhotoImage(imageforsend,master=chat_page)
    buttonforsend = Button(chat_page, image=openimageforsend, command=lambda: [send_message_backend(entryforchatbox.get(), contact, chat_page)])

    buttonforsend.place(relx=0.7, rely=0.9)
    buttonforsend.image = openimageforsend

    send = Image.open('images/attachment.webp')
    imageforsend = send.resize((20, 20), Image.ANTIALIAS)
    openimageforsend = ImageTk.PhotoImage(imageforsend, master=chat_page)
    buttonforsend = Button(chat_page, image=openimageforsend)
    buttonforsend.place(relx=0.6799, rely=0.9)
    buttonforsend.image = openimageforsend


    chat_page.mainloop()


def changepassword(user):

    root = Tk()
    root.title('Change your Password')
    root.state('zoomed')
    root.configure(background='#ECE5DD')
    root.iconbitmap('images/logo.ico')

    fra = Frame(root, bg="#25D366", width=1500, height=120)
    fra.place(relx=0.00001, rely=0.0000001)

    Label(fra, text='Change your Password', bg='#25D366', fg='white', font=('Helvetica', 20, 'bold')).place(relx=0.32, rely=0.4)

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=fra)

    backbutton = Button(fra, image=openbackimage, command=lambda: [root.destroy(), settings()])

    backbutton["border"] = "0"
    backbutton["bg"] = "#25D366"
    backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
    backbutton.image = openbackimage

    userdetails = server_local.get_user(user)

    profileimage = userdetails['ProfilePicture']

    profileimg = Image.open(f'images/profile_image/{profileimage}')
    profileimage = profileimg.resize((50, 50), Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage, master=fra)

    ProfileImage = Button(root, image=openprofileimage)

    ProfileImage["border"] = "0"
    ProfileImage["bg"] = "#ECE5DD"
    ProfileImage.place(relx=0.5, rely=0.3, anchor=CENTER)
    ProfileImage.image = openprofileimage

    profilename = userdetails['Username']

    Label(root, bg='#ECE5DD', text=profilename, fg='#075E54', font=('Kalpurush', 20, 'bold')).place(relx=0.45, rely=0.4)

    currentpassword = '*'*len(userdetails['Password'])

    # Label(root, text='Your Current Password', bg='#ECE5DD',fg='#075E54',font=('Kaplurush',15,'bold')).place(relx=0.02,rely=0.5)

    Label(root, text='Your current password', bg='#ECE5DD', fg='#075E54', font=('Kalpurush', 13, 'bold')).place(relx=0.01, rely=0.6)

    Label(root, text=currentpassword, bg='#ECE5DD', fg='#075E54', font=('Kalpurush', 10, 'normal')).place(relx=0.4, rely=0.6)

    Label(root, text='Enter your new password here:', bg='#ECE5DD', fg='#075E54', font=('Kalpurush', 13, 'bold')).place(relx=0.01, rely=0.7)

    passwordentry = Entry(root, bg='#BEFAFA', relief='flat', width=90, justify='center', show='*')
    passwordentry.place(relx=0.4, rely=0.7)

    Label(root, text='Confirm your password entry:', bg='#ECE5DD', fg='#075E54', font=('Kalpurush', 13, 'bold')).place(relx=0.01, rely=0.8)

    confirmpasswordentry = Entry(root, bg='#BEFAFA', relief='flat', width=90, justify='center', show='*')
    confirmpasswordentry.place(relx=0.4,rely=0.8)

    passimg = Image.open('images/change_password.webp')
    passimage = passimg.resize((50, 50), Image.ANTIALIAS)
    openpassimage = ImageTk.PhotoImage(passimage, master=root)

    passimagebutton = Button(root, image=openpassimage)

    passimagebutton["border"] = "0"
    passimagebutton["bg"] = "#ECE5DD"
    passimagebutton.place(relx=0.4, rely=0.9)
    passimagebutton.image = openpassimage

    Button(root, text='Change your password', bg='#075E54', fg='white',
           command=lambda: [password_back(passwordentry.get(), confirmpasswordentry.get())]).place(relx=0.45, rely=0.925)


def on_keypress(char, window, test):
    window.destroy()
    if ord(char) == 8:
        test = test[:-1]
    else:
        test = test+char
    default(test)


def updateprofilepic(user):

    root = Tk()

    root.withdraw()

    n = server_local.get_user(user)



    filename = f.askopenfilename(initialdir="/", title="Select file",
                        filetypes=(("jpeg files", "*.jpg"), ("all files", "*.*")))

    username_profile = Image.open(f'{filename}')

    ext = str(filename).split('.')[1]

    if ext.upper() == 'JPG':
        ext = 'jpeg'

    username_profile.save(f'images/profile_image/{user}',ext)

    uploadimage_func(user,username_profile)

    default()

    root.mainloop()


def changetheme():

    root = Tk()
    root.title('Change the theme')
    root.configure(background='#ECE5DD')

    root.iconbitmap('images/logo.ico')

    root.state('zoomed')

    options = ['Default','Light','Dark']

    fra = Frame(root, bg="#25D366", width=1500, height=120)
    fra.place(relx=0.00001, rely=0.0000001)

    Label(fra, text='Change your Password', bg='#25D366', fg='white', font=('Helvetica', 20, 'bold')).place(relx=0.32,
                                                                                                            rely=0.4)

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=fra)

    backbutton = Button(fra, image=openbackimage, command=lambda: [root.destroy(), settings()])

    backbutton["border"] = "0"
    backbutton["bg"] = "#25D366"
    backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
    backbutton.image = openbackimage

    clicked = StringVar()
    clicked.set(options[0])

    Label(root,text='Your Current theme is:',bg='#ECE5DD',font=('Kalpurush',15,'bold'),fg='#075E54').place(relx=0.0001,rely=0.2)

    current_theme = 'Default'

    Label(root,text=current_theme,bg='#ECE5DD',font=('Kalpurush',15,'normal'),fg='#075E54').place(relx=0.3,rely=0.2)

    Label(root,text='Change your theme',bg='#ECE5DD',font=('Kalpurush',20,'bold'),fg='#075E54').place(relx=0.00001,rely=0.5)

    dropdown = OptionMenu(root,clicked,*options)
    dropdown.config(width=50,bg='#00ACEE',fg='#075E54',font=('Helvetica',10,'bold'))
    dropdown.place(relx=0.3,rely=0.5)

    Button(root,text='Change the theme',bg='#075E54',fg='white').place(relx=0.5,rely=0.9)


def github():
    webbrowser.open_new(r"https://github.com/thinking-tomorrow/chatapplication")


def aboutus():
    root = Tk()

    root.configure(background = '#ECE5DD')

    root.state('zoomed')

    root.iconbitmap('images/logo.ico')
    root.title('About Us')

    frame = Frame(root, bg="#25D366", width=2000, height=100)
    frame.place(relx=0.00001, rely=0.0000001)

    Label(frame, text="ABOUT US", bg="#25D366", fg="white", font=('Helvetica', 20, 'bold')).place(relx=0.32, rely=0.3)

    logoimg = Image.open('images/logo.png')
    logoimage = logoimg.resize((200,200),Image.ANTIALIAS)
    openlogoimage = ImageTk.PhotoImage(logoimage,master=root)

    logoLabel = Label(root,image=openlogoimage)

    logoLabel.place(relx=0.45,rely=0.2)
    logoLabel['border'] = 0
    logoLabel['background'] = '#ECE5DD'

    logoLabel.image = openlogoimage

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50,50),Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage,master=frame)

    backbutton = Button(frame,image = openbackimage,command = lambda : [root.destroy(),settings()])

    backbutton.place(relx=0.01,rely=0.3)

    backbutton['border'] = 0
    backbutton['background'] = '#25D366'

    backbutton.image = openbackimage

    Label(root,text='THINKING TOMORROW',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.4,rely=0.5)

    Label(root,text='What is Thinking Tomorrow ? ',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.001,rely=0.55)

    info = 'Thinking Tomorrow is a non-profittable organisation that has worked on building this chat application . We hope u like it !'

    Label(root,text=info,bg='#ECE5DD',fg='#075E54',font=('Kalpurush',12,'bold')).place(relx=0.001,rely=0.6)

    Label(root,text='WHO ARE WE?',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',20,'bold')).place(relx=0.001,rely=0.65)

    devinfo =  "The developers behind this project are Sajjad Ahmed Shaaz(the major part)and Hrishikesh Bhanja . The team has worked in the best way possible to provide all the necessary"

    dev2info = 'functions to the user. If they are any problems u are always free to email us to the below addresses'

    Label(root,text=devinfo,bg='#ECE5DD',fg='#075E54',font=('Kalpurush',12,'bold')).place(relx=0.001,rely=0.7)
    Label(root, text=dev2info, bg='#ECE5DD', fg='#075E54', font=('Kalpurush', 12, 'bold')).place(relx=0.001, rely=0.73)

    gitimg = Image.open('images/git.png')
    gitimage = gitimg.resize((50, 50), Image.ANTIALIAS)
    opengitimage = ImageTk.PhotoImage(gitimage, master=root)

    gitbutton = Button(root, image=opengitimage, command=lambda: [root.destroy(), github()])

    gitbutton["border"] = "0"
    gitbutton["bg"] = "#ECE5DD"
    gitbutton.place(relx=0.02, rely=0.9, anchor=CENTER)
    gitbutton.image = opengitimage

    Label(root,text='The Email-ids are as follows:',bg='#ECE5DD',fg='#075E54',font=('Kalpurush',15,'bold')).place(relx=0.34,rely=0.8)

    Label(root,text='mailsajjad006@gmail.com,hrishipotter123@gmail.com',fg='#00ACEE',bg='#ECE5DD',font=('Kalpurush',12,'bold')).place(relx=0.3,rely=0.9)


def settings(user=db.get_setting('username')):
    s = Tk()
    s.state('zoomed')
    s.title('Settings')
    s.configure(background='#ECE5DD')

    s.iconbitmap('images/logo.ico')

    userdetails = server_local.get_user(user)

    frame = Frame(s,bg="#25D366",width=2000,height=100)
    frame.place(relx=0.00001,rely=0.0000001)

    Label(frame,text="SETTINGS",bg="#25D366",fg="white",font=('Helvetica',15,'bold')).place(relx=0.32,rely=0.25)

    backimg = Image.open('images/back.webp')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=frame)

    backbutton = Button(frame, image=openbackimage,command=lambda: [s.destroy(), default()] )

    backbutton["border"] = "0"
    backbutton["bg"] = "#25D366"
    backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
    backbutton.image = openbackimage

    x = userdetails['ProfilePicture']

    userimg = Image.open(f'images/profile_image/{x}')
    userimage = userimg.resize((50, 50), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage, master=s)

    buttonforuserimage = Button(s, image=openuserimage)

    buttonforuserimage["border"] = "0"
    buttonforuserimage["bg"] = "#ECE5DD"
    buttonforuserimage.place(relx=0.5, rely=0.24, anchor=CENTER)
    buttonforuserimage.image = openuserimage

    Label(s, text= f"{user}",bg='#ECE5DD',fg='#075E54', font=('Kalpurush', 20, 'bold')).place(relx=0.45,rely=0.3)

    b = Button(s,text='Change your Password',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w', command = lambda : [s.destroy(),changepassword(user)])
    b.place(relx=0.04,rely=0.4)

    menuimg = Image.open('images/password.jpg')
    menuimageopen = menuimg.resize((50, 50), Image.ANTIALIAS)
    openmenuimage = ImageTk.PhotoImage(menuimageopen, master=s)

    button1 = Button(s, bg="#ECE5DD", image=openmenuimage, anchor = 'w',command= lambda : [s.destroy(),changepassword(user)])
    button1.place(relx=0.02, rely=0.45, anchor=CENTER)
    button1.image = openmenuimage

    b = Button(s,text='Change your Profile Picture',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w')#command = lambda : [s.destroy(),updateprofilepic(user)])
    b.place(relx=0.00001,rely=0.5)

    b = Button(s,text='Change the Theme',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w', command = lambda : [s.destroy(),changetheme()])
    b.place(relx=0.00001,rely=0.6)

    b = Button(s,text='Turn off Notifications',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w')
    b.place(relx=0.00001,rely=0.7)

    b = Button(s,text='Change your status',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w')
    b.place(relx=0.00001,rely=0.8)

    b = Button(s,text='About Us',bg="#ECE5DD",fg="#075E54",font=('Kalpurush', 20, 'bold'),width=90,relief='flat',anchor='w',command = lambda : [s.destroy(),aboutus()])
    b.place(relx=0.00001,rely=0.9)


    s.mainloop()


def openimage(image, username):

    root = Tk()

    root.iconbitmap('images/logo.ico')

    root.state('zoomed')

    root.attributes('-alpha', 0.9)

    root.configure(background='black')

    root.title(f'{username}')

    menuimg = Image.open(f'images/profile_image/{image}')
    menuimageopen = menuimg.resize((500, 500), Image.ANTIALIAS)
    openmenuimage = ImageTk.PhotoImage(menuimageopen, master=root)

    button1 = Label(root, bg='black', image=openmenuimage)
    button1.place(relx=0.5, rely=0.5, anchor=CENTER)
    button1.image = openmenuimage

    root.mainloop()


def default(query=''):
    user = db.get_setting('username')
    n = server_local.get_user(user)


    root = Tk()
    root.state("zoomed")
    root.title("Home Page")
    root.configure(background="#ECE5DD")

    root.iconbitmap('images/logo.ico')

    fra = Frame(root, bg="#25D366", width=2000, height=100)
    fra.place(relx=0.00001, rely=0.0000001)

    if query != '':
        backimg = Image.open('images/back.webp')
        backimage = backimg.resize((50, 50), Image.ANTIALIAS)
        openbackimage = ImageTk.PhotoImage(backimage, master=fra)

        backbutton = Button(fra, image=openbackimage, command=lambda: [root.destroy(), default()])

        backbutton["border"] = "0"
        backbutton["bg"] = "#25D366"
        backbutton.place(relx=0.02, rely=0.4, anchor=CENTER)
        backbutton.image = openbackimage

    else:
        pass



    Label(fra, text="HOME", bg="#25D366", fg="white", font=('Helvetica', 25, 'bold')).place(relx=0.32, rely=0.3)

    menuimg = Image.open('images/menu.webp')
    menuimageopen = menuimg.resize((50, 50), Image.ANTIALIAS)
    openmenuimage = ImageTk.PhotoImage(menuimageopen, master=root)

    button1 = Button(fra, bg='#25D366', image=openmenuimage,
                     command=lambda: [root.destroy(), settings()])
    button1.place(relx=0.65, rely=0.5, anchor=CENTER)
    button1.image = openmenuimage


    button1['border'] = 0

    Button(fra, text="Logout", width=10, bg="#075E54", fg="white",
           command=lambda: [db.set_setting('remember', 'False'), root.destroy(),
                            login()]).place(relx=0.55, rely=0.4)

    backimg = Image.open('images/home.png')
    backimage = backimg.resize((50, 50), Image.ANTIALIAS)
    openbackimage = ImageTk.PhotoImage(backimage, master=fra)

    homebutton = Label(fra, image=openbackimage, bg='#25D366')
    homebutton.place(relx=0.29, rely=0.3)

    username = Label(root, font=('Kalpurush', 20, 'bold'), text=f"{user}", bg="#ECE5DD", fg="#075E54")
    username.place(relx=0.5, rely=0.3, anchor=N)

    x = n['ProfilePicture']


    userimg = Image.open(f'images/profile_image/{x}')
    userimage = userimg.resize((50, 50), Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage, master=root)

    buttonforuserimage = Button(root, image=openuserimage, bg="#ECE5DD",command = lambda  : [root.destroy(),updateprofilepic(user)])

    buttonforuserimage["border"] = "0"
    buttonforuserimage["bg"] = "#ECE5DD"
    buttonforuserimage.place(relx=0.5, rely=0.24, anchor=CENTER)
    buttonforuserimage.image = openuserimage




    pathVar = StringVar()
    searchbar = Entry(root, bg="pink", fg="blue", justify="center", borderwidth=3, textvariable=pathVar)
    searchbar.place(relx=0.5, rely=0.4, width=250, anchor=CENTER)
    searchbar.bind('<KeyPress>', lambda event: [on_keypress(event.char, root, searchbar.get())])
    searchbar.focus()

    mainframe = Frame(root, bg="#ECE5DD")

    if query != '':
        mainframe.grid(row=18, column=10, rowspan=20, columnspan=5, padx=500, pady=300)
        searchbar.delete(0, END)
        searchbar.insert(0, query)
    else:
        mainframe.grid(row=18, column=10, rowspan=20, columnspan=5, padx=500, pady=300)
    canvas = Canvas(mainframe, height=375, bg="#ECE5DD")

    frame = Frame(canvas, bg="#ECE5DD")

    scroll_y = Scrollbar(mainframe, orient="vertical", command=canvas.yview)

    row = 8

    contacts_image = Image.open('images/add_contacts.png')
    add_contacts_image = contacts_image.resize((80, 80), Image.ANTIALIAS)
    open_add_contacts_image = ImageTk.PhotoImage(add_contacts_image, master=root)

    buttonadd_contact = Button(root, image=open_add_contacts_image, bg="#ECE5DD", command=lambda: [root.destroy(), add_contact()])

    buttonadd_contact["border"] = "0"
    buttonadd_contact["bg"] = "#ECE5DD"
    buttonadd_contact.place(relx=0.7, rely=0.9, anchor=CENTER)
    buttonadd_contact.image = open_add_contacts_image

    contactcount = 0

    if query == '':

        contacts = db.get_all_contacts()
    else:
        contacts = db.search_user(query)

    for contact in contacts:

        Button(frame, bg="#34B7F1", text=f"{contact[1]}\t\t {contact[3]}", width=48, height=2,
               anchor="center", justify="center", command=lambda c=contact: [root.destroy(), click(c)]).grid(row=row, column=4)


        img = Image.open(f'images/profile_image/{contact[4]}')

        image = img.resize((30, 30), Image.ANTIALIAS)
        openimg = ImageTk.PhotoImage(image, master=root)

        conbi = Button(frame, image=openimg, command=lambda c = contact : openimage(c[4],c[1]))

        conbi.grid(row=row, column=3)
        conbi.image = openimg
        contactcount += 1
        row += 1

    if len(contacts) == 0:
        Button(frame, text="No results found !!", bg='yellow', width=60, justify='center').grid(row=5, column=4)

    searchimage = Image.open('images/search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen, master=root)

    button1 = Button(root, image=opensearchimage, command=lambda: [default()])
    button1.place(relx=0.6, rely=0.4, anchor=CENTER)
    button1.image = opensearchimage

    canvas.create_window(0, 0, anchor='nw', window=frame)

    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'), yscrollcommand=scroll_y.set)

    canvas.grid(row=18, column=12, columnspan=2, rowspan=2,pady=7)
    scroll_y.grid(row=18, column=14, rowspan=2, sticky='ns')


    root.mainloop()
