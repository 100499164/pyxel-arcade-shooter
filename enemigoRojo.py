import config
from enemigo import Enemigo
from balaEnemigo import BalaEnemigo
import random

#Al igual que el resto de Enemigos utilizamos herencia
class EnemigoRojo(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        #Este atributo define el sprite de la lista
        self.sprite = config.sprites_eRoj[0]
        #Estos dos atributos definen el banco en el que se encuentran los sprites de muerte y de giro
        self.sprite_location = 0
        self.sprite_locationM = 0
        #Estos atributos son las vidas y los diferentes contadores para la gestión de los cambios de sprites
        self.vidas = 1
        self.contador = 0
        self.contadorsprite = 15
        #Estos atributos son los que verifican si el avión está en un giro y si ha realizado los dos giros necesarios
        self.girando = False
        self.giro1 = True
        self.giro2 = True
        #Atributos para el funcionamiento del dispano y gestión del momento de este
        self.cargada = random.randint(0,1)
        self.disparo = True
        self.momento_disparo = random.randint (50, 150)
        #Diferentes contadores para la gestión de sprites de la muerte y los puntos
        self.contadormuerte = 0
        self.contadormuertesprite = 0
        self.puntos = 100

#Este avión tiene 2 estados, girando o no
    def move(self):
        #Si no está girando avanza en dirección +x
        if not self.girando:
            self.x += 3
        #Cuando llega a este limite realiza el giro
        if self.x >= 50 and self.giro1 == True:
            self.girando = True
            self.giro1 = False
        #Cuando llega a este limite realiza el giro
        if self.x >= 150 and self.giro2 == True:
            self.girando = True
            self.giro2 = False
        #Esto es la consecución de instrucciones encargadas del giro
        if self.girando == True:
            if self.contador < 28:
                if self.contador % 2 == 0 and self.contador != 0:
                    self.contadorsprite -= 1
                if self.contador < 6:
                    self.y += 2
                    self.x += 2
                elif self.contador < 8:
                    self.y += 2
                    self.x += 0
                elif self.contador < 14:
                    self.y += 2
                    self.x += -2
                elif self.contador < 16:
                    self.y += 0
                    self.x += -2
                elif self.contador < 22:
                    self.y += -2
                    self.x += -2
                elif self.contador < 24:
                    self.y += -2
                    self.x += 0
                elif self.contador < 28:
                    self.y += -2
                    self.x += 2
                self.sprite = config.sprites_eRoj[self.contadorsprite]
                self.contador += 0.5

            #Al finalizar el giro se restablece los contadores al momento inicial
            else:
                self.girando = False
                self.sprite = config.sprites_eRoj[0]
                self.contadorsprite = 15
                self.contador = 0

    #El método disparo solo se da si el enemigo está vivo y si este avión cuenta con munición
    def shoot(self, x, y):
        if self.is_alive == True:
            if self.cargada == 0 and self.disparo == True and self.x >= self.momento_disparo:
                BalaEnemigo(self.x,self.y, x, y)
                self.disparo = False

    #El método muerte muestra la animacion de muerte del enemigo, además antes de terminar elina al enemigo de la lista en la que se encontraba y suba los puntos al jugador.
    #Utilizamos contadores para su correcta implementación
    def muerte(self):
        if self.contadormuerte < 12: 
            if self.contadormuerte % 2 == 0 and self.contadormuerte != 0:
                self.contadormuertesprite += 1
            self.sprite = config.sprites_explosion_eReg[self.contadormuertesprite]
            self.contadormuerte += 1
        else:
            config.enemigosMuertos.remove(self)
            config.pts += self.puntos 


