from avion import Avion
import config

#La clase Enemigo tiene herencia de la clase Avión añadiendo el método que hace que se añada a lista de enemimos. 
#El is dead para no incluir dos veces el mismo enemigo en la lista que se encarga de las animaciones de muerte.
class Enemigo(Avion):
    def __init__(self, x, y):
        super().__init__(x, y)
        config.enemigos.append(self)
        self.is_dead = False
    