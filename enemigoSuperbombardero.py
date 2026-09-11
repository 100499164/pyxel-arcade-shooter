import config
from enemigo import Enemigo
from balaEnemigo import BalaEnemigo
import random
from powerup import Powerup

#Al igual que el resto de Enemigos utilizamos herencia
class Superbombardero(Enemigo):
    def __init__(self, x, y):
        super().__init__(x, y)
        #Este avión cuenta con 15 vidas
        self.vidas = 15
        #Aqui definimos el sprite inicial
        self.sprite = config.sprites_superbombardero[0]
        #Estos dos atributos definen el banco en el que se encuentran los sprites de muerte y de giro
        self.sprite_location = 1
        self.sprite_locationM = 1
        #Estos atributos son los diferentes contadores para la gestión de los cambios de sprites
        self.contador = 0
        self.contador2 = 0
        #Estos atributos son los diferentes contadores para la gestión de los disparon y los cambios de sprites de la muerte
        self.contadorShoot = 0
        self.contadormuerte = 1
        self.contadormuertesprite = 0
        #Atributos encargados del movimiento característico de superbonbardero
        self.movimiento = False
             #Este en concreto determina si ya ha realizado su movimiento
        self.movimientoRestante = True
        self.xMov = 0
        self.yMov = 0
        self.cambioMov = True
        #Puntuación recibida tras matar al enemigo
        self.puntos = 500

    def move(self):
        #El movimiento base del superbonbardero
        if not self.movimiento:
            self.y -= 2
        #Si alcanza esta posición realiza su movimiento siempre y cuando no se haya realizado todavía
        if self.y <= 50 and self.movimientoRestante == True:
            self.movimiento = True
            self.movimientoRestante = False
        #Cuando se activa el movimiento propio del surperbombardero, este efectua un giro aleatorio en un radio reducido en función del lado en el que este aparece
        if self.movimiento == True:
            if self.contador < 20:
                if self.cambioMov == True:
                    if self.x < 30:
                        self.xMov = 1
                    elif self.x > config.W_BOARD - config.sprites_superbombardero[0][3]-30:
                        self.xMov = -1
                    else:
                        self.xMov = random.randint(-1,1)
                    if self.y < 30:
                        self.yMov = 1
                    elif self.y > 70:
                        self.yMov = -1
                    else:
                        self.yMov = random.randint(-1,1)
                    while self.xMov == 0 and self.yMov == 0:
                        self.xMov = random.randint(-1,1)
                        self.yMov = random.randint(-1,1)
                    self.cambioMov = False
                if self.contador2 < random.randint(10,30):
                    self.x += self.xMov
                    self.y += self.yMov
                    self.contador2 += 1
                else:
                    self.contador2 = 0
                    self.cambioMov = True
                    self.contador += 1
            else:
                self.movimiento = False
    
    #El método disparo solo se da si el enemigo está vivo y además este avión dispara 3 veces
    def shoot(self, x, y):
        if self.movimiento == True:
            if self.contadorShoot >= 30:
                BalaEnemigo(self.x + 30,self.y + 40, x, y)
                BalaEnemigo(self.x + 30,self.y + 40, x + 100, y)
                BalaEnemigo(self.x + 30,self.y + 40, x - 100, y)
                self.contadorShoot = 0
            self.contadorShoot += 1


    #El método muerte muestra la animacion de muerte del enemigo, además antes de terminar elina al enemigo de la lista en la que se encontraba y suba los puntos al jugador.
    #Utilizamos contadores para su correcta implementación
    def muerte(self):
        if self.contadormuerte < 20: 
            if self.contadormuerte % 2 == 0 and self.contadormuerte != 0:
                self.contadormuertesprite += 1
                if self.contadormuerte >= 12:
                    self.x += 3
                    self.y += 3
            if self.contadormuerte == 12:
                 self.sprite_locationM += 1
            self.sprite = config.sprites_superbombardero[self.contadormuertesprite]
            self.contadormuerte += 1
        else:
            config.enemigosMuertos.remove(self)
            config.pts += self.puntos 
            Powerup(self.x,self.y)

