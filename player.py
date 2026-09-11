from avion import Avion
import config

#Esta es la clase protagonista del juego y bebe de la herencia de Avión
class player1(Avion):
    def __init__(self, x, y):
        self.sprite = (0, config.PLAYER_X_INICIAL, config.PLAYER_Y_INICIAL, config.PLAYER_X_FINAL, config.PLAYER_Y_FINAL, 8)
        self.lives = config.player_lives
        self.dodge = config.num_dodges
        super().__init__(x, y)
        #Este atributo corresponde a la inmunidad en la esquiva
        self.inmunidad = False
        self.fin = False
        #Contadores para la correcta implementación de las animaciones y cambios de sprites
        self.contador = 0
        self.contadorDisfraz = 0
        self.contadormuerte = 0
        self.contadormuertesprite = 0
        #Estos atributos se utilizan para resetear el jugador cuando pierde una vida
        self.finMuerte = False
        self.vidaperdida = False

    #Define el movimiento del jugador teniendo en cuenta los límites del movimiento y enviando estos mensajes al board para poder verse por pantalla
    def move(self, direction: str, sizew:int,sizeh:int):
        plane_x_size = self.sprite[3]
        if direction == 'right' and self.x < sizew - plane_x_size:
            self.x += config.main_plane_speed 
            return self.x
        if direction == 'left' and self.x > 0:
            self.x -= config.main_plane_speed
            return self.x
        if direction == 'up' and self.y > config.MIN_Y_BOARD_LIMIT:
            self.y -= config.main_plane_speed
            return self.y
        if direction == 'down'  and self.y < config.MAX_Y_BOARD_LIMIT:
            self.y += config.main_plane_speed
            return self.y

    #Define el cambio de sprite al mantener presionada alguna tecla de movimiento horizontal
    def cambioSprite(self, disfraz: int):
        if disfraz==3:
            self.sprite = (0, config.PLAYER_X_INICIAL, config.PLAYER_Y_INICIAL, config.PLAYER_X_FINAL, config.PLAYER_Y_FINAL, 8)
        if disfraz==2:
            self.sprite = (0, 130, 1 , 21, 17, 8)
        if disfraz==1:
            self.sprite = (0, 196, 1, 18, 17,8)
        if disfraz == 4:
            self.sprite = (0, 97, 1, 22, 17, 8) 
        if disfraz == 5:
            self.sprite = (0, 162, 1, 18, 17, 8)
    
    #Define el looping para esquivar a los enemigos con el cambio de sprite y la inmunidad que este recibe durante el giro
    #Utilizamos contadores para su correcta implementación
    def esquiva(self):
        if self.dodge > 0:
            if self.contador < 13:
                self.y -=2
            elif self.contador < 34:
                self.y +=2
            elif self.contador < 40:
                self.y -=2
            if (self.contador - 1) % 3 == 0 and self.contador != 1 and self.contador != 16 and self.contador !=37 and self.contador != 40:
                self.contadorDisfraz += 1
            self.inmunidad = True
            self.sprite = config.LISTA_SPRITES_GIRO[self.contadorDisfraz]
            if self.contador == 40:
                self.dodge -=1
                self.inmunidad = False
                self.fin = True
                self.contador = 0
                self.contadorDisfraz = 0
            self.contador += 1
        else:
            self.fin = True

    #Define la animación de muerte del jugador
    #Utilizamos contadores para su correcta implementación
    def muerte(self):
        if self.contadormuerte < 12: 
            if self.contadormuerte % 2 == 0 and self.contadormuerte != 0:
                self.contadormuertesprite += 1
            x, y, w, h =  config.sprites_muerte_player[self.contadormuertesprite]
            self.sprite = (0, x, y, w, h, 8)

            self.contadormuerte += 1
        else:
            self.sprite = (0,0,0,0,0,0)
            self.finMuerte = True
            self.contadormuerte = 0
            self.contadormuertesprite = 0

    #Define el reseteo una vez que el jugador ha perdido una vida
    def reset(self):
        self.x = config.W_BOARD / 2 - self.sprite[3]
        self.y = 200
        self.sprite = (0, config.PLAYER_X_INICIAL, config.PLAYER_Y_INICIAL, config.PLAYER_X_FINAL, config.PLAYER_Y_FINAL, 8)
        self.vidaperdida = True
        self.finMuerte = False
        self.inmunidad = False

