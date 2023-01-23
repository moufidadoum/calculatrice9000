import tkinter
from tkinter import *
from tkinter import Toplevel


root=Tk()
root.title("Calculatrice 9000")
root.geometry("710x600+100+200")
root.resizable(False,False)
root.configure(bg="#e5e5e5")

calcul = ""

historiquecalcul = []
label_historiquecalcul = None

def afficher(value):
    global calcul
    calcul+=value
    label_resultat.config(text=calcul)

def clear():
    global calcul
    calcul = ""
    label_resultat.config(text=calcul)

def clear_historique():
    global historiquecalcul
    historiquecalcul.clear()
    label_historiquecalcul.config(text="")

def historique():
    global historiquecalcul
    historiquecalcul_win = Toplevel(root)
    historiquecalcul_win.title("Historique des calculs")
    historiquecalcul_win.geometry("710x200+500+500")
    global label_historiquecalcul
    label_historiquecalcul = Label(historiquecalcul_win, width=25, height=5, text=historiquecalcul, font=("arial", 10))
    label_historiquecalcul.pack()
    Button(historiquecalcul_win, text="Effacer l'historique", width=25, height=1, font=("arial", 10, "bold"), bd=1,
           fg="#000", bg="#3697f5", command=lambda: clear_historique()).pack()

def racinecarre():
        global calcul
        try:
            resultat = eval(calcul)**(1/2)
            calcul = str(resultat)
            label_resultat.config(text=calcul)
        except:
            label_resultat.config(text="erreur")
            calcul = ""

def carre():
    global calcul
    try:
        resultat = eval(calcul)**2
        calcul = str(resultat)
        label_resultat.config(text=calcul)
    except:
        label_resultat.config(text="erreur")
        calcul = ""

def cube():
    global calcul
    try:
        resultat = eval(calcul)**3
        calcul = str(resultat)
        label_resultat.config(text=calcul)
    except:
        label_resultat.config(text="erreur")
        calcul = ""

def pourcentage():
    global calcul
    try:
        resultat = eval(calcul) / 100
        calcul = str(resultat)
        label_resultat.config(text=calcul)
    except:
        label_resultat.config(text="erreur")
        calcul = ""

def calculer():
    global calcul
    global historiquecalcul
    resultat = ""
    if calcul != "":
        try:
            resultat = eval(calcul)
            historiquecalcul.append(calcul + " = " + str(resultat))
        except:
            resultat = "erreur"
            calcul = ""
    label_resultat.config(text=resultat)


label_resultat= Label(root,width=25,height=2,text="",font=("arial",30))
label_resultat.pack()

Button(root,text="C", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#fe9037",command=lambda: clear()).place(x=10,y=100)
Button(root,text="/", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: afficher("/")).place(x=150,y=100)
Button(root,text="%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: afficher("%")).place(x=290,y=100)
Button(root,text="*", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: afficher("*")).place(x=430,y=100)
Button(root,text="√", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: racinecarre()).place(x=570,y=100)



Button(root,text="7", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("7")).place(x=10,y=200)
Button(root,text="8", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("8")).place(x=150,y=200)
Button(root,text="9", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("9")).place(x=290,y=200)
Button(root,text="-", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: afficher("-")).place(x=430,y=200)
Button(root,text="x²", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: carre()).place(x=570,y=200)

Button(root,text="4", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("4")).place(x=10,y=300)
Button(root,text="5", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("5")).place(x=150,y=300)
Button(root,text="6", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("6")).place(x=290,y=300)
Button(root,text="+", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: afficher("+")).place(x=430,y=300)
Button(root,text="x³", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1",command=lambda: cube()).place(x=570,y=300)

Button(root,text="1", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("1")).place(x=10,y=400)
Button(root,text="2", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("2")).place(x=150,y=400)
Button(root,text="3", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("3")).place(x=290,y=400)
Button(root,text="0", width=11, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher("0")).place(x=10,y=500)
Button(root, text="pour%", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#bcb8b1", command=lambda: pourcentage()).place(x=570,y=400)
Button(root, text="H", width=5, height=1, font=("arial", 30, "bold"), bd=1, fg="#000", bg="#fe9037", command=lambda: historique()).place(x=570, y=500)


Button(root,text=".", width=5, height=1, font=("arial",30,"bold"), bd=1,fg="#000",bg="#e5e5e5",command=lambda: afficher(".")).place(x=290,y=500)
Button(root,text="=", width=5, height=3, font=("arial",30,"bold"), bd=1,fg="#000",bg="red",command=lambda: calculer()).place(x=430,y=400)


root.mainloop()