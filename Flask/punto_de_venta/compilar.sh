#!/bin/bash
cd /home/mauricio/proyecto/punto_de_venta/pantallas
pwd
pyuic4 -x logueo.ui -o logueo.py
pyuic4 -x root.ui -o root.py


cd /home/mauricio/proyecto/punto_de_venta/iconos
pwd
pyrcc4 iconos.qrc -o icono_rc.py
mv icono_rc.py /home/mauricio/proyecto/punto_de_venta/pantallas

