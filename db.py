from tkinter import *
import sqlite3
from tkinter import messagebox


with sqlite3.connect("informational.db") as db:
    cursor=db.cursor()
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS baza_d(id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, content text NOT NULL); """)

root = Tk()
root.geometry("1250x700")
root.title("niezapominajek")

def fetch_data():
    ciagnij = db.cursor()
    ciagnij.execute("SELECT * FROM baza_d")
    dane = ciagnij.fetchall()
    for dana in dane:
        print(dana)
        tekst.insert(INSERT,dana)
        
        


def add_new_content():
    newTitle = title.get()
    newContent = content.get()


    cursor.execute("SELECT COUNT(*) from baza_d WHERE title = '"+ newTitle + "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Title already exists"
    else:
        error["text"] = "Added New User"
        cursor.execute("INSERT INTO baza_d(title, content)VALUES(?,?)",(newTitle, newContent))
        db.commit()
        fetch_data()


#
error = Message(text="", width=160)
error.place(x = 30, y = 10)
#
#

label1 = Label(text = "Enter Title:")
label1.place(x = 30, y = 50)
label1.config(bg = 'lightgreen', padx=0)
#
title = Entry(text = "")
title.place(x=30, y=75, width=200, height=25)
title.config(bg = 'lightgreen')
#
label2 = Label(text = "Enter Content:")
label2.place(x = 30, y = 110)
label2.config(bg = 'lightgreen', padx=0)
#
content = Entry(text = "")
content.place(x=30, y=160, width=200, height=375)
content.config(bg = 'orange')
# 
button = Button(text = "Add", command = add_new_content)
button.place(x=30, y=650, width=75, height=35)
button.config(bg='#a17e41')
#
button1 = Button(text = "Fetch", command = fetch_data)
button1.place(x=110, y=650, width=75, height=35)
button1.config(bg='#a17e41')

tekst = Text()
tekst.place(x=300, y=30, width=850, height=570)


root.mainloop()
