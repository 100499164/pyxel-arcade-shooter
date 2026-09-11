from bala import Bala
import config

#Utilizamos la herencia para importar los atributos base de Bala
class BalaPlayer(Bala):
    #Los sprites de esta clase están definidos en el Config, como también su ancho y alto
    #Las balas del jugador cuentan con el atributo daño para que cuando impacte con el bombardero y super-bombardero no les mate de un balazo
    # Los dos atributos contadores nos ayudan a gestionar bien las animaciones del impacto y para que sean lo más realistas posibles    
    def __init__(self, x, y):
        super().__init__(x,y)
        self.sprite = (
            0 ,config.BALA_PLAYER_X_INICIAL, config.BALA_PLAYER_Y_INICIAL, 
            config.BALA_PLAYER_X_FINAL, config.BALA_PLAYER_Y_FINAL, 8
            )
        self.w = config.BALA_PLAYER_X_FINAL
        self.h = config.BALA_PLAYER_Y_FINAL
        self.categoria = "player"
        self.bulletDamage = 1
        self.contador = 0
        self.contadorsprite = 0
    
    #El movimiento de la bala del jugador es bastante simple, simplemente avanza hasta encontrar un enemigo o salirse de la pantalla.
    def move(self):
        self.y -= config.PLAYER_BULLET_SPEED

    #Este método es el encargado de que se vea la colisión en pantalla cuando impacta contra algun enemigo
    def impacto(self):
        if self.contador < 12: 
            if self.contador % 2 == 0 and self.contador != 0:
                self.contadorsprite += 1
            self.sprite = config.sprites_explosion_eReg[self.contadorsprite]
            self.contador += 1
        else:
            config.impactoBala.remove(self)
        