from tkinter import *

import sqlite3
from unittest import result

with sqlite3.connect("details.db") as db:
    cursor=db.cursor()
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS users(id integer PRIMARY KEY AUTOINCREMENT, username text NOT NULL, password text NOT NULL); """)


def add_new_user():
    newUsername = username.get()
    newPassword = password.get()


    cursor.execute("SELECT COUNT(*) from users WHERE username = '"+ newUsername + "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Username already exists"
    else:
        error["text"] = "Added New User"
        cursor.execute("INSERT INTO users(username, password)VALUES(?,?)",(newUsername, newPassword))
        db.commit()

window = Tk()
window.geometry("1250x700")
#
error = Message(text="", width=160)
error.place(x = 30, y = 10)
#
#

label1 = Label(text = "Enter Username:")
label1.place(x = 30, y = 50)
label1.config(bg = 'lightgreen', padx=0)
#
username = Entry(text = "")
username.place(x=30, y=75, width=200, height=25)
username.config(bg = 'lightgreen')
#
label2 = Label(text = "Enter Password:")
label2.place(x = 30, y = 110)
label2.config(bg = 'lightgreen', padx=0)
#
password = Entry(text = "")
password.place(x=30, y=160, width=200, height=75)
password.config(bg = 'orange')
# 
button = Button(text = "Add", command = add_new_user)
button.place(x=30, y=250, width=75, height=35)


window.mainloop()
