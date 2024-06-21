from tkinter import *
from tkinter import messagebox
import db_contacts
bg='#ff2b00'

win = Tk()
win.geometry('500x300')
win.title('Contacts')
win.config(bg=bg)
win.resizable(0,0)
db1 = db_contacts.Database('mydata.db')
#|||||||||||||||||||||||||||||||||functions||||||||||||||||||||||||||||||||||||
def insert():
    fname = ent_fname.get()
    lname = ent_lname.get()
    city = ent_city.get()
    phone = ent_phone.get()
    if fname =='' or len(lname)==0:
        messagebox.showerror('ERROR','Firstname or Lastname is empty!!!')
        return
    db1.insert(fname, lname, city, phone)
    clear()
    show()
def clear():
    ent_fname.delete(0,END)
    ent_lname.delete(0,END)
    ent_city.delete(0,END)
    ent_phone.delete(0,END)
    ent_fname.focus_set()
def show():
    lst_info.delete(0,END)
    records = db1.select()
    for record in records:
        lst_info.insert(END, f'{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}')
def delete():
    try:
        index = lst_info.curselection()
        data = lst_info.get(index)
        ask = messagebox.askquestion('Delete',f'do you want delete item [{data}]?')
        if ask.lower()=='yes':
            db1.delete(data[0])
        show()
    except Exception:
        messagebox.showwarning('Index Error','Select item in listbox!!!')
def select_item(event):
    global data
    index = lst_info.curselection()
    if index:
        info = lst_info.get(index)
        data = info.split(',')
        ent_fname.delete(0,END)
        ent_lname.delete(0,END)
        ent_city.delete(0,END)
        ent_phone.delete(0,END)
        ent_fname.insert(END, data[1])
        ent_lname.insert(END, data[2])
        ent_city.insert(END, data[3])
        ent_phone.insert(END, data[4])
def update():
    global data
    db1.update(data[0], ent_fname.get(), ent_lname.get(), ent_city.get(), ent_phone.get())
    show()
    clear()
def search(event):
    info = ent_search.get()
    records = db1.search(info)
    if records:
        lst_info.delete(0,END)
        for record in records:
            lst_info.insert(END, f'{record[0]},{record[1]},{record[2]},{record[3]},{record[4]}')
        return
    else:
        messagebox.showerror('ERORR',f'Record {info} not found!!!')
        ent_search.delete(0,END)
        ent_search.focus_set()

#|||||||||||||||||||||||||||||||||widgets||||||||||||||||||||||||||||||||||||||
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>lable<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lbl_fname = Label(win, text='Fname:', font='tahoma 10 bold',fg='white', bg=bg)
lbl_fname.place(x = 0, y=40)
lbl_lname = Label(win, text='Lname:', font='tahoma 10 bold',fg='white', bg=bg)
lbl_lname.place(x = 0, y=60)
lbl_city = Label(win, text='City:', font='tahoma 10 bold',fg='white', bg=bg)
lbl_city.place(x = 0, y=80)
lbl_tel = Label(win, text='Phone:', font='tahoma 10 bold',fg='white', bg=bg)
lbl_tel.place(x = 0, y=100)
lbl_search = Label(win, text='Search :', font='tahoma 7 bold',fg='white', bg=bg)
lbl_search.place(x = 0, y=0)
lbl=Label(text="را بزنیدEnter برای جستجو", font='tahoma 7 bold',fg='black', bg=bg)
lbl.place(x=70,y=20)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>entry<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
ent_fname = Entry(win, font='tahoma 7 bold')
ent_fname.place(x = 60, y=45)
ent_lname = Entry(win, font='tahoma 7 bold')
ent_lname.place(x = 60, y=65)
ent_city = Entry(win, font='tahoma 7 bold')
ent_city.place(x = 60, y=85)
ent_phone = Entry(win, font='tahoma 7 bold')
ent_phone.place(x = 60, y=105)
ent_search = Entry(win, font='tahoma 5 bold',width=50)
ent_search.place(x = 50, y=5)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>listbox<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
lst_info = Listbox(win,width=25, height=11)
lst_info.pack(side=RIGHT,fill=BOTH)
lst_info.bind('<<ListboxSelect>>',select_item)
sb = Scrollbar(win)
sb.pack(side=RIGHT,fill=Y)
sb.config(command=lst_info.yview)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>button<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
btn_insert = Button(win, text='insert', font='tahoma 12 bold', bg='white', width=10, command=insert)
btn_insert.place(x=2, y= 150)
btn_delete = Button(win, text='delete', font='tahoma 12 bold', bg='white', width=15, command=delete)
btn_delete.place(x=120, y= 150)
btn_update = Button(win, text='update', font='tahoma 12 bold', bg='white', width=10, command=update)
btn_update.place(x=2, y= 190)
btn_show = Button(win, text='show', font='tahoma 12 bold', bg='white', width=15, command=show)
btn_show.place(x=120, y= 190)
btn_clear = Button(win, text='clear', font='tahoma 12 bold', bg='white', width=10, command=clear)
btn_clear.place(x=2, y= 230)
btn_exit = Button(win, text='exit', font='tahoma 12 bold', bg='white', width=15, command=win.destroy)
btn_exit.place(x=120, y= 230)

ent_search.bind('<Return>',search)
win.mainloop()