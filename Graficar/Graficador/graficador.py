#!/usr/bin/env python
# -*- coding: utf-8 -*-
import tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg #NavigationToolbar2Tk
from matplotlib import style
import matplotlib.animation as animation
import matplotlib.pyplot as plt
import numpy as np
from tkinter import messagebox
from math import *

root = tkinter.Tk()
root.wm_title("Graficador")
ta=root.geometry("1000x700")

style.use('fivethirtyeight')#'

fig = Figure()
ax1 = fig.add_subplot(111)

canvas = FigureCanvasTkAgg(fig, master=root)  # CREAR AREA DE DIBUJO DE TKINTER.
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#toolbar = NavigationToolbar2Tk(canvas, root)# barra de iconos
#toolbar.update()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
act_rango=False
ul_ran=""
ran=""

funciones={"sin":"np.sin","cos":"np.cos","tan":"np.tan","log":"np.log",
           "pi":"np.pi","sqrt":"np.sqrt"}

def reemplazo(s):
    for i in funciones:
        if i in s:
            s=s.replace(i, funciones[i])
    return s
    
def animate(i):
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
            act_rango=False
            ets.delete(0,len(ets.get()))
    else:
        if ul_ran!="":
            x = np.arange(ul_ran[0],ul_ran[1], .01)#.01
        else:
            x = np.arange(1, 10, .01)#.01
    try:
        solo=eval(graph_data)
        #print(graph_data)
        ax1.clear()
        ax1.plot(x,solo)
    except:
        ax1.plot()
    ax1.axhline(0, color="gray")
    ax1.axvline(0, color="gray")
    ani.event_source.stop()

def represent():
    global graph_data
    global ran
    global act_rango
    texto_orig=et.get()
    if ets.get()!="":
        rann=ets.get()
        ran=rann.split(",")
        act_rango=True
    graph_data=reemplazo(texto_orig)
    ani.event_source.start()

ani = animation.FuncAnimation(fig, animate, interval=1000)
plt.show()

#ENTRADA FUNCION
et = tkinter.Entry(master=root,width=60)
et.config(bg="gray87", justify="left")
#ENTRADA RANGO
ets=tkinter.Entry(master=root,width=10)
#ETIQUETA RANGO
label = tkinter.Label(master = root, text = "RANGO DE 'X'")
#BOTÓN "SET"
button = tkinter.Button(master=root, text="SET", bg="gray69", command=represent)

#UBICACIÓN ELEMENTOS.
button.pack(side=tkinter.BOTTOM)
et.pack(side=tkinter.BOTTOM)
ets.pack(side=tkinter.RIGHT)
label.pack(side = tkinter.RIGHT)

tkinter.mainloop()
