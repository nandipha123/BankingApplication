from tkinter import*
import os 
from PIL import ImageTk, Image
from tkinter import messagebox


master=Tk()
master.title('Banking App')
master.geometry('600x400')

master.configure(bg="#395a67",pady=40)

def finish_reg():
    name=temp_name.get()
    account_num=temp_account_num.get()
    # idNumber=temp_idNumber.get()
    password=temp_password.get()

    all_accounts= os.listdir()
    if name=="" or account_num==""  or password=="":
        notif.config(fg="#c3042e", text="All fields required *")
        return
    
    for name_check in all_accounts:
        if name ==name_check:
            notif.config(fg="#c3042e", text="Account already exists")
            return
        else:
            new_file = open(name,"w")
            new_file.write(name+'\n')
            new_file.write(account_num+"\n")
            new_file.write(password+'\n')

            new_file.write("0")
            new_file.close()

            notif.config(fg="green", text="Account has been created")


#functions
def register():
    global temp_name
    global temp_account_num
    global temp_idNumber
    global temp_password
    global notif

    temp_name= StringVar()
    temp_account_num=StringVar()
    temp_idNumber=StringVar()
    temp_password=StringVar()

    register_screen= Toplevel(master)
    register_screen.title('Register')
    register_screen.configure(bg='#395a67',padx=30)
    register_screen.geometry('600x400')

    #Reg screen labels and Entries

    Label(register_screen, text="Enter your details", font=('Baskervill Old Face', 12),bg='#395a67',fg='#8ea9bc').grid(row=0,sticky='news', pady=40)
    # Label (register_screen, image=reg_img, bg='white').grid(row=1,sticky=N)

    Label(register_screen, text="Full Name: ", font=('Baskervill Old Face', 12), bg='#395a67',fg='#8ea9bc').grid(row=2,sticky=W, padx=100)
    Entry(register_screen, textvariable=temp_name).grid(row=2, column=4, sticky=E)
    Label(register_screen, text="Account Number: ", font=('Baskervill Old Face', 12), bg='#395a67',fg='#8ea9bc').grid(row=3,sticky=W, padx=100)
    Entry(register_screen, textvariable=temp_account_num).grid(row=3, column=4, sticky=E)
    # Label(register_screen, text="ID Number: ", font=('Baskervill Old Face', 12), bg='white',fg='black').grid(row=4,sticky=W, padx=100)
    # Entry(register_screen, textvariable=temp_idNumber).grid(row=4, column=4,sticky=E)
    Label(register_screen, text="Password: ", font=('Baskervill Old Face', 12), bg='#395a67',fg='#8ea9bc').grid(row=5,sticky=W, padx=100)
    Entry(register_screen, textvariable=temp_password,show="*").grid(row=5,column=4,sticky=E)

    notif=Label(register_screen, font=('Baskervill Old Face', 12), bg='white')
    notif.grid(row=6,sticky=N, pady=10)

    Button(register_screen, text="Register", command=finish_reg, font=('Baskervill Old Face',12)).grid(row=7,sticky=N,pady=5,padx=90)

def login_session():

    global login_name
    all_accounts=os.listdir()
    login_name=temp_login_name.get()
    login_password=temp_login_password.get()


    for name in all_accounts:

        if name==login_name:
            file=open(name,"r")
            file_data = file.read()
            file_data= file_data.split('\n')
            password= file_data[2]

            if login_password==password:
                login_screen.destroy()
                account_dashboard=Toplevel(master)
                account_dashboard.title('Home')
                account_dashboard.configure(bg='#395a67',pady=30, padx=30)
                account_dashboard.geometry('600x400')

                Label(account_dashboard, text="Account Dashboard", bg='#395a67', fg='#8ea9bc', font=("Baskervill Old Face",12)).grid(row=0,sticky=N,pady=10)
                # Label(account_dashboard, text="Welcome " +name,bg='black',fg='white', font=("Baskervill Old Face",12, 'bold')).grid(row=1,sticky=N,pady=5)
                # Label (account_dashboard, image=login_img, borderwidth=0).grid(row=2,sticky=N,pady=15)

                Button(account_dashboard, text="Personal Details",font=("Baskervill Old Face",12),width=20,command=personal_details).grid(row=3, column=1,sticky=N,padx=2,pady=40)
                Button(account_dashboard, text="Deposit",font=("Baskervill Old Face",12),width=20,command=deposit).grid(row=3, column=2,sticky=N,padx=2,pady=40)
                Button(account_dashboard, text="Withdraw",font=("Baskervill Old Face",12),width=20,command=withdraw).grid(row=3, column=0,sticky=N,padx=2,pady=40)
                # Label(account_dashboard).grid(row=5,sticky=N,pady=10)

                return
            else: 
                login_notif.config(fg="#c3042e", text="Incorrect Password")    
                return
    login_notif.config(fg="#c3042e", text="Account does not exist")

