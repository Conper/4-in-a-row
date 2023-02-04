import tkinter as tk

root = tk.Tk()
root.geometry("950x640")
root.configure(background="#b8d0eb")
root.resizable(False, False)
tk.Wm.wm_title(root, "4 in a row")
l1,l2,l3,l4,l5,l6,l7,turns,piece = [0]*9


#------ The game board ------#
tk.Label(
    root,
    bg="#004e98",
    width=80,
    height=32,
    bd=5,
    relief="solid"
).place(x=60,y=30)

#------ TURN Label ------#
tk.Label(
    root,
    text="TURN: ",
    font=("Courier", 40, "bold"),
    bg="#b8d0eb",
).place(x=660,y=250)

#------ Square that changes color depending on whose turn it is ------#
class turn():
    def __init__(self, root):
        self._turn = tk.Label(
            root,
            bg="#e74545",
            width=6,
            height=3,
            bd=2,
            relief="solid"
        )
turn_color = turn(root)
turn_color._turn.place(x=850,y=257)


#----------------------------------------------------------#
#------ Function to reset game ------#
def reset_c():
    global l1,l2,l3,l4,l5,l6,l7
    l1,l2,l3,l4,l5,l6,l7 = [0]*7
    r = a1,a2,a3,a4,a5,a6,a7,b1,b2,b3,b4,b5,b6,b7,c1,c2,c3,c4,c5,c6,c7,d1,d2,d3,d4,d5,d6,d7,e1,e2,e3,e4,e5,e6,e7,f1,f2,f3,f4,f5,f6,f7
    for i in r:
        i.a.configure(bg="#004e98")

#------ RESET BUTTON ------#
tk.Button(
    root,
    text="RESET",
    font=("Courier", 30, "bold"),
    bg="#e74545",
    bd=4,
    relief="solid",
    command=reset_c
).place(x=725,y=480)
#----------------------------------------------------------#

#----- Function to change squares colors (red or yellow) -----#
def colors():
    global turns
    if turns % 2 == 0:
        turn_color._turn.configure(bg="#faf968")
        return "#e74545"
    else: 
        turn_color._turn.configure(bg="#e74545")
        return "#faf968"

#------ Function that takes the position of the button that you have pressed ------#
def pos(value):
    global l1,l2,l3,l4,l5,l6,l7,turns
    if value == 1:
        if l1 == 0:
            f1.a.config(bg=colors())
            l1 += 1
            turns += 1
        elif l1 == 1:
            e1.a.config(bg=colors())
            l1 += 1
            turns += 1
        elif l1 == 2:
            d1.a.config(bg=colors())
            l1 += 1
            turns += 1
        elif l1 == 3:
            c1.a.config(bg=colors())
            l1 += 1
            turns += 1
        elif l1 == 4:
            b1.a.config(bg=colors())
            l1 += 1
            turns += 1
        elif l1 == 5:
            a1.a.config(bg=colors())
            l1 += 1
            turns += 1


    if value == 2:
        if l2 == 0:
            f2.a.config(bg=colors())
            l2 += 1
            turns += 1
        elif l2 == 1:
            e2.a.config(bg=colors())
            l2 += 1
            turns += 1
        elif l2 == 2:
            d2.a.config(bg=colors())
            l2 += 1
            turns += 1
        elif l2 == 3:
            c2.a.config(bg=colors())
            l2 += 1
            turns += 1
        elif l2 == 4:
            b2.a.config(bg=colors())
            l2 += 1
            turns += 1
        elif l2 == 5:
            a2.a.config(bg=colors())
            l2 += 1
            turns += 1

    if value == 3:
        if l3 == 0:
            f3.a.config(bg=colors())
            l3 += 1
            turns += 1
        elif l3 == 1:
            e3.a.config(bg=colors())
            l3 += 1
            turns += 1
        elif l3 == 2:
            d3.a.config(bg=colors())
            l3 += 1
            turns += 1
        elif l3 == 3:
            c3.a.config(bg=colors())
            l3 += 1
            turns += 1
        elif l3 == 4:
            b3.a.config(bg=colors())
            l3 += 1
            turns += 1
        elif l3 == 5:
            a3.a.config(bg=colors())
            l3 += 1
            turns += 1

    if value == 4:
        if l4 == 0:
            f4.a.config(bg=colors())
            l4 += 1
            turns += 1
        elif l4 == 1:
            e4.a.config(bg=colors())
            l4 += 1
            turns += 1
        elif l4 == 2:
            d4.a.config(bg=colors())
            l4 += 1
            turns += 1
        elif l4 == 3:
            c4.a.config(bg=colors())
            l4 += 1
            turns += 1
        elif l4 == 4:
            b4.a.config(bg=colors())
            l4 += 1
            turns += 1
        elif l4 == 5:
            a4.a.config(bg=colors())
            l4 += 1
            turns += 1

    if value == 5:
        if l5 == 0:
            f5.a.config(bg=colors())
            l5 += 1
            turns += 1
        elif l5 == 1:
            e5.a.config(bg=colors())
            l5 += 1
            turns += 1
        elif l5 == 2:
            d5.a.config(bg=colors())
            l5 += 1
            turns += 1
        elif l5 == 3:
            c5.a.config(bg=colors())
            l5 += 1
            turns += 1
        elif l5 == 4:
            b5.a.config(bg=colors())
            l5 += 1
            turns += 1
        elif l5 == 5:
            a5.a.config(bg=colors())
            l5 += 1
            turns += 1

    if value == 6:
        if l6 == 0:
            f6.a.config(bg=colors())
            l6 += 1
            turns += 1
        elif l6 == 1:
            e6.a.config(bg=colors())
            l6 += 1
            turns += 1
        elif l6 == 2:
            d6.a.config(bg=colors())
            l6 += 1
            turns += 1
        elif l6 == 3:
            c6.a.config(bg=colors())
            l6 += 1
            turns += 1
        elif l6 == 4:
            b6.a.config(bg=colors())
            l6 += 1
            turns += 1
        elif l6 == 5:
            a6.a.config(bg=colors())
            l6 += 1
            turns += 1


    if value == 7:
        if l7 == 0:
            f7.a.config(bg=colors())
            l7 += 1
            turns += 1
        elif l7 == 1:
            e7.a.config(bg=colors())
            l7 += 1
            turns += 1
        elif l7 == 2:
            d7.a.config(bg=colors())
            l7 += 1
            turns += 1
        elif l7 == 3:
            c7.a.config(bg=colors())
            l7 += 1
            turns += 1
        elif l7 == 4:
            b7.a.config(bg=colors())
            l7 += 1
            turns += 1
        elif l7 == 5:
            a7.a.config(bg=colors())
            l7 += 1
            turns += 1

class box():
    def __init__(self, root):
        self.a = tk.Label(
            root,
            bg="#004e98",
            width=8,
            height=4,
            bd=2,
            relief="solid"
    )


class boton():
    def __init__(self,root,value):
        self.butt = tk.Button(
            root,
            bg="#26cca3",
            width=7,
            height=3,
            bd="3",
            relief="solid",
            command=lambda: pos(value)
        )

a1 = box(root)
a1.a.place(x=75,y=45)

a2 = box(root)
a2.a.place(x=155,y=45)

a3 = box(root)
a3.a.place(x=235,y=45)

a4 = box(root)
a4.a.place(x=315,y=45)

a5 = box(root)
a5.a.place(x=395,y=45)

a6 = box(root)
a6.a.place(x=475,y=45)

a7 = box(root)
a7.a.place(x=555,y=45)
#------------------------------------------------
b1 = box(root)
b1.a.place(x=75,y=125)

b2 = box(root)
b2.a.place(x=155,y=125)

b3 = box(root)
b3.a.place(x=235,y=125)

b4 = box(root)
b4.a.place(x=315,y=125)

b5 = box(root)
b5.a.place(x=395,y=125)

b6 = box(root)
b6.a.place(x=475,y=125)

b7 = box(root)
b7.a.place(x=555,y=125)
#---------------------------------------------------
c1 = box(root)
c1.a.place(x=75,y=205)

c2 = box(root)
c2.a.place(x=155,y=205)

c3 = box(root)
c3.a.place(x=235,y=205)

c4 = box(root)
c4.a.place(x=315,y=205)

c5 = box(root)
c5.a.place(x=395,y=205)

c6 = box(root)
c6.a.place(x=475,y=205)

c7 = box(root)
c7.a.place(x=555,y=205)
#--------------------------------------------------
d1 = box(root)
d1.a.place(x=75,y=285)

d2 = box(root)
d2.a.place(x=155,y=285)

d3 = box(root)
d3.a.place(x=235,y=285)

d4 = box(root)
d4.a.place(x=315,y=285)

d5 = box(root)
d5.a.place(x=395,y=285)

d6 = box(root)
d6.a.place(x=475,y=285)

d7 = box(root)
d7.a.place(x=555,y=285)
#--------------------------------------------------
e1 = box(root)
e1.a.place(x=75,y=365)

e2 = box(root)
e2.a.place(x=155,y=365)

e3 = box(root)
e3.a.place(x=235,y=365)

e4 = box(root)
e4.a.place(x=315,y=365)

e5 = box(root)
e5.a.place(x=395,y=365)

e6 = box(root)
e6.a.place(x=475,y=365)

e7 = box(root)
e7.a.place(x=555,y=365)
#--------------------------------------------------
f1 = box(root)
f1.a.place(x=75,y=445)

f2 = box(root)
f2.a.place(x=155,y=445)

f3 = box(root)
f3.a.place(x=235,y=445)

f4 = box(root)
f4.a.place(x=315,y=445)

f5 = box(root)
f5.a.place(x=395,y=445)

f6 = box(root)
f6.a.place(x=475,y=445)

f7 = box(root)
f7.a.place(x=555,y=445)

#------ GREEN BUTTONS POSITION ------#
butt1,butt2,butt3,butt4,butt5,butt6,butt7 = [None]*7
buttons = [butt1,butt2,butt3,butt4,butt5,butt6,butt7]
pos_buttons = [[75,530],[155,530],[235,530],[315,530],[395,530],[475,530],[555,530]]
v,j = 1,0
for i in buttons:
    ps_butt = pos_buttons[j]
    i = boton(root, v)
    i.butt.place(x=ps_butt[0], y=ps_butt[1])
    v += 1
    j += 1

root.mainloop()