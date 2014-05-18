import pygame, sys, os, random, math
from funciones import *
from pygame.locals import *
pygame.init() #inicia pygame
#inicia la ventana
dimx=1280;dimy=720 #dimensiones de la ventana
warning=pygame.image.load(os.path.join("media","warn.png"))
ven=pygame.display.set_mode((dimx,dimy),pygame.FULLSCREEN)
warning.convert()
pygame.display.set_caption("Adit Games: Game 1") #Inicia el nombre de juego
background = pygame.image.load(os.path.join("media","menu.png"))
backgroundrect = background.get_rect()
background = background.convert()  
ven.blit(background,(0,0))
sprtx=0;sprty=0

#Codigo de musica
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'media')         ##para que la musica este en la carpeta media
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096) ##iniciador de mixer
paso=pygame.mixer.Sound(os.path.join(data_dir, "wood1.ogg"))         ##sonido cuando caminas
error=pygame.mixer.Sound(os.path.join(data_dir, "error.ogg"))         ##sonido de error
menu=pygame.mixer.Sound(os.path.join(data_dir, "menu.ogg"))     ##musica del menu
#menu.set_volume(0.7)       ##volumen del menu
pygame.mixer.Sound.play(menu, loops=-1) ##se reproduce la musica de fondo
click1=pygame.mixer.Sound(os.path.join(data_dir, "hit1.ogg"))
cambiarmusica = False
test=pygame.mixer.Sound(os.path.join(data_dir, "test.ogg"))  ##test para cambio de musica (sera cambiada)

clock = pygame.time.Clock()        #clock para milisec.
juego = False
creditos = False
instructions = False
menuloop=True
charselect=False
pausa=False
FPS = 65                 #FPS dejemos la caga con los fps :D okno C:
playtime = 0
cycletime = 0
interval = .10 # cuanto tiempo esta cada imagen app .-.
picnr = 0
posx=300;posy=300 #posiciones de img
der= False;aba=False;izq=False;arr= False # variables de movimiento en falso
standf=True;standb=False #detenido hacia adelante o atras
balas=[]
while menuloop:
    if cambiarmusica==True:
        pygame.mixer.Sound.stop(test)
        pygame.mixer.Sound.play(menu, loops=-1)
        cambiarmusica=False
    mouspos=pygame.mouse.get_pos()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego = False # X de la ventana
            
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True: #Ejecuta el juego
                    if (500<mouspos[0]<750 )and (300<mouspos[1]<340): #Start Game
                        cambiarmusica = True
                        pygame.mixer.Sound.play(click1)
                        #juego=True;background.fill((255,255,255)) #comentado por q pasa a charselect
                        charselect=True
                        background = pygame.image.load(os.path.join("media","Characters_Selector.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                    if (530<mouspos[0]<710)and (350<mouspos[1]<390): #opciones (sonido de error)
                        pygame.mixer.Sound.play(error)
                    if (530<mouspos[0]<710)and (400<mouspos[1]<440): #creditos
                        pygame.mixer.Sound.play(click1)
                        background = pygame.image.load(os.path.join("media","creditos.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        creditos = True
                    if (480<mouspos[0]<780)and (450<mouspos[1]<490): #instrucciones
                        pygame.mixer.Sound.play(click1)
                        background = pygame.image.load(os.path.join("media","instructions.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        instructions = True
                    if (560<mouspos[0]<680)and (500<mouspos[1]<540): # exit del "menu"
                        pygame.mixer.Sound.play(click1)
                        sys.exit() 

    while charselect:
        #cambiar_musica(cambiarmusica,charselect,menu,test)
        if cambiarmusica == True:
            pygame.mixer.Sound.stop(menu)
            pygame.mixer.Sound.play(test, loops=-1)
            cambiarmusica = False
        mouspos=pygame.mouse.get_pos()

        #los personajes se mueven en el menu :P
        posx=300;posy=300
        spritesheet = pygame.image.load(os.path.join("media","Arq44x76.png"))
        spritesheet.convert()
        arq=[];sprtx=48;sprty=76
        init_sprite(arq,spritesheet,sprtx,sprty)

        spritegue = pygame.image.load(os.path.join("media","Gue45x57.png"))
        spritegue.convert()
        gue=[];guex=45;guey=57
        init_sprite(gue,spritegue,guex,guey)

        FPS = 5
        milliseconds = clock.tick(FPS)  # milisec despues del ultimo frame
        seconds = milliseconds * 1000.0 # seconds q pasaron del utimo frame
        playtime += seconds
        cycletime += seconds
        ven.blit(background.subsurface((posx,posy,48,76)),(73,73)) ##
        ven.blit(arq[picnr], (73,73)) 
        ven.blit(background.subsurface((posx,posy,45,57)),(73,196)) ##
        ven.blit(gue[picnr], (73,196)) 
        picnr += 1
        if picnr > 19:
            picnr = 0
        cycletime = 0

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    cambiarmusica=True
                    creditos = False;background = pygame.image.load(os.path.join("media","menu.png"))
                    charselect = False
                    ven.blit(background,(0,0))
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True: #Ejecuta el juego
                    if (62<mouspos[0]<325)and (64<mouspos[1]<160):
                        spritesheet = pygame.image.load(os.path.join("media","Arq44x76.png"))
                        spritesheet.convert()
                        arq=[];sprtx=48;sprty=76
                        init_sprite(arq,spritesheet,sprtx,sprty)
                        posx=300;posy=300
                        pygame.mixer.Sound.play(click1)
<<<<<<< HEAD
                        juego=True;background= pygame.image.load(os.path.join("media","background_resized.png"))
=======
                        juego=True;background= pygame.image.load(os.path.join("media","fase_01.png"))
>>>>>>> ca02cf45f207b7d1128e1bb80dc03bf7a0e2841c
                        background = background.convert()
                        ven.blit(background,(0,0))
                        charselect = False
                    elif (62<mouspos[0]<350)and (190<mouspos[1]<255):
                        spritesheet = pygame.image.load(os.path.join("media","Gue45x57.png"))
                        spritesheet.convert()
                        arq=[];sprtx=45;sprty=57
                        init_sprite(arq,spritesheet,sprtx,sprty)
                        posx=300;posy=300
                        pygame.mixer.Sound.play(click1)
                        juego=True;background= pygame.image.load(os.path.join("media","fase_01.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        charselect = False
        pygame.display.flip()

    while creditos:
        mouspos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    creditos = False;background = pygame.image.load(os.path.join("media","menu.png"))
                    background.convert()
                    ven.blit(background,(0,0))
        pygame.display.flip()

    while instructions:
        mouspos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    instructions = False;background = pygame.image.load(os.path.join("media","menu.png"))
                    background.convert()
                    ven.blit(background,(0,0))
        pygame.display.flip()
    
    while juego:         
        if cambiarmusica == True:
            pygame.mixer.Sound.stop(menu)
            pygame.mixer.Sound.play(test, loops=-1)
            cambiarmusica = False
        FPS = 65
        milliseconds = clock.tick(FPS)  # milisec despues del ultimo frame
        seconds = milliseconds / 1000.0 # seconds q pasaron del utimo frame
        playtime += seconds
        cycletime += seconds
        mypicture = arq[picnr]
        mouspos=pygame.mouse.get_pos()
        centrx,centry=(posx+sprtx/2), (posy+sprty/2)
        dx, dy = mouspos[0]-centrx, mouspos[1]-centry

        #proyectiles!!!
        nb=0
        for prr in balas:
            prr.mover()
            if prr.comprovar() == False:
                if prr.posx<0:prr.posx+=6
                if prr.posy<0:prr.posy+=6
                if prr.posy>684:prr.posy-=3
                ven.blit(background.subsurface((prr.posx,prr.posy,prr.prox,prr.proy)),(prr.posx,prr.posy))
                delete=balas.pop(nb)
                print len(balas)
            nb+=1
        #condicionales de stand y direccion
        if (der and izq and arr and aba) == False:
            standf=True
        if (der or izq or arr or aba) == True:
            standf=False
        if cycletime > interval:
            if standf:
                picnr=0
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) #limpia imagen anterior
                ven.blit(mypicture, (posx,posy))     

            if (der or aba)and not (arr or izq):
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 3:
                    picnr = 1       

            if izq and not (der or aba or arr):
                if picnr!=12:
                    picnr=11
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 13:
                    picnr = 11

            if (aba and izq) and not (arr or der):
                if picnr!=12:
                    picnr=11
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 13:
                    picnr = 11

            if (aba and izq and der) and not (arr):
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 3:
                    picnr = 1   

            if (arr and der) and not (aba and izq):
                if picnr!=15:
                    picnr=14
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 16:
                    picnr = 14

            if arr and not der:
                if picnr!=5:
                    picnr=4
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                picnr += 1
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                if picnr >= 6:
                    picnr = 4

            # if (der and arr and pygame.mouse.get_pressed()[0]):
            # if (posx< mouspos[0] and posy>mouspos[0] and pygame.mouse.get_pressed()[0]):
            #     picnr = 17
            #     ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
            #     ven.blit(mypicture, (posx,posy))
            cycletime = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego = False # X de la ventana
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE: 
                    background = pygame.image.load(os.path.join("media","pause.png"))
                    background.convert()
                    ven.blit(background,(0,0))
                    pausa = True
                    juego = False
                    #juego = False
                    #cambiarmusica=True
                #if presionar tecla
                if event.key == pygame.K_d: der=True
                if event.key == pygame.K_a: izq = True
                if event.key == pygame.K_w: arr= True
                if event.key == pygame.K_s: aba= True
            elif event.type == pygame.KEYUP:
                #if soltar tecla
                if event.key == pygame.K_d: der=False
                if event.key == pygame.K_a: izq = False
                if event.key == pygame.K_w: arr= False
                if event.key == pygame.K_s: aba= False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    ven.blit(warning,(random.randint(0,dimx),random.randint(0,dimy)))
                    balas.append(proyect(ven,posx,posy,9,background,direccion(angulo((mouspos[0]-centrx),(mouspos[1]-centry)))))
                    balas[len(balas)-1].poner()
                    pygame.mixer.Sound.play(click1)
        if der and posx<(dimx-sprtx):
            ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy))#limpia y redibuja
            posx +=3;ven.blit(mypicture, (posx,posy))
        if izq and posx > 0:
            ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy))
            posx -=3;ven.blit(mypicture, (posx,posy))
        if arr and posy > 0:
            ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy))
            posy -=3;ven.blit(mypicture, (posx,posy))
        if aba and posy<(dimy-sprty):
            ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy))
            posy +=3;ven.blit(mypicture, (posx,posy))

        pygame.display.flip()

    while pausa:
        mouspos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    if (540<mouspos[0]<741)and (280<mouspos[1]<314): #Continue
                        print 'sacar pausa'
                        #cambiarmusica = True
                        pygame.mixer.Sound.play(click1)
                        background = pygame.image.load(os.path.join("media","fase_01.png")).convert
                        #background.convert()
                        ven.blit(background,(0,0))
                        juego=True
                        pausa=False
                    elif (540<mouspos[0]<741)and (327<mouspos[1]<358): #Restart
                        pygame.mixer.Sound.play(click1)
                        posx=300;posy=300
                        background.fill((255,255,255))
                        background.convert()
                        ven.blit(background,(0,0))
                        pausa=False
                        juego=True
                    elif (540<mouspos[0]<741)and (371<mouspos[1]<403): #Help
                        pygame.mixer.Sound.play(error)
                    elif (540<mouspos[0]<741)and (419<mouspos[1]<448):#MainMenu
                        pygame.mixer.Sound.play(click1)
                        background = pygame.image.load(os.path.join("media","menu.png"))
                        background.convert()
                        ven.blit(background,(0,0))
                        pausa=False
                        juego=False
                        cambiarmusica=True
        pygame.display.flip()

    pygame.display.flip()