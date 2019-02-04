import os
import pygame
import random
import time


pygame.init()
def load_image(name):
    path = os.path.join('', name)
    return pygame.image.load(path).convert()
    

Blanco = (255, 255, 255)
Negro = (0, 0, 0)
Rojo = (255, 0, 0)
Azul = (0, 0, 255)
Verde = (0, 128, 0)
Lila = (204, 0, 204)
Colonial = (153, 0, 0)

ancho = 800
altura = 500
superficie = pygame.display.set_mode((ancho,altura))
icono = pygame.image.load("icon.png")
pygame.display.set_icon(icono)
background = load_image("29.jpg")

superficie.blit(background, [0, 0])

pygame.display.set_caption("Serpiente")

reloj = pygame.time.Clock()

serp_tamano = 20

font = pygame.font.SysFont("arial_narrow_7.ttf", 35)

def pausa():
    pausado = True

    while pausado:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    pausado = False
                elif event.key == pygame.K_q:
                    pygame.quit()
                    quit()
            background = load_image("25.jpg")
            superficie.blit(background, [0, 0])
            #superficie.fill(Blanco)
            message_to_screen("Para continuar presiona \"C\"", Negro, 100)
            pygame.display.update()
            reloj.tick(5)

def puntos(score,velocidad):
        text = font.render("Puntos: "+str(score)+" Velocidad: "+str(velocidad), True, Negro)
        superficie.blit(text, [0,0])

def intro_juego():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_c:
                    intro = False
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        background = load_image("FONDO jp-01.png")
        superficie.blit(background, [0, 0])
        message_to_screen("Bienvenido, bienvenida", Colonial, -100)
        message_to_screen("El objetivo del juego es controlar una serpiente usando", Negro, -75)
        message_to_screen("teclas flechas de movimiento para comer manzanas", Negro, -50)
        message_to_screen("El puntaje por manzana es: Roja:+1 lila: +10", Colonial, -25);
        message_to_screen("Cada tres puntos la manzana roja aumenta la velocidad en 1", Colonial, 0);
        message_to_screen("Si se come la manzana verde la velocidad aumenta en 1", Colonial, 25);
        message_to_screen("Si la serpiente toca el borde o se toca a si misma, pierdes.", Negro, 50)
        message_to_screen("Para pausar partida, presiona tecla P.", Negro, 75)
        message_to_screen("Para continuar partida, presiona tecla C", Negro, 100)
        message_to_screen("Para terminar de jugar y salir, preciona tecla Q.", Colonial, 125)
        pygame.display.update()
        reloj.tick(15)
        
def serpiente(serp_tamano, listaSerpiente):
    for i in listaSerpiente:
        pygame.draw.rect(superficie, Negro, [i[0], i[1], serp_tamano, serp_tamano])

def text_objetos(text, color):
    textSuperficie = font.render(text, True, color)
    return textSuperficie, textSuperficie.get_rect()

def message_to_screen(msg, color, y_displace=0):
    textSur, textRect = text_objetos(msg, color)
    textRect.center = (ancho/2), (altura/2) + y_displace
    superficie.blit(textSur, textRect)
    #pantalla_texto = font.render(msg, True, color)
    #superficie.blit(pantalla_texto,[300, 300])

def gameLoop():
    gameExit = False
    gameOver = False
       
    mover_x = 300
    mover_y = 300

    CPS = 15
    
    puntos_rojo = 0

    mover_x_cambio = 0
    mover_y_cambio = 0
     
    listaSerpiente = []
    largoSerpiente = 1
    #Manzana roja da 1 punto
    azarManzanaX = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzanaY = round(random.randrange(0, 300 - 20)/20.0)*20.0
    #Manzana verde de velocidad
    azarManzana2X = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzana2Y = round(random.randrange(0, 300 - 20)/20.0)*20.0
    #Manzana lila da 10 puntos
    azarManzana3X = round(random.randrange(0, 300 - 20)/20.0)*20.0
    azarManzana3Y = round(random.randrange(0, 300 - 20)/20.0)*20.0

    #Si manzana verde es igual a manzana roja
    if(azarManzana2X>(azarManzanaX-20) and azarManzana2X<(azarManzanaX+20) or azarManzana2Y>(azarManzanaY-20) and azarManzana2Y<(azarManzanaY+20)):
        azarManzana2X += 20
        azarManzana2Y += 20
    #Si manzana verde es igual a manzana lila
    if(azarManzana2X>(azarManzana3X-20) and azarManzana2X<(azarManzana3X+20) or azarManzana2Y>(azarManzana3Y-20) and azarManzana2Y<(azarManzana3Y+20)):
        azarManzana2X += 20
        azarManzana2Y += 20
    #Si manzana lila es igual a manzana verde
    if(azarManzana3X>(azarManzanaX-20) and azarManzana3X<(azarManzanaX+20) or azarManzana3Y>(azarManzanaY-20) and azarManzana3Y<(azarManzanaY+20)):
        azarManzana3X += 20
        azarManzana3Y += 20
    #Si manzana lila es igual a manzana roja 
    if(azarManzana3X>(azarManzanaX-20) and azarManzana3X<(azarManzanaX+20) or azarManzana3Y>(azarManzanaY-20) and azarManzana3Y<(azarManzanaY+20)):
        azarManzana3X += 20
        azarManzana3Y += 20
    #Si manzana roja es igual a manzana lila
    if(azarManzanaX>(azarManzana3X-20) and azarManzanaX<(azarManzana3X+20) or azarManzanaY>(azarManzana3Y-20) and azarManzanaY<(azarManzana3Y+20)):
        azarManzanaX += 20
        azarManzanaY += 20
    #Si manzana roja es igual a manzana verde
    if(azarManzanaX>(azarManzana2X-20) and azarManzanaX<(azarManzana2X+20) or azarManzanaY>(azarManzana2Y-20) and azarManzanaY<(azarManzana2Y+20)):
        azarManzanaX += 20
        azarManzanaY += 20
        
    pulsar_sonido = pygame.mixer.Sound("song.ogg")
    pulsar_sonido.set_volume(0.50)
    pulsar_sonido.play(18)
    
    
    while not gameExit:

        while gameOver == True:
            ##superficie.fill(blanco)
            superficie.blit(background, [0,0])
            pulsar_sonido.stop()
            message_to_screen("Game Over", Negro, -50)
            message_to_screen("Para continuar presione C. Para terminar presione Q", Rojo, 50)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()
                        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    mover_x_cambio = -serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_RIGHT:
                    mover_x_cambio = serp_tamano
                    mover_y_cambio = 0
                elif event.key == pygame.K_UP:
                    mover_y_cambio = -serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_DOWN:
                    mover_y_cambio = serp_tamano
                    mover_x_cambio = 0
                elif event.key == pygame.K_p:
                    pulsar_sonido.set_volume(0.0)
                    pausa()
                    pulsar_sonido.set_volume(0.50)
                

        if mover_x >= ancho or mover_x < 0 or mover_y >= altura or mover_y <0:
            gameOver = True
            
        mover_x += mover_x_cambio
        mover_y += mover_y_cambio
        #superficie.fill(Blanco)
        superficie.blit(background, [0,0])
        
        pygame.draw.rect(superficie, Rojo, [azarManzanaX, azarManzanaY, 20, 20])
        pygame.draw.rect(superficie, Verde, [azarManzana2X, azarManzana2Y, 20, 20])
        pygame.draw.rect(superficie, Lila, [azarManzana3X, azarManzana3Y, 20, 20])
        
        cabezaSerpiente = []
        cabezaSerpiente.append(mover_x)
        cabezaSerpiente.append(mover_y)
        listaSerpiente.append(cabezaSerpiente)
        if len(listaSerpiente) > largoSerpiente:
            del listaSerpiente[0]

        for eachSegment in listaSerpiente[:-1]:
            if eachSegment == cabezaSerpiente:
                gameOver = True
                
        serpiente(serp_tamano, listaSerpiente)
        puntos(largoSerpiente-1, CPS)
        pygame.display.update()
        #rojo
        if mover_x == azarManzanaX and mover_y == azarManzanaY:
            pygame.mixer.music.load("Sonig.ogg")
            azarManzanaX = round(random.randrange(0, 300 - 20)/20.0)*20.0
            azarManzanaY = round(random.randrange(0, 300 - 20)/20.0)*20.0
            largoSerpiente += 1
            puntos_rojo += 1
            if puntos_rojo%3==0:
                CPS+=1
            pygame.mixer.music.play(0)
            
        #verde    
        if mover_x == azarManzana2X and mover_y == azarManzana2Y:
            pygame.mixer.music.load("Sonig.ogg")
            azarManzana2X = round(random.randrange(0, 300 - 20)/20.0)*20.0
            azarManzana2Y = round(random.randrange(0, 300 - 20)/20.0)*20.0
            pygame.mixer.music.play(0)
            CPS +=1
        #lila
        if mover_x == azarManzana3X and mover_y == azarManzana3Y:
            pygame.mixer.music.load("Sonig.ogg")
            azarManzana3X = round(random.randrange(0, 300 - 20)/20.0)*20.0
            azarManzana3Y = round(random.randrange(0, 300 - 20)/20.0)*20.0
            largoSerpiente += 10
            pygame.mixer.music.play(0)
        
        reloj.tick(CPS)
    pygame.display.update()
    time.sleep(3)
    pygame.quit()
    quit()
intro_juego()
gameLoop()


