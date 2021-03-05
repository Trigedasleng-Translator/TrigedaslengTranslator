from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('500x400')
root.iconbitmap('slak.ico')
root.title('Trigedasleng Translator')
root.resizable(False,False)
root.configure(bg='gray')
def tt():
    pass
def main_exit():
    rr = messagebox.askyesnocancel('Confirm Exit','Are you sure you want to exit?',parent=root)
    if(rr==True):
        root.destroy()
######################################################################### Binding Functions
def on_enterentry1(e):
    entry1['bg'] = 'silver'
def on_leaveentry1(e):
    entry1['bg'] = 'white'

def on_enterentry2(e):
    entry2['bg'] = 'silver'
def on_leaveentry2(e):
    entry2['bg'] = 'white'

def on_enterbtn1(e):
    btn1['bg'] = 'limegreen'
def on_leavebtn1(e):
    btn1['bg'] = 'springgreen'

def on_enterbtn2(e):
    btn2['bg'] = 'firebrick'
def on_leavebtn2(e):
    btn2['bg'] = 'red'

#########################################################################  Entry Box
varname1 = StringVar()
entry1 = Entry(root,width=30,textvariable=varname1,font=('times',15,''))
entry1.place(x=150,y=40)

varname2 = StringVar()
entry2 = Entry(root,width=30,textvariable=varname2,font=('times',15,'italic'))
entry2.place(x=150,y=100)
#########################################################################  Labels
label1 = Label(root,text='English: ',font=('times',15,'bold'),bg='gray')
label1.place(x=20,y=40)

label2 = Label(root,text='Trigedasleng: ',font=('times',15,'bold'),bg='gray')
label2.place(x=20,y=100)

#########################################################################  Buttons
btn1 = Button(root,text='Translate!',bd=10,bg='springgreen',activebackground='limegreen',width=10,font=('times',15,''),
              command=tt)
btn1.place(x=70,y=170)

btn2 = Button(root,text='Exit',bd=10,bg='red',activebackground='firebrick',width=10,font=('times',15,''),
              command=main_exit)
btn2.place(x=280,y=170)
######################################################################### Binding
entry1.bind('<Enter>',on_enterentry1)
entry1.bind('<Leave>',on_leaveentry1)

entry2.bind('<Enter>',on_enterentry2)
entry2.bind('<Leave>',on_leaveentry2)

btn1.bind('<Enter>',on_enterbtn1)
btn1.bind('<Leave>',on_leavebtn1)

btn2.bind('<Enter>',on_enterbtn2)
btn2.bind('<Leave>',on_leavebtn2)


root.mainloop()