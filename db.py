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
        error["text"] = "Error: Title already exists"
    else:
        error["text"] = "Added New User"
        cursor.execute("INSERT INTO users(username, password)VALUES(?,?)",(newUsername))
        db.commit()

window = Tk()
window.geometry("650x240")
#
error = Message(text="", width=160)
error.place(x = 30, y = 10)
#
#

label1 = Label(text = "Title:")
label1.place(x = 30, y = 50)
label1.config(bg = 'lightgreen', padx=0)
#
username = Entry(text = "")
username.place(x=150, y=50, width=200, height=25)
#
label2 = Label(text = "Content:")
label2.place(x = 30, y = 100)
label2.config(bg = 'lightgreen', padx=0)
#
password = Entry(text = "")
password.place(x=150, y=100, width=200, height=50)
# 
button = Button(text = "Add", command = add_new_user)
button.place(x=150, y=160, width=75, height=35)


window.mainloop()
