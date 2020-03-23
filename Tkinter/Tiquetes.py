"""                                     Proyecto 2 – Panel de compra/venta de billetes de una aerolínea

cursotkinterpython

Bienvenidos al último proyecto del curso de Tkinter. Este proyecto está basado en el desarrollo de una interfaze gráfica donde los usuarios pueden comprar un billete de avión.
Objetivo del 6º tutorial de Curso de Interfaz Gráfica con TKinter

Desarrollar la interfaz gráfica para un programa de compra de billetes de avión

En la siguiente imagen puede ver la ventana principal de este ejemplo:cursotkinterpython

La imagen de arriba representa la ventana principal de nuestra interface pero está interface esta compuesta de otras 3 interfaces más:

    Interface principal:
        El usuario elige el número de billetes
        El usuario escribe el nombre de la persona que va a comprar los billetes
        El usuario marca si quiere solo ida o ida y vuelta
        El usuario marca si viaja en turista, 2º clase o 1º clase
        El usuario marca las fechas y en este botón se abre la interface de fechas
        El usuario marca el origen de su vuelo y en este botón se abre la interface de origen
        El usuario marca el destino de su vuelo y en este botón se abre la interface de destino
        Despues de “A Pagar (euros)” el usario puede ver cuanto vale lo que está seleccionando
        El botón de “Calcular” es una función que muestra el coste de lo seleccionado
        El botón de “Salir” cerrará la interface

cursotkinterpythonfechas

    Interface fechas:
        El usuario introduce la fecha de ida y de vuelta de su vuelocursotkinterpythonorigen

    Interface origen:
        El usuario selecciona el origen de su vuelocursotkinterpythondestino

    Interface destino:
        El usuario selecciona el destino de su vuelo

Aquí adjuntamos el código completo del Proyecto 2 – Panel de compra/venta de billetes de una aerolínea:"""