def login():

    global temp_login_name
    global temp_login_password
    global login_notif
    global login_screen
    temp_login_name=StringVar()
    temp_login_password=StringVar()

#for login scree
    login_screen = Toplevel(master)
    login_screen.title('Login')
    login_screen.configure(bg='#395a67',pady=70, padx=30)
    login_screen.geometry('600x400')
    # Label(login_screen, text=" BGD bank ", font=('Broadway', 30,'bold'),bg='white',fg='black').grid(row=0,sticky=N, padx=100)

    Label(login_screen, text="Login",bg='#395a67',fg='#8ea9bc',
          font=('Baskervill Old Face',20, 'bold')).grid(row=1,sticky=N,pady=40,padx=100)

    Label(login_screen, text="Username:",bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face',12)).grid(row=2,sticky=W)
    Entry(login_screen, textvariable=temp_login_name).grid(row=2, column=0, sticky=E)

    Label(login_screen, text="Password:",bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face',12)).grid(row=3,sticky=W)
    Entry(login_screen, textvariable=temp_login_password,show="*").grid(row=3, column=0,sticky=E)

    login_notif=Label(login_screen,bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face',12))
    login_notif.grid(row=4,sticky=N)
    Button(login_screen,text="Login", command=login_session, width=15,font=("Baskervill Old Face", 12)).grid(row=5,sticky=W,padx=100,pady=10)

def deposit(): 
     global amount
     global deposit_notif
     global current_balance_label
     amount= StringVar()
     file=open(login_name, "r")
     file_data = file.read()
     user_details=file_data.split('\n')
     details_balance=user_details[3]

     deposit_screen=Toplevel(master)
     deposit_screen.title('Deposit')
     deposit_screen.configure(bg='#395a67', pady=40,padx=20)
     deposit_screen.geometry('500x400')

     # Label(deposit_screen, image=deposit_img, borderwidth=0,bg='black').grid(row=0,sticky=W)

     Label(deposit_screen, text="Deposit",bg='#395a67', fg='#8ea9bc', font=("Baskervill Old Face", 16, 'bold')).grid(row=0,sticky=N,pady=10)
     Label(deposit_screen,text='Please enter the amount you\n would like to deposit below.',bg='#395a67',fg='#8ea9bc', font=("Baskervill Old Face",12)).grid(row=1,sticky=N,pady=10)
     current_balance_label=Label(deposit_screen, text="Current Balance: R"+details_balance,bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face', 12))
     current_balance_label.grid(row=3,sticky=W)
     Label(deposit_screen,text="Amount: R",bg='#395a67', fg='#8ea9bc', font=('Baskervill Old Face',12)).grid(row=4,sticky=W)
     Entry(deposit_screen,textvariable=amount).grid(row=4,column=0,sticky=E)

     deposit_notif=Label(deposit_screen, font=('Baskervill Old Face',12),bg='white')
     deposit_notif.grid(row=5, sticky=N, pady=5)

     
     Button(deposit_screen,text='Proceed',font=('Baskervill Old Face', 12), command=finish_deposit).grid(row=6,sticky=W,pady=5)

def finish_deposit():
    if amount.get()=="":
        deposit_notif.config(text="Please enter amount", fg="#c3042e")
        return
    if float(amount.get())<=0:
        deposit_notif.config(text='Please enter valid amount', fg="#c3042e")
        return
    
    file=open(login_name, 'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[3]
    updated_balance=current_balance
    updated_balance= float(updated_balance)+float(amount.get())
    file_data=file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()


    current_balance_label.config(text="Current Balance: R"+str(updated_balance),fg="green",bg='white')
    deposit_notif.config(text="Balance Updated",fg='green',bg='white')

def withdraw():
     global withdraw_amount
     global withdraw_notif
     global current_balance_label
     withdraw_amount= StringVar()
     file=open(login_name, "r")
     file_data = file.read()
     user_details=file_data.split('\n')
     details_balance=user_details[3]

     withdraw_screen=Toplevel(master)
     withdraw_screen.title('Withdraw')
     withdraw_screen.geometry('400x400')
     withdraw_screen.configure(bg='#395a67',pady=60, padx=30)

     Label(withdraw_screen, text="Withdraw",bg='#395a67',fg='#8ea9bc',  font=("Baskervill Old Face", 12)).grid(row=0,sticky=N,pady=10)
     current_balance_label=Label(withdraw_screen,bg='#395a67',fg='#8ea9bc', text="Current Balance: R"+details_balance, font=('Baskervill Old Face', 12))
     current_balance_label.grid(row=1,sticky=W)
     Label(withdraw_screen,text="Amount: R",bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face',12)).grid(row=2,sticky=W)
     withdraw_notif=Label(withdraw_screen,bg='#395a67', fg='#8ea9bc',font=('Baskervill Old Face',12))
     withdraw_notif.grid(row=4, sticky=N, pady=5)

     Entry(withdraw_screen,textvariable=withdraw_amount).grid(row=2,column=1)
     
     Button(withdraw_screen,text='Proceed',font=('Baskervill Old Face', 12), command=finish_withdraw).grid(row=3,sticky=W,pady=5)

def finish_withdraw():
    if withdraw_amount.get()=="":
        withdraw_notif.config(text="Enter amount", fg="red",bg='#395a67')
        return
     
    if float(withdraw_amount.get())<=0:
        messagebox.showinfo(title="!!!!", message="Zero (0) and Negative numbers(-1) are not accepted. \nPlease enter a valid amount.")

        withdraw_notif.config(text='Please enter valid amount', fg="red",bg='#395a67')
        return
    
    file=open(login_name, 'r+')
    file_data=file.read()
    details=file_data.split('\n')
    current_balance=details[3]

    if float(withdraw_amount.get())>float(current_balance):

        withdraw_notif.config(text="Insufficient Funds!", fg="#c3042e",bg='#395a67')
        return

    updated_balance=current_balance
    updated_balance= float(updated_balance)-float(withdraw_amount.get())
    file_data=file_data.replace(current_balance, str(updated_balance))
    file.seek(0)
    file.truncate(0)
    file.write(file_data)
    file.close()

    messagebox.showinfo(title="Congratulations!", message=("YOUR TRANSACTION WAS SUCCESSFUL!!! "))

    current_balance_label.config(text="Current Balance: R"+str(updated_balance))
    withdraw_notif.config(text="Balance Updated",fg='green',bg='#395a67')
    



def personal_details():
    file=open(login_name, 'r')
    file_data=file.read()
    user_details=file_data.split('\n')
    details_name=user_details[0]
    details_account_num=user_details[1]
    # details_idNumber=user_details[2]
    details_balance=user_details[3]

    personal_details_screen=Toplevel(master)
    personal_details_screen.title('Personal Details')
    personal_details_screen.configure(bg='#395a67',pady=50, padx=30)
    personal_details_screen.geometry('400x400')

    # Label(personal_details_screen, image=details_img, borderwidth=0).grid(row=0,sticky=W,pady=15)

    Label(personal_details_screen, text="Personal Details", bg='#395a67', fg='#8ea9bc', font=("Baskervill Old Face",16, 'bold')).grid(row=0,sticky=E,pady=10)
    Label(bg='#395a67',fg='#8ea9bc', pady=35, padx=50)
    Label(personal_details_screen, text="Account Holder: "+details_name,bg='#395a67',fg='#8ea9bc', font=("Baskervill Old Face",12)).grid(row=1,sticky=W)
    Label(personal_details_screen, text="Account Number: "+details_account_num, bg='#395a67',fg='#8ea9bc', font=("Baskervill Old Face",12)).grid(row=2,sticky=W)
    # Label(personal_details_screen, text="ID Number: "+details_idNumber,bg='#343c54',fg='white', font=("Baskervill Old Face",12)).grid(row=3,sticky=W)
    Label(personal_details_screen, text="Balance: R"+details_balance,bg='#395a67',fg='#8ea9bc', font=("Baskervill Old Face",12)).grid(row=4,sticky=W)


#image
img= Image.open('Image.jpeg')
img = img.resize((200,150))
img= ImageTk.PhotoImage(img)

#Home window

Label(master, text="UBS Bank", font=('Engravers MT', 30,'bold'),bg='#395a67',fg='#8ea9bc').grid(row=0,sticky=N, padx=100)
Label(master, text="",bg='white').grid(row=1, pady=10)
Label(master, text="Bank Better",bg='#395a67',fg='#8ea9bc', font=('Baskervill Old Face', 15, 'italic')).grid(row=1,sticky=N, padx=100)
Label (master, image=img, borderwidth=0).grid(row=2,sticky=N,pady=15)

Button(master, text="Register", font=('Baskervill Old Face', 12),width=20,command=register).grid(row=4,sticky=W, padx=80)
Button(master, text="Login", font=('Baskervill Old Face', 12),width=20,command=login).grid(row=4,sticky=E, pady=10)

master.mainloop()

