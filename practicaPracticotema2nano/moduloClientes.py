class Clientes: 
    
    __nombre:str
    __apellido:str
    __dni : int
    __numCC: int
    __saldoAnterior:float
    
    
    def __init__(self,nombre,apellido,dni,numCC,saldoAnterior):
        
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni
        self.__numCC = numCC
        self.__saldoAnterior = saldoAnterior

    
    
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__nombre,self.__apellido,self.__dni,self.__numCC,self.__saldoAnterior)

    def getnombre(self):
        
        return self.__nombre
    
    def getapellido(self):
        
        return self.__apellido
    
    def getdni(self):
        
        return self.__dni
    
    def getnumCC(self):
        
        return self.__numCC
    
    def getsaldo(self):
        
        return self.__saldoAnterior
        
    def setsaldo(self,r):
        
        self.__saldoAnterior = r