from tkinter import *
from tkinter import ttk, font
import datetime
class Aplicacion():
  def __init__(self):
    self.raiz = Tk()
    self.raiz.title("Billetes de Avion")
    self.raiz.geometry('400x600')
    self.raiz.resizable(10,10)
    # Declara variables de control
    self.num_via = IntVar(value=1)
    self.ida_vue = BooleanVar()
    self.clase = StringVar(value='t')
    self.tipovuelo = StringVar(value='g')
    self.errores = StringVar()
    self.nombre = StringVar()
    self.precio = DoubleVar(value=50)
    self.total = DoubleVar(value=0.0)
    self.etiq1 = ttk.Label(self.raiz, text="Nº de billetes:")
    self.viaje = Spinbox(self.raiz, from_=1, to=20, wrap=True,textvariable=self.num_via,state='readonly')
    self.idavue = ttk.Checkbutton(self.raiz, text='Ida y vuelta',variable=self.ida_vue,onvalue=True, offvalue=False)
    self.etiq2 = ttk.Label(self.raiz, text="Nombre y apellidos:")
    self.etiq3 = ttk.Label(self.raiz, text="Solo ida o vuelta también:")
    self.nombre1= ttk.Entry(self.raiz, textvariable=self.nombre,width=15)
    self.etiq4 = ttk.Label(self.raiz, text="Clase:")
    self.clase1 = ttk.Radiobutton(self.raiz, text='Turista',variable=self.clase, value='t')
    self.clase2 = ttk.Radiobutton(self.raiz, text='Segunda Clase',variable=self.clase, value='p')
    self.clase3 = ttk.Radiobutton(self.raiz, text='Primera Clase',variable=self.clase, value='l')
    self.boton3 = ttk.Button(self.raiz, text="Fechas",command=self.fechas)
    self.boton4 = ttk.Button(self.raiz, text="Origen",command=self.origen)
    self.boton5 = ttk.Button(self.raiz, text="Destino",command=self.destino)
    self.etiq4 = ttk.Label(self.raiz, text="Precio:")
    self.etiq5 = ttk.Label(self.raiz, text="A Pagar (euros):")
    self.etiq6 = ttk.Label(self.raiz, textvariable=self.total,foreground="yellow", background="black",borderwidth=5, anchor="e")
    self.separ1 = ttk.Separator(self.raiz, orient=HORIZONTAL)
    self.boton1 = ttk.Button(self.raiz, text="Calcular",command=self.calcular)
    self.boton2 = ttk.Button(self.raiz, text="Salir",command=quit)
    self.etiq1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.viaje.pack(side=TOP, fill=X, expand=True,padx=20, pady=5)
    self.etiq2.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.nombre1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.etiq3.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.idavue.pack(side=TOP, fill=X, expand=True,padx=20, pady=5)
    self.etiq4.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.clase1.pack(side=TOP, fill=BOTH, expand=True,padx=20, pady=5)
    self.clase2.pack(side=TOP, fill=BOTH, expand=True,padx=20, pady=5)
    self.clase3.pack(side=TOP, fill=BOTH, expand=True,padx=20, pady=5)
    self.boton3.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=10)
    self.boton4.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=10)
    self.boton5.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=10)
    self.etiq4.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.etiq5.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.etiq6.pack(side=TOP, fill=BOTH, expand=True,padx=20, pady=5)
    self.separ1.pack(side=TOP, fill=BOTH, expand=True,padx=5, pady=5)
    self.boton1.pack(side=LEFT, fill=BOTH, expand=True,padx=10, pady=10)
    self.boton2.pack(side=RIGHT, fill=BOTH, expand=True,padx=10, pady=10)
    self.raiz.mainloop()
  def calcular(self):
  # Función para validar datos y calcular importe a pagar
    error_dato = False
    total = 0
    date1=self.autof_dia1.get()
    date2=self.autof_dia2.get()
    dia11= datetime.datetime.strptime(date1, '%d/%m/%Y')
    dia22= datetime.datetime.strptime(date2, '%d/%m/%Y')
    try:
      precio = float(self.precio.get())
    except:
      error_dato = True
    if not error_dato:
      total = self.num_via.get() * precio
      if self.ida_vue.get():
        total = total * 1.5
      if self.clase.get() == 't':
        total = total * 1.2
      elif self.clase.get() == 'p':
        total = total * 2
      elif self.clase.get() == 'l':
        total = total * 3
      self.total.set(total)
    if self.destino1.get() == self.origen1.get():
      self.total.set("¡ERROR misma ciudad de ida que vuelta!")
    if dia11 > dia22 :
      self.total.set("Error, aún no hacesmo viajes al pasado!")
  def fechas(self):
    self.raiz2 = Toplevel()
    self.raiz2.geometry('300x300')
    self.raiz2.resizable(10,10)
    self.raiz2.title('Selecciona tus fechas')
    self.autof_dia1 = StringVar(value='01/02/2019')
    self.autof_dia2 = StringVar(value='30/03/2019')
    self.etiq1 = ttk.Label(self.raiz2,text="Fecha de ida (01/01/2018):")
    self.fecha1 = ttk.Entry(self.raiz2, textvariable=self.autof_dia1,width=10)
    self.etiq2 = ttk.Label(self.raiz2,text="Fecha de vuelta (01/02/2018):")
    self.fecha2 = ttk.Entry(self.raiz2, textvariable=self.autof_dia2,width=10)
    dia1 = self.autof_dia1.get()
    dia2 = self.autof_dia2.get()
    self.etiq1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.fecha1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.etiq2.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.fecha2.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.raiz2.transient(master=self.raiz)
    self.raiz2.grab_set()
    self.raiz.wait_window(self.raiz2)
  def origen(self):
    self.raiz3 = Toplevel()
    self.raiz3.geometry('200x600')
    self.raiz3.resizable(10,10)
    self.raiz3.title('Selecciona el origen de tu vuelo')
    self.origen1 = StringVar(value='t')
    self.or1 = ttk.Radiobutton(self.raiz3, text='Madrid',variable=self.origen1, value='t')
    self.or2 = ttk.Radiobutton(self.raiz3, text='Barcelona',variable=self.origen1, value='l')
    self.or3 = ttk.Radiobutton(self.raiz3, text='Berlin',variable=self.origen1, value='r')
    self.or4 = ttk.Radiobutton(self.raiz3, text='Paris',variable=self.origen1, value='s')
    self.or5 = ttk.Radiobutton(self.raiz3, text='New York',variable=self.origen1, value='p')
    origen1 = self.origen1.get()
    self.or1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.or2.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.or3.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.or4.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.or5.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.raiz3.transient(master=self.raiz)
    self.raiz3.grab_set()
    self.raiz.wait_window(self.raiz3)
  def destino(self):
    self.raiz4 = Toplevel()
    self.raiz4.geometry('200x600')
    self.raiz4.resizable(10,10)
    self.raiz4.title('Selecciona tu Destino')
    self.destino1 = StringVar(value='t')
    self.de1 = ttk.Radiobutton(self.raiz4, text='Madrid',variable=self.destino1, value='t')
    self.de2 = ttk.Radiobutton(self.raiz4, text='Barcelona',variable=self.destino1, value='l')
    self.de3 = ttk.Radiobutton(self.raiz4, text='Berlin',variable=self.destino1, value='r')
    self.de4 = ttk.Radiobutton(self.raiz4, text='Paris',variable=self.destino1, value='s')
    self.de5 = ttk.Radiobutton(self.raiz4, text='New York',variable=self.destino1, value='p')
    destino1 = self.destino1.get()
    self.de1.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.de2.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.de3.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.de4.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.de5.pack(side=TOP, fill=BOTH, expand=True,padx=10, pady=5)
    self.raiz4.transient(master=self.raiz)
    self.raiz4.grab_set()
    self.raiz.wait_window(self.raiz4)
