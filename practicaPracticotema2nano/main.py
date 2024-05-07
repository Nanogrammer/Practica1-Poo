from moduloGestorMovimientos import GestorMovimientos
from moduloGestorClientes import GestorCliente
import Menu


if __name__ == "__main__":


    instanciaGM = GestorMovimientos()
    instanciaGC = GestorCliente()

    instanciaGM.cargarGestorM()
    instanciaGC.cargarGC()
    # # instanciaGM.mostrarGestorM()
    # # instanciaGC.mostrarGC()

    op = 0
    while op != "5":
        op = Menu.menu()
        if op == "1":
            dni = input("ingrese DNI del cliente\n")
            instanciaGC.buscardni(dni,instanciaGM)
            
        elif op =="2": 
            dni = input("ingrese DNI del cliente\n")
            instanciaGC.buscardni(dni,instanciaGM)

        elif op == "4":
            print("clientes sin ordenar\n")
            instanciaGC.mostrarGC()
            instanciaGC.ordenarListclientes()
            print("clientes ordenados\n") 
            instanciaGC.mostrarGC()

        
        elif op == "3":
            print("movimientos sin ordenar\n")
            instanciaGM.mostrarGestorM()
            instanciaGM.ordenarMovimientos()
            print("movimientos ordenados\n")
            instanciaGM.mostrarGestorM()

        elif op == "5":
            print("SALIENDO")
        else:
            print("ingrese un numero valido")
            op = Menu.menu()
        