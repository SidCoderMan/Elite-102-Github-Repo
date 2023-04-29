
#connections
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import mysql.connector
id_list = [""]
connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")
leave = "y"
#functions
def create_account_window():
    new_account_window = Tk()

    new_account_window_label = Label(new_account_window,text="Write your ID(only numbers please!)", fg = "blue",  font=("Aerial", 16))
    new_account_window_label.grid(row=0,column=0)
    new_account_window_id_entry = Entry(new_account_window, bg = "blue", fg = "white", font = ("Aerial", 16))
    new_account_window_id_entry.grid(row=0,column=1)
    
    new_account_window_label_2 = Label(new_account_window,text="Write the amount you want to put in your account(only numbers please!)", fg = "blue",  font=("Aerial", 16))
    new_account_window_label_2.grid(row=1,column=0)
    new_account_window_amnt_entry = Entry(new_account_window, bg = "blue", fg = "white", font = ("Aerial", 16))
    new_account_window_amnt_entry.grid(row=1,column=1)

    def run_data():
        connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")
        cursor = connection.cursor()
        id_info = new_account_window_id_entry.get()
        amount = new_account_window_amnt_entry.get()

        addData = (f"INSERT INTO accountinfo (BALANCE, USERNAME) VALUES ({amount}, {id_info})")



        cursor.execute(addData)
        addData = (f"INSERT INTO ids (REGISTEREDIDS) VALUES ({id_info})")



        cursor.execute(addData)
        



        connection.commit()

        cursor.close()

        connection.close()
    new_account_window_button =  Button(new_account_window, text = "Sign up!", fg = "white", bg = "blue", font = ("Aerial", 15), 
    command = run_data)
    new_account_window_button.grid(row = 2, column= 1, columnspan= 2)
    

    new_account_window.mainloop()
def check():
    connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")

    check_window = Tk()
    check_window.title("Amount in your account!")
    cursor = connection.cursor()

    

    testQuery = (f"SELECT SUM(BALANCE) FROM accountinfo WHERE USERNAME = {id};")

    cursor.execute(testQuery)
    

    for item in cursor:
        #fixes item
        item = str(item)
        item = list(item)
        print(item)
        item.remove("(")
        item.remove("D")
        item.remove("e")
        item.remove("c")
        item.remove("i")
        item.remove("m")
        item.remove("a")
        item.remove("l")
        item.remove("(")
        item.remove("'")
        item.remove("'")
        item.remove(")")
        item.remove(",")
        item.remove(")")
        print(item)
        item = "".join(item)
        print(item)
        amount_label = Label(check_window, text = f"You have {item} dollars in your account!", fg = "blue",  font=("Aerial", 30))
        print(item)
        amount_label.pack()
    connection.close()
    check_window.mainloop()
def deposit_database(amount):
    
     
    connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")

    final_amount_window = Tk()
    final_amount_window.title("Total!")
     
      
    cursor = connection.cursor()

    addData = (f"INSERT INTO accountinfo (BALANCE, USERNAME) VALUES ({(amount)},{id})")


        

    cursor.execute(addData)


    testQuery = (f"SELECT SUM(BALANCE) FROM accountinfo WHERE USERNAME = {id};")
    
    cursor.execute(testQuery)

    for item in cursor:
        #fixes item
        item = str(item)
        item = list(item)
        print(item)
        item.remove("(")
        item.remove("D")
        item.remove("e")
        item.remove("c")
        item.remove("i")
        item.remove("m")
        item.remove("a")
        item.remove("l")
        item.remove("(")
        item.remove("'")
        item.remove("'")
        item.remove(")")
        item.remove(",")
        item.remove(")")
        print(item)
        item_true = "".join(item)
    connection.commit()
    cursor.close() 


    cursor = connection.cursor()
    final_amount = item_true
    final_amount_label = Label(final_amount_window, text = f"This is the final amount, {final_amount}", fg = "blue",  font=("Aerial", 16))
    final_amount_label.pack()
    testQuery = (f"UPDATE accountinfo SET BALANCE = {final_amount}")   
    cursor.execute(testQuery)
    cursor.close()
    connection.close()
    final_amount_window.mainloop()
    
    
    
