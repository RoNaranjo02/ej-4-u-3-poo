class MenuOpciones:
    __opcion : int
    
    def __init__(self):
        self.__opcion = 0

    def opciones(self, empleados):
        while self.__opcion != 5:
            print("---MENU DE OPCIONES---")
            print("1)- Registrar horas.")
            print("2)- Total de tarea")
            print("3)- Ayuda economica")
            print("4)- Calcular sueldo")
            print("5)- Salir")
            self.__opcion = int(input("Ingrese una opcion "))
            
            if self.__opcion == 1:
                ingdni = str(input("Ingrese el DNI de una persona: "))
                pos = empleados.buscarDNI(ingdni)
                if pos != None:
                    inghoras = int(input("Ingrese la cantidad de horas trabajadas: "))
                    empleados.registrarHoras(pos, inghoras)
                else:
                    print("El DNI ingresado no se encontro ")
            
            elif self.__opcion == 2:
                ingtarea = str(input("Ingrese una tarea: "))
                fechaActual = str(input("Ingrese la fecha actual: "))
                empleados.totalTarea(ingtarea, fechaActual)

            elif self.__opcion == 3:
                empleados.ayudaEconomica()

            elif self.__opcion == 4:
                empleados.calcularSueldo()
            
            elif self.__opcion == 5:
                print("FIN")

            else:
                print("Opcion invalida, vuelva a ingresar una opcion ")
            

