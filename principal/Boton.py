import pygame
import random
import string
from Estructura.Tanque import *

class Boton(pygame.sprite.Sprite):

    def __init__(self, imagen, imagen1 , x, y):
        super(Boton, Boton).__init__(self)
        self.normal = imagen
        self.seleccion = imagen1
        self.actual = self.normal
        self.rect = self.actual.get_rect()
        self.rect.left , self.rect.top = (x,y)
        self.x = x
        self.y = y

    def update(self, vetana , cursor , agregar):
        if cursor.colliderect(self.rect):
            self.actual = self.seleccion
        else:
            self.actual = self.normal
        vetana.blit(self.actual , self.rect)
        vetana.blit(agregar ,(self.x,self.y + 30))

    def agregar(self , grafo1):
        if self is not grafo1:
            grafo = grafo1
            dato = "Barrio " + random.choice(string.ascii_letters)
            pas = False
            i = 0
            x = random.randint(250, 1300)
            y = random.randint(60, 670)
            if len(grafo.nodos) > 0 :
                while i in range(len(grafo.nodos)):
                    if len(grafo.nodos) == 40:
                        print("No se pueden añadir mas nodos")
                        break
                    else:
                        if dato != grafo.nodos[i].dato:
                            if pas is not True:
                                pas = True
                            if i == len(grafo.nodos) -1 :
                                while self.sobrepos(x,y, grafo):
                                    x = random.randint(250,1300)
                                    y = random.randint(60,670)
                        else:
                            dato = "Barrio "+ random.choice(string.ascii_letters)
                            i = -1
                            if pas is not False:
                                pas = False
                    i += 1

            else:
                tanq = None
                if randint(0,1) == 1:
                    tanq = Tanque(randint(1, 200))
                grafo.agregar(dato,[],x,y,tanq)
            if pas is True:
                tanq = None
                if randint(0, 1) == 1:
                    tanq = Tanque(randint(1, 200))
                grafo.agregar(dato,[],x,y , tanq)
                n = random.randint(0 , len(grafo.nodos) -1)
                while pas:
                    if grafo.nodos[n].dato != dato:
                          pas = False
                    else:
                        n = random.randint(0, len(grafo.nodos)-1)
                grafo.agregarArista(grafo.buscarNodo(dato),grafo.buscarNodo(grafo.nodos[n].dato), random.randint(1,50))
            return  grafo

    def sobrepos(self,x,y,grafo):
        if self is not grafo:
            for nd in grafo.nodos:
                if nd.x >= x + 100 and nd.y >= - 100:
                    if nd.x <= + 100 and nd.y <= +100:
                        return True
            return False