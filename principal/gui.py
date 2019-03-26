import pygame, sys, threading
from pygame.locals import *
from .Boton import Boton
from .Cursor import Cursor
from random import randint
import os
from pygame import mouse
from math import sin, atan2, cos, hypot, degrees, pi
from pygame import Rect


pygame.init()
pygame.font.init()


class Gui:

    def __init__(self, grafo):
        self.grafo = grafo
        self.cursor = Cursor()
        self.x = 0
        self.y = 0
        self.obs = False
        self.conexion = False
        self.aux = []
        hilo = threading.Thread(self.hilo())
        hilo.start()

    def hilo(self):
        ventana = pygame.display.set_mode((1366, 768), pygame.RESIZABLE)
        pygame.display.set_caption("Proyecto")
        fuente = pygame.font.SysFont('Comic Sans MS', 15)

        os.environ["SDL_VIDEO_WINDOW_POS"] = "%i,%i" % (self.x,self.y)
        os.environ["SDL_VIDEO_CENTERED"] = "0"


        """Cargar las images"""
        barrio = pygame.image.load("..\\imagenes\\barrio.png")
        imagenboton = pygame.image.load("..\\imagenes\\boton.png")
        tanquefull = pygame.image.load("..\\imagenes\\tanquefull.png")
        tanquemitad = pygame.image.load("..\\imagenes\\tanquemitad.png")
        tanquepoco = pygame.image.load("..\\imagenes\\tanquepoco.png")
        cuartodetanque = pygame.image.load("..\\imagenes\\cuartodetanque.png")
        tanquevacio = pygame.image.load("..\\imagenes\\tanquevacio.png")
        """gotas = pygame.image.load("..\\imagenes\\gotas.png")"""
        hueco = pygame.image.load("..\\imagenes\\hueco.png")

        """Escala las imagenes"""
        barrio = pygame.transform.scale(barrio, (60, 40))
        imagenboton = pygame.transform.scale(imagenboton, (140, 75))
        imagen2 = pygame.transform.scale(imagenboton, (110, 90))
        tanquefull = pygame.transform.scale(tanquefull, (90, 80))
        tanquemitad = pygame.transform.scale(tanquemitad, (90, 80))
        tanquepoco = pygame.transform.scale(tanquepoco, (90, 80))
        cuartodetanque = pygame.transform.scale(cuartodetanque, (90, 80))
        tanquevacio = pygame.transform.scale(tanquevacio, (90, 80))
        hueco = pygame.transform.scale(hueco, (30, 30))
        """gotas = pygame.transform.scale(gotas, (20, 20))"""

        """Asignacion de botones"""
        boton = Boton(imagenboton, imagen2, 60, 60)
        botonAgg = Boton(imagenboton, imagen2, 60, 120)
        botonOb = Boton(imagenboton, imagen2, 60, 180)
        botonCambiar = Boton(imagenboton, imagen2, 60, 240)

        """Texto de botones"""
        agregar = fuente.render("Agregar barrio", True, (0, 0, 0))
        agregar2 = fuente.render("Agregar conexion", True, (0, 0, 0))
        agregar3 = fuente.render("Obstruccion", True, (0, 0, 0))
        agregar4 = fuente.render("Cambiar sentido", True, (0, 0, 0))

        """Dibujando el grafo y gestionando eventos"""
        while True:
            """pygame.display.flip()
            for donde se ejecutan los eventos"""
            for evento in pygame.event.get():

                if evento.type == pygame.MOUSEBUTTONDOWN:

                    if self.cursor.colliderect(boton.rect):
                        self.grafo = boton.agregar(self.grafo)

                    elif self.cursor.colliderect(botonAgg.rect):
                        self.conexion = True
                    elif self.conexion:

                        for nodo in self.grafo.nodos:

                            if nodo.line.x < pygame.mouse.get_pos()[0] < nodo.line.right and nodo.line.y < pygame.mouse.get_pos()[1] < nodo.line.bottom:
                                self.aux.append(nodo)
                                if len(self.aux) == 2:
                                    self.grafo.agregarArista(self.aux[0], self.aux[1], randint(1, 50))
                                    self.conexion = False
                                    self.aux = []
                                break

                    elif self.cursor.colliderect(botonOb.rect):
                        self.obs = True
                    elif self.obs:

                        for a in range(len(self.grafo.aristas)):
                            print(self.grafo.aristas[a].line)

                            if (self.grafo.aristas[a].line.x < pygame.mouse.get_pos()[0]
                                    < self.grafo.aristas[a].line.right and self.grafo.aristas[a].line.y
                                    < pygame.mouse.get_pos()[1] < self.grafo.aristas[a].line.bottom):
                                self.grafo.aristas[a].obs = True
                                break
                            self.obs = False

                    elif self.cursor.colliderect(botonCambiar.rect):
                        return

                if evento.type == QUIT:
                    pygame.quit()
                    sys.exit()

            ventana.fill((76, 145, 65))
            self.cursor.update()
            boton.update(ventana, self.cursor, agregar)
            botonAgg.update(ventana, self.cursor, agregar2)
            botonOb.update(ventana, self.cursor, agregar3)
            botonCambiar.update(ventana, self.cursor, agregar4)

            if self.grafo == None:

                print("Grafo vacío, no se puede dibujar")

            else:

                """for tubo in self.grafo.aristas:
                    desx = tubo.destino.x
                    orix = tubo.origen.x
                    desy = tubo.destino.y
                    oriy = tubo.origen.y
                    rads = atan2(desy - oriy, desx - orix)
                    rads %= 2 * pi

                    dirx = 1
                    diry = 1

                    if desx - orix < 0:
                        dirx = -1
                    if desy - oriy < 0:
                        diry = -1

                    tubo.rect.x += dirx
                    tubo.rect.y += diry"""

                for i in range(0, len(self.grafo.nodos)):

                    """grafica nodo"""
                    self.grafo.nodos[i].line = ventana.blit(barrio, (self.grafo.nodos[i].x - 30,
                                                                     self.grafo.nodos[i].y - 40))
                    texto = fuente.render(self.grafo.nodos[i].dato, True, (0, 0, 0))

                    """grafica tanques"""
                    if self.grafo.nodos[i].tanque is not None:
                        if self.grafo.nodos[i].tanque.capacidad == 0:
                            ventana.blit(tanquevacio, (self.grafo.nodos[i].x + 10, self.grafo.nodos[i].y - 80))
                        elif self.grafo.nodos[i].tanque.capacidad < 50:
                            ventana.blit(cuartodetanque, (self.grafo.nodos[i].x + 10, self.grafo.nodos[i].y - 80))
                        elif self.grafo.nodos[i].tanque.capacidad < 100:
                            ventana.blit(tanquemitad, (self.grafo.nodos[i].x + 10, self.grafo.nodos[i].y - 80))
                        elif self.grafo.nodos[i].tanque.capacidad < 150:
                            ventana.blit(tanquepoco, (self.grafo.nodos[i].x + 10, self.grafo.nodos[i].y - 80))
                        elif self.grafo.nodos[i].tanque.capacidad == 200:
                            ventana.blit(tanquefull, (self.grafo.nodos[i].x + 10, self.grafo.nodos[i].y - 80))

                    ventana.blit(texto, (self.grafo.nodos[i].x - 15, self.grafo.nodos[i].y + 10))

                """grafica las aristas"""
                for j in range(0, len(self.grafo.aristas)):

                    """texto1 = fuente.render(str(self.grafo.aristas[j].peso), True, (0, 0, 0))"""
                    pos = self.pos_peso(j)
                    self.grafo.aristas[j].line = (pygame.draw.line(ventana, (130, 130, 130),
                                                                   (self.grafo.aristas[j].origen.x,
                                                                    self.grafo.aristas[j].origen.y),
                                                                   (self.grafo.aristas[j].origen.x,
                                                                    self.grafo.aristas[j].destino.y), 10))
                    self.grafo.aristas[j].line = (pygame.draw.line(ventana, (130, 130, 130),
                                                                   (self.grafo.aristas[j].origen.x,
                                                                    self.grafo.aristas[j].destino.y),
                                                                   (self.grafo.aristas[j].destino.x,
                                                                    self.grafo.aristas[j].destino.y), 10))

                    if self.grafo.aristas[j].obs:
                        ventana.blit(hueco, (pos[0], pos[1]))

            pygame.display.update()

    def pos_peso(self, j):

                if self.grafo.aristas[j].origen.x < self.grafo.aristas[j].destino.x:
                    posx = self.grafo.aristas[j].origen.x + \
                           ((self.grafo.aristas[j].destino.x - self.grafo.aristas[j].origen.x) / 2)
                    tipo = 1
                else:
                    posx = self.grafo.aristas[j].destino.x + \
                           ((self.grafo.aristas[j].origen.x - self.grafo.aristas[j].destino.x) / 2)
                    tipo = 2
                if self.grafo.aristas[j].origen.y < self.grafo.aristas[j].destino.y:
                    posy = self.grafo.aristas[j].origen.y + \
                           ((self.grafo.aristas[j].destino.y - self.grafo.aristas[j].origen.y) / 2)
                    tipo2 = 1
                else:
                    posy = self.grafo.aristas[j].destino.y + \
                           ((self.grafo.aristas[j].origen.y - self.grafo.aristas[j].destino.y) / 2)
                    tipo2 = 2

                if (tipo is 1 and tipo2 is 1) or (tipo is 2 and tipo2 is 2):
                        posx += -13
                        posy += -20
                elif (tipo is 1 and tipo2 is 2) or (tipo is 2 and tipo2 is 1):
                        posx += -13
                        posy += -30
                pos = [posx, posy]

                return pos