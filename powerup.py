import random
import config

#Power up no tiene herencia ya que es totalmente independiente al resto de las clases
class Powerup():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        #No se define sprite inicial ya que es aleatorio
        self.sprite = None
        #El tipo de power up es random
        self.tipoPow = random.randint(0,3)
        self.time = 0
        #Este atributo está definido para que el power up no cambie de manera constante y su uso se ve en el board
        self.definido = False
        self.usado = False
        #Se añade a la lista de power ups acumulados por el jugador
        config.powerup.append(self)

    #Este método selecciona el tipo de power up que se enseña por pantalla
    def tipo(self, num:int):
        if self.tipoPow == 0:
            self.sprite = config.power_up_sprites[0]
        elif self.tipoPow == 1:
            self.sprite = config.power_up_sprites[1]
        elif self.tipoPow == 2:
            self.sprite = config.power_up_sprites[2]
        elif self.tipoPow == 3:
            self.sprite = config.power_up_sprites[3]

    #Este método defina en relacción con el tipo la característica que se le aplica al jugador
    def accion(self):
        if self.usado == False:
            if self.tipoPow == 0:
                config.pts += 1000
            elif self.tipoPow == 1:
                config.main_plane_speed += 1
            elif self.tipoPow == 2:
                config.moredodge += 1
            elif self.tipoPow == 3:
                config.morelive += 1
            self.usado = True

    #Los power ups se mueven a la misma velocidad que el fondo
    def move(self):
        self.y += 1

    

