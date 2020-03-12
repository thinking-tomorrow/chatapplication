from tkinter import *
from tkinter.font import Font


def onClick():
    x = Tk()

    x.configure(background="light green")
    x.title("Login Form")
    fontFamilyy = StringVar(value="Verdana")
    fontSizze = IntVar(value=12)
    fontSizze2 = IntVar(value=8)
    fontconi = Font(family=fontFamilyy.get(), size=fontSizze.get(), weight='normal')
    fontconfi = Font(family=fontFamilyy.get(), size=fontSizze2.get(), weight='normal')



    mylabel = Label(x, text="LOGIN", font=fontconi, bg="light green", fg="dark green", padx=20, pady=50)
    mylabel.grid(row=0,column=4,columnspan=5,padx=20,pady=20)

    q = Entry(x,width=100,bg="light blue",justify="center")
    q.insert(END,"Enter your username")
    q.grid(row=1,column=4,columnspan=5,padx=20,pady=20)






    s = Entry(x, width=100, bg="light blue", justify="center")
    s.insert(END, "Enter your password")
    s.grid(row=2, column=4,columnspan=5, padx=20, pady=20)

    ut = Checkbutton(x, text="Remember Me!!",bg="light green")
    ut.grid(row=3 , column=4 , padx=20 , pady=20)

    bi = Button(x, text="LOGIN", fg="white", bg="black")
    bi.grid(row=4, column=4,columnspan=5, padx=20, pady=20)

    fontFamily12 = StringVar(value="Arial")
    fontSize15 = IntVar(value=7)

    tFont = Font(family=fontFamily12.get(), size=fontSize15.get(), weight='normal')

    ylabel = Button(x, text="Not yet registered??", font=tFont,bg="forest green", command=withoutClick)
    ylabel.grid(row=5, column=5)

    x.mainloop()

def withoutClick():
    root = Tk()
    root.configure(background="light green")
    root.title("Sign-up Form")
    fontFamily = StringVar(value="Verdana")
    fontSize = IntVar(value=12)
    fontSize2 = IntVar(value=8)
    fontcon = Font(family=fontFamily.get(), size=fontSize.get(), weight='normal')
    fontconf = Font(family=fontFamily.get(), size=fontSize2.get(), weight='normal')



    myLabel = Label(root, text="SIGN-UP TODAY!!", font=fontcon, bg="light green", fg="dark green", padx=20, pady=50)
    myLabel.grid(row=0,column=4,columnspan = 5,padx=20,pady=20)


    e = Entry(root, width = 100,bg="light blue",justify="center")
    e.insert(END , "Enter your Username:")
    e.grid(row = 1,column=4,columnspan=5,padx=20,pady=20)



    f = Entry(root, width = 100,bg="light blue",justify="center")
    f.insert(END , "Enter your email-id:")
    f.grid(row=2,column=4,columnspan=5,padx=20,pady=20)


    h = Entry(root, width = 100,bg="light blue",justify="center")
    h.insert(END , "Enter your Password:")
    h.grid(row=3,column=4,columnspan=5,padx=20,pady=20)



    g = Entry(root, width = 100,bg="light blue",justify="center")
    g.insert(END , "Re-enter your Password:")
    g.grid(row=4,column=4,columnspan=5,padx=20,pady=20)



    b = Button(root,text="SUBMIT",fg="white",bg="black")
    b.grid(row=5,column=4,columnspan=5,padx=20,pady=20)

    fontFamily2 = StringVar(value="Arial")
    fontSize5 = IntVar(value=7)
    WFont = Font(family=fontFamily2.get(), size=fontSize5.get(), weight='normal')

    yLabel = Button(root,text="Already registered??",font=WFont,bg="forest green",command=onClick,justify="center")
    yLabel.grid(row=6,column=6)

    root.mainloop()


onClick()
