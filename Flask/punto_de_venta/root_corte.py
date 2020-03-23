# -*- encoding: utf-8 -*-
# ------------------------------------------------------------------------#
# Programa: Punto de venta 2.0				                              #
# ------------------------------------------------------------------------#
# Propósito: Realizar corte de las ventas echas                           #
# ------------------------------------------------------------------------#
# Autor: Abuelazo                                                         #
# ------------------------------------------------------------------------#
# Fecha: 01/05/2016                                                       #
# ------------------------------------------------------------------------#

#importamos librerias necesarias
import time
import csv
import os.path
from PyQt4 import QtGui, QtCore
from reportlab.pdfgen import canvas


#metodo para mostrar las ventas en una tabla
def mostrar_ventas(self, nombre):
    self.vendedor = nombre
    #se toma la fecha del sistema
    self.fecha = str(time.strftime("%d") + "-" + time.strftime("%m") + "-" + time.strftime("%Y"))
    if os.path.isfile("/home/mauricio/proyecto/punto_de_venta/corte/" + self.fecha + ".csv"):
        #se abre el archivo y se asigna a una variable """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        archivo_corte = csv.reader(open("/home/mauricio/proyecto/punto_de_venta/corte/" + self.fecha + ".csv", 'r'))
        #se cuenta la longitud del archivo """OJO CAMBIAR LA DIRECCION POR DONDE VAYA A ESTAR SU ARCHIVO"""
        filas_archivo = len(open("/home/mauricio/proyecto/punto_de_venta/corte/" + self.fecha + ".csv").readlines())
        #se definen las columnas para la tabla
        self.ui.corte_mostrar.setColumnCount(2)
        #se definen las filas para la tabla dependiendo la longitud del archivo
        self.ui.corte_mostrar.setRowCount(filas_archivo)
    else:
        QtGui.QMessageBox.warning(self, "Informacion", "Aun no se an realizado ventas", QtGui.QMessageBox.Ok)


    #bucle para obtener los datos
    for dato, fila in enumerate(archivo_corte):
        #se crea un item
        item = QtGui.QTableWidgetItem()
        #se asigna el valor al item
        item.setText(fila[0])
        #se manda el valor a la pocision
        self.ui.corte_mostrar.setItem(dato, 0, item)
        # se crea un item
        item = QtGui.QTableWidgetItem()
        # se asigna el valor al item
        item.setText(fila[1])
        # se manda el valor a la pocision
        self.ui.corte_mostrar.setItem(dato, 1, item)
    #se manda llamar el metodo total_corte
    total_corte(self)

#metodo para mostrar total de las ventas
def total_corte(self):
    #se crea una lista vacia
    corte = []
    #se cuentas las filas que existen en la tabla
    filas = self.ui.corte_mostrar.rowCount()
    #bucle para recorrer la tabla
    for suma in xrange(filas):
        #se asigna valor tomado de la tabla
        dato = float(self.ui.corte_mostrar.item(suma, 1).text())
        #se agrega a la lista
        corte.append(dato)

    #se manda llamar el metodo suma_total y se le pasa la lista
    suma_total(self, corte)

#metodo de suma_total y recibe la lista
def suma_total(self, lista):
    #se declara variable suma con valor de 0
    suma = 0
    #bucle para sumar los valores de la lista
    for i in range(0,len(lista)):
        #operacion para sumar los datos de la lista
        suma = suma + lista[i]
    #se manda el valor total al qline
    self.ui.corte_total.setText(str(float(suma)))
    reporte_realizado(self)


def reporte_realizado(self):
    if os.path.isfile("/home/mauricio/proyecto/punto_de_venta/corte/" + self.fecha + ".csv"):
        respuesta = QtGui.QMessageBox.warning(self, "Informacion", "Corte realizado desea sobreescribir", QtGui.QMessageBox.Ok, QtGui.QMessageBox.Cancel)
        if respuesta == QtGui.QMessageBox.Ok:
            reporte_pdf(self)
        else:
            pass
    else:
        reporte_pdf(self)


def reporte_pdf(self):

    self.filas = self.ui.corte_mostrar.rowCount()
    self.total = unicode(self.ui.corte_total.text())
    #valores pdf
    #y 830 especio de 10 para cada renglon 100 de margen arriba y abajo  queda 100 - 730
    #x 600  50 de margen de cada lado y queda 50-550
    self.reporte = canvas.Canvas ("/home/mauricio/Escritorio/reporte-"+self.fecha+".pdf")

    self.pagina = 1
    fila_pdf = 685
    columna_1 = 80
    columna_2 = 210
    index = 0

    pdf_encabezado(self)
    pdf_pie_de_pagina(self)

    for fila in xrange(self.filas):
        datos = []
        index = index + 1
        for columna in xrange(2):
            dato = unicode(self.ui.corte_mostrar.item(fila, columna).text())
            datos.append(dato)

        self.reporte.setFont("Helvetica-Bold", 8)
        self.reporte.drawString(columna_1, fila_pdf, datos[0])
        self.reporte.drawString(columna_2, fila_pdf, datos[1])

        fila_pdf = fila_pdf - 12

        if (fila_pdf == 85) and (index < 100):
            fila_pdf = 685
            columna_1 = 330
            columna_2 = 460
        elif (fila_pdf == 85) and (index >= 100):
            self.pagina = self.pagina + 1
            self.reporte.showPage()
            pdf_encabezado(self)
            pdf_pie_de_pagina(self)

            fila_pdf = 685
            columna_1 = 80
            columna_2 = 210
            index = 0
        else:
            continue

    self.reporte.save()

    # PARA WINDOWS: os.system("start AcroRD32 ruta_y_archivo.pdf &")
    os.system("atril /home/mauricio/Escritorio/reporte-"+self.fecha+".pdf &")


def pdf_encabezado(self):
    self.reporte.setFont("Helvetica-Bold", 14)
    self.reporte.drawString(50, 800, "REPORTE DE VENTAS REALIZADAS EL DIA " + self.fecha + "")
    self.reporte.drawString(50, 770, "DE LA EMPRESA ENCOM")
    self.reporte.drawString(50, 740, "REALIZADO POR EL USUARIO " + self.vendedor)
    self.reporte.drawImage("/home/mauricio/proyecto/punto_de_venta/iconos/cash_register.2.2.png", 450, 730, width=105, height=80)
    self.reporte.line(50, 720, 550, 720)
    self.reporte.drawString(60, 704, unicode("#"))
    self.reporte.drawString(80, 704, unicode("Producto"))
    self.reporte.drawString(210, 704, unicode("Precio"))
    self.reporte.line(50, 695, 550, 695)
    self.reporte.drawString(310, 704, unicode("#"))
    self.reporte.drawString(330, 704, unicode("Producto"))
    self.reporte.drawString(460, 704, unicode("Precio"))
    self.reporte.line(300, 85, 300, 720)
    self.reporte.line(50, 85, 50, 720)
    self.reporte.line(550, 85, 550, 720)
    self.reporte.line(50, 85, 550, 85)

def pdf_pie_de_pagina(self):
    self.reporte.setFont("Helvetica-Bold", 8)
    self.reporte.line(300, 45, 300, 85)
    self.reporte.line(550, 45, 550, 85)
    self.reporte.line(300, 45, 550, 45)
    self.reporte.line(300, 65, 550, 65)
    self.reporte.line(425, 45, 425, 85)
    self.reporte.drawString(310, 75, unicode("total de productos"))
    self.reporte.drawString(310, 55, unicode("total de efectivo"))
    self.reporte.drawString(430, 75, str(self.filas))
    self.reporte.drawString(430, 55, str(self.total))
    self.reporte.drawString(60, 75, unicode("Contacto: mauro_ruiz2001@hotmail.com"))
    self.reporte.drawString(60, 55, unicode("                  crostow.ewinkeiton@gmail.com"))
    self.reporte.drawString(60, 35, str("                  pagina numero : "+ str(self.pagina )))


