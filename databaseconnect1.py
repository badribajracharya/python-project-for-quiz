from tkinter import *
import sqlite3
from random import randint
from functools import partial
import os
import sys

conn=sqlite3.connect("quiz.db")

window = Tk()
frame = Frame(window)
frame.pack()
window.title('QUIZ')


w=1000
h=500
ws=window.winfo_screenwidth()
hs=window.winfo_screenheight()
x=ws/2-w/2
y=hs/2-h/2
window.geometry('%dx%d+%d+%d'%(w,h,x,y-20))
askedquestion=list()


def nextround():
    window.destroy()
    #os.system(sys.executable+'python databaseconnect1videoround.py')
    import databaseconnect1videoround

def question(x):
    
    global count
    count=count+1
    #global countquestion
    #countquestion+=1
    bwindow1=Frame(window)
    bwindow1.place_forget()
    bwindow1.place(x=50,y=50,relwidth=1,relheight=1)
    qno=randint(1,10)
    while (qno in askedquestion):
        qno=randint(1,10)
    else:
        askedquestion.append(qno)
        
    cmd="select * from questions where qno=%d"%qno
    cursor=conn.execute(cmd)
    row=cursor.fetchone()
    global Group1,Group2
    if count%2==1:
        Group2.pack_forget()
        Group1.config(text='    TEAM A       Score:%d'%scoreteamA)
        Group1.pack()
        
    else:
        Group1.pack_forget()
        Group2.config(text='    TEAM B       Score:%d'%scoreteamB)
        Group2.pack()
       
    label=Label(bwindow1, text=row[1]).place(x=230, y=0, relwidth=0.5, relheight=0.5)
    global a1,a2,a3,a4
    a1=Button(bwindow1,text=row[2])
    a1text=a1.cget('text')[0]
    a1.config(command=lambda i=1,c_answer=row[6],ans=a1text : check(c_answer,ans,i))
    
    a2=Button(bwindow1, text=row[3])
    a2text=a2.cget('text')[0]
    a2.config(command=lambda i=2,c_answer=row[6],ans=a2text: check(c_answer,ans,i))

    a3=Button(bwindow1, text=row[4])
    a3text=a3.cget('text')[0]
    a3.config(command=lambda i=3,c_answer=row[6],ans=a3text: check(c_answer,ans,i))

    a4=Button(bwindow1, text=row[5])
    a4text=a4.cget('text')[0]
    a4.config(command=lambda i=4,c_answer=row[6],ans=a4text: check(c_answer,ans,i))

    a1.place(x=400,y=250)
    a2.place(x=500,y=250)
    a3.place(x=400,y=300)
    a4.place(x=500,y=300)

    if x==1:
        b1.config(state=DISABLED)
    elif x==2:
        b2.config(state=DISABLED)
    elif x==3:
        b3.config(state=DISABLED)
    elif x==4:
        b4.config(state=DISABLED)
    elif x==5:
        b5.config(state=DISABLED)
    elif x==6:
        b6.config(state=DISABLED)
    return


def check(c_answer,ans,x):
    global scoreteamA,scoreteamB
    if x==1:
        if c_answer==ans:
            a1.config(bg='green')
            if count%2==1:
                scoreteamA+=10
            else:
                scoreteamB+=10
        else:
            a1.config(bg='red')

    if x==2:
        if c_answer==ans:
            a2.config(bg='green')
            if count%2==1:
                scoreteamA+=10
            else:
                scoreteamB+=10
        else:
            a2.config(bg='red')
    if x==3:
        if c_answer==ans:
            a3.config(bg='green')
            if count%2==1:
                scoreteamA+=10
            else:
                scoreteamB+=10
        else:
            a3.config(bg='red')
    if x==4:
        if c_answer==ans:
            a4.config(bg='green')
            if count%2==1:
                scoreteamA+=10
            else:
                scoreteamB+=10
        else:
            a4.config(bg='red')

    if count%2==1:
        Group2.pack_forget()
        Group1.config(text='    TEAM A       Score:%d'%scoreteamA)
        Group1.pack()
        
    else:
        Group1.pack_forget()
        Group2.config(text='    TEAM B       Score:%d'%scoreteamB)
        Group2.pack()

    a1.config(state = DISABLED)
    a2.config(state = DISABLED)
    a3.config(state = DISABLED)
    a4.config(state = DISABLED)




Group1=Label(frame)
Group2=Label(frame)
count = 0
scoreteamA=0
scoreteamB=0
countquestion=0

b1=Button(frame, text= '1', command=lambda  i=1 : question(i))
b1.pack( side = LEFT)

b2=Button(frame, text= '2', command=lambda i=2 : question(i))
b2.pack( side = LEFT)

b3=Button(frame, text= '3', command=lambda i=3 : question(i))
b3.pack( side = LEFT)

b4=Button(frame, text= '4', command=lambda i=4 : question(i))
b4.pack( side = LEFT)

b5=Button(frame, text= '5', command=lambda i=5 : question(i))
b5.pack( side = LEFT)

b6=Button(frame, text='6', command=lambda i=6 : question(i))
b6.pack(side = LEFT)

b7=Button(frame,text='Next Round',command=nextround)
b7.pack(side = LEFT)

window.mainloop()