def main():
  mi_app = Aplicacion()
  return 0
if __name__ == '__main__':
  main()

 
"""Cosas a tener en cuenta en este proyecto de Tkinter

    El proyecto tiene varias interfaces para realizar varias interfaces revisa el siguiente ejemplo"""

from tkinter import *
from tkinter import ttk, font
import datetime
class Aplicacion():
    def __init__(self):
        self.raiz = Tk()
        self.raiz.title("Billetes de Avion")
        self.raiz.geometry('400x600')
        self.raiz.resizable(10,10)  
 
        self.boton3 = ttk.Button(self.raiz, text="Fechas", 
                                 command=self.fechas)  
        self.boton4 = ttk.Button(self.raiz, text="Origen", 
                         command=self.origen) 
        self.boton5 = ttk.Button(self.raiz, text="Destino", 
                 command=self.destino) 
                
        self.boton2 = ttk.Button(self.raiz, text="Salir", 
                                 command=quit)  
                               
        self.boton3.pack(side=TOP, fill=BOTH, expand=True, 
                 padx=10, pady=10)  
        self.boton4.pack(side=TOP, fill=BOTH, expand=True, 
                 padx=10, pady=10)  
        self.boton5.pack(side=TOP, fill=BOTH, expand=True, 
                 padx=10, pady=10)          
        
        self.boton2.pack(side=RIGHT, fill=BOTH, expand=True, 
                         padx=10, pady=10)                
        self.raiz.mainloop()
    def fechas(self):        
        self.raiz2 = Toplevel()
        self.raiz2.geometry('300x300')
        self.raiz2.resizable(10,10)      
        self.raiz2.title('Selecciona tus fechas')              
        
        self.raiz2.transient(master=self.raiz)       
        self.raiz2.grab_set()
        self.raiz.wait_window(self.raiz2)
    def origen(self):        
        self.raiz3 = Toplevel()
        self.raiz3.geometry('200x600')
        self.raiz3.resizable(10,10)      
        self.raiz3.title('Selecciona el origen de tu vuelo')              
        self.raiz3.transient(master=self.raiz)       
        self.raiz3.grab_set()
        self.raiz.wait_window(self.raiz3)
    def destino(self):        
        self.raiz4 = Toplevel()
        self.raiz4.geometry('200x600')
        self.raiz4.resizable(10,10)      
        self.raiz4.title('Selecciona tu Destino')              
        
        self.raiz4.transient(master=self.raiz)       
        self.raiz4.grab_set()
        self.raiz.wait_window(self.raiz4)
            
def main():
    mi_app = Aplicacion()
    return 0
if __name__ == '__main__':
    main()

""" En el botón de “Calcular” hemos desarrollado una funcion que calcula el coste de tu vuelo pero tambien maneja errores. Uno de 
los errores que maneja es si el usuario elige un mismo origen que destino cuando pulsamos en calcular nos aparece el mensaje de ”
 ¡ERROR misma ciudad de ida que vuelta!”. Otro de los errores que maneja es si el usario escribe una fecha de vuelta anterior a 
 la ida nos aparece l mensaje de “Error, aún no hacesmo viajes al pasado!”. Revisa la función y trata de entenderla:"""

def calcular(self):
    
    # Función para validar datos y calcular importe a pagar
#        origen1 = self.origen1.get()
#        destino1 = self.destino1.get()
    error_dato = False
    total = 0
    date1=self.autof_dia1.get()
    date2=self.autof_dia2.get()
    dia11= datetime.datetime.strptime(date1, '%d/%m/%Y')
    dia22= datetime.datetime.strptime(date2, '%d/%m/%Y')        
    try:
        precio = float(self.precio.get())
    except:
        error_dato = True      
    if not error_dato:
        total =  self.num_via.get() * precio
        if self.ida_vue.get():
            total = total * 1.5
        if self.clase.get() == 't':
            total = total * 1.2
        elif self.clase.get() == 'p':
            total = total * 2
        elif self.clase.get() == 'l':
            total = total * 3
        self.total.set(total)
        
    if   self.destino1.get() ==  self.origen1.get():
        self.total.set("¡ERROR misma ciudad de ida que vuelta!")
    
    if    dia11 > dia22 :
        self.total.set("Error, aún no hacesmo viajes al pasado!")

"""En este proyecto hemos tratado de aplicar todos los conocimientos que se ha ido adquiriendo a lo largo de este curso, no 
obstante te animamos a mejorar esta interface. Puedes añadir mas campos, puedes añadir un botón que diriga al usuario a paypal y 
haga el pago, puedes manejar mas errores o también puedes añadir tantas interfaces secundarias como quieras …"""