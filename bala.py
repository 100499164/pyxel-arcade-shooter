import config

#La clase bala cuenta con atributos simples para ser utilizada como herencia en las balas del jugador principal y el jugador enemigo
#Cada vez que una bala es creada esta se añade a la lista de balas
#También tiene el atributo is alive para verificar si esta sigue activa la bala

class Bala:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        config.balas.append(self)
        self.is_alive = True
        