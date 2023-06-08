from claseEmpleado import Empleado

class EmpleadoContratado(Empleado):
    __fechaInicio : str
    __fechaFinal : str
    __cantidadHoras : int
    __valorporhora = 100

    def __init__(self, dni='', nombre='', direccion='', telefono='', fechain = '', fechafin = '', horas = 0):
        super().__init__(dni, nombre, direccion, telefono)
        self.__fechaInicio = fechain
        self.__fechaFinal = fechafin
        self.__cantidadHoras = horas

    def getFechaInicio(self):
        return self.__fechaInicio
    
    def getFechaFinal(self):
        return self.__fechaFinal
    
    def getCantidadHoras(self):
        return self.__cantidadHoras
    
    def getValorHora(self):
        return self.__valorporhora
    
    def calcularSueldo(self):
        return self.__cantidadHoras * self.__valorporhora
    
    def __str__(self):
        return super().__str__() + " " + self.__fechaInicio + " " + self.__fechaFinal + "\n Cantidad de horas: " + str(self.__cantidadHoras)
    
    def modificarHoras(self, horas):
        self.__cantidadHoras += horas