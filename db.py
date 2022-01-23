from tkinter import *
import tkinter as tk
import sqlite3
from os import system, name
from unittest import result


with sqlite3.connect("informational.db") as db:
    cursor=db.cursor()
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS baza_d(id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, content text NOT NULL); """)


root = Tk()
root.geometry("1250x700")
root.title("Pamietnik")
root.tk.call('wm','iconphoto',root._w, tk.PhotoImage(file='ichtis-no-bg.png'))
var = StringVar(root)


def clear():
    # windows
    if name=='nt':
        _=system('cls')

        # linux & mac
    else:
        _=system('clear')
        tekst.delete("1.0",END)


def fetch_data():
    pobierz = db.cursor()
    pobierz.execute("SELECT title,content FROM baza_d ORDER BY id DESC LIMIT 1")
    dane = pobierz.fetchone()
    for dana in dane:
        print(dana,[0])
        tekst.delete("1.0",END)
        tekst.insert(INSERT,dana)


def am():
    pobierz = db.cursor()
    pobierz.execute("SELECT title,content FROM baza_d where id=13")
    dane = pobierz.fetchone()
    for dana in dane:
        print(dana, [0])
        tekst.delete("1.0",END)
        tekst.insert(INSERT,dana)
        

def add_new_content():
    newTitle = title.get()
    newContent = content.get("1.0",END)


    cursor.execute("SELECT COUNT(*) from baza_d WHERE title = '"+ newTitle + "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Title already exists"
    else:
<<<<<<< HEAD
        error["text"] = "Added New Information"
        cursor.execute("INSERT INTO baza_d(title, content)VALUES(?,?)",(newTitle, newContent))
=======
        error["text"] = "Added New User"
        cursor.execute("INSERT INTO users(username, password)VALUES(?,?)",(newUsername))
>>>>>>> 3a016964b98230ecc63fa9dffcdb77850ac28679
        db.commit()
        
        content.delete()
#
def search():
    try:
        conn = sqlite3.connect('informational.db')
        cur=conn.cursor()
        sql="SELECT content FROM baza_d WHERE title='%s"%title.get
        cur.execute(sql)
        result=cur.fetchone()
        content.set(result[0])
        conn.close()
    except:
        print('success')
            

#
error = Message(text="", width=160)
error.place(x = 30, y = 10)
#
#

<<<<<<< HEAD
etykieta1 = Label(text = "Enter Title:")
etykieta1.place(x = 30, y = 60)
etykieta1.config(bg = 'lightgreen', padx=0)
=======
label1 = Label(text = "Title:")
label1.place(x = 30, y = 50)
label1.config(bg = 'lightgreen', padx=0)
>>>>>>> 3a016964b98230ecc63fa9dffcdb77850ac28679
#
title = Entry(text = "")
title.place(x=30, y=85, width=200, height=25)
title.config(bg = 'lightgreen')
#
<<<<<<< HEAD
etykieta2 = Label(text = "Enter Content:")
etykieta2.place(x = 30, y = 120)
etykieta2.config(bg = 'lightgreen', padx=0)
#
content = Text()
content.place(x=30, y=170, width=200, height=275)
content.config(bg = 'orange')
=======
label2 = Label(text = "Content:")
label2.place(x = 30, y = 100)
label2.config(bg = 'lightgreen', padx=0)
#
password = Entry(text = "")
password.place(x=150, y=100, width=200, height=50)
>>>>>>> 3a016964b98230ecc63fa9dffcdb77850ac28679
# 
button = Button(text = "Add", command = add_new_content)
button.place(x=30, y=650, width=75, height=35)
button.config(bg='#a17e41')
#
button1 = Button(text = "Last ID", command = fetch_data)
button1.place(x=110, y=650, width=75, height=35)
button1.config(bg='#a17e41')
#
button2 = Button(text = "+", command = am)
button2.place(x=30, y=600, width=75, height=35)
button2.config(bg='#a17e41')
#
button3 = Button(text = "Clear", command = clear)
button3.place(x=110, y=600, width=75, height=35)
button3.config(bg='#a17e41')
#
tekst = Text()
tekst.place(x=300, y=75, width=850, height=570)
#
search = Entry()
search.place(x=550, y=25, width=200, height=35)
search.config(bg = 'lightgreen')
#
btn4 = Button(text='Search', command=search)
btn4.place(x=190, y=600, width=75, height=35)
btn4.config(bg='#a17e41')
#

###
###
root.mainloop()
