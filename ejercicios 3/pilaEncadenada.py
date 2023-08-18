class Nodo:
    __item=None
    __siguiente=None
    def __init__(self):
        self.__item=None
        self.__siguiente=None
    def obtenerItem(self):
        return self.__item
    def obtenerSiguiente(self):
        return self.__siguiente
    def cargarItem(self,x):
        self.__item=x
    def cargarSiguiente(self,siguiente):
        self.__siguiente=siguiente

class PilaEncadenada:
    __tope=None
    __cantidad=0
    def __init__(self):
        self.__tope=None
        self.__cantidad=0
    def vacia(self):
        return self.__cantidad==0
    def insertar(self,x):
        nodo=Nodo()
        nodo.cargarItem(x)
        nodo.cargarSiguiente(self.__tope)
        self.__tope=nodo
        self.__cantidad+=1
        return nodo
    def suprimir(self):
        x=0
        if self.vacia():
            print('Pila vacia.')
        else:
            x=self.__tope.obtenerItem()
            self.__tope=self.__tope.obtenerSiguiente()
            self.__cantidad-=1
        return x
    def mostrar(self):
        if self.vacia():
            print('Pila Vacia')
        else:
            aux=self.__tope
            while aux!=None:
                print(aux.obtenerItem())
                aux=aux.obtenerSiguiente()

if __name__=='__main__':
    p=PilaEncadenada()
    p.insertar(22)
    p.insertar(20)
    p.mostrar()