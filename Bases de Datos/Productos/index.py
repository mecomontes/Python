from tkinter import ttk
from tkinter import *
import sqlite3

#descargar la base de datos desde www.sqlite.org

class Product:

    db_name = 'database.db'

    def __init__(self,window):
        self.wind = window
        self.wind.title('Products Aplication')

        #CReating a Frame Container
        frame = LabelFrame(self.wind, text = 'Register a new product')
        frame.grid(row = 0, column = 0, columnspan = 3, pady =20)

        #Name Input
        Label(frame, text = 'Name: ').grid(row = 1, column = 0)
        self.name = Entry(frame).grid(row = 2, column = 1)
        #self.name.focus() #para que el cursor se posicione en la casilla donde se ingresa nombre

        #Price Input
        Label(frame, text = 'Price: ').grid(row = 2, column = 0)
        self.price = Entry(frame).grid(row = 1, column = 1)

        #Button add Product
        ttk.Button(frame, text ='Save Product').grid(row =3, columnspan =2, sticky = W + E)# sticky es para que el boton ocupe todo el ancho

        #table with  products
        self.tree = ttk.Treeview(height = 10, columns = 2).grid(row = 4, column = 0, columnspan = 2)
        #self.tree.heading('#0', text = 'Name', anchor = CENTER)
        #self.tree.heading('#1', text = 'Price', anchor = CENTER)

        self.get_products()

    def run_query(self, query, parameters = ()): #funcion encargada de realizar la conexion con la basse de datos y otener los datos de la base
        with sqlite3.connect(self.db_name) as conn:
             cursor = conn.cursor() #obtener la posición en la base de datos
             result = cursor.execute(query, parameters)#también se pide que tome los parámetros
             conn.commit() #ejecutar la conexión
        return result #retornar el resultadod e la base de datos

    def get_products(self): #trae los productos de la base de datos
        #cleaning table in tree
        records = self.tree.get_children()    #comando para obtener todos los datos
        for element in records:#revisar si la tabla está vacía y si no se limpia
            self.tree.delete(element)

        query = 'SELECT * FROM product ORDER BY name DESC' #traer los datos de la base de datos de manera descendente - DES
        db_rows = self.run_query(query)#pasar la consulta para ejecutarla

        for row in db_rows:
            #self.tree.insert('', 0, text = row[1])
            print(row)#mostrar a tabla con resultados

if __name__ == '__main__':
    window = Tk()
    application =Product(window)
    window.mainloop()