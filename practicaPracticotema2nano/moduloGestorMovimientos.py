
import csv
import numpy as np
import moduloMovimientos 


class GestorMovimientos:

    __listaM : np.array

    def __init__(self):
        self.__listaM = np.array([])

    def agregar(self, newmovimiento):
        self.__listaM = np.append(self.__listaM, newmovimiento)

    def cargarGestorM(self):
        with open("MovimientosAbril2024.csv",mode="r",newline="",encoding="UTF-8") as file:
            reader = csv.reader(file,delimiter=";")
            next(reader)
            for row in reader:
                Newmovimiento = moduloMovimientos.Movimientos(row[0],row[1],row[2],row[3],row[4])
                self.agregar(Newmovimiento)
            file.close()
        print("se cargo de Movimientos")

    def mostrarGestorM(self):
        for i in range (len(self.__listaM)):
            print(self.__listaM[i])

    def buscarMovimientos(self,numCC,saldoAnteriorC):
        i=0
        print(f"Movimientos del cliente con numero de cuenta {numCC}:")
        for i in range(len(self.__listaM)):
            if numCC == self.__listaM[i].getnumCM():
              
                print(f"FECHA: {self.__listaM[i].getfecha()}\t\t DESCRIPCION:{self.__listaM[i].getdescripcion()}\t\tTIPO:{self.__listaM[i].gettipoM()}\t\tImporte:{self.__listaM[i].getimporte()}")
                if self.__listaM[i].gettipoM() == "P":
                    saldoAnteriorC = float(saldoAnteriorC) + float(self.__listaM[i].getimporte())
                elif self.__listaM[i].gettipoM() == "C":
                    saldoAnteriorC = float(saldoAnteriorC) - float(self.__listaM[i].getimporte())
            i+=1   
        return float(saldoAnteriorC)

    def ordenarMovimientos(self):
        indicesOrd = np.argsort([movimiento.getnumCM() for movimiento in self.__listaM])
        self.__listaM = self.__listaM[indicesOrd]


    def __lt__(self,otro):
    
         return self.__listaM[0].getnumCM() > otro.listaM[0].getnumCM()
          

    # def __lt__(self, otro_punto):
        
    #   # Sobrecargar el metodo '<'
    #     puntos_gestor_actual = self.__listaM[0].getNroCuenta()
    #     puntos_otro_gestor = otro_punto.__listaM[0].getNroCuenta()
    #     return puntos_gestor_actual > puntos_otro_gestor
   
#estructura
    

# class puto:
#     __listaputo : np.array



#     def __init__(self):
#         self.__listaputo = np.array([])

#     def agregarPuto(self,unPuto):
#         self.__listaputo = np.append(self.__listaputo, unPuto)



