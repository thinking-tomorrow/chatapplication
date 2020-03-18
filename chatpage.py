from tkinter import *
from PIL import ImageTk, Image
from tkinter.font import Font
import tkinter.ttk as x


def click(num=1):

    chat_page = Tk()
    chat_page.configure(background="light blue")
    chat_page.title("Contact  " + str(num) + " Chat Page")
    Button(chat_page,  text=" <- Back ",  font=("Courier",  8,  "normal"),  padx=20,  bg="white",  fg="red",  command=lambda: [x.destroy(),  default()]).grid(row=0,  column=0)
    contact_details = Frame(chat_page,  bg="light blue",  pady=20,  padx=50)
    contact_details.grid(row=0,  column=1)
    profileimg = Image.open('pr.jpg')  # the location of the image would change according to every user
    profileimage = profileimg.resize((30,  30),  Image.ANTIALIAS)
    openprofileimage = ImageTk.PhotoImage(profileimage)
    buttonforprofileimage = Button(contact_details,  image=openprofileimage)
    buttonforprofileimage.grid(row=0,  column=1)
    buttonforprofileimage.image = openprofileimage
    Button(contact_details, text="Contact  "+str(num), font=("Courier", 12, "bold"), bg="light green", fg="red").grid(row=0, column=2)
    messagebox=Frame(chat_page, bg="pink")
    messagebox.grid(row=1, column=0)
    Label(messagebox, text="Hello!!", bg="pink", fg="black").grid(row=1, column=0)
    Label(messagebox, text="14.08", bg="pink", font=("Arial", 6, 'roman'), padx=5).grid(row=1, column=1)
    Label(chat_page, text="                                                                                                                                                          ", bg="light blue", fg="black").grid(row=2, column=0)
    messagebox2 = Frame(chat_page, bg="snow")
    messagebox2.grid(row=2, column=3)
    Label(messagebox2, text="Who are you?", bg="snow", fg="black").grid(row=2, column=4)
    Label(messagebox2, text="14.08", bg="snow", font=("Arial", 6, 'roman')).grid(row=2, column=5)
    messagebox3 = Frame(chat_page, bg="pink")
    messagebox3.grid(row=3, column=0)
    Label(messagebox3, text="I am contact "+str(num), bg="pink", fg="black").grid(row=3, column=0)
    Label(messagebox3, text="14.08", bg="pink", font=("Arial", 6, 'roman')).grid(row=3, column=1)
    chatbox = Frame(chat_page, pady=300, bg="light blue")
    chatbox.grid(row=5, column=1)
    
    entryforchatbox = Entry(chatbox, borderwidth=5, bg="yellow", justify="center")
    entryforchatbox.grid(row=5, column=1)
        
    send = Image.open('send.png')
    imageforsend = send.resize((20,  20),  Image.ANTIALIAS)
    openimageforsend = ImageTk.PhotoImage(imageforsend)
    buttonforsend = Button(chatbox,  image=openimageforsend)
    buttonforsend.grid(row=5, column=3)
    buttonforsend.image = openimageforsend
        
    chat_page.mainloop()
    

def default():
    root = Tk()
    root.title("Chat Page")
    root.configure(background="light green")
    
    userdetails = Frame(root, bg="light green")
    userdetails.grid(row=0, column=5, pady=20, padx=100)
    
    fontfamily = StringVar(value="Kalpurush")
    font_size = IntVar(value=14)
    app_font = Font(family=fontfamily.get(), size=font_size.get(), weight='bold')
    
    username = Label(userdetails, font=app_font, text="USERNAME", bg="light green", fg="red", padx=10)
    username.grid(row=0, column=0, columnspan=3)
    
    userimg = Image.open('default.jfif')
    userimage = userimg.resize((30,  30),  Image.ANTIALIAS)
    openuserimage = ImageTk.PhotoImage(userimage)
    
    buttonforuserimage = Button(userdetails,  image=openuserimage,  command=click, bg="light green")
    buttonforuserimage.grid(row=0, column=4)
    buttonforuserimage.image = openuserimage

    fontfamily = StringVar(value="Magneto")
    font_size = IntVar(value=14)
    app_font = Font(family=fontfamily.get(), size=font_size.get(), weight='normal')
    
    frame = Frame(root, bg="light green")
    frame.grid(row=1, column=5, padx=100)
    
    searchimage = Image.open('search.png')
    searchimageopen = searchimage.resize((20, 20), Image.ANTIALIAS)
    opensearchimage = ImageTk.PhotoImage(searchimageopen)
    
    searchbar = Entry(frame, font=app_font, bg="pink", fg="blue", justify="center", borderwidth=0)
    
    searchbar.grid(row=1, column=0, columnspan=4)
    
    button1 = Button(frame,  image=opensearchimage ,  bg='white',  command=click)
    button1.grid(row=1, column=5)
    button1.image = opensearchimage
    
    fontstyle = StringVar(value="Courier")
    font_size = IntVar(value=20)
    
    # contactfont = Font(family=fontstyle.get(), size=font_size.get(), weight='normal')
    
    # scrollbar = Scrollbar(root, orient="vertical")
    
    canvas = Canvas(root, bg="light green")
    scroll_y = Scrollbar(root, orient="vertical",  command=canvas.yview)
    
    frame = Frame(canvas, bg="light green")
    
    img = Image.open('pr.jpg')  # the location of the image would change according to every user
    image = img.resize((30,  30),  Image.ANTIALIAS)
    openimg = ImageTk.PhotoImage(image)
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(1), width=48, anchor="center", justify="center").grid(row=(3), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(1+1), width=48, anchor="center", justify="center").grid(row=(2+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(2+1), width=48, anchor="center", justify="center").grid(row=(3+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(3+1), width=48, anchor="center", justify="center").grid(row=(4+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(4+1), width=48, anchor="center", justify="center").grid(row=(5+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(5+1), width=48, anchor="center", justify="center").grid(row=(6+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(6+1), width=48, anchor="center", justify="center").grid(row=(7+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(7+1), width=48, anchor="center", justify="center").grid(row=(8+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(8+1), width=48, anchor="center", justify="center").grid(row=(9+2), column=(5))
    
    Button(frame, bg="yellow", command= lambda: [root.destroy(), click()], text="Contact "+str(9+1), width=48, anchor="center", justify="center").grid(row=(10+2), column=(5))
    
    for i in range(10):
        conbi = Button(frame, image=openimg)
        conbi.grid(row=(i+3), column=0)
        conbi.image = openimg
    
    canvas.create_window(0,  0,  anchor='nw',  window=frame)
    
    canvas.update_idletasks()
    
    canvas.configure(scrollregion=canvas.bbox('all'),  
                     yscrollcommand=scroll_y.set)
                     
    canvas.grid(row=2, column=5, rowspan=20, padx=100)
    scroll_y.grid(row=2, column=6, rowspan=20, sticky="ns")

    root.mainloop()


default()
