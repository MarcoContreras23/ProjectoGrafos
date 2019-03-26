class Nodo:
    def __init__(self, dato, adyacentes=[], x=0, y=0, tanque = None):
        self.dato = dato
        self.adyacentes = adyacentes
        self.visitado = False
        self.x = x
        self.y = y
        self.tanque = tanque
        self.line = None
