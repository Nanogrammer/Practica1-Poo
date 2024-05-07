import csv
from moduloClientes import Clientes


class GestorCliente:
     
    __listaC : list
    
    
    def __init__(self):  
        self.__listaC = []
        
    def agregarClientes(self,newCliente):
        self.__listaC.append(newCliente)
        
    def cargarGC(self):
        with open("ClientesAbril2024.csv", mode="r", newline="", encoding="UTF-8") as file:
            reader = csv.reader(file, delimiter=";")
            next(reader)
            for row in reader: 
                newcliente = Clientes(row[0], row[1],row[2] ,row[3], row[4])
                self.agregarClientes(newcliente)
            file.close()
        
    
    def mostrarGC(self):
        for i in range (len(self.__listaC)):
            print(self.__listaC[i])
            
    def buscardni(self,dni,instanciaGM):
        i=0
        while i < len(self.__listaC) and dni != self.__listaC[i].getdni():
            i=i+1
        if dni == self.__listaC[i].getdni():
            print("DATOS ACTUALES\n")
            print(f"Numero de cuenta: {self.__listaC[i].getnumCC()}\tNombre:{self.__listaC[i].getnombre()}\tApellido:{self.__listaC[i].getapellido()}\tDNI:{self.__listaC[i].getdni()} \tSaldo Anterior:{self.__listaC[i].getsaldo()}")
           
            r = instanciaGM.buscarMovimientos(self.__listaC[i].getnumCC(),self.__listaC[i].getsaldo())
            if r == float(self.__listaC[i].getsaldo()):
                print("------------El cliente no tuvo movimientos en Abril--------------") 
            elif r!=self.__listaC[i].getsaldo():
                print("\n -------------El cliente tuvo movimientos en abril-------------")
                x = input("desea actualizar el saldo? '1' para si y '0' para no")
                if x == "1":
                    self.__listaC[i].setsaldo((r))
                    print("SALDO ACTUALIZADO:\n")
                    print(f"Numero de cuenta: {self.__listaC[i].getnumCC()}\tNombre:{self.__listaC[i].getnombre()}\tApellido:{self.__listaC[i].getapellido()}\tDNI:{self.__listaC[i].getdni()} \tSaldo Nuevo:{self.__listaC[i].getsaldo()}")
                elif x == "0":
                    print("hasta luego")

    def __lt__(self,otro):
    
        return self.__listaC[0].getnumCC() > otro.__listaC[0].getnumCC()
          

    def ordenarListclientes(self):
        self.__listaC.sort(key=lambda cliente: cliente.getnumCC())
        