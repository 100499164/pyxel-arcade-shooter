from enemigo import Enemigo
import config
import random
from balaEnemigo import BalaEnemigo

#Al igual que el resto de Enemigos utilizamos herencia
#Además se han añadido nuevos atributos como regreso(característico del movimiento de este avión), cargada y limite_y(establece la posición del giro)
class EnemigoRegular(Enemigo):
    def __init__(self, x, y, j1, j2):
        super().__init__(x, y)
        self.regreso = False
        self.vidas = 1
        self.sprite = config.sprites_eReg[0]
        self.sprite_location = 0
        self.sprite_locationM = 0
        self.posicion_x = j1
        self.limite_y = random.randint(j2-15,j2)
        self.cargada = random.randint(0,1)
        self.disparo = True
        #El momento del disparo es random antes del giro de vuelta
        self.momento_disparo = random.randint(self.limite_y//2,int(self.limite_y*(9/10)))
        self.contador = 0
        self.contadorsprite = 0
        self.puntos = 100
    
    #El movimiento del avión regular se describe avanzando hasta una posición ramdom que será en la que comienza el giro
    def move(self):
        #Cambios  de los diferentes sprites respecto al movimiento y posición del avión
        plane_x_size = self.sprite[2]
        if self.y >= self.limite_y:
            self.regreso= True
        if self.y >= self.limite_y-1:
                self.sprite = config.sprites_eReg[1]
        elif self.y > self.limite_y*(9/10) and self.regreso == False:
                self.sprite = config.sprites_eReg[2]
        elif self.y > self.limite_y*(9/10) and self.regreso == True:
            self.sprite = config.sprites_eReg[3]
        elif self.y < self.limite_y and self.regreso == True:
                self.sprite = config.sprites_eReg[4]
        #Movimiento del avión en las diferentes fases del la vida de este
        if self.y < self.limite_y and self.regreso == False:
            self.y += 3
        elif self.y < self.limite_y and self.regreso == True:
            self.y -= 3
        elif self.y >= self.limite_y:
            self.y -= 3
        if self.x < self.posicion_x and self.y > self.limite_y/2 and self.x < config.W_BOARD - plane_x_size:
            self.x += 1 
        if self.x > self.posicion_x and self.y > self.limite_y/2 and self.x < config.W_BOARD - plane_x_size:
            self.x -= 1          

    #El método disparo solo se da si el enemigo está vivo y si este avión cuenta con munición
    def shoot(self, x, y):
        if self.is_alive == True:
            if self.cargada == 0 and self.disparo == True and self.y > self.momento_disparo:
                BalaEnemigo(self.x,self.y, x, y)
                self.disparo = False

    #El método muerte muestra la animacion de muerte del enemigo, además antes de terminar elimina al enemigo de la lista en la que se encontraba y suma los puntos al jugador.
    #Utilizamos contadores para su correcta implementación
    def muerte(self):
        if self.contador < 12: 
            if self.contador % 2 == 0 and self.contador != 0:
                self.contadorsprite += 1
            self.sprite = config.sprites_explosion_eReg[self.contadorsprite]
            self.contador += 1
        else:
            config.enemigosMuertos.remove(self)
            config.pts += self.puntos 