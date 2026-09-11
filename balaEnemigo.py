from bala import Bala

#Utilizamos la herencia para importar los atributos base de Bala
class BalaEnemigo(Bala):
    #Como atributos principales de la bala enemigo definimos el ancho y alto, el sprite que utiliza, la posición del jugador en el instante de disparo y a que tipo pertenece
    def __init__(self, x, y, j1 ,j2):
        super().__init__(x,y)
        self.w, self.h = 3, 3
        self.sprite = (0, 12, 91, 3, 3,  8)
        self.categoria = "Enemigo"
        self.posX, self.posY = j1, j2
        #Con estos condicionales define la pendiente y direccion que va a tomar la bala para ir en dirección al jugador
        if j1 != self.x and j2 != self.y: 
            self.pendiente = round(4/((j2-self.y)/(j1-self.x)))
        if j1 == self.x:
            self.pendiente = round(4/((j2-self.y)/(j1-self.x+1)))
        if j2 == self.y:
            self.pendiente = round(4/((j2-self.y+1)/(j1-self.x)))
        if j2-self.y < 0:
            self.signo = -1
        else:
            self.signo = 1
    
    #La función move esta basada en el sistema de cálculo de pendiente y dirección definido en el init
    def move(self):
        if self.pendiente > 7:
            self.x += 4 * self.signo
        elif self.pendiente < -7:
            self.x -= 4 * self.signo
        elif self.pendiente > 3 or self.pendiente < -3:
            self.y += 2 * self.signo
            self.x += (self.pendiente//2) * self.signo
        else:
            self.y += 4 * self.signo
            self.x += self.pendiente * self.signo
        

