import tkinter 
from tkinter import *
from tkinter import messagebox

val = ""
A = 0
operator = ""


#Initial Widget creation using Tkinter


root = tkinter.Tk()
root.geometry("250x400+300+300")
#root.resizable()
root.title("vkcalc")

# Function sections

def btn_1_isclicked():
    global val
    val = val + "1"
    data.set(val)


def btn_2_isclicked():
    global val
    val = val + "2"
    data.set(val)

def btn_3_isclicked():
    global val
    val = val + "3"
    data.set(val)

def btn_4_isclicked():
    global val
    val = val + "4"
    data.set(val)

def btn_5_isclicked():
    global val
    val = val + "5"
    data.set(val)

def btn_6_isclicked():
    global val
    val = val + "6"
    data.set(val)

def btn_7_isclicked():
    global val
    val = val + "7"
    data.set(val)

def btn_8_isclicked():
    global val
    val = val + "8"
    data.set(val)

def btn_9_isclicked():
    global val
    val = val + "9"
    data.set(val)


def btn_0_isclicked():
    global val
    val = val + "0"
    data.set(val)




def btn_plus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "+"
    val = val + "+"
    data.set(val)


def btn__minus_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "-"
    val = val + "-"
    data.set(val)


def btn__mul_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "*"
    val = val + "*"
    data.set(val)





def btn_div_clicked():
    global A
    global operator
    global val
    A = int(val)
    operator = "/"
    val = val + "/"
    data.set(val)

def btn_c_pressed():
    global A,operator,val
    val = ""
    A = 0
    operator = ""
    data.set(val)



#Functions for Result


def result():
    global A,operator,val
    val2 = val
    if operator == "+":
        x = int((val2.split("+")[1]))
        C = A + x
        val = str(C)
        data.set(val)
    if operator == "-":
        x = int((val2.split("-")[1]))
        C = A - x
        val = str(C)
        data.set(val)
    if operator == "*":
        x = int((val2.split("*")[1]))
        C = A*x
        val = str(C)
        data.set(val)
    if operator == "/":
        x = int((val2.split("/")[1]))
        if x == 0:
            messagebox.showerror("Error", "Division By 0 Not Supported")
            A = ""
            val = ""
            data.set(val)
        else:
            C = int(A / x)
            data.set(C)        






# the label that shows the result

data = StringVar()

lbl = Label(
    root,
    text="Label",
    anchor = SE,                 #Direction : South-East
    font = ("Verdana",20),
    textvariable = data,
    background = "#ffffff",
    fg = "#000000",
)
lbl.pack(expand = True, fill = "both",)




# step 1: defining the 4 button row using (Frame)

btnrow1 = Frame(root,bg="#ffffff")
btnrow1.pack(expand= True,fill="both",)

btnrow2 = Frame(root,)
btnrow2.pack(expand= True,fill="both",)

btnrow3 = Frame(root,)
btnrow3.pack(expand= True,fill="both",)

btnrow4 = Frame(root,)
btnrow4.pack(expand= True,fill="both",)


# defining child element in each button row

# 4 button in btnrow1

btn_1 = Button(
    btnrow1,
    text = "1",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_1_isclicked,
)
btn_1.pack(side = LEFT, expand = True, fill ="both",)

btn_2 = Button(
    btnrow1,
    text = "2",
    font = ("Verdana",22),
    relief = "groove",
    border = 0,
    command = btn_2_isclicked,
)
btn_2.pack(side = LEFT, expand = True, fill ="both",)

btn_3 = Button(
    btnrow1,
    text = "3",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_3_isclicked,
)
btn_3.pack(side = LEFT, expand = True, fill ="both",)


btn_plus = Button(
    btnrow1,
    text = "+",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_plus_clicked,

)
btn_plus.pack(side = LEFT, expand = True, fill ="both",)




# 4 button in btnrow2



btn_4 = Button(
    btnrow2,
    text = "4",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_4_isclicked,
)
btn_4.pack(side = LEFT, expand = True, fill ="both",)

btn_5 = Button(
    btnrow2,
    text = "5",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_5_isclicked,
)
btn_5.pack(side = LEFT, expand = True, fill ="both",)

btn_6 = Button(
    btnrow2,
    text = "6",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_6_isclicked,
)
btn_6.pack(side = LEFT, expand = True, fill ="both",)


btn_minus = Button(
    btnrow2,
    text = "-",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn__minus_clicked,
)
btn_minus.pack(side = LEFT, expand = True, fill ="both",)


# 4 button in btnrow3

btn_7 = Button(
    btnrow3,
    text = "7",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_7_isclicked,
)
btn_7.pack(side = LEFT, expand = True, fill ="both",)

btn_8 = Button(
    btnrow3,
    text = "8",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_8_isclicked,
)
btn_8.pack(side = LEFT, expand = True, fill ="both",)

btn_9 = Button(
    btnrow3,
    text = "9",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_9_isclicked,
)
btn_9.pack(side = LEFT, expand = True, fill ="both",)


btn_mul = Button(
    btnrow3,
    text = "x",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn__mul_clicked,
        
)
btn_mul.pack(side = LEFT, expand = True, fill ="both",)



# 4 button in btnrow4



btn_clear = Button(
    btnrow4,
    text = "C",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_c_pressed,

)
btn_clear.pack(side = LEFT, expand = True, fill ="both",)

btn_0 = Button(
    btnrow4,
    text = "0",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_0_isclicked,
)
btn_0.pack(side = LEFT, expand = True, fill ="both",)

btn_equal = Button(
    btnrow4,
    text = "=",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = result,
)
btn_equal.pack(side = LEFT, expand = True, fill ="both",)


btn_div = Button(
    btnrow4,
    text = "/",
    font = ("Verdana",22),
    relief="groove",
    border = 0,
    command = btn_div_clicked,
)
btn_div.pack(side = LEFT, expand = True, fill ="both",)


root.mainloop()