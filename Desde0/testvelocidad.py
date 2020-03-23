from tkinter import *
from tkinter import ttk

def convertir(bytes, to, tamano_bloque=1024):
    table={'k':1,'m':2,'g':3,'t':4,'p':5}
    number=float(bytes)
    number/=(tamano_bloque ** table[to])
    return number

def mostrar():
    print(Resultado_dict)
    d=str(round(convertir((resultado_dict["download"]),'m'),2))
    u=str(round(convertir((resultado_dict["upload"]),'m'),2))
    p=str(round(convertir((resultado_dict["ping"]))))
    etiq_desc2.configure(text=d)
    etiq_carga2.configure(text=u)
    etiq_ping2.configure(text=p)

ventana=Tk()
ventana.title("Test de Velocidad (Internet)")
ventana.configure(bd=5)

img=PhotoImage(file="logo.png")
#etiqueta_logo=Label(ventana,image=img)
#etiqueta_logo.grid(column=0,row=0,rowspan=2)

etiq_desc1=Label(ventana,text="Descarga (Mbps)",font="Arial 10 bold",fg="#8A66BD")
etiq_desc1.grid(column=1,row=0)
etiq_desc2=Label(ventana,text="00.00",font="Arial 35 bold",fg="#FF2E70")
etiq_desc2.grid(column=1,row=1,sticky=N)

etiq_carga1=Label(ventana,text="Carga (Mbps)",font="Arial 10 bold",fg="#8A66BD")
etiq_carga1.grid(column=2,row=0)
etiq_carga2=Label(ventana,text="00.00",font="Arial 35 bold",fg="#FF2E70")
etiq_carga2.grid(column=2,row=1,sticky=N)

etiq_ping1=Label(ventana,text="Ping (Mbps)",font="Arial 10 bold",fg="#8A66BD")
etiq_ping1.grid(column=3,row=0)
etiq_ping2=Label(ventana,text="00",font="Arial 35 bold",fg="#FF2E70")
etiq_ping2.grid(column=3,row=1,sticky=N)

barra=ttk.Progressbar(ventana,orient=HORIZONTAL,length=581,mode="indeterminate")
barra.grid(column=0,row=2,columnspan=4,pady=2)
barra.configure(maximum=100,value=5)
barra.start(10)

boton_mostrar=Button(ventana,text="MOSTRAR",width=72,height=2,bd=0,fg="#ffffff",cursor="hand2",font="Arial 10 bold",bg="#8A66BD")
boton_mostrar.grid(column=0,row=3,columnspan=4)

ventana.mainloop()


