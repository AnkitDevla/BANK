from tkinter import *
from tkinter import font
from tkinter import messagebox
import re
import sqlite3 as sql
# form PIL import Image, ImageTk

con=sql.connect(database='banking,sqlite')
cur=con.cursor()
cur.execute("create table users(acn integer primary key autoincrement,name text,pass text,email test,phone text,balance int)")
con.commit()
con.close()
print("table created")

win = Tk()
win.state("zoomed")
win.configure(bg='powder blue')

title= Label(win,text="Bank Account Simulation",bg='powder blue', font=('Arial',50,'bold','underline'))
title.pack()

# back_img=Image.open("D:/DuCat/2021-11-01  Project/images/back.png")
# bacnk_imgtk=ImageTk.photoImage(back_img,master=win)

def login_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=0.15,relwidth=1,relheight=.85)

    def openaccount():
        frm.destroy()
        openaccount_screen()

    def forgot():
        frm.destroy()
        forgot_screen()

    def welcome():
        a=e_acn.get()
        b=e_pass.get()
        if(len(a)==0 or len(b)==0):
            messagebox.showerror("validation", "Acn/Pass can't be Empty")
            return
        elif(a.isdigit==False):    
            messagebox.showerror("validation", "Acn must contain only Digit")
            return

        frm.destroy()
        welcome_screen()

    def reset():
        e_acn.delete(0,"end")
        e_pass.delete(0,"end")
        e_acn.focus()






    lbl_acn=Label(frm,text="Account Number :", font=('Arail',20,'bold'),bg='pink')
    lbl_acn.place(relx=.3,rely=.2)

    lbl_pass=Label(frm,text="Password :", font=('Arail',20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.3)

    e_acn=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7)
    e_acn.place(relx=.5,rely=.2)
    e_acn.focus()

    e_pass=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7,show="*")
    e_pass.place(relx=.5,rely=.3)

    
    btn_login=Button(frm,command=welcome,text='Login',font=('Arail',20,'bold'),bd=7, width=8,bg='powder blue')
    btn_login.place(relx=.45,rely=.45)

    btn_reset=Button(frm,command=reset,text='Reset',font=('Arail',20,'bold'),bd=7, width=8,bg='powder blue')
    btn_reset.place(relx=.45,rely=.57)

    btn_forgot_pass=Button(frm,command=forgot,text='Forgot Password',font=('Arail',20,'bold'),bd=7, width=15,bg='powder blue')
    btn_forgot_pass.place(relx=.56,rely=.45)

    btn_Open_account=Button(frm,command=openaccount,text='Open Account',font=('Arail',20,'bold'),bd=7, width=15,bg='powder blue')
    btn_Open_account.place(relx=.56,rely=.57)


def openaccount_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=0.15,relwidth=1,relheight=.85)


    def back():
        frm.destroy()
        login_screen()


    def reset():
        e_email.delete(0,'end')
        e_phone.delete(0,'end')
        e_name.delete(0,'end')
        e_pass.delete(0,'end')
        e_name.focus()
        openaccount_screen()

    def open():

        name=e_name.get()
        pwd=e_pass.get()
        email=e_email.get()
        phone=e_phone.get()
        bal=1000

        con=sql.connect(database='banking,sqlite')
        cur=con.cursor()
        cur.execute("insert into users(name,pass,email,phone,bal) values(?,?,?,?,?"),(name,pwd,email,phone,bal)
        con.commit()
        con.close()

        con=sql.connect(database='banking,sqlite')
        cur=con.cursor()
        cur.execute("select max(acn) from users")
        row=cur.fetchone()
        messagebox.showinfo("Open Account","Account created with ACN:{row}")
        con.close()





        
        # if(len(a)==0 or len(b)==0 or len(c)==0 or len(d)==0):
        #     messagebox.showerror("validation", "Name/Password/email/phone can't be Empty")
        #     return

        # elif(a.isalpha==False):    
        #     messagebox.showerror("validation", "Name must contain only Alphabets")
        #     return
        
        # elif((r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')== True):
        #     def check(email):
        #         if(re.fullmatch((r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'), email)):
        #             print("Valid Email")
            
        #         else:
        #             print("Invalid Email")
    
        # elif(d.isdigit==False):    
        #     messagebox.showerror("validation", "Phone Number must contain only Digit")
        #     return


        

        frm.destroy()
        login_screen()

    lbl_name=Label(frm,text="Name", font=('Arail',20,'bold'),bg='pink')
    lbl_name.place(relx=.3,rely=.2)

    e_name=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7)
    e_name.place(relx=.5,rely=.2)
    e_name.focus()


    lbl_pass=Label(frm,text="Password :", font=('Arail',20,'bold'),bg='pink')
    lbl_pass.place(relx=.3,rely=.3)

    e_pass=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7,show="*")
    e_pass.place(relx=.5,rely=.3)


    lbl_email=Label(frm,text="Email", font=('Arail',20,'bold'),bg='pink')
    lbl_email.place(relx=.3,rely=.4)

    e_email=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7)
    e_email.place(relx=.5,rely=.4)


    lbl_phone=Label(frm,text="Phone Number", font=('Arail',20,'bold'),bg='pink')
    lbl_phone.place(relx=.3,rely=.5)

    e_phone=Entry(frm,font=('Arail',20,'bold'),bg='white',bd=7)
    e_phone.place(relx=.5,rely=.5)


    btn_open=Button(frm,command=open,text='Open',font=('Arail',20,'bold'),bd=7, width=8,bg='powder blue')
    btn_open.place(relx=.5,rely=.6)

    btn_reset=Button(frm,command=reset,text='Reset',font=('Arail',20,'bold'),bd=7, width=8,bg='powder blue')
    btn_reset.place(relx=.6,rely=.6)

    btn_back=Button(frm,command=back,text='back',font=('Arail',20,'bold'),bd=7,bg='powder blue')
    btn_back.place(relx=0,rely=0)




def forgot_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=0.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        login_screen()

    btn_back=Button(frm,command=back,text='back',font=('Arail',20,'bold'),bd=7,bg='powder blue')
    btn_back.place(relx=0,rely=0)



def welcome_screen():
    frm=Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0,rely=0.15,relwidth=1,relheight=.85)

    def back():
        frm.destroy()
        login_screen()

    btn_back=Button(frm,command=back,text='back',font=('Arail',20,'bold'),bd=7,bg='powder blue')
    btn_back.place(relx=0,rely=0)




login_screen()
win.mainloop()