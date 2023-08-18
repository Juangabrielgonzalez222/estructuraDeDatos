from pila import Pila
class Factorial:
    __numero=0
    __pila=None
    def __init__(self,numero=0,tamaño=10):
        self.__numero=numero
        self.__pila=Pila(tamaño)
    def cargarNumerosFactorial(self):
        numero=self.__numero
        while numero>0:
            self.__pila.insertar(numero)
            numero-=1
    def calcularFactorial(self):
        self.cargarNumerosFactorial()
        factorial=1
        valorPila=1
        while valorPila!=-1:
            factorial*=valorPila
            valorPila=self.__pila.suprimir()
        print(factorial)

if __name__=='__main__':
    f=Factorial(8)
    f.calcularFactorial()