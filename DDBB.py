
import mysql.connector
import tkinter
from tkinter import messagebox

import time
from time import sleep

#

class DDBB():

    def __init__(self):
        self.host = "127.0.0.1"
        self.user = "root"
        self.passwd = "123abc"
        #self.conexion = None
    
    def conectar(self):
        self.conexion = mysql.connector.connect(host=self.host, user=self.user, password=self.passwd)
        #self.cursor = self.conexion.cursor()

        if self.conexion.is_connected():
            print("conectado correctamente con la base de datos")
            messagebox.showinfo(message="conectado correctamente con la base de datos")
            

        self.crearDDBB()
        
    def desconectar(self):
        self.conexion.close()
        if not self.conexion.is_connected():
            print("Se ha desconectado la base de datos")
            messagebox.showinfo(message="Se ha desconectado la base de datos")

    def crearDDBB(self):
        self.cursor = self.conexion.cursor()
        self.cursor.execute("CREATE DATABASE IF NOT EXISTS hilos")
        self.cursor.execute("USE hilos")
        self.cursor.execute("CREATE TABLE IF NOT EXISTS Alumnos("+
            "dni VARCHAR(9) PRIMARY KEY,"+
            "nombre VARCHAR(25),"+
            "apellido1 VARCHAR(25),"+
            "apellido2 VARCHAR(25),"+
            "direccion VARCHAR(25),"+
            "telefono VARCHAR(9) "+
            ")ENGINE=InnoDB")
        
        self.cargarDatos()
        
        #self.cursor.close()

    def cargarDatos(self):
        #self.cursor = self.conexion.cursor() `

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000001', 'Jorge', 'Carmona', 'Carreño', 'C/Mortadela', '658394853')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000002', 'Manu', 'Gaga', 'Gonzalez', 'C/Lechuga', '685947564')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000003', 'Alex', 'Fernandez', 'Haro', 'C/Espinaca', '583495040')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000004', 'Luis Alberto', 'Maquina', 'Virtual', 'C/Divas', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000005', 'Miguel', 'Santos', 'Martin', 'C/Datos accesibles', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000006', 'Mario', 'Sutil', 'Rebollo', 'C/Interfaces', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000007', 'Maria', 'Ruiz', 'Laguapa', 'C/Bombon', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000008', 'Jose Julio', 'Landazuri', 'Elcrack', 'C/Joseju', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000009', 'Paula', 'Detodos', 'Losantos', 'C/Paulipaula', '863045303')")

        self.cursor.execute("INSERT INTO hilos.Alumnos (dni, nombre, apellido1, apellido2, direccion, telefono) "+
        "VALUES ('000000010', 'Bill', 'El', 'Botas', 'C/Ucrania', '863045303')")

        self.conexion.commit()

    def mostrarAlumnos(self, st):
        self.cursor.execute("SELECT * FROM hilos.Alumnos")
        st.delete("1.0", tkinter.END)
        fetchAll = self.cursor.fetchall()

        #st.insert(tkinter.INSERT, fetchAll)
        #print(fetchAll)
        
        #print("Total rows are:  ", len(fetchAll))
        
        for fila in fetchAll:
            st.insert(tkinter.INSERT, ("DNI: "+ fila[0] +"\n") )
            st.insert(tkinter.INSERT, ("Nombre: "+ fila[1] +"\n") )
            st.insert(tkinter.INSERT, ("Apellido1: "+ fila[2] +"\n") )
            st.insert(tkinter.INSERT, ("Apellido2: "+ fila[3] +"\n") )
            st.insert(tkinter.INSERT, ("Dirección: "+ fila[4] +"\n") )
            st.insert(tkinter.INSERT, ("Teléfono: "+ fila[5] +"\n") )
            st.insert(tkinter.INSERT, "\n\n")
            '''
            print("DNI: ", fila[0])
            print("Nombre: ", fila[1])
            print("Apellido1: ", fila[2])
            print("Apellido2: ", fila[3])
            print("Dirección: ", fila[4])
            print("Teléfono: ", fila[5])
            print("\n")
            '''

    def bonanitDDBB(self):
        self.cursor.execute("DROP SCHEMA IF EXISTS hilos")
        print("Se ha eliminado la base de datos")
        print(self.cursor.fetchall())

    def hacerConsulta(self, consulta, st):
        #self.cursor.execute("SHOW DATABASES")
        #self.cursor.execute("USE hilos")
        self.cursor.execute(consulta)
        st.delete("1.0", tkinter.END)
        fetchAll = self.cursor.fetchall()
        st.insert(tkinter.INSERT, fetchAll)
        print(fetchAll)
        self.conexion.commit()
        
        
        