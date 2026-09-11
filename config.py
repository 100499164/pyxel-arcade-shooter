
#Posiciones limites
MIN_X_BOARD_LIMIT = -4

MIN_Y_BOARD_LIMIT = 50

MAX_X_BOARD_LIMIT = 0

MAX_Y_BOARD_LIMIT = 220

#Tamaño de impresión del board
W_BOARD = 224

H_BOARD = 256

#Posiciones de los sprites de la bala y el jugador
BALA_PLAYER_X_INICIAL = 72

BALA_PLAYER_Y_INICIAL = 75

BALA_PLAYER_X_FINAL = 12

BALA_PLAYER_Y_FINAL = 12

PLAYER_BULLET_SPEED = 6

PLAYER_X_INICIAL = 0

PLAYER_Y_INICIAL = 0

PLAYER_X_FINAL = 26

PLAYER_Y_FINAL = 17

#Cantidades de enemigos predeterminados por oleada
OLEADA1 = (10, 4, 3, 1)

OLEADA2 = (15, 6, 4, 1)

OLEADA3 = (20, 8, 4, 2)

OLEADA4 = (20, 10, 5, 2)

OLEADA5 = (20, 16, 5, 3)

#Caracteristicas base del jugador
main_plane_speed = 3

player_lives = 3

num_dodges = 3

position = [10, 10]

#Listas donde se almacenan los enemigos, balas, animaciones de muerte y records de puntos que se dan durante la partida
enemigos = []

enemigosMuertos = []

balas = []

impactoBala = []

powerup = []

lista_record = [0]

#Estas variables se encuentran vinculadas a los powerups
morelive = 0

moredodge = 0

#Cantidad de puntos que el jugador ha generado en el trascurso de esa partida
pts = 0

#Listas donde se encuentran todos los sprites utilizados en las diferentes clases, animaciones etc.
sprites_eReg = ((1, 195, 15, 14),(206, 104, 14, 5), (153, 195, 14, 10), (191, 196, 14, 10), (77, 156, 14, 13))

sprites_explosion_eReg = ((117, 77, 11, 9), (132, 76, 14, 9), (150, 74, 15, 14), (169, 75, 16, 13), (190, 74, 14, 14), (208, 66, 15, 14))

sprites_explosion_bomb = ((104, 238, 12, 12), (121, 236, 16, 16), (133, 210, 16, 17), (2, 227, 26, 27), (33, 228, 22, 24), (60, 230, 20, 22), (85, 231, 15, 17))

sprites_eRoj = ((2, 216, 14, 13), (192, 237, 13, 12), (212, 238, 12, 11), (231, 237, 12, 13),
 (60, 236, 4, 4), (2, 236, 13, 13), (22, 236, 13, 13), (40, 236, 14, 12), (2, 175, 13, 12), 
 (79, 237, 13, 12), (98, 237, 12, 12), (117, 236, 12, 14), (1, 195, 14, 13), (136, 236, 14, 13), 
 (156, 237, 12, 13), (174, 238, 14, 11))

sprites_bombardero = ((1, 118, 30, 21),(39, 117, 28 , 22),(72, 117, 26, 22),(106, 118, 23, 22), (136, 115, 24, 26), (117, 19, 26, 23), 
(148, 20, 27, 23), (180, 21, 30, 22), (3, 85, 30, 22), (38, 85, 28, 22), (71, 85, 25, 23), (109, 84, 22, 22), (137, 84, 24, 24), (167, 87, 25, 21),(165, 114, 25, 22),(199, 113, 25, 22))

sprites_superbombardero = ((2, 61, 62, 44),(69 ,61 , 62, 44),(136, 61, 62, 44),(76, 4, 62, 44),(154, 113, 62, 44), (152, 165, 62, 44),
(3, 1, 53, 39), (3, 46, 44, 32), (52, 50, 43, 26),(100, 53, 38, 22),(144, 53, 174, 72))

power_up_sprites = ((2, 135, 12, 9), (36, 135, 12, 9), (87, 135, 12, 9), (70, 135, 12, 9))

LISTA_SPRITES_GIRO = ((0, 0, 21, 27, 13, 8),(0, 31, 22, 28, 10, 8),(0, 31, 47, 29, 16, 8),(0, 62, 43, 31, 21, 8),(0, 125, 41, 31, 24, 8),
(0, 162, 43, 29, 20, 8),(0, 195, 44, 27, 16, 8),(0, 191, 21, 26, 11, 8),(0, 160, 26, 24, 6, 8),
(0, 1, 42, 24, 10, 8),(0, PLAYER_X_INICIAL, PLAYER_Y_INICIAL, PLAYER_X_FINAL, PLAYER_Y_FINAL, 8))

sprites_muerte_player=  ((1, 100, 26, 21), (31, 97, 32, 27), (65, 95, 33, 32), (100, 95, 32, 32), (135, 96, 32, 30), (171, 98, 30, 25))

y_fondo = [156, -8, -80, 60, -18, -90, -800, -512, -230, -50, -120, -333, 262, -180, -230, -50, -120, -256, -280, -320, -809, -1023, 300]

y_mar = [0, 90, 180, 270]

oleadas = [[10, 4, 3, 1], [15, 6, 4, 1], [20, 8, 4, 2], [20, 10, 5, 2], [20, 16, 5, 3], [0, 0, 0, 0]]

#Cantidad de enemigos que aparecen por pantalla en un momento inicial que va aumentando en el trascurso del juego
cant_enem = 2

#Número de oleada en la que nos encontramos que siempre se mostrará por pantalla un número más
num_oleada = 0