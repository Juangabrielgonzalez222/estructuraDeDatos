from pila import Pila
class Conversor:
    __numero=0
    __pila=None
    def __init__(self,numero=0,tamañoBinario=8):
        self.__numero=numero
        self.__pila=Pila(tamañoBinario)
    def calcularBinario(self):
        aux=self.__numero
        aux2=0
        while aux>0:
            aux2=aux%2
            self.__pila.insertar(aux2)
            aux=int(aux/2)
    def mostrar(self):
        self.__pila.mostrar()

if __name__=='__main__':
    c=Conversor(8)
    c.calcularBinario()
    c.mostrar()