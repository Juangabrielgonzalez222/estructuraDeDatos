import numpy as np
class Pila:
    __items=None
    __tope=0
    __cantidad=0
    def __init__(self,cantidad=0):
        self.__cantidad=cantidad
        self.__items=np.empty(cantidad)
        self.__tope=-1
    def vacia(self):
        return self.__tope==-1
    def getValorTope(self):
        return self.__items[self.__tope]
    def insertar(self,x):
        resultado=0
        if self.__tope<self.__cantidad-1:
            self.__tope+=1
            self.__items[self.__tope]=x
            resultado=x
        return resultado
    def suprimir(self):
        x=-1
        if self.vacia():
            print('Pila vacia.')
        else:
            x=self.__items[self.__tope]
            self.__tope-=1
        return x
    def mostrar(self):
        if self.vacia():
            print('Pila Vacia')
        else:
            for i in range(self.__tope,-1,-1):
                print(self.__items[i])
