from tkinter import *
import psycopg2 as pg2
from tkinter import messagebox


def submit():
    conn = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
    cur = conn.cursor()
    cur.execute('SELECT email,password FROM registered_users')
    b = cur.fetchall()
    lenn = len(b)

    for i in range(lenn):

        if b[i][0] == e1.get() and b[i][1] == e2.get():
            print(b[i][0])
            print(b[i][1])
            conn.close()
            #messagebox.showinfo('info', 'login successfully')
            booking = Tk()
            booking.title('Book An Appointment')
            booking.geometry("350x500")
            
            options_list = [
                "Oncology","Neurology","Cardiology","Gastroenterology","Ophthalmology","Urology"
            ]
            
            day_list=[ 
                "Monday", 'Tuesday', "Wednesday","Thursday","Friday" 
            ]
            
            time = ["10:00 AM","11:00 AM", "12:00 PM", "1:00PM"]
            
            Doctor =[ "Dr. Ashu Agarwal","Dr Sanjay Singh"]
            
            def show(value_inside):
#                 mylabel1 = Label(booking,text = value_inside1.get()).pack()
            
                if value_inside1.get() == "Oncology":
                    value_inside4 = StringVar(booking)
                    value_inside4.set("Select Doctor")
                    drop4= OptionMenu(booking, value_inside4, *Doctor)
                    drop4.pack(ipady=5,ipadx=40)
#                     mylabel4 = Label(booking,text = value_inside4.get()).pack()
                    
                    value_inside2 = StringVar(booking)
                    value_inside2.set("Select Day")
                    drop2= OptionMenu(booking, value_inside2, *day_list)
                    drop2.pack(ipady=5,ipadx=40)
#                     mylabel2 = Label(booking,text = value_inside2.get()).pack()
            
                    value_inside3 = StringVar(booking)
                    value_inside3.set("Time")
                    drop3 = OptionMenu(booking, value_inside3, *time)
                    drop3.pack(ipady=5,ipadx=40)
#                     mylabel3 = Label(booking,text = value_inside3.get()).pack()
                    
                    def final():
                        conn5 = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
                        cur5 = conn5.cursor()
                        cur5.execute('SELECT * FROM registered_users')
                        c = cur5.fetchall()
                        for i in range(len(c)):
                            if c[i][2]==e1.get():
                                q1=c[i][0]
                                q2=c[i][1]
                                q3=c[i][3]
                        conn5.close()
                        
                        conn3 = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
                        cur3 = conn3.cursor()
                        cur3.execute(
                        f"""INSERT INTO confirmed_appointments Values ('{q1}', '{q2}', '{e1.get()}', '{q3}','{value_inside4.get()}','{value_inside1.get()}',
                            '{value_inside3.get()}','{value_inside2.get()}')""")
                        conn3.commit()
                     
                        conn3.close()
                        
                        messagebox.showinfo('info', f'Your Appointment has been scheduled on {value_inside2.get()} {value_inside3.get()}')
                        
                        booking.destroy()
                    
                    
                    submit_button2 = Button(booking,text="Submit",command=final)
                    submit_button2.pack(pady=20,padx=10)
                    
                    
            
            value_inside1 = StringVar(booking)
            value_inside1.set("Select An Specialist")
            drop1= OptionMenu(booking, value_inside1, *options_list, command=show)
            drop1.pack(ipady=5,ipadx=40)                
            
            
#             submit_button= Button(booking,text="Submit", command=show)
#             submit_button.pack(pady=20,padx=10)


def reset_password():
    def reset_submit():
        messagebox.showinfo('info', 'successfully registered')

        conn1 = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
        cur1 = conn1.cursor()
        cur1.execute(
            f"INSERT INTO registered_users Values ('{q1.get()}', '{q2.get()}', '{q3.get()}', '{q4.get()}', '{q5.get()}')")
        conn1.commit()

        cur1.close()

        s.destroy()

    s = Tk()
    s.title('NEW REGISTER')
    s.geometry("500x190")

    R1 = Label(s, text='First Name', fg='white', bg='black')
    R1.place(x=40, y=10)
    q1 = Entry(s)
    q1.place(x=110, y=10)

    R2 = Label(s, text='Last Name', fg='white', bg='black')
    R2.place(x=260, y=10)
    q2 = Entry(s)
    q2.place(x=330, y=10)

    R3 = Label(s, text='E.mail', fg='white', bg='black')
    R3.place(x=40, y=40)
    q3 = Entry(s)
    q3.place(x=110, y=40)

    R4 = Label(s, text='Phone', fg='white', bg='black')
    R4.place(x=40, y=70)
    q4 = Entry(s)
    q4.place(x=110, y=70)

    R3 = Label(s, text='Password', fg='white', bg='black')
    R3.place(x=40, y=100)
    q5 = Entry(s)
    q5.place(x=110, y=100)

    w1 = Button(s, text='Submit', fg='white', bg='black', command=reset_submit)  ####command=reset_submit
    w1.place(x=370, y=140)

    s.mainloop()


def registered_users():
    e = 40
    n = Tk()
    n.title('PROJECT LOGIN REG PAGE')
    n.geometry("400x700")
    conn = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
    cur = conn.cursor()
    cur.execute('SELECT *FROM registered_users')
    b = cur.fetchall()
    for i in b:
        j = Button(n, text=i, fg='white', bg='black')
        j.place(x=40, y=e)
        e = e + 30


def password_pop():
    def get_password():

        conn = pg2.connect(database='PROJECT LOGIN REG PAGE', user='postgres', password='password')
        cur = conn.cursor()
        cur.execute('SELECT email,password FROM registered_users')
        b = cur.fetchall()
        k = len(b)

        for i in range(k):
            if b[i][0] == f1.get():
                password = b[i][1]
                messagebox.showinfo('password', password)
                break
            else:
                if i == k - 1:
                    messagebox.showinfo('info', "Enter Valid I'd")

        conn.close()
        z.destroy()

    z = Tk()
    z.title('get_password')
    z.geometry("200x80")
    z1 = Label(z, text='E.mail', fg='white', bg='black')
    z1.place(x=10, y=6)
    f1 = Entry(z)
    f1.place(x=55, y=6)
    v1 = Button(z, text='Submit', fg='white', bg='black', command=get_password)  ####command=submit
    v1.place(x=70, y=40)


a = Tk()
a.title('MAX Healthcare')
a.geometry("400x200")

L1 = Label(a, text='Email', fg='white', bg='black')
L1.place(x=100, y=10)
e1 = Entry()
e1.place(x=170, y=10)

L2 = Label(a, text='Password', fg='white', bg='black')
L2.place(x=95, y=45)
e2 = Entry()
e2.place(x=170, y=45)

b1 = Button(a, text='Log In', fg='white', bg='black', command=submit)  ####command=submit
b1.place(x=245, y=75)
b2 = Button(a, text='Sign up', fg='white', bg='black', command=reset_password)  ####command=forget pswd
b2.place(x=24, y=100)
b3 = Button(a, text='Forgotten Password', fg='white', bg='black', command=password_pop)  #### command= reg
b3.place(x=24, y=130)
b4 = Button(a, text='registered_users', fg='white', bg='black', command=registered_users)
b4.place(x=280, y=150)

a.mainloop()