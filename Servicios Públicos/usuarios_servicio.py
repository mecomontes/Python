#!/usr/bin/env python
#-*- coding: utf-8 -*-
def Usuarios_Servicio():

    try:
        Usuarios_Servicio = open("Servicios_Publicos.csv")
        Lineas = Usuarios_Servicio.readlines()
        Usuarios_Servicio_EPM = {}

        febrero = '02'

        for linea in range(1, len(Lineas)):
            elementos = Lineas[linea].strip().split(";")
            fecha = elementos[1]
            servicio = elementos[2]
            fecha_separada = fecha.split("/")

            if fecha_separada[1] == febrero:
                if servicio not in Usuarios_Servicio_EPM:
                     Usuarios_Servicio_EPM.update({servicio:1})
                elif servicio in Usuarios_Servicio_EPM:
                    Usuarios_Servicio_EPM[servicio]+=1
        print("Servicios:",Usuarios_Servicio_EPM.keys())
        print("Servicios:",Usuarios_Servicio_EPM.values())
        print("Servicios:",Usuarios_Servicio_EPM)

        for servicio,usuarios in Usuarios_Servicio_EPM.items():
            print("Número de usuarios por", servicio,":",usuarios)

        Usuarios_Servicio.close()
    except IOError:
        print("El archivo no existe")

Usuarios_Servicio()
