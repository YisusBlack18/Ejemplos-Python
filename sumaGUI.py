from tkinter import *
from tkinter import messagebox
# Autor: Jesus Angel Juarez Zazueta

def sumar():
    a = int(entrada.get())
    b = int(entrada2.get())

    try:
        labelC["text"] = "Resultado: "+str(a+b)
    except:
        labelC["text"] = "No se puede"

ventana = Tk()
ventana.geometry("600x400")
ventana.title("The King of Fighters")

labelA = Label(ventana,text="A: ")
labelA.place(x=50,y=20)

entrada = Entry(ventana)
entrada.place(x=70,y=20)

labelB = Label(ventana,text="B: ")
labelB.place(x=50,y=40)

entrada2 = Entry(ventana)
entrada2.place(x=70,y=40)

labelC = Label(ventana,text="Resultado: ")
labelC.place(x=50,y=60)

boton = Button(ventana,text="Calcular",command=lambda:sumar())
boton.place(x=50,y=100)

ventana.mainloop()

