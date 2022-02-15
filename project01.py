from tkinter import *
from tkinter import messagebox
import sqlite3 as sql
from tkinter import font


try:
    con = sql.connect(database="banking.sqlite")
    cur = con.cursor()
    cur.execute("create table users(acn integer primary key autoincrement,name text,pass text,email text,mob text,bal int)")
    con.commit()
    con.close()
    print("table created")
except sql.Error as error:
    print("Table Exist")
finally:
    if con:
        con.close()


win = Tk()
win.state("zoomed")
win.configure(bg='powder blue')

title = Label(win, text="Bank Account Simulation",
              bg='powder blue', font=('Arial', 50, 'bold', 'underline'))
title.pack()


def home_screen():
    frm = Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0, rely=0.15, relwidth=1, relheight=.85)

    def login():
        a = e_acn.get()
        p = e_pass.get()
        if(len(a) == 0 or len(p) == 0):
            messagebox.showerror("validation", "Acn/Pass can't be Empty")
            return
        elif(a.isdigit() == False):
            messagebox.showerror("validation", "Acn must contain only Digit")
            return

        else:
            con = sql.connect(database="banking.sqlite")
            cur = con.cursor()
            cur.execute("select * from users where acn=? and pass=?", (a, p))
            global loggedin_user
            loggedin_user = cur.fetchone()
            if(loggedin_user == None):
                messagebox.showerror("validation", "Invalid acn/pass")
                return
            else:
                frm.destroy()
                login_screen()

    def reset():
        e_acn.delete(0, 'end')
        e_pass.delete(0, 'end')
        e_acn.focus()

    lbl_acn = Label(frm, text="Account Number :",
                    font=('Arail', 20, 'bold'), bg='pink')
    lbl_acn.place(relx=.3, rely=.2)

    lbl_pass = Label(frm, text="Password :", font=(
        'Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.3)

    e_acn = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_acn.place(relx=.5, rely=.2)
    e_acn.focus()

    e_pass = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7, show="*")
    e_pass.place(relx=.5, rely=.3)

    btn_login = Button(frm, command=login, text='login', font=(
        'Arail', 20, 'bold'), bd=7, width=8, bg='powder blue')
    btn_login.place(relx=.45, rely=.45)

    btn_reset = Button(frm, command=reset, text='Reset', font=(
        'Arail', 20, 'bold'), bd=7, width=8, bg='powder blue')
    btn_reset.place(relx=.45, rely=.57)

    btn_forgot_pass = Button(frm, command=forget_pass, text='Forgot Password', font=(
        'Arail', 20, 'bold'), bd=7, width=15, bg='powder blue')
    btn_forgot_pass.place(relx=.56, rely=.45)

    btn_Open_account = Button(frm, command=openaccount_screen, text='Open Account', font=(
        'Arail', 20, 'bold'), bd=7, width=15, bg='powder blue')
    btn_Open_account.place(relx=.56, rely=.57)


def openaccount_screen():
    frm = Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0, rely=0.15, relwidth=1, relheight=.85)

    def back():
        frm.destroy()
        home_screen()

    btn_back = Button(frm, command=back, text='back', font=(
        'Arail', 20, 'bold'), bd=7, bg='powder blue')
    btn_back.place(relx=0, rely=0)

    def reset():
        e_name.delete(0, 'end')
        e_pass.delete(0, 'end')
        e_phone.delete(0, 'end')
        e_email.delete(0, 'end')
        e_name.focus()

    def open():
        name = e_name.get()
        pwd = e_pass.get()
        email = e_email.get()
        mob = e_phone.get()
        bal = 1000

        if(len(name) == 0 or len(pwd) == 0 or len(email) == 0 or len(mob) == 0):
            messagebox.showerror("validation", "Space can't be Empty")
            return
        elif(mob.isdigit() == False):
            messagebox.showerror(
                "validation", "Mobile must contain only Digit")
            return
        frm.destroy()
        openaccount_screen()

        con = sql.connect(database="banking.sqlite")
        cur = con.cursor()
        cur.execute("insert into users(name,pass,email,mob,bal) values(?,?,?,?,?)",
                    (name, pwd, email, mob, bal))
        con.commit()
        con.close()

        con = sql.connect(database="banking.sqlite")
        cur = con.cursor()
        cur.execute("select max(acn) from users")
        row = cur.fetchone()
        messagebox.showinfo("Open Account", f"Account Number is :{row[0]}")
        con.commit()
        con.close()
        frm.destroy()
        home_screen()

    lbl_acn = Label(frm, text="Name :", font=('Arail', 20, 'bold'), bg='pink')
    lbl_acn.place(relx=.3, rely=.2)

    lbl_pass = Label(frm, text="Password :", font=(
        'Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.3)

    lbl_pass = Label(frm, text="Mobile :", font=(
        'Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.4)

    lbl_pass = Label(frm, text="Email :", font=(
        'Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.5)

    e_name = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_name.place(relx=.5, rely=.2)
    e_name.focus()

    e_pass = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7, show="*")
    e_pass.place(relx=.5, rely=.3)

    e_phone = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_phone.place(relx=.5, rely=.4)

    e_email = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_email.place(relx=.5, rely=.5)

    btn_Open_account = Button(frm, command=open, text='Open Account', font=(
        'Arail', 20, 'bold'), bd=7, width=15, bg='powder blue')
    btn_Open_account.place(relx=.45, rely=.6)

    btn_reset = Button(frm, command=reset, text='Reset', font=(
        'Arail', 20, 'bold'), bd=7, width=8, bg='powder blue')
    btn_reset.place(relx=.64, rely=.6)


def forget_pass():
    frm = Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0, rely=0.15, relwidth=1, relheight=.85)

    def back():
        frm.destroy()
        home_screen()

    btn_back = Button(frm, command=back, text='back', font=(
        'Arail', 20, 'bold'), bd=7, bg='powder blue')
    btn_back.place(relx=0, rely=0)

    def Forget():
        acn = e_acn.get()
        mob = e_mob.get()
        email = e_email.get()

        con = sql.connect(database="banking.sqlite")
        cur = con.cursor()
        cur.execute("select pass from users where acn=? and mob=? and email=?", (acn, mob, email))
        row = cur.fetchone()
        if(row == None or mob.isdigit() == False):
            messagebox.showerror("Invalid Crediantials",
                                 "Account Number Does Not exists")
            frm.destroy()
            forget_pass()

        else:
            messagebox.showinfo("Password Recovery",
                                f"Your Password is: {row[0]}")
            frm.destroy()
            home_screen()

    def reset():
        e_acn.delete(0, "end")
        e_mob.delete(0, "end")
        e_email.delete(0, "end")
        e_acn.focus()

    lbl_acn = Label(frm, text="Account Number :",
                    font=('Arail', 20, 'bold'), bg='pink')
    lbl_acn.place(relx=.3, rely=.2)

    lbl_pass = Label(frm, text="Mobile Number :",
                     font=('Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.3)

    lbl_pass = Label(frm, text="Email :", font=(
        'Arail', 20, 'bold'), bg='pink')
    lbl_pass.place(relx=.3, rely=.4)

    e_acn = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_acn.place(relx=.5, rely=.2)
    e_acn.focus()

    e_mob = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7, )
    e_mob.place(relx=.5, rely=.3)

    e_email = Entry(frm, font=('Arail', 20, 'bold'), bg='white', bd=7)
    e_email.place(relx=.5, rely=.4)

    btn_forget = Button(frm, command=Forget, text='Forget', font=(
        'Arail', 20, 'bold'), bd=7, width=8, bg='powder blue')
    btn_forget.place(relx=.5, rely=.52)

    btn_reset = Button(frm, command=reset, text='Reset', font=(
        'Arail', 20, 'bold'), bd=7, width=8, bg='powder blue')
    btn_reset.place(relx=.62, rely=.52)


def login_screen():
    frm = Frame(win)
    frm.configure(bg='pink')
    frm.place(relx=0, rely=0.15, relwidth=1, relheight=.85)

    def out():
        frm.destroy()
        home_screen()

    def details():
        inr_frm = Frame(win)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=0.3, rely=0.3, relwidth=.5, relheight=.4)

        con=sql.connect(database="banking.sqlite")
        cur=con.cursor()
        cur.execute("select bal from users where acn=?",(loggedin_user[0],))
        update_bal=cur.fetchone()[0]
        con.close()
       
        lbl_bal = Label(
            inr_frm, text=f"Balance:\t\t\t {update_bal}", bg='pink', font=('Arail', 15, 'bold'))
        lbl_bal.place(relx=0.3, rely=0.7)
       
        lbl_acn = Label(
            inr_frm, text=f"Account Number:\t\t {loggedin_user[0]}", bg='pink', font=('Arail', 15, 'bold'))
        lbl_acn.place(relx=0.3, rely=0.3)

        lbl_name = Label(
            inr_frm, text=f"Name:\t\t\t {loggedin_user[1]}", bg='pink', font=('Arail', 15, 'bold'))
        lbl_name.place(relx=0.3, rely=0.4)
        
        lbl_mob = Label(
            inr_frm, text=f"Mobile Number:\t\t {loggedin_user[4]}", bg='pink', font=('Arail', 15, 'bold'))
        lbl_mob.place(relx=0.3, rely=0.5)
        
        lbl_email = Label(
            inr_frm, text=f"Email ID:\t\t\t {loggedin_user[3]}", bg='pink', font=('Arail', 15, 'bold'))
        lbl_email.place(relx=0.3, rely=0.6)
        

    def deposit():
        inr_frm = Frame(win)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=0.3, rely=0.3, relwidth=.5, relheight=.4)

        def deposit_db():
            amount =int(e_amount.get())
            con=sql.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("update users set bal=bal+? where acn=?",(amount,loggedin_user[0]))
            con.commit()
            con.close()
            messagebox.showinfo("Deopsit Successful","Done")
            e_amount.delete(0, 'end')


        lbl_amt = Label(inr_frm, text="Amount:", bg='pink', font=('Arail', 15, 'bold'))
        lbl_amt.place(relx=0.1, rely=.2)

        e_amount = Entry (inr_frm, font=('Arail', 15, 'bold'))
        e_amount.place(relx=.3,rely=.2)
        e_amount.focus()
        

        btn_dep = Button(inr_frm, command=deposit_db, text='Deposit', font=(
            'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
        btn_dep.place(relx=0.2, rely=.4)
        


    def withdraw():
        inr_frm = Frame(win)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=0.3, rely=0.3, relwidth=.5, relheight=.4)


        def withdraw_wd():
            amount =int(e_amount.get())
            con=sql.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("select bal from users where acn=?",(loggedin_user[0],))
            update_bal=cur.fetchone()[0]
            con.close()

            if (update_bal >=amount):
                con=sql.connect(database="banking.sqlite")
                cur=con.cursor()
                cur.execute("update users set bal=bal-? where acn=?",(amount,loggedin_user[0]))
                con.commit()
                con.close()
                messagebox.showinfo("Withdraw Successful","Done")
                e_amount.delete(0, 'end')

            else:
                messagebox.showwarning("Withdraw","Insuffient Balance")
                e_amount.delete(0, 'end')


        lbl_amt = Label(inr_frm, text="Amount:", bg='pink', font=('Arail', 15, 'bold'))
        lbl_amt.place(relx=0.1, rely=.2)

        e_amount = Entry (inr_frm, font=('Arail', 15, 'bold'))
        e_amount.place(relx=.3,rely=.2)
        e_amount.focus()
        

        btn_wit = Button(inr_frm, command=withdraw_wd, text='Withdarw', font=(
            'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
        btn_wit.place(relx=0.2, rely=.4)


    def transfer():
        inr_frm = Frame(win)
        inr_frm.configure(bg='pink')
        inr_frm.place(relx=0.3, rely=0.3, relwidth=.5, relheight=.4)


        def transfer_tr():
            amount =int(e_amount.get())
            toacn=int(e_toacn.get())
            con=sql.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("select bal from users where acn=?",(loggedin_user[0],))
            update_bal=cur.fetchone()[0]
            con.close()

            con=sql.connect(database="banking.sqlite")
            cur=con.cursor()
            cur.execute("select acn from users where acn=?",(toacn,))
            toacn_frm_db=cur.fetchone()
            con.close()
            if(toacn_frm_db==None):
                messagebox.showwarning("Withdraw","Invalid Account Nunber")
                e_amount.delete(0,'end')
                e_toacn.delete(0,'end')
            else:
                if (update_bal >=amount):
                    con=sql.connect(database="banking.sqlite")
                    cur=con.cursor()
                    cur.execute("update users set bal=bal-? where acn=?",(amount,loggedin_user[0]))
                    cur.execute("update users set bal=bal+? where acn=?",(amount,toacn))
                    con.commit()
                    con.close()
                    messagebox.showinfo("Transaction","Done")
                    e_amount.delete(0, 'end')
                    e_toacn.delete(0, 'end')
                    e_amount.focus()

                else:
                    messagebox.showwarning("Withdraw","Insuffient Balance")
                    e_amount.delete(0, 'end')
                    e_toacn.delete(0, 'end')
                    e_amount.focus()

        lbl_amount = Label(inr_frm, text="Amount:", bg='pink', font=('Arail', 15, 'bold'))
        lbl_amount.place(relx=0.1, rely=.2)

        e_amount = Entry (inr_frm, font=('Arail', 15, 'bold'))
        e_amount.place(relx=.3,rely=.2)
        e_amount.focus()
        

        lbl_toacn = Label(inr_frm, text="To Account:", bg='pink', font=('Arail', 15, 'bold'))
        lbl_toacn.place(relx=0.1, rely=.35)

        e_toacn = Entry (inr_frm, font=('Arail', 15, 'bold'))
        e_toacn.place(relx=.3,rely=.35) 

         
        btn_transfer = Button(inr_frm, command=transfer_tr, text='Transfer', font=(
            'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
        btn_transfer.place(relx=0.25, rely=.48)



    btn_deposit = Button(frm, command=deposit, text='Deposit', font=(
        'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
    btn_deposit.place(relx=0, rely=.6)

    btn_withdraw = Button(frm, command=withdraw, text='Withdraw', font=(
        'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
    btn_withdraw.place(relx=0, rely=.4)

    btn_details = Button(frm, command=details, text='Details', font=(
        'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
    btn_details.place(relx=0, rely=.2)

    btn_transfer_bal = Button(frm, command=transfer, text='Transfer', font=(
        'Arail', 20, 'bold'), bd=7, width=10, bg='powder blue')
    btn_transfer_bal.place(relx=0, rely=.8)

    btn_out = Button(frm, command=out, text='Log Out', font=(
        'Arail', 15, 'bold'), bd=7, width=10, bg='powder blue')
    btn_out.place(relx=.9, rely=0)

    lbl_wel = Label(
        frm, text=f"Welcome,{loggedin_user[1]}", bg='pink', font=('Arail', 15, 'bold'))
    lbl_wel.place(relx=0, rely=0)


home_screen()
win.mainloop()