def deposit():
    
    deposit_window = Tk()
    deposit_window.title("Deposit to your account!")
    amount_deposit_label = Label(deposit_window, text = "Amount to deposit", fg = "blue",  font=("Aerial", 16))
    amount_deposit_entry = Entry(deposit_window, bg = "blue", fg = "white", font = ("Aerial", 16))
    amount_deposit_label.grid(row=1,column=0)
    amount_deposit_entry.grid(row=1,column=1)

    def send_amount():
        amount = int(amount_deposit_entry.get())
        deposit_database(amount)
        
        

    amount_deposit_button = Button(deposit_window, text = "Deposit", fg = "white", bg = "blue", font = ("Aerial", 15), 
    command = send_amount)
    amount_deposit_button.grid(row=2,column=1)
    deposit_window.mainloop()



def withdraw_database(amount):
    connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")

    final_amount_window_withdraw = Tk()
    final_amount_window_withdraw.title("Total!")
     
      
    cursor = connection.cursor()

    addData = (f"INSERT INTO accountinfo (BALANCE, USERNAME) VALUES ({-(amount)},{id})")

        

    cursor.execute(addData)


    testQuery = (f"SELECT SUM(BALANCE) FROM accountinfo WHERE USERNAME = {id};")
    
    cursor.execute(testQuery)

    for item in cursor:
        #fixes item
        item = str(item)
        item = list(item)
        print(item)
        item.remove("(")
        item.remove("D")
        item.remove("e")
        item.remove("c")
        item.remove("i")
        item.remove("m")
        item.remove("a")
        item.remove("l")
        item.remove("(")
        item.remove("'")
        item.remove("'")
        item.remove(")")
        item.remove(",")
        item.remove(")")
        print(item)
        item_true = "".join(item)
    connection.commit()
    cursor.close() 
    

    cursor = connection.cursor()
    final_amount = item_true
    final_amount_label = Label(final_amount_window_withdraw, text = f"This is the final amount, {final_amount}", fg = "blue",  font=("Aerial", 16))
    final_amount_label.pack()
    testQuery = (f"UPDATE accountinfo SET BALANCE = {final_amount}")   
    cursor.execute(testQuery)
    cursor.close()
    connection.close()
    final_amount_window_withdraw.mainloop()
  

  
def withdraw():
    withdraw_window = Tk()
    withdraw_window.title("Withdraw from your account!")
    amount_withdraw_label = Label(withdraw_window, text = "Amount to withdraw", fg = "blue",  font=("Aerial", 16))
    amount_withdraw_entry = Entry(withdraw_window, bg = "blue", fg = "white", font = ("Aerial", 16))
    amount_withdraw_label.grid(row=1,column=0)
    amount_withdraw_entry.grid(row=1,column=1)
   

    def send_amount():
        connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")
        amount = int(amount_withdraw_entry.get())
        cursor = connection.cursor()
        testQuery = (f"SELECT SUM(BALANCE) FROM accountinfo WHERE USERNAME = {id};")

        cursor.execute(testQuery)

        for item in cursor:
            #fixes item
            item = str(item)
            item = list(item)
            print(item)
            item.remove("(")
            item.remove("D")
            item.remove("e")
            item.remove("c")
            item.remove("i")
            item.remove("m")
            item.remove("a")
            item.remove("l")
            item.remove("(")
            item.remove("'")
            item.remove("'")
            item.remove(")")
            item.remove(",")
            item.remove(")")
            print(item)
            item = "".join(item)
            item = int(item)
            if item < amount:
                too_much_window = Tk()
                too_much_window_label = Label(too_much_window,  text = "You don't have that much money!", fg = "blue",  font=("Aerial", 30))
                too_much_window_label.pack()
                too_much_window.mainloop()
        connection.commit()
        cursor.close() 
        if item >= amount:
            withdraw_database(amount)
            
        
        
    amount_deposit_button = Button(withdraw_window, text = "Withdraw", fg = "white", bg = "blue", font = ("Aerial", 15), 
    command = send_amount)
    amount_deposit_button.grid(row=2,column=1)
    
        

    withdraw_window.mainloop()
    
        



    

def control_window():
    
    control_window = Tk()
    control_window.title("Manage your account!")
    window.destroy()
    bottom_bar = Label(control_window, text="Sid Banks", bd = 1, relief = SUNKEN, anchor=W, bg = "blue", fg = "white")
    bottom_bar.pack(side=BOTTOM,fill=X)
    account_label = Label(control_window, text = "Welcome to your account!", fg = "blue",  font=("Aerial", 30))
    account_label.pack()
    secondary_account_label = Label(control_window, text = "What do you want to do?", fg = "blue",  font=("Aerial", 15))
    secondary_account_label.pack()
    check_button = Button(control_window, text = "Check Balance", fg = "white", bg = "blue", font = ("Aerial", 30), command=check)
    deposit_button = Button(control_window, text = "Deposit Money", fg = "white", bg = "blue", font = ("Aerial", 30), command=deposit)
    withdraw_button = Button(control_window, text = "Withdraw Money", fg = "white", bg = "blue", font = ("Aerial", 30), command=withdraw)
    check_button.pack(side=BOTTOM,pady = 30)
    deposit_button.pack(side=BOTTOM,pady = 30)
    withdraw_button.pack(side=BOTTOM,pady = 30)
    control_window.mainloop()
#work
window = Tk()

window.title("Log in to Sid Banks!")
window.geometry("340x440")
window.configure(bg = "white")
print("Welcome to Sid Banks!")
#info_screen()
#balance()
def info_screen():
   global id
   connection = mysql.connector.connect(user = "root", database = "bank", password = "Siddy%955")
   cursor = connection.cursor()
   testQuery = ("SELECT REGISTEREDIDS FROM ids")

   cursor.execute(testQuery)
   first_time = 0
   for item in cursor:
        #fixes item
        item = str(item)
        item = item.split()
        print(item)
        first_time + 1
        item = "".join(item)
        print(item)
        #checks if id is a username
        if id_entry.get() in str(item):
            print(id_entry.get())
            print(item)
            messagebox.showinfo(title="", message = "Logging in...")
            id = id_entry.get()
            print(id)
            control_window()
            break
   if id_entry.get() not in str(item):
        messagebox.showinfo(title="", message = "Wrong id!")
        print(id_entry.get())
        print(item)
        answer = messagebox.askquestion("New Account?", "Do you want to create a new account?")
        if answer == "yes":
            create_account_window()
    
   connection.close()

#making frame
frame = Frame(bg = "white")
#making widgets
title_label = Label(frame, text = "Sid Banks", fg = "blue", bg = "white", font=("Aerial", 40, UNDERLINE))
login_label = Label(frame, text = "Login", fg = "blue", bg = "white", font=("Aerial", 16))
id_label = Label(frame, text = "ID",fg = "blue", bg = "white", font = ("Aerial", 16))
id_entry = Entry(frame, bg = "blue", fg = "white", font = ("Aerial", 16))
login_button = Button(frame, text = "login", fg = "white", bg = "blue", font = ("Aerial", 16), command=info_screen)
signup_button = Button(frame, text = "Signup",fg = "white", bg = "blue", font = ("Aerial", 16), command=create_account_window)
# Placing widgets on the screen
title_label.grid(row = 0, column = 0, columnspan = 2, sticky = "news")
login_label.grid(row = 1, column = 0, columnspan = 2, sticky = "news", pady = 10)
id_label.grid(row = 2, column = 0)
id_entry.grid(row = 2, column = 1, pady = 20)
login_button.grid(row = 3, column = 0, columnspan = 2)
signup_button.grid(row = 4, column = 0, columnspan = 2)
frame.pack()


#fancy things in login screen
#bottom bar
bottom_bar = Label(window, text="Sid Banks", bd = 1, relief = SUNKEN, anchor=W, bg = "blue", fg = "white")
bottom_bar.pack(side=BOTTOM,fill=X)


window.mainloop()
#control window

