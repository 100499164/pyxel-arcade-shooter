import pyxel
import config
from player import player1
from balaPlayer import BalaPlayer
import random
from enemigoRegular import EnemigoRegular
from enemigoRojo import EnemigoRojo
from enemigoBombardero import Bombardero
from enemigoSuperbombardero import Superbombardero


class Board:
    def __init__(self, w: int, h: int):
        self.width = w
        self.height = h
        self.player = player1(self.width / 2, 200)
        #Atributo para verificar si el avión esta en momento de esquiva
        self.press_z = False
        #Atributo para verificar si el juego ha acabado
        self.fin_del_juego = False
        #Cargamos el banco de imágenes e inicializamos pyxel
        pyxel.init(self.width, self.height, title="1942")
        pyxel.load("Assets/banco_general.pyxres")
        pyxel.run(self.update, self.draw)

    
    def update(self):
        if self.fin_del_juego == False:

            #Actualiza el desplazamiento vertical del mar
            for i in range(len(config.y_mar)):
                    config.y_mar[i] += +1
                    if config.y_mar[i] > 260:
                        config.y_mar[i] -= 360

            #Actualiza el desplazamiento vertical del fondo
            for i in range(len(config.y_fondo)):
                config.y_fondo[i] += +1
                if config.y_fondo[i] > 333:
                    config.y_fondo[i] -= 360

            #Si se pulsa la Q se sale del juego
            if pyxel.btnp(pyxel.KEY_Q):
                pyxel.quit()
            
            #Si se pulsa la Z el jugador realiza la esquiva
            if pyxel.btn(pyxel.KEY_Z):
                self.press_z = True
            if self.press_z == True:
                self.player.esquiva()
                if self.player.fin == True:
                    self.press_z = False
                    self.player.fin = False
                    
            #Este movimiento lo tiene cuando no esta en la esquiva    
            if self.press_z == False :
                #Esto corresponde al movimiento del jugador que envia esa señal a su clase para que este se mueva
                #El de 1000 frames está para evitar el fallo de pyxel
                if pyxel.btnp(pyxel.KEY_RIGHT,1000,1):
                    self.player.cambioSprite(3)
                elif pyxel.btnp(pyxel.KEY_RIGHT,30,1):
                    self.player.cambioSprite(5)
                elif pyxel.btnp(pyxel.KEY_RIGHT,15,1):
                    self.player.cambioSprite(4)
                elif pyxel.btnp(pyxel.KEY_RIGHT,1,1):
                    self.player.cambioSprite(3)
                if pyxel.btnr(pyxel.KEY_RIGHT):
                    self.player.cambioSprite(3)
            
                #El de 1000 frames está para evitar el fallo de pyxel
                if pyxel.btnp(pyxel.KEY_LEFT,1000,1):
                    self.player.cambioSprite(3)
                elif pyxel.btnp(pyxel.KEY_LEFT,30,1):
                    self.player.cambioSprite(1)
                elif pyxel.btnp(pyxel.KEY_LEFT,15,1):
                    self.player.cambioSprite(2)
                elif pyxel.btnp(pyxel.KEY_LEFT,1,1):
                    self.player.cambioSprite(3)
                if pyxel.btnr(pyxel.KEY_LEFT):
                    self.player.cambioSprite(3)
                if pyxel.btn(pyxel.KEY_UP):
                    self.player.move("up",self.width, self.height)
                if pyxel.btn(pyxel.KEY_DOWN):
                    self.player.move('down', self.width, self.height)
                
                #Aqui definimos la aparicion de la bala cuando el jugador presiona espacio
                if pyxel.btnp(pyxel.KEY_SPACE):
                    BalaPlayer(
                        self.player.x + (config.PLAYER_X_FINAL - 12) // 2, self.player.y - 12 // 2
                    )

            #Si esta en la esquiva solo se mueve de derecha a izquierda
            if pyxel.btn(pyxel.KEY_RIGHT):
                    self.player.move('right', self.width, self.height)
            if pyxel.btn(pyxel.KEY_LEFT):
                    self.player.move("left", self.width, self.height)
            
            #Esto actualiza el movimiento de las balas y si sobrepasa los límites se elimina
            for bala in config.balas[:]:
                bala.move()
                if bala.y < -7 or bala.y > self.height + 7 or bala.x < -7 or bala.x > self.width + 7:
                    config.balas.remove(bala)
                
            #Aquí se define la muerte del jugador y el reseteo de puntos como también su guardado
            if self.player.inmunidad and self.player.vidaperdida == False:
                self.player.muerte()

                if self.player.finMuerte == True:
                    if self.player.lives <= 0:
                        self.fin_del_juego = True
                        config.lista_record.append(config.pts)
                        config.pts = 0
                    else:
                        config.enemigos.clear()
                        config.balas.clear()

                    self.player.reset()
                    
            #Aquí definimos las colisiones del jugador con los enemigos
            for enemigo in config.enemigos[:]:
                enemigo.move()
                enemigo.shoot(self.player.x,self.player.y)
                if enemigo.is_alive:
                    if (enemigo.x + enemigo.sprite[2] >self.player.x 
                            and self.player.x + self.player.sprite[3] > enemigo.x
                            and enemigo.y + enemigo.sprite[3] > self.player.y 
                            and self.player.y + self.player.sprite[4]  > enemigo.y
                            ) and self.player.inmunidad == False:
                        enemigo.is_alive = False
                        config.pts -= enemigo.puntos
                        self.player.lives -= 1
                        self.player.vidaperdida = False
                        self.player.inmunidad = True

                    if enemigo.is_alive == False and enemigo.is_dead == False:
                        enemigo.is_dead = True
                        config.enemigosMuertos.append(enemigo)
                        config.enemigos.remove(enemigo)

                #Aqui definimos las colisiones de las balas con los enemigosy, con el jugador y las acciones tras suceder
                for bala in config.balas[:]:
                    #Colisiones con enemigos
                    if (enemigo.x + enemigo.sprite[2] > bala.x 
                        and bala.x  + bala.w > enemigo.x
                        and enemigo.y + enemigo.sprite[3] > bala.y 
                        and bala.y + bala.h > enemigo.y) and bala.categoria == "player":
                        enemigo.vidas -= bala.bulletDamage
                        if enemigo.vidas <= 0:
                            enemigo.is_alive = False
                        else:
                            config.impactoBala.append(bala)
                        bala.is_alive = False
                        config.balas.remove(bala)
                        
                    if enemigo.is_alive == False and enemigo.is_dead == False:
                        enemigo.is_dead = True
                        config.enemigosMuertos.append(enemigo)
                        config.enemigos.remove(enemigo)

                    #Colisiones con jugador
                    if (self.player.x + self.player.sprite[3] > bala.x 
                        and bala.x  + bala.w  > self.player.x
                        and self.player.y + self.player.sprite[4] > bala.y 
                        and bala.y  + bala.h   > self.player.y
                        ) and bala.categoria == "Enemigo" and self.player.inmunidad == False:
                        bala.is_alive = False
                        config.balas.remove(bala)
                        self.player.lives -= 1
                        self.player.vidaperdida = False
                        self.player.inmunidad = True

                if enemigo.y <= -40:
                        enemigo.is_alive = False
                if enemigo.y >= config.H_BOARD + 40:
                        enemigo.is_alive = False
                if enemigo.x >= config.W_BOARD + 20:
                        enemigo.is_alive = False
            
            #Esto ejecuta la animación de muerte de los enemigos
            for enemigo in config.enemigosMuertos:
                enemigo.muerte()

            #Esto ejecuta la animación de impacto de las balas
            for bala in config.impactoBala:
                bala.impacto()

            #Aquí definimos las colisiones con los posibles powerups dropeados por los enemigod
            for powerup in config.powerup[:]:
                
                if powerup.definido == False:
                    powerup.tipo(powerup.tipoPow)
                    powerup.definido = True
                powerup.move()
                
                if (self.player.x + self.player.sprite[3] > powerup.x 
                        and powerup.x  + powerup.sprite[2]  > self.player.x
                        and self.player.y + self.player.sprite[4] > powerup.y 
                        and powerup.y  + powerup.sprite[3]   > self.player.y) and self.player.is_alive == True:
                    powerup.accion()
                    self.player.lives += config.morelive
                    self.player.dodge += config.moredodge
                    config.morelive = 0
                    config.moredodge = 0
                    config.powerup.remove(powerup)
            
            #Esto limita la cantidad de enemigos por pantalla dependiendo de la oleada en la que nos encontremos y crea los enemigos restantes
            if len(config.enemigos) < config.cant_enem:
                tipo = random.randint(0,3)
                
                if config.oleadas[config.num_oleada][tipo] > 0:
                    if tipo == 0:
                        if config.cant_enem - len(config.enemigos)  >=  config.oleadas[config.num_oleada][tipo]:
                            num_enemigos_regulares = random.randint(1, config.oleadas[config.num_oleada][tipo])
                        if config.cant_enem - len(config.enemigos) < config.oleadas[config.num_oleada][tipo]:
                            num_enemigos_regulares = random.randint(1, config.cant_enem - len(config.enemigos))
                        for i in range(0, num_enemigos_regulares):
                            EnemigoRegular(random.randint(0, 215), -6, self.player.x, self.player.y)
                        config.oleadas[config.num_oleada][tipo] -= num_enemigos_regulares

                    elif tipo == 1:
                        y_comun =  random.randint(50, 100)
                        num_enemigos_rojos = random.randint(2, config.oleadas[config.num_oleada][1])

                        if config.oleadas[config.num_oleada][tipo] - num_enemigos_rojos == 1:
                            num_enemigos_rojos += 1

                        for i in range(0, num_enemigos_rojos):
                            EnemigoRojo((-5)*i*4, y_comun) 
                        config.oleadas[config.num_oleada][tipo] -= num_enemigos_rojos

                    elif tipo == 2:
                        Bombardero(random.randint(10,config.W_BOARD - config.sprites_bombardero[0][3]- 10) , -10)
                        config.oleadas[config.num_oleada][tipo] -= 1

                    elif tipo == 3:
                        Superbombardero(random.randint(50,config.W_BOARD - config.sprites_superbombardero[0][3]- 50),self.height)
                        config.oleadas[config.num_oleada][tipo] -=1
            
            #Si la oleada es eliminada con este código avanzamos a la siguiente
            if config.oleadas[config.num_oleada] == [0,0,0,0] and config.num_oleada != 5:
                config.num_oleada += 1
                config.cant_enem += 1
        
        #Si se acaba el juego se eliminan todo lo creado en la partida y se restablecen las variables modificadas
        if self.fin_del_juego == True:
            config.enemigos.clear()
            config.enemigosMuertos.clear()
            config.impactoBala.clear()
            config.balas.clear()
            config.powerup.clear()
            config.main_plane_speed = 3
            config.cant_enem = 2
             
            #Al presionar la R el juego se reinicia
            if pyxel.btn(pyxel.KEY_R):
                self.player.lives = 3
                self.player.dodge = 3
                config.num_oleada = 0

                self.fin_del_juego = False
                config.oleadas = [list(config.OLEADA1), list(config.OLEADA2), list(config.OLEADA3), list(config.OLEADA4), list(config.OLEADA5), [0, 0, 0, 0] ]
                      
    #Dibujo el fondo y el sprite del jugador, junto a las balas y los enemigos
    def draw(self):
        #color base del fondo
        pyxel.cls(5)
        #Textura del fondo
        pyxel.blt(0, config.y_mar[0], 2, 0, 160, 167, 95)
        pyxel.blt(0, config.y_mar[1], 2, 0, 160, 167, 95)
        pyxel.blt(0, config.y_mar[2], 2, 0, 160, 167, 95)
        pyxel.blt(0, config.y_mar[3], 2, 0, 160, 167, 95)
        pyxel.blt(167, config.y_mar[0], 2, 0, 160, 57, 95)
        pyxel.blt(167, config.y_mar[1], 2, 0, 160, 57, 95)
        pyxel.blt(167, config.y_mar[2], 2, 0, 160, 57, 95)
        pyxel.blt(167, config.y_mar[3], 2, 0, 160, 57, 95)
        
        #figuras fondo
        #nubes
        pyxel.blt(20, config.y_fondo[0], 2, 208, 250, 11, 4, 8)
        pyxel.blt(29, config.y_fondo[1], 2, 208, 230, 13, 5, 8)
        pyxel.blt(80,config.y_fondo[2], 2, 234, 213, 11, 5, 8)
        pyxel.blt(93, config.y_fondo[3], 2, 230, 220, 16, 6, 8)
        pyxel.blt(120,config.y_fondo[4], 2, 228, 237, 20, 6, 8)
        pyxel.blt(150,config.y_fondo[5], 2, 225, 248, 13, 5, 8)
        pyxel.blt(185,config.y_fondo[6], 2, 208, 230, 13, 5, 8)
        pyxel.blt(199, config.y_fondo[7], 2, 209, 211, 19, 5, 8)
        pyxel.blt(29, config.y_fondo[14], 2, 208, 230, 13, 5, 8)
        pyxel.blt(45, config.y_fondo[15], 2, 208, 211, 19, 5, 8)
        pyxel.blt(170,config.y_fondo[17], 2, 208, 250, 10, 6, 8)
        pyxel.blt(185,config.y_fondo[18], 2, 208, 230, 13, 5, 8)
        pyxel.blt(199, config.y_fondo[19], 2, 209, 211, 19, 5, 8)
        pyxel.blt(45, config.y_fondo[20], 2, 208, 211, 19, 5, 8)
        pyxel.blt(80,config.y_fondo[21], 2, 234, 213, 11, 5, 8)
        pyxel.blt(93, config.y_fondo[22], 2, 230, 220, 16, 6, 8)
        #islas
        pyxel.blt(75,config.y_fondo[8], 2, 224, 87, 21, 15, 8)
        pyxel.blt(80,config.y_fondo[12], 2, 204, 60, 53, 21, 8)
        pyxel.blt(130,config.y_fondo[13], 2, 206, 145, 49, 22, 8 )

        #Dibujamos el avión
        pyxel.blt(self.player.x, self.player.y, *self.player.sprite)
       
        #Animaciones de las hélices del avión principal siempre y cuando el avión este en su sprite original
        if self.player.sprite ==  (0, config.PLAYER_X_INICIAL, config.PLAYER_Y_INICIAL, 
        config.PLAYER_X_FINAL, config.PLAYER_Y_FINAL, 8
        ):
            if pyxel.frame_count % 2:
                pyxel.rect(self.player.x + 5, self.player.y + 2, 3, 1, 3)
                pyxel.rect(self.player.x + 19, self.player.y + 2, 3, 1, 3)
            else:
                pyxel.rect(self.player.x + 9, self.player.y + 2, 3, 1, 3)
                pyxel.rect(self.player.x + 15, self.player.y + 2, 3, 1, 3)
        
        #Dibujamos cada bala presente en el juego, tanto de los enemigos como del jugador
        for balas in config.balas:
            if balas.is_alive == True and balas.categoria == "player":
                pyxel.blt(balas.x, balas.y , *balas.sprite)
            if balas.is_alive == True and balas.categoria == "Enemigo":
                pyxel.blt(balas.x, balas.y, *balas.sprite)
        
        #Dibujamos todos los enemigos de la lista de los enemigos
        for enemigo in config.enemigos:
            pyxel.blt(enemigo.x, enemigo.y, enemigo.sprite_location ,enemigo.sprite[0] ,
            enemigo.sprite[1], enemigo.sprite[2] ,enemigo.sprite[3] ,8
            )
        
        #Dibujamos todos los enemigos de la lista de los enemigos muertos para ver su explosión de muerte
        for enemigo in config.enemigosMuertos:
            pyxel.blt(enemigo.x, enemigo.y, enemigo.sprite_locationM  ,enemigo.sprite[0] ,
            enemigo.sprite[1], enemigo.sprite[2] ,enemigo.sprite[3] ,8
            )
        
        #Dibujamos los impactos de las balas con cada enemigo
        for bala in config.impactoBala:
            pyxel.blt(bala.x, bala.y, 0 ,bala.sprite[0] ,
            bala.sprite[1], bala.sprite[2] ,bala.sprite[3] ,8
            )
        
        #Dibujamos los diferrentes powerups que sueltan las enemigos
        for powerup in config.powerup:
            pyxel.blt(powerup.x, powerup.y, 0 ,powerup.sprite[0] ,
            powerup.sprite[1], powerup.sprite[2] ,powerup.sprite[3] ,8
            )
        
        #Estas tres lineas forman el marcador de puntos
        pyxel.rect(200, 0 , 25, 12, 9)
        pyxel.rect(202, 0 , 25, 10, 7)
        pyxel.text(204, 2, str(config.pts), pyxel.frame_count % 16)
        
        #Estas lineas forman el marcador de vidas
        if self.player.lives > 0:
            pyxel.blt(2, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 1:
            pyxel.blt(19, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 2:
            pyxel.blt(36, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 3:
            pyxel.blt(53, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 4:
            pyxel.blt(70, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 5:
            pyxel.blt(87, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 6:
            pyxel.blt(100, 241, 2, 184, 219, 16, 14, 8)
        if self.player.lives > 7:
            pyxel.blt(117, 241, 2, 184, 219, 16, 14, 8)
        
        #Estas lineas forman el marcador de esquivas
        if self.player.dodge > 0:
            pyxel.blt(212, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 1:
            pyxel.blt(204, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 2:
            pyxel.blt(196, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 3:
            pyxel.blt(188, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 4:
            pyxel.blt(180, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 5:
            pyxel.blt(172, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 6:
            pyxel.blt(164, 241, 2, 227,186, 9, 9, 7)
        if self.player.dodge > 7:
            pyxel.blt(156, 241, 2, 227,186, 9, 9, 7)
        
        #Mostramos el Record de la partida actual
        pyxel.text(5, 5, "RECORD:", 7)
        pyxel.text(10, 12, str(max(config.lista_record)), 7)
        #Mostramos la oleada en la que estamos jugando
        pyxel.text(93, 5, "OLEADA: {}".format(config.num_oleada + 1), pyxel.frame_count % 5)

        #Si has llegado a la última oleada se muestra el siguiente mesaje
        if config.num_oleada >= 5:
            pyxel.text(80, 125, "HAS ELIMINADO TODAS LAS OLEADAS", 7)

        #Si el jugador pierde todas las vidas puede reiniciar la partida presionando la R
        if self.player.lives <= 0:
            pyxel.text(75, 125, "PULSA \"R\" PARA REINICIAR", 7)