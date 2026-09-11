import config
from enemigo import Enemigo
from balaEnemigo import BalaEnemigo
import random


class Bombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        self.vidas = 6
        self.sprite = config.sprites_bombardero[0]
        #Estos dos atributos hacen referencia a la localización del sprite en el banco de imágenes
        self.sprite_location = 2
        self.sprite_locationM = 1
        #Estos 4 atributos siguientes son para las animaciones de giro y de muerte del avión
        self.contador = 0
        self.contadorsprite = 0
        self.girando = False
        self.giro = True
        #Definimos dos atributos porque el bombardero dispara dos veces
        self.disparo1 = True
        self.disparo2 = True
        self.momento_disparo1 = random.randint(20,config.H_BOARD//2 -10)
        self.momento_disparo2 = random.randint(20,config.H_BOARD//2 -10)
        #Contadores para la animación de la muerte
        self.contadormuerte = 0
        self.contadormuertesprite = 0
        #Puntos que recibe el jugador al eliminarlo
        self.puntos = 300
        #Definir la dirección de giro dependiendo de donde aparezca
        if self.x <= (config.W_BOARD//2):
            self.lado = "izquierda"
            self.contadorsprite = 1
        else:
            self.lado = "derecha"
            self.contadorsprite = 15
    
    #El movimiento del bombardero tiene 2 estados, girando o no
    #Si no se encuentra girando el bombardero avanza siempre en dirección a la parte baja de la pantalla sin modificar la x en la que se encuentra
    def move(self):
        if not self.girando:
            self.y +=2

        if self.y >= (config.H_BOARD/2 - 10) and self.giro == True:
            self.girando = True
            self.giro = False
        
        #Giro que describe el bombardero dependiendo de el lado en el que se genere
        if self.girando == True:
            if self.lado == "izquierda":
                if self.contador < 38:
                    if self.contador % 2 == 0 and self.contador !=0 and self.contador != 8 and self.contador != 10 and self.contador != 28 and self.contador != 30:
                        self.contadorsprite += 1
                    if self.contador < 6:
                        self.y += 2
                        self.x += 2
                    elif self.contador < 12:
                        self.y += 0
                        self.x += 2
                    elif self.contador < 18:
                        self.y += -2
                        self.x += 2
                    elif self.contador < 20:
                        self.y += -2
                        self.x += 0
                    elif self.contador < 26:
                        self.y += -2
                        self.x += -2
                    elif self.contador < 32:
                        self.y += 0
                        self.x += -2
                    elif self.contador < 38:
                        self.y += 2
                        self.x += -2
            if self.lado == "derecha":
                if self.contador < 38:
                    if self.contador % 2 == 0 and self.contador !=0 and self.contador != 8 and self.contador != 10 and self.contador != 28 and self.contador != 30:
                        self.contadorsprite -= 1
                    if self.contador < 6:
                        self.y += 2
                        self.x += -2
                    elif self.contador < 12:
                        self.y += 0
                        self.x += -2
                    elif self.contador < 18:
                        self.y += -2
                        self.x += -2
                    elif self.contador < 20:
                        self.y += -2
                        self.x += 0
                    elif self.contador < 26:
                        self.y += -2
                        self.x += 2
                    elif self.contador < 32:
                        self.y += 0
                        self.x += 2
                    elif self.contador < 38:
                        self.y += 2
                        self.x += 2
            #Cambios de sprites del giro del bombardero y contadores para una duración correcta tanto del movimiento como del cambio de sprite
            self.sprite = config.sprites_bombardero[self.contadorsprite]
            self.contador += 0.5
            if self.contador >= 38:
                self.girando = False
                self.sprite = config.sprites_bombardero[0]

    #El método disparo el cual dispara 2 veces en posiciones distintas
    def shoot(self, x, y):
        if self.disparo1 == True and self.y > self.momento_disparo1:
            BalaEnemigo(self.x + 9,self.y + 12, x, y)
            self.disparo1 = False
        if self.disparo2 == True and self.y > self.momento_disparo2:
            BalaEnemigo(self.x + 9,self.y + 12, x, y)
            self.disparo2 = False

    #El método muerte muestra la animacion de muerte del enemigo, además antes de terminar elina al enemigo de la lista en la que se encontraba y suba los puntos al jugador.
    #Utilizamos contadores para su correcta implementación
    def muerte(self):
        if self.contadormuerte < 14: 
            if self.contadormuerte % 2 == 0 and self.contadormuerte != 0:
                self.contadormuertesprite += 1
            self.sprite = config.sprites_explosion_bomb[self.contadormuertesprite]
            self.contadormuerte += 1
        else:
            config.enemigosMuertos.remove(self)
            config.pts += self.puntos 

    
