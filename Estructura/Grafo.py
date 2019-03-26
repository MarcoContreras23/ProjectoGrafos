from Estructura.Nodo import *
from Estructura.Arista import *
from Estructura.Queue import *


class Grafo:
    def __init__(self):
        self.nodos = []
        self.aristas = []

    def agregar(self, dato, adyacentes, x, y ,tanque):
        temp = []
        for i in adyacentes:
            nodoTemp = Nodo(i, [], x, y ,tanque)
            temp.append(nodoTemp)
        nodo = Nodo(dato, temp, x, y, tanque)
        self.nodos.append(nodo)

    def agregarArista(self, origen, destino, peso):
        arista = Arista(origen, destino, peso)
        aux =  Arista(destino, origen, peso)
        if arista in self.aristas or aux in self.aristas:
            return
        self.aristas.append(arista)
        origen.adyacentes.append(destino)
        origen.adyacentes.append(origen)


    def getNodo(self, identificador):
        for i in self.nodos:
            if i.dato == identificador:
                return i
        return None


    def contieneElemento(self, nodo, lista):
        for i in lista:
            if nodo.dato == i.dato:
                return True
        return False

    def buscarNodo(self, nombre):
        for i in self.nodos:
            if i.dato == nombre:
                return i

    def buscarArista(self, inicio, fin):
        for i in range(0, len(self.aristas)):
            if self.aristas[i].origen.dato == inicio and self.aristas[i].destino.dato == fin:
                return self.aristas[i]
        return None

    def verificarNodos(self, estructura, letra):
        for i in estructura:
            if i.dato == letra:
                return True
        return False

    def verificarAristas(self, estructura, letra, tipo):
        for i in estructura:
            if tipo == 1:
                if i.origen == letra:
                    return True
            if tipo == 2:
                if i.destino == letra:
                    return True
        return False

    def modificarAdyacencias(self, origen, destino, estructura):
        for i in range(0, len(estructura)):
            if estructura[i].dato == origen:
                nodo = self.getNodo(destino)
                nuevo = Nodo(destino, [], nodo.x, nodo.y)
                estructura[i].adyacentes.append(nuevo)

    def agregarAristas(self, origen, destino, peso):
        if self.verificarNodos(self.nodos, origen) and self.verificarNodos(self.nodos, destino):
            a = Arista(self.buscarNodo(origen), self.buscarNodo(destino), peso)
            if not self.verificarAristas(self.aristas, origen, 1) or self.verificarAristas(self.aristas, destino, 2):
                self.aristas.append(a)
                self.modificarAdyacencias(origen, destino, self.nodos)




