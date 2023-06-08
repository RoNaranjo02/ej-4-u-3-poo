from claseEmpleado import Empleado

class EmpleadoPlanta(Empleado):
    __sueldoBasico : int
    __antiguedad : int

    def __init__(self, dni='', nombre='', direccion='', telefono='', sueldo = 0, antiguedad = 0):
        super().__init__(dni, nombre, direccion, telefono)
        self.__sueldoBasico = sueldo
        self.__antiguedad = antiguedad

    def getSueldo(self):
        return self.__sueldoBasico
    
    def getAntiguedad(self):
        return self.__antiguedad
    
    def calcularSueldo(self):
        return self.__sueldoBasico + ((self.__sueldoBasico * 1/100) * self.__antiguedad)
    
    def __str__(self):
        return super().__str__() + "\nSueldo: $"+ str(self.__sueldoBasico) + "  Antiguedad: " + str(self.__antiguedad)