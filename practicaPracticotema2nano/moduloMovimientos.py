
class Movimientos:
    
    __numCM : int
    __fecha : str
    __descripcion : str
    __tipoM:str
    __importe : float
    
    
    def __init__(self,numCM,fecha,descripcion,tipoM,importe):
        
        self.__numCM = numCM
        self.__fecha = fecha
        self.__descripcion = descripcion
        self.__tipoM = tipoM
        self.__importe = importe

    
    def __str__(self):
        
        return "%s %s %s %s %s" % (self.__numCM,self.__fecha,self.__descripcion,self.__tipoM,self.__importe)

    def getnumCM(self):
        
        return self.__numCM
    
    def getfecha(self):
        
        return self.__fecha
    
    def getdescripcion(self):
        
        return self.__descripcion
    
    def gettipoM(self):
        
        return self.__tipoM
    
    def getimporte(self):
        
        return self.__importe
    
