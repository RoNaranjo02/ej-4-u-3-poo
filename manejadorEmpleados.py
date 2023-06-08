import csv
import numpy as np
from claseEmpladoExterno import EmpleadoExterno as EE
from claseEmpleadoContratado import EmpleadoContratado as EC
from claseEmpleadoPlanta import EmpleadoPlanta as EP

class controlEmpleados:
    def __init__(self, dimension = 0):
        self.__dimension = dimension
        self.__arregloEmpleados = np.empty((dimension), dtype= object)

    def setDimension(self, dim):
        self.__dimension = dim
        self.__arregloEmpleados = np.empty((dim), dtype= object)


    def cargarLista(self):
        dim = int(input("Ingrese la cantidad de empleados (9): "))
        self.setDimension(dim)
        indice = 0
        indice = self.cargarPlanta(indice)
        indice = self.cargarContratado(indice)
        indice = self.cargarExterno(indice)


    def cargarPlanta(self, indice):
        archivo = open('planta.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                dni = str(fila[0])
                nom = str(fila[1])
                dir = str(fila[2])
                tel = str(fila[3])
                sbasico = int(fila[4])
                antiguedad = int(fila[5])
                instancia = EP(dni,nom,dir,tel,sbasico,antiguedad)
                self.__arregloEmpleados[indice] = instancia
                indice += 1
        archivo.close
        return indice

    def cargarContratado(self, indice):
        archivo = open('contratados.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                dni = str(fila[0])
                nom = str(fila[1])
                dir = str(fila[2])
                tel = str(fila[3])
                fechai = str(fila[4])
                fechaf = str(fila[5])
                horas = int(fila[6])
                instancia = EC(dni,nom,dir,tel,fechai,fechaf,horas)
                self.__arregloEmpleados[indice] = instancia
                indice += 1
        archivo.close
        return indice
    

    def cargarExterno(self, indice):
        archivo = open('externos.csv')
        reader = csv.reader(archivo, delimiter = ';')
        cabecera = True
        for fila in reader:
            if cabecera:
                cabecera = False
            else:
                dni = str(fila[0])
                nom = str(fila[1])
                dir = str(fila[2])
                tel = str(fila[3])
                tarea = str(fila[4])
                fechai = str(fila[5])
                fechaf = str(fila[6])
                montovia = int(fila[7])
                costo = int(fila[8])
                montoseg = int(fila[9])
                instancia = EE(dni,nom,dir,tel,tarea, fechai,fechaf, montovia, costo, montoseg)
                self.__arregloEmpleados[indice] = instancia
                indice += 1
        archivo.close
        return indice
    
    def mostrarEmpleados(self):
        for empleado in self.__arregloEmpleados:
            print("\n")
            print(empleado)
    
    def buscarDNI(self, ingdni):
        i = 0
        while (i < self.__dimension) and (self.__arregloEmpleados[i].getDni() != ingdni):
            i += 1

        if i == self.__dimension:
            i = None
    
        return i
        
    def registrarHoras(self, pos, inghoras):
        print("Horas trabajadas antes del registro: {}".format(self.__arregloEmpleados[pos].getCantidadHoras()))
        self.__arregloEmpleados[pos].modificarHoras(inghoras)
        print("Nueva cantidad de horas registrada: {}".format(self.__arregloEmpleados[pos].getCantidadHoras()))


    def totalTarea(self, ingtarea, fechaActual):
        montoTot = 0
        for empleado in self.__arregloEmpleados:
            if isinstance(empleado, EE) and empleado.getTarea() == ingtarea and empleado.getFechaFinalizacion() > fechaActual:
                montoTot += empleado.calcularSueldo()
        print("El monto total a pagar para la tarea {} es: {}".format(ingtarea, montoTot))

    def ayudaEconomica(self):
        print("La empresa le otorgara una ayuda economica a los siguientes empleados: ")
        for empleado in self.__arregloEmpleados:
            if empleado.calcularSueldo() < 150000:
                print("{}\t{}\t{}".format(empleado.getNombre(), empleado.getDireccion(), empleado.getDni()))

    def calcularSueldo(self):
        print("Nombre\t\t\tTelefono\t\tSueldo")
        for empleado in self.__arregloEmpleados:
            print("{}\t\t{}\t\t{}".format(empleado.getNombre(), empleado.getTelefono(), empleado.calcularSueldo()))