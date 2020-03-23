from tkinter import *

ventana=Tk()
ventana.option_add("*Font", "courier 50")
ventana.title('Cambio de Tasa')
ventana.configure(bg='light blue')
Label(ventana,text='Tasa',bg='light blue',fg='black').grid(row=0,column=0)
Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=0,column=1)
Label(ventana,text='%',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=0,column=2)
Label(ventana,text='Inicial',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=1,column=0)
Label(ventana,text='Final',bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=2,column=0)

Button(ventana,text='CALCULAR',justify='center',padx=5,pady=5,bg='gray58',fg='black',font=('Arial Bold',50)).grid(row=3,column=2)

Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=4,column=1,columnspan=4,padx=5,pady=5)
Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=5,column=1)
Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=6,column=1)
Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=7,column=1)
Entry(ventana,width=10,bg='light blue',fg='black',font=('Arial Bold',50)).grid(row=8,column=1)

from tkinter import ttk
from tkinter.ttk import *

Combobox(ventana,state='readonly',width=10,values=('Anual','Semestral','Trimestral','Bimestral','Mensual','Quincenal','Diario',' ')).grid(row=1,column=1)
Combobox(ventana,state='readonly',width=10,values=('Anual','Semestral','Trimestral','Bimestral','Mensual','Quincenal','Diario')).grid(row=1,column=2)
Combobox(ventana,state='readonly',width=10,values=('Vencido','Anticipado')).grid(row=1,column=3)

Combobox(ventana,state='readonly',width=10,values=('Anual','Semestral','Trimestral','Bimestral','Mensual','Quincenal','Diario',' ')).grid(row=2,column=1)
Combobox(ventana,state='readonly',width=10,values=('Anual','Semestral','Trimestral','Bimestral','Mensual','Quincenal','Diario')).grid(row=2,column=2)
Combobox(ventana,state='readonly',width=10,values=('Vencido','Anticipado')).grid(row=2,column=3)

ventana.mainloop()
