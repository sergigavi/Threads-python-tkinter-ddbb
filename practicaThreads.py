
from datetime import datetime
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter import *
import time
from time import sleep
from threading import Thread
from tkinter import simpledialog
from DDBB import *


class Procesos():

    def __init__(self):
        self.mainVentana = tk.Tk()
        self.cargarVentana()
        self.db = DDBB()
        self.db.conectar()
        self.generarHilo()
    
    def conectarDDBB(self):
        self.db.conectar()
        self.generarHilo()

    def generarHilo(self):

        self.hilo = Thread(target=self.mostrarTiempo) #, args=[datetime.now()]

        if self.con2==1:
            self.hilo.setDaemon(True)

        self.hilo.start()

    def mostrarTiempo(self): #, tiempoInicio      
        
        self.threadVivo.set("El hilo está activo")

        if self.con.get() == 0:
            self.tiempoRemaining.set("50")

            for i in range(int(self.tiempoRemaining.get())):#Espera x segundos y cierra la conexion
                time.sleep(1)
                self.tiempoRemaining.set(value=str(int(self.tiempoRemaining.get())-1))

            self.db.desconectar()
            self.threadVivo.set("el hilo NO está activo")

    def consultaSeleccion(self):
        conSelec = simpledialog.askstring("Consulta de seleccion", "Consulta:")
        self.db.hacerConsulta(conSelec, self.sT)
        

    def consultaInsercion(self):
        conSelec = simpledialog.askstring("Consulta de insercion", "Consulta:")
        self.db.hacerConsulta(conSelec, self.sT)

    def mostrarAlumnos(self):
        self.db.mostrarAlumnos(self.sT)
    
    def eliminarDDBB(self):
        self.db.bonanitDDBB()
        messagebox.showinfo(message="Se ha eliminado la base de datos")
    
    def cargarVentana(self):

        self.mainVentana.title("Practica hilos")
        self.mainVentana.geometry("600x350")

        ttk.Button(self.mainVentana, text="Reconectar DDBB: ", command=self.conectarDDBB).grid(row=0, column=0, padx=10, pady=10, sticky="W")
        
        self.con = tk.IntVar()
        ttk.Checkbutton(self.mainVentana, text="Control cierre", variable=self.con,onvalue=1, offvalue=0).grid(row=0, column=1, padx=10, pady=10, sticky="W")

        self.con2 = tk.IntVar()
        ttk.Checkbutton(self.mainVentana, text="Dependencia", variable=self.con2, onvalue=1, offvalue=0).grid(row=0, column=2, padx=10, pady=10, sticky="W")

        ttk.Button(self.mainVentana, text="Consulta seleccion: ", command=self.consultaSeleccion).grid(row=1, column=0, padx=10, pady=10, sticky="W")

        ttk.Button(self.mainVentana, text="Consulta insercion: ", command=self.consultaInsercion).grid(row=2, column=0, padx=10, pady=10, sticky="W")
        #Ejemplo para copiar y probar:
        #INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) VALUES ('000000011', 'NombreEjemplo', 'ApellidoEjemplo', 'Apellido2Ejemplo', 'C/Ejemplo', '111111111')

        self.threadVivo = tk.StringVar()
        self.threadVivo.set("El hilo está activo")
        ttk.Entry(self.mainVentana, textvariable=self.threadVivo, state="readonly").grid(row=1, column=1, padx=10, pady=10, sticky="W")

        self.tiempoRemaining = tk.StringVar()
        self.tiempoRemaining.set(value="Tiempo de la conexion")
        ttk.Entry(self.mainVentana, text="Segundos que quedan", textvariable=self.tiempoRemaining, state="readonly").grid(row=2, column=1, padx=10, pady=10, sticky="W")

        ttk.Button(self.mainVentana, text="Mostrar alumnos", command=self.mostrarAlumnos).grid(row=1, column=2, padx=10, pady=10, sticky="W")

        ttk.Button(self.mainVentana, text="Eliminar Base de datos", command=self.eliminarDDBB).grid(row=2, column=2, padx=10, pady=10, sticky="W")

        self.sT = scrolledtext.ScrolledText(self.mainVentana, wrap = tk.WORD, width = 80, height = 10, font = ("Times New Roman",11))
        self.sT.grid(column = 0,row= 3, pady = 10, columnspan=3, padx = 10)


#



ej = Procesos()



ej.mainVentana.mainloop()