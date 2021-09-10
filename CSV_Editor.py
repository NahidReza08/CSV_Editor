import pandas as pd
import numpy as np
import csv
from tkinter import *
from tkinter import messagebox
import math

datafile = 'CSV_Files/fake_news.csv'
data = pd.read_csv(datafile)
csvfile = csv.reader(open(datafile))
data.head()


def load(n):
    title_text.delete("1.0", "end")
    title_text.insert(INSERT, data["title"][n])

    content_text.delete("1.0", "end")
    content_text.insert(INSERT, data["content"][n])

    date_text.delete("1.0", "end")
    date_text.insert(INSERT, data["date"][n])

    domain_text.delete("1.0", "end")
    domain_text.insert(INSERT, data["domain"][n])

    url_text.delete("1.0", "end")
    url_text.insert(INSERT, data["url"][n])

    if data["init_cat"][n] == "None":
        category.set('Select Initial News Type')
    else:
        category.set(data["init_cat"][n])

    page.delete("1.0", "end")
    page.insert(INSERT, str(n))


def previous():
    current = int(page.get("1.0", "end-1c"))
    if current == 0:
        load(len(data) - 1)
    else:
        load(current - 1)


def _next():
    current = int(page.get("1.0", "end-1c"))
    if current == len(data) - 1:
        load(0)
    else:
        load(current + 1)


def go():
    visit = int(page.get("1.0", "end-1c"))
    if visit >= len(data):
        load(len(data) - 1)
    elif visit < 0:
        load(0)
    else:
        load(visit)


def save():
    i = int(page.get("1.0", "end-1c"))
    # print("Row "+str(i)+" trying to update")
    if i >= 0 and i < len(data):
        data['title'][i] = title_text.get("1.0", "end-1c")
        data['content'][i] = content_text.get("1.0", "end-1c")
        data['date'][i] = date_text.get("1.0", "end-1c")
        data['domain'][i] = domain_text.get("1.0", "end-1c")
        data['url'][i] = url_text.get("1.0", "end-1c")
        data['init_cat'][i] = category.get()
        data.to_csv("CSV_Files/fake_news.csv", index=False)
        messagebox.showinfo("Info:", "Row " + str(i) + " has been updated!!!")

root = Tk()
root.geometry("1200x900")
#root.configure(bg='blue')
root.title('CSV Editor')
var = "Content 2"

label_0 = Label(root,text="CSV Editor", width=20, font=("bold",20), fg="green")
label_0.place(x=410,y=20)

title = Label(root,text="Title", width=20,font=("bold",10), fg="blue")
title.place(x=0,y=100)
title_text=Text(root, height = 2, width = 100, wrap="word")
title_text.place(x=130,y=100)

content = Label(root,text="Content", width=20,font=("bold",10), fg="blue")
content.place(x=0,y=150)
scrollbar = Scrollbar(root)
content_text=Text(root, height = 20, width = 100, wrap="word",yscrollcommand=scrollbar.set)
content_text.place(x=130,y=150)
scrollbar.config(command=content_text.yview)
scrollbar.pack(side=RIGHT, fill=Y)


date = Label(root,text="Date", width=20,font=("bold",10), fg="blue")
date.place(x=0,y=560)
date_text=Text(root, height = 2, width = 100)
date_text.place(x=130,y=560)
#date_text.configure(state='disabled')

domain = Label(root,text="Domain", width=20,font=("bold",10),fg="blue")
domain.place(x=0,y=610)
domain_text=Text(root, height = 2, width = 100)
domain_text.place(x=130,y=610)
#domain_text.configure(state='disabled')

url = Label(root,text="URL", width=20,font=("bold",10),fg="blue")
url.place(x=0,y=660)
url_text=Text(root, height = 2, width = 100)
url_text.place(x=130,y=660)
#url_text.configure(state='disabled')


initial_type=Label(root,text="Initial Category",width=20,font=("bold",10),fg="blue")
initial_type.place(x=0,y=710)
list_of_value=['Real','Fake']
category=StringVar()
droplist=OptionMenu(root, category, *list_of_value)
droplist.config(width=100)
category.set('Select Initial News Type')
droplist.place(x=200,y=710)

save = Button(root, text='Save' , width=20,bg="black", fg='white', command=save)
save.place(x=530,y=760)

previous = Button(root, text='<<', width=10, bg="black", fg='white', command=previous)
previous.place(x=250,y=810)

page=Text(root, height = 1, width = 5)
page.place(x=550,y=815)

go = Button(root, text='Jump', width=5, bg="black", fg='white', command=go)
go.place(x=610,y=810)

_next = Button(root, text='>>' , width=10,bg="black",fg='white', command=_next)
_next.place(x=850,y=810)


load(0)

root.mainloop()