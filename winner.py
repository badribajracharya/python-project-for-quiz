import tkinter as tk

window = tk.Tk()
w=1000
h=500
ws=window.winfo_screenwidth()
hs=window.winfo_screenheight()
x1=ws/2-w/2
y1=hs/2-h/2
window.geometry('%dx%d+%d+%d'%(w,h,x1,y1-20))

from databaseconnect1videoround import scoreteamA,scoreteamB

if scoreteamA>scoreteamB:
    win='TEAM A'

else:
    win='TEAM B'

label=tk.Label(window,text="Winner is "+win)
label.place(x=x1,y=y1)


