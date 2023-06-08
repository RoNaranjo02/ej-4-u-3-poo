from menu import MenuOpciones
from manejadorEmpleados import controlEmpleados

def test():
    listaemp = controlEmpleados()
    listaemp.cargarLista()
    #listaemp.mostrarEmpleados()
    menu = MenuOpciones()
    menu.opciones(listaemp)


if __name__ == "__main__":
    test()