from tkinter import * 
import time
#========Variables======
#                      #
#                      #
#                      #
#=======================
global active
active="X"
d="    "
def get(object):
    return object.cget("text")
def winx():
    root.title('X Wins')
def wino():
    root.title('O Wins')
def chck():
    #For X
    if(get(lbl1)==get(lbl5)==get(lbl9)=="X"):
        winx()
    if(get(lbl1)==get(lbl4)==get(lbl7)=="X"):
        winx()
    if(get(lbl3)==get(lbl6)==get(lbl9)=="X"):
        winx()
    if(get(lbl3)==get(lbl5)==get(lbl7)=="X"):
        winx()
    #
    if(get(lbl1)==get(lbl2)==get(lbl3)=="X"):
        winx()
    if(get(lbl4)==get(lbl5)==get(lbl6)=="X"):
        winx()
    if(get(lbl7)==get(lbl8)==get(lbl9)=="X"):
        winx()
    #For O 
    if(get(lbl1)==get(lbl5)==get(lbl9)=="O"):
        wino()
    if(get(lbl1)==get(lbl4)==get(lbl7)=="O"):
        wino()
    if(get(lbl3)==get(lbl6)==get(lbl9)=="O"):
        wino()
    if(get(lbl3)==get(lbl5)==get(lbl7)=="O"):
        wino()
    if(get(lbl1)==get(lbl2)==get(lbl3)=="O"):
        wino()
    if(get(lbl4)==get(lbl5)==get(lbl6)=="O"):
        wino()
    if(get(lbl7)==get(lbl8)==get(lbl9)=="O"):
        wino()
def f1(event):
    global active
    if(active =="X" and get(lbl1)==d):
        lbl1.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl1)==d):
        lbl1.configure(text='O')
        active="X"

def f2(event):
    global active
    print(active)
    if(active =="X" and get(lbl2)==d):
        lbl2.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl2)==d):
        lbl2.configure(text='O')
        active="X"
def f3(event):
    global active
    print(active)
    if(active =="X" and get(lbl3)==d):
        lbl3.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl3)==d):
        lbl3.configure(text='O')
        active="X"
def f4(event):
    global active
    print(active)
    if(active =="X" and get(lbl4)==d):
        lbl4.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl4)==d):
        lbl4.configure(text='O')
        active="X"
def f5(event):
    global active
    print(active)
    if(active =="X" and get(lbl5)==d):
        lbl5.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl5)==d):
        lbl5.configure(text='O')
        active="X"
def f6(event):
    global active
    print(active)
    if(active =="X" and get(lbl6)==d):
        lbl6.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl6)==d):
        lbl6.configure(text='O')
        active="X"
def f7(event):
    global active
    print(active)
    if(active =="X" and get(lbl7)==d):
        lbl7.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl7)==d):
        lbl7.configure(text='O')
        active="X"
def f8(event):
    global active
    print(active)
    if(active =="X" and get(lbl8)==d):
        lbl8.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl8)==d):
        lbl8.configure(text='O')
        active="X"
def f9(event):
    global active
    if(active =="X" and get(lbl9)==d):
        lbl9.configure(text='X')
        active ="O"
        return None
    elif(active =="O" and get(lbl9)==d):
        lbl9.configure(text='O')
        active="X"
root=Tk()
root.title('TicTacToe')
root.geometry('300x300')
pos=[[20,4],[130,4],[210,4],[20,73],[130,73],[210,73],[20,145],[130,145],[210,145]]
#drawing the grid
canvas = Canvas(root)
canvas.create_line(100, 20, 100, 200)
canvas.create_line(200, 20, 200, 200)
canvas.create_line(100, 35, 100, 200)
canvas.create_line(10, 70, 260, 70)
canvas.create_line(10, 140, 260, 140)
canvas.grid(column=2,row=3)
#end of drawing grid
lbl1=Label(root,text=d,font=('font',40))
lbl1.place(x=pos[0][0],y=pos[0][1])
lbl1.bind('<Button-1>',f1)

lbl2=Label(root,text=d,font=('font',40))
lbl2.place(x=pos[1][0],y=pos[1][1])
lbl2.bind('<Button-1>',f2)

lbl3=Label(root,text=d,font=('font',40))
lbl3.place(x=pos[2][0],y=pos[2][1])
lbl3.bind('<Button-1>',f3)

lbl4=Label(root,text=d,font=('font',40))
lbl4.place(x=pos[3][0],y=pos[3][1])
lbl4.bind('<Button-1>',f4)

lbl5=Label(root,text=d,font=('font',40))
lbl5.place(x=pos[4][0],y=pos[4][1])
lbl5.bind('<Button-1>',f5)

lbl6=Label(root,text=d,font=('font',40))
lbl6.place(x=pos[5][0],y=pos[5][1])
lbl6.bind('<Button-1>',f6)

lbl7=Label(root,text=d,font=('font',40))
lbl7.place(x=pos[6][0],y=pos[6][1])
lbl7.bind('<Button-1>',f7)

lbl8=Label(root,text=d,font=('font',40))
lbl8.place(x=pos[7][0],y=pos[7][1])
lbl8.bind('<Button-1>',f8)

lbl9=Label(root,text=d,font=('font',40))
lbl9.place(x=pos[8][0],y=pos[8][1])
lbl9.bind('<Button-1>',f9)
while True:
    chck()
    root.update()
root.mainloop()
