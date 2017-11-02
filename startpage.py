
import tkinter as tk
from PIL import Image, ImageTk
from os import startfile


window = tk.Tk()
w=1000
h=500
ws=window.winfo_screenwidth()
hs=window.winfo_screenheight()
x=ws/2-w/2
y=hs/2-h/2
window.geometry('%dx%d+%d+%d'%(w,h,x,y-20))



def Round1():
    import databaseconnect1
    #execfile('databaseconnect1.py')
    #window.withdraw()
    return
def open():
    window2=tk.Tk()
    window2.geometry('%dx%d+%d+%d'%(w,h,x,y-20))
    bRound1=tk.Button(window2,text="Round 1  MCQ QUESTIONS ",command=Round1).place(x=450,y=200)
    #bRound1.pack()
    bRound2=tk.Button(window2,text="Round 2 AUDIO VIDEO ROUND").place(x=450,y=300)
    window.destroy()






    
photo = ImageTk.PhotoImage(Image.open('image.jpg'))
image1= Image.open('E:\Python\quiz\image.jpg')
photo_image = ImageTk.PhotoImage(image1)
label = tk.Label(window,image=photo_image).place(x=0,y=0,relwidth=1,relheight=1)
buttonStart=tk.Button(window,fg='blue',bg='red',text="Get Started",command=open).place(x=500,y=350,relwidth=0.075,relheight=0.075)

window.mainloop()




    
    
