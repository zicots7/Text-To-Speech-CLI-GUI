from tkinter import *
from ttosmale import *
from ttosfemale import*


#Root Declaration
root = Tk()
takeName=StringVar()
root.geometry("800x500")
root.minsize(800,300)
root.maxsize(800,500)
root.title("Test to Speech")
root.configure(bg="#fac612")
frame=Frame(root,bg="#cefe69").place(y=0,x=0,width=800,height=500)
entry=Entry(frame,bg="#808080",textvariable=takeName,borderwidth=4,fg="black",
              font=("Arial ",20 ,"italic bold")).place(x=24,y=10,width=750,height=60)
#Checkbox male and female
checkmale=Checkbutton(frame,text="Male Voice",bg="#cefe69",font=('Arial Narrow',12,'italic bold'),foreground='#7e04ce',command=ml_).place(x=100,y=100,height=50,width=150)
checkfemale=Checkbutton(frame,text="Female Voice",bg="#cefe69",font=('Arial Narrow',12,'italic bold'),foreground='#7e04ce',command=f_m_).place(x=108,y=150,height=50,width=150)

#Buttons
start=Button(frame,text="Start ",bg="#7c0dc1",font=('Arial Narrow',30,'italic bold'),
              foreground='#e6fffe').place(x=500,y=120,height=50,width=200)
enter=Button(frame,text="Enter",bg="#7c0dc1",font=('Arial Narrow',30,'italic bold'),
              foreground='#e6fffe').place(x=500,y=180,height=50,width=200)
exit=Button(frame,text="Stop",bg="#7c0dc1",font=('Arial Narrow', 30,'italic bold'),foreground='#e6fffe',
              command=root.quit).place(x=500,y=240,height=50,width=200)

root.mainloop()
