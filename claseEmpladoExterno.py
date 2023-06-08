from claseEmpleado import Empleado

class EmpleadoExterno(Empleado):
        __tarea : str 
        __fechainicio : str
        __fechafinalizacion : str
        __montoviatico : int
        __costoobra : int
        __montosegurovida : int

        def __init__(self, dni='', nombre='', direccion='', telefono='',tarea = '', fechaI = '', fechaF = '', montovi = 0, costo = 0, montoseguro = 0):
            super().__init__(dni, nombre, direccion, telefono)
            self.__tarea = tarea 
            self.__fechainicio = fechaI
            self.__fechafinalizacion = fechaF
            self.__montoviatico = montovi
            self.__costoobra = costo
            self.__montosegurovida = montoseguro                

        def getTarea(self):
            return self.__tarea
        
        def getFechaInicio(self):
            return self.__fechainicio
        
        def getFechaFinalizacion(self):
            return self.__fechafinalizacion
        
        def getMontoViatico(self):
            return self.__montoviatico
        
        def getCostoObra(self):
            return self.__costoobra
        
        def getMontoSeguro(self):
            return self.__montosegurovida
        
        def calcularSueldo(self):
            return self.__costoobra - self.__montoviatico - self.__montosegurovida
        
        def __str__(self):
            return super().__str__() + " " + self.__tarea + " " + self.__fechafinalizacion + "\nmonto viatico: $" + str(self.__montoviatico) + "\t costo de obra: $" + str(self.__costoobra) + "\tseguro: $" + str(self.__montosegurovida)