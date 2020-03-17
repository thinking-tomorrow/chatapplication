from tkinter import *
from PIL import ImageTk,Image
from tkinter.font import Font
import tkinter.ttk as x

def click(num):
	if(num==1):
		x = Tk()
		x.configure(background="light blue")
		x.title("Contact  "+ str(num) + " Chat Page")
		top = Frame(x,bg="light blue",pady=20,padx=500)
		top.grid(row=0,column=0,columnspan=30)
		img = Image.open('pr.jpg')#the location of the image would change according to every user
		image = img.resize((30, 30), Image.ANTIALIAS)
		openimg = ImageTk.PhotoImage(image)
		conbi = Button(top,image=openimg)
		conbi.grid(row=(0),column=(0))
		conbi.image = openimg
		Button(top,text="Contact  "+str(num),font=("Courier",12,"bold"),bg="light green",fg="red").grid(row=0,column=1)
		new=Frame(x,bg="pink")
		new.grid(row=1,column=0)
		Label(new,text="Hello!!",bg="pink",fg="black").grid(row=1,column=0)
		Label(new,text="14.08",bg="pink",font=("Arial",6,'roman'),padx=5).grid(row=1,column=1)
		Label(x,text="                                                                                                                                                          ",bg="light blue",fg="black").grid(row=2,column=0)
		ne=Frame(x,bg="snow")
		ne.grid(row=2,column=3)
		Label(ne,text="Who are you?",bg="snow",fg="black").grid(row=2,column=4)
		Label(ne,text="14.08",bg="snow",font=("Arial",6,'roman')).grid(row=2,column=5)
		n=Frame(x,bg="pink")
		n.grid(row=3,column=0)
		Label(n,text="I am contact "+str(num),bg="pink",fg="black").grid(row=3,column=0)
		Label(n,text="14.08",bg="pink",font=("Arial",6,'roman')).grid(row=3,column=1)
		me = Frame(x,pady=300,bg="light blue")
		me.grid(row=15,column=3)
		fontfa = StringVar(value="Magneto")
		fonts = IntVar(value=12)
		mesfont = Font(family=fontfa.get(),size=fonts.get(),weight='normal')
		e = Entry(me,font=mesfont,borderwidth=5,bg="yellow",justify="center")
		e.grid(row=5,column=0)
		e.insert(END,"Type in to chat:")
		
		img = Image.open('send.png')
		image = img.resize((20, 20), Image.ANTIALIAS)
		openimg = ImageTk.PhotoImage(image)
		button1 = Button(me, image=openimg)
		button1.grid(row=5,column=3)
		button1.image = openimg
		
		x.mainloop()
		x.destroy()
	
	else:
		x = Tk()
		x.configure(background="light blue")
		x.title("Contact  "+ str(num) + " Chat Page")
		top = Frame(x,bg="light blue",pady=20,padx=500)
		top.grid(row=0,column=0,columnspan=30)
		img = Image.open('pr.jpg')#the location of the image would change according to every user
		image = img.resize((30, 30), Image.ANTIALIAS)
		openimg = ImageTk.PhotoImage(image)
		conbi = Button(top,image=openimg)
		conbi.grid(row=(0),column=(0))
		conbi.image = openimg
		Button(top,text="Contact  "+str(num),font=("Courier",12,"bold"),bg="light green",fg="red").grid(row=0,column=1)
		new=Frame(x,bg="pink")
		new.grid(row=1,column=0)
		Label(new,text="Hello!!",bg="pink",fg="black").grid(row=1,column=0)
		Label(new,text="14.08",bg="pink",font=("Arial",6,'roman'),padx=5).grid(row=1,column=1)
		Label(x,text="                                                                                                                                                          ",bg="light blue",fg="black").grid(row=2,column=0)
		ne=Frame(x,bg="snow")
		ne.grid(row=2,column=3)
		Label(ne,text="Who are you?",bg="snow",fg="black").grid(row=2,column=4)
		Label(ne,text="14.08",bg="snow",font=("Arial",6,'roman')).grid(row=2,column=5)
		n=Frame(x,bg="pink")
		n.grid(row=3,column=0)
		Label(n,text="I am contact "+str(num),bg="pink",fg="black").grid(row=3,column=0)
		Label(n,text="14.08",bg="pink",font=("Arial",6,'roman')).grid(row=3,column=1)
		me = Frame(x,pady=300,bg="light blue")
		me.grid(row=15,column=3)
		fontfa = StringVar(value="Magneto")
		fonts = IntVar(value=12)
		mesfont = Font(family=fontfa.get(),size=fonts.get(),weight='normal')
		e = Entry(me,font=mesfont,borderwidth=5,bg="yellow",justify="center")
		e.grid(row=5,column=0)
		e.insert(END,"Type in to chat:")
		
		img = Image.open('send.png')
		image = img.resize((20, 20), Image.ANTIALIAS)
		openimg = ImageTk.PhotoImage(image)
		button1 = Button(me, image=openimg)
		button1.grid(row=5,column=3)
		button1.image = openimg
		
		x.mainloop()
		x.destroy()

root = Tk()
root.title("Chat Page")
root.configure(background="light green")

ame = Frame(root,bg="light green")
ame.grid(row=0,column=5,pady=20,padx=100)

fontfamily = StringVar(value="Kalpurush")
fontSize = IntVar(value=14)
appFont = Font(family=fontfamily.get(),size=fontSize.get(),weight='bold')


myLabel = Label(ame,font=appFont,text="USERNAME",bg="light green",fg="red",padx=10)
myLabel.grid(row=0,column=0,columnspan=3)

img = Image.open('default.jfif')
image = img.resize((30, 30), Image.ANTIALIAS)
openimg = ImageTk.PhotoImage(image)


button1 = Button(ame, image=openimg, command=click,bg="light green")
button1.grid(row=0,column=4)
button1.image = openimg


fontfamily = StringVar(value="Magneto")
fontSize = IntVar(value=14)
appFont = Font(family=fontfamily.get(),size=fontSize.get(),weight='normal')

frame = Frame(root,bg="light green")
frame.grid(row=1,column=5,padx=100)

sm = Image.open('search.png')
sem = sm.resize((20,20),Image.ANTIALIAS)
searchmenu = ImageTk.PhotoImage(sem)



newlabel = Entry(frame,font=appFont,bg="pink",fg="blue",justify="center",borderwidth=0)
newlabel.insert(END,"Search to start a new chat")
newlabel.grid(row=1,column=0,columnspan=4)

button1 = Button(frame, image=searchmenu , bg='white', command=click)
button1.grid(row=1,column=5)
button1.image = searchmenu

f = StringVar(value="Courier")
s = IntVar(value=20)

cf = Font(family=f.get(),size=s.get(),weight='normal')

scrollbar = Scrollbar(root,orient="vertical")

canvas = Canvas(root,bg="light green")
scroll_y = Scrollbar(root,orient="vertical", command=canvas.yview)

frame = Frame(canvas,bg="light green")

img = Image.open('pr.jpg')#the location of the image would change according to every user
image = img.resize((30, 30), Image.ANTIALIAS)
openimg = ImageTk.PhotoImage(image)


Button(frame,bg="yellow",command= lambda: [root.destroy(),click(1)],text="Contact "+str(1),width=48,anchor="center",justify="center").grid(row=(3),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(3),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(2)],text="Contact "+str(1+1),width=48,anchor="center",justify="center").grid(row=(2+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(4),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(3)],text="Contact "+str(2+1),width=48,anchor="center",justify="center").grid(row=(3+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(5),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(4)],text="Contact "+str(3+1),width=48,anchor="center",justify="center").grid(row=(4+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(6),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(5)],text="Contact "+str(4+1),width=48,anchor="center",justify="center").grid(row=(5+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(7),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(6)],text="Contact "+str(5+1),width=48,anchor="center",justify="center").grid(row=(6+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(8),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(7)],text="Contact "+str(6+1),width=48,anchor="center",justify="center").grid(row=(7+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(9),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(8)],text="Contact "+str(7+1),width=48,anchor="center",justify="center").grid(row=(8+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(10),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(9)],text="Contact "+str(8+1),width=48,anchor="center",justify="center").grid(row=(9+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(11),column=(0))
conbi.image = openimg
Button(frame,bg="yellow",command= lambda: [root.destroy(),click(10)],text="Contact "+str(9+1),width=48,anchor="center",justify="center").grid(row=(10+2),column=(5))
conbi = Button(frame,image=openimg)
conbi.grid(row=(12),column=(0))
conbi.image = openimg


canvas.create_window(0, 0, anchor='nw', window=frame)

canvas.update_idletasks()

canvas.configure(scrollregion=canvas.bbox('all'), 
                 yscrollcommand=scroll_y.set)
                 
canvas.grid(row=2,column=5,rowspan=20,padx=100)
scroll_y.grid(row=2,column=6,rowspan=20,sticky="ns")



root.mainloop()
