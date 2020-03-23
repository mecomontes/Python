from tkinter import *


#CREAR LA VENTANA

ventana=Tk()
ventana.title('Calculadora')
ventana.geometry('300x300')
ventana.configure(background='dark turquoise')


lbl1 = Label(ventana, text="N1",width=5,height=1,font=("Arial Bold", 50), bg="orange", fg="red")
lbl1.grid(column=0, row=0)


lbl2 = Label(ventana, text="N1",width=5,height=1,font=("Arial Bold", 50), bg="orange", fg="red")
lbl2.grid(column=0, row=1)


txt1 = Entry(ventana,width=10,font=("Arial Bold", 50), bg="blue", fg="white")
txt1.grid(column=1, row=0)


txt2 = Entry(ventana,width=10,font=("Arial Bold", 50), bg="blue", fg="white")
txt2.grid(column=1, row=1)


lbl3 = Label(ventana, text="Resultado",width=5,height=1,font=("Arial Bold", 50), bg="orange", fg="red")
lbl3.grid(column=3, row=1)


def clicked():
    N1=float(txt1.get())
    N2=float(txt2.get())
    print(N1,N2)
    lbl3.configure(text=str(N1+N2),width=5,height=1,font=("Arial Bold", 50), bg="orange", fg="red")

btn = Button(ventana, text="SUMAR",font=("Arial Bold", 50), bg="orange", fg="red",command=clicked)
btn.grid(column=2, row=2)



ventana.mainloop()