from principal import gui
from random import randint
from principal.gui import *
from Estructura.Grafo import *
from Estructura.Queue import *
from Estructura.Tanque import *
import json

import threading

class Main:
    if __name__ == '__main__':
        grafo = Grafo()

        with open('p.json') as f:
            data = json.load(f)
        for Ciudadades in data['Ciudad']:
            for n in Ciudadades:
                posx = Ciudadades['Posx']
                posy = Ciudadades['Posy']
                tanque = Ciudadades['Tanque']
                nombre = Ciudadades['Nombre']
                for c in Ciudadades:
                    tanq = None
                    if tanque == 1:
                        tanq = Tanque(randint(1,200))
                    grafo.agregar(Ciudadades['Nombre'], [],  posx , posy , tanq)
                for n in Ciudadades:
                    grafo.agregarAristas(Ciudadades['Nombre'],"Estrella",randint(1, 50))
                    grafo.agregarAristas(Ciudadades['Nombre'],"Palermo",randint(1, 5))

        ventana = Gui(grafo)

