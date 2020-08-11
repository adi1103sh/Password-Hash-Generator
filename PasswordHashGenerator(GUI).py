from tkinter import *
# Frontend Design
window=Tk()
window.config(bg="light green")
window.title("Password Hash Generator{by--->'ADARSH SHARMA'}")
window.geometry('500x300')
l1=Label(window,text="WELCOME!!!\nLets encrypt🔐 your password🔑",bg='light blue')
labelfont=('times',20,'bold','underline')
l1.config(font=labelfont)
l1.pack()
l2=Label(window,text="Enter any password",bg='red',fg='white')
labelfont=('arial',15)
l2.config(font=labelfont)
l2.pack()
wl=StringVar()
wd=Entry(window,width=50,textvariable=wl)
wd.pack()
# Password Hash Conversion
from hashlib import md5
pswd_hash=md5(wd.get().encode()).hexdigest()
# Button Functionality
def click():
    b.configure(text=f"Password Hash for '{wd.get()}' is:\n{pswd_hash}")
b=Button(window,text="Generate🔄",bg='Black',fg='Yellow',command=click)
b.pack()
window.mainloop()