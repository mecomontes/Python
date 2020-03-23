from tkinter import *


#CREAR LA VENTANA

ventana=Tk()
ventana.title('Calculadora')
ventana.geometry('300x300')
ventana.configure(background='dark turquoise')
 
# LABEL

lbl = Label(ventana, text="Hello",width=20,height=10,font=("Arial Bold", 50), bg="orange", fg="red")
lbl.grid(column=0, row=0)

# TEXTBOX

entrada = tk.StringVar()
txt = Entry(ventana,width=10,textvariable=entrada)
txt.grid(column=1, row=0)

# LISTBOX

combo = Combobox(ventana) 
combo['values']= (1, 2, 3, 4, 5, "Text") 
combo.current(1) #set the selected item 
combo.grid(column=2, row=1)
a=combo.get()

# CHECKBUTTOM

chk_state = BooleanVar() 
chk_state.set(True) #set check state 
chk = Checkbutton(ventana, text='Choose', var=chk_state)
chk.grid(column=2, row=2)

# RADIO BUTTOM

selected = IntVar()
rad1 = Radiobutton(ventana,text='First', value=1,variable=selected)
rad2 = Radiobutton(ventana,text='Second', value=2,variable=selected)
rad3 = Radiobutton(ventana,text='Third', value=3,variable=selected)
rad1.grid(column=3, row=0)
rad2.grid(column=3, row=1)
rad3.grid(column=3, row=2)
b=selected.get()

# BOTON

def clicked():
 
    lbl.configure(text="Button was clicked !!")

btn = Button(ventana, text="Click Me",font=("Arial Bold", 50), bg="orange", fg="red",command=clicked)
btn.grid(column=1, row=1)






ventana.mainloop()