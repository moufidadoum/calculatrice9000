import tkinter
from tkinter import *
from tkinter import Toplevel


root=Tk()
root.title("Calculatrice 9000")
root.geometry("710x600+100+200")
root.resizable(False,False)
root.configure(bg="#e5e5e5")

equation = ""

history = []
label_history = None

def show(value):
    global equation
    equation+=value
    label_result.config(text=equation)

def clear():
    global equation
    equation = ""
    label_result.config(text=equation)

def clear_history():
    global history
    history.clear()
    label_history.config(text="")

def history_window():
    global history
    history_win = Toplevel(root)
    history_win.title("Historique des calculs")
    history_win.geometry("710x200+500+500")
    global label_history
    label_history = Label(history_win, width=25, height=5, text=history, font=("arial", 10))
    label_history.pack()
    Button(history_win, text="Effacer l'historique", width=25, height=1, font=("arial", 10, "bold"), bd=1,
           fg="#000", bg="#3697f5", command=lambda: clear_history()).pack()

def sqrt():
        global equation
        try:
            result = eval(equation)**(1/2)
            equation = str(result)
            label_result.config(text=equation)
        except:
            label_result.config(text="erreur")
            equation = ""

def carre():
    global equation
    try:
        result = eval(equation)**2
        equation = str(result)
        label_result.config(text=equation)
    except:
        label_result.config(text="erreur")
        equation = ""

def cube():
    global equation
    try:
        result = eval(equation)**3
        equation = str(result)
        label_result.config(text=equation)
    except:
        label_result.config(text="erreur")
        equation = ""

def percentage():
    global equation
    try:
        result = eval(equation) / 100
        equation = str(result)
        label_result.config(text=equation)
    except:
        label_result.config(text="erreur")
        equation = ""

def calculate():
    global equation
    global history
    result = ""
    if equation != "":
        try:
            result = eval(equation)
            history.append(equation + " = " + str(result))
        except:
            result = "erreur"
            equation = ""
    label_result.config(text=result)


label_result= Label(root,width=25,height=2,text="",font=("arial",30))
label_result.pack()

Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#fe9037",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: show("/")).place(x=150,y=100)
Button(root,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: show("%")).place(x=290,y=100)
Button(root,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: show("*")).place(x=430,y=100)
Button(root,text="√", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: sqrt()).place(x=570,y=100)



Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: show("-")).place(x=430,y=200)
Button(root,text="x²", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: carre()).place(x=570,y=200)

Button(root,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: show("+")).place(x=430,y=300)
Button(root,text="x³", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: cube()).place(x=570,y=300)

Button(root,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("3")).place(x=290,y=400)
Button(root,text="0", width=11, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show("0")).place(x=10,y=500)
Button(root, text="pour%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1", command=lambda: percentage()).place(x=570,y=400)
Button(root, text="H", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#fe9037", command=lambda: history_window()).place(x=570, y=500)


Button(root,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: show(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#000",bg="red",command=lambda: calculate()).place(x=430,y=400)







root.mainloop()