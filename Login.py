from tkinter import *
from tkinter import messagebox
import ast


root=Tk()
root.title("login")
root.geometry('900x550+300+200')
root.configure(bg="#85BDA6")
root.resizable(False,False)

def signin():
    username=user.get()
    password=code.get()

    file=open('datasheet.txt','r')
    d=file.read()
    r=ast.literal_eval(d)
    file.close()

    # print(r.keys())
    # print(r.values())


    if username in r.keys() and password==r[username]:
        screen=Toplevel(root)
        screen.title("Quiz")
        screen.geometry('925x500+300+200')
        screen.config(bg="white")

        Label(screen, text="Hello Everyone!!",bg="#fff",font=('Calibri(Body)',50,'bold')).pack(expand=True)


        screen.mainloop()
    else:
        messagebox.showerror('Invalid','invalid username or password')

######ooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooo
def signup_command():
    window=Toplevel(root)
    window.title("signup")
    window.geometry('900x500+300+200')
    window.configure(bg="#fff")
    window.resizable(False, False)

    def signup():
        username = user.get()
        password = code.get()
        confirm_pass = confirm.get()

        if password == confirm_pass:
            try:
                file = open('datasheet.txt', 'r+')
                d = file.read()
                r = ast.literal_eval(d)

                dict2 = {username: password}
                r.update(dict2)
                file.truncate(0)
                file.close()

                file = open('datasheet.txt', 'w')
                w = file.write(str(r))

                messagebox.showinfo('Signup', 'Successfull sign up')

            except:
                file = open('datasheet.txt', 'w')
                pp = str({'Username': 'password'})
                file.write(pp)
                file.close()

        else:
            messagebox.showerror('Invalid', "Both Password should match")

    def sign():
        window.destroy()

    img = PhotoImage(file='signup.png')
    Label(window, image=img, border=0, bg='white').place(x=-40, y=-50)

    frame = Frame(window, width=350, height=390, bg='#85bda6')
    frame.place(x=480, y=50)

    heading = Label(frame, text='Sign up', fg='black', bg='#85bda6', font=('Microsoft YaHei UI Light', 23, 'bold'))
    heading.place(x=100, y=5)

    #####----------------------------------------------------------------
    def on_enter(e):
        user.delete(0, 'end')

    def on_leave(e):
        if user.get() == '':
            user.insert(0, 'Username')

    user = Entry(frame, width=25, fg='black', border=0, bg='#85bda6', font=('Microsoft YaHei UI Light', 11))
    user.place(x=30, y=80)
    user.insert(0, "Username")
    user.bind('<FocusIn>', on_enter)
    user.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

    ######--------------------------------------------------------
    def on_enter(e):
        code.delete(0, 'end')

    def on_leave(e):
        if code.get() == '':
            code.insert(0, 'Password')

    code = Entry(frame, width=25, fg='black', border=0, bg='#85bda6', font=('Microsoft YaHei UI Light', 11))
    code.place(x=30, y=150)
    code.insert(0, "Password")
    code.bind('<FocusIn>', on_enter)
    code.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

    ################----------------------------------------------
    def on_enter(e):
        confirm.delete(0, 'end')

    def on_leave(e):
        if confirm.get() == '':
            confirm.insert(0, 'Confirm Password')

    confirm = Entry(frame, width=25, fg='black', border=0, bg='#85bda6', font=('Microsoft YaHei UI Light', 11))
    confirm.place(x=30, y=220)
    confirm.insert(0, "Confirm Password")
    confirm.bind('<FocusIn>', on_enter)
    confirm.bind('<FocusOut>', on_leave)

    Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

    ####-------------------------------------------------------------

    Button(frame, width=39, pady=7, text='Sign up', bg='#57a1f8', fg="white", border=0, command=signup).place(x=35,
                                                                                                              y=280)
    label = Label(frame, text='Already have an account?', fg='black', bg='#85bda6',
                  font=('Microsoft Yahei UI Light', 9))
    label.place(x=90, y=340)

    signin = Button(frame, width=6, text='Sign in', border=0, bg='#85bda6', cursor='hand2', fg='#57a1f8', command=sign)
    signin.place(x=250, y=340)

    window.mainloop()





###########0000000000000000000000000000000000000000000000000000000000000000000

img = PhotoImage(file='logo.png')
Label(root,image=img,border=0,bg='#85BDA6').place(x=385,y=10)

frame=Frame(root,width=350,height=350,bg="#BEDCFE")
frame.place(x=280,y=150)

heading=Label(frame,text='Sign in',fg='black',bg='#BEDCFE',font=('Microsoft YaHei UI Light',23,'bold'))
heading.place(x=100,y=5)


##-------------------------------------------------

def on_enter(e):
    user.delete(0,'end')

def on_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'Username')


user=Entry(frame,width=25,fg='black',border=0,bg='#BEDCFE',font=('Microsoft YaHei UI Light',11))
user.place(x=30,y=80)
user.insert(0,'Username')
user.bind('<FocusIn>',on_enter)
user.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=105)

##----------------------------------------------------
def on_enter(e):
    code.delete(0,'end')

def on_leave(e):
    name=code.get()
    if name=='':
        code.insert(0,'Password')


code=Entry(frame,width=25,fg='black',border=0,bg='#BEDCFE',font=('Microsoft YaHei UI Light',11))
code.place(x=30,y=150)
code.insert(0,'Password')
code.bind('<FocusIn>',on_enter)
code.bind('<FocusOut>',on_leave)

Frame(frame,width=295,height=2,bg='black').place(x=25,y=175)

#####-----------


Button(frame,width=39,pady=7,text='Sign in',bg='#57a1f8',fg='white',border=0,command=signin).place(x=35,y=204)
label=Label(frame,text="Dont have an account?",fg='black',bg='#BEDCFE',font=('Microsoft Yahei UI Light',9))
label.place(x=75,y=270)

sign_up= Button(frame,width=6,text='Sign up',border=0,bg='#BEDCFE',cursor='hand2',fg="#57a1f8",command=signup_command)
sign_up.place(x=215,y=270)

root.mainloop()