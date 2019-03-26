class Queue:
    def __init__(self):
        self.items = []

    def estaVacia(self):
        return self.items == []

    def encolar(self, x):
        """ Agrega el elemento x como último de la cola. """
        self.items.append(x)

    def desencolar(self):
        """ Elimina el primer elemento de la cola y devuelve su
            valor. Si la cola está vacía, levanta ValueError. """
        try:
            return self.items.pop(0)
        except:
            raise ValueError("La cola está vacía")

    def tamano(self):
        return len(self.items)
