from tkinter import *
import tkinter as tk
import sqlite3
import tkinter.ttk as ttk
from os import system, name


with sqlite3.connect("informational.db") as db:
    cursor=db.cursor()
    
cursor.execute(""" CREATE TABLE IF NOT EXISTS baza_d(id integer PRIMARY KEY AUTOINCREMENT, title text NOT NULL, content text NOT NULL); """)



root = Tk()
root.geometry("1250x700")
root.title("Pamiętnik")
root.tk.call('wm','iconphoto',root._w, tk.PhotoImage(file='ichtis-no-bg.png'))
var = StringVar(root)
error = Message(text="", width=160)
error.place(x = 30, y = 10)
#
#


def clear():
    # windows
    if name=='nt':
        _=system('cls')

        # linux & mac
    else:
        _=system('clear')
        tekst.delete("1.0",END)
        title.delete(0,END)
        content.delete(1.0,END)
        searchbar.delete(0,END)


def fetch_data():
    pobierz = db.cursor()
    pobierz.execute("SELECT content FROM baza_d ORDER BY id DESC LIMIT 1")
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
        

def pn():
    pobierz = db.cursor()
    pobierz.execute("SELECT title,content FROM baza_d WHERE id=17")
    dane = pobierz.fetchone()
    for dana in dane:
        print(dana, [0])
        tekst.delete("1.0", END)
        tekst.insert(INSERT,dana)
        

def add_new_content():
    newTitle = title.get()
    newContent = content.get("1.0",END)


    cursor.execute("SELECT COUNT(*) from baza_d WHERE title = '"+ newTitle + "' ")
    result = cursor.fetchone()

    if int(result[0]) > 0:
        error["text"] = "Error: Title already exists"
    else:
        error["text"] = "Added New Information"
        cursor.execute("INSERT INTO baza_d(title, content)VALUES(?,?)",(newTitle, newContent))
        db.commit()
        title.delete(0,END)
        content.delete(1.0,END)
#
# def seearch():
#     with sqlite3.connect("informational.db") as db:
#         cursor=db.cursor()
#         wyciag = content
#         cursor.execute("SELECT content FROM baza_d WHERE title='%s'" ('%'+wyciag+'%',))
#         dataFound = cursor.fetchone()
#         # searchbar.delete(0,END)
#         return dataFound()
# def search():
#     if SEARCH.get() != "":
#         tree.delete(*tree.get_children())
#         conn = sqlite3.connect("informational.db")
#         cursor = conn.cursor()
#         cursor.execute("SELECT * FROM `member` WHERE `firstname` LIKE ? OR `lastname` LIKE ?", ('%'+str(SEARCH.get())+'%', '%'+str(SEARCH.get())+'%'))
#         fetch = cursor.fetchall()
#         for data in fetch:
#             tree.insert('', 'end', values=(data))
#         cursor.close()
#         conn.close()


SEARCH = StringVar()

#

etykieta1 = Label(text = "Enter Title:")
etykieta1.place(x = 30, y = 60)
etykieta1.config(bg = 'lightgreen', padx=0)
        #
title = Entry(text = "")
title.place(x=30, y=85, width=235, height=25)
title.config(bg = 'cyan')
        #
etykieta2 = Label(text = "Enter Content:")
etykieta2.place(x = 30, y = 120)
etykieta2.config(bg = 'lightgreen', padx=0)
#
content = Text(root)
content.place(x=30, y=170, width=235, height=275)
content.config(bg = 'cyan')
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
searchbar = Entry()
searchbar.place(x=550, y=25, width=200, height=35)
searchbar.config(bg = 'orange')
#
# 
#
btn5 = Button(text='+', command=pn)
btn5.place(x=190, y=650, width=75, height=35)
btn5.config(bg='#a17e41')
###error = Message(text="", width=160)



            

#
#
###
root.mainloop()

