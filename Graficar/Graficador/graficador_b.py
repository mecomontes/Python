#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

root = tkinter.Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")#1000x700
#root.configure(background="SkyBlue4")

style.use('fivethirtyeight')#'

#fig = Figure(figsize=(5, 4), dpi=100)
fig = Figure()
ax1 = fig.add_subplot(111)
expresiones=[""]
canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
#toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

act_rango=False
ul_ran=""
ran=""
    
def animate(i):
    global ejes
    global act_rango
    global ul_ran
    if act_rango==True:
        try:
            lmin = float(ran[0]); lmax = float(ran[1])
            if lmin < lmax:
                x = np.arange(lmin, lmax, .01)#.01
                ul_ran = [lmin, lmax]
            else:
                act_rango = False
        except:
            messagebox.showwarning("Error","Entrada no válida")
            #print("Se repite")
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        if ul_ran!="":
            x = np.arange(ul_ran[0],ul_ran[1], .01)#.01
        else:
            x = np.arange(1, 10, .01)#.01
    try:
        solo=eval(graph_data)
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")

def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig=et.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    ta=texto_orig.replace("sin","np.sin")
    tb=ta.replace("cos","np.cos")
    tl=tb.replace("log","np.log")
    tc=tl.replace("tan","np.tan")
    tr=tc.replace("sqrt","np.sqrt")
    graph_data=tr

def guardar(e):
    global expresiones
    expresiones.append(e)
    print(expresiones)


ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)
button.pack(side=tkinter.BOTTOM)
et.pack(side=tkinter.BOTTOM)
#button = tkinter.Button(master=root, text="VER EJES", command=marca_ejes)
#button.pack(side=tkinter.LEFT)

ets=tkinter.Entry(master=root,width=10)
ets.pack(side=tkinter.RIGHT)
label = tkinter.Label(master = root, text = "RANGO DE 'X'")
label.pack(side = tkinter.RIGHT)
button = tkinter.Button(master=root, text="GUARDAR FUNCIÓN", bg="gray69", command=lambda:guardar(et.get()))
button.place(x=1, y=1)
var=tkinter.StringVar()
var.set(expresiones[0])
guardado=tkinter.OptionMenu(root, var, *expresiones)
guardado.pack(side=tkinter.LEFT)
#sti=var.get()

tkinter.mainloop()
#label = tkinter.Label(master = root, text = "RANGO PARA 'X'")
#label.pack(side = tkinter.RIGHT)
