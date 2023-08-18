from pila import Pila
class Juego:
    __pilas=None
    __nDiscos=0
    __gano=False
    def __init__(self,nDiscos=1):
        self.__nDiscos=nDiscos
        self.__pilas=[]
        for i in range(3):
            self.__pilas.append(Pila(nDiscos))
        for i in range(5,-1,-1):
            self.__pilas[0].insertar(i)
    def controlador(self):
        jugando=True
        while jugando:
            self.mostrar()
            print('Para mover ingrese el numero de la pila:')
            origen=int(input('Pila origen: '))
            destino=int(input('Pila destino: '))
            origen-=1
            destino-=1
            if not self.__pilas[origen].vacia() and (self.__pilas[destino].vacia() or self.__pilas[origen].getValorTope()<self.__pilas[destino].getValorTope()) :
                aux=self.__pilas[origen].suprimir()
                self.__pilas[destino].insertar(aux)
            print(self.__pilas[origen].getValorTope()<self.__pilas[destino].getValorTope(),self.__pilas[origen].getValorTope(),self.__pilas[destino].getValorTope())
    def mostrar(self):
        for i in range(3):
            print('Pila',i+1)
            self.__pilas[i].mostrar()
            print('-----')
j=Juego(5)
j.controlador()