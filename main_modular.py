import pygame, sys, os, random, math
from funciones import *
from pygame.locals import *
pygame.init() #inicia pygame
#inicia la ventana   #dimensiones de la ventana
dimx,dimy        = (1280,720)
warning          = pygame.image.load(os.path.join("media","warn.png"))
ven              = pygame.display.set_mode((dimx,dimy),pygame.FULLSCREEN)
warning.convert()
pygame.display.set_caption("Adit Games: Game 1") #Inicia el nombre de juego
background     = pygame.image.load(os.path.join("media","menu.png"))
backgroundrect = background.get_rect()
background     = background.convert()  
ven.blit(background,(0,0))
sprtx,sprty    = (0,0)

#Codigo de musica
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'media')         ##para que la musica este en la carpeta media
pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096) ##iniciador de mixer
paso     = pygame.mixer.Sound(os.path.join(data_dir, "wood1.ogg"))         ##sonido cuando caminas
error    = pygame.mixer.Sound(os.path.join(data_dir, "error.ogg"))         ##sonido de error
menu     = pygame.mixer.Sound(os.path.join(data_dir, "menu.ogg"))     ##musica del menu
#menu.set_volume(0.7)       ##volumen del menu
pygame.mixer.Sound.play(menu, loops=-1) ##se reproduce la musica de fondo
click1   = pygame.mixer.Sound(os.path.join(data_dir, "hit1.ogg"))
cambiarmusica  = False
test     = pygame.mixer.Sound(os.path.join(data_dir, "test.ogg"))  ##test para cambio de musica (sera cambiada)

clock          = pygame.time.Clock()        #clock para milisec.
juego          = False
creditos       = False
instructions   = False
menuloop       = True
charselect     = False
pausa          = False
FPS            = 65      #FPS dejemos la caga con los fps :D okno C:
playtime       = 0
cycletime      = 0
interval       = .10 # cuanto tiempo esta cada imagen app .-.
picnr          = 0
posx           = 300;     posy   =300    #posiciones de img
der            = False;  aba    =False; izq=False;  arr= False # variables de movimiento en falso
standf         = True;    standb =False #detenido hacia adelante o atras
arquera        = prota(ven,posx,posy,'Arq')
guerrero       = prota(ven,posx,posy,'Gue')
foes           = []


balas=[]
while menuloop:
    if cambiarmusica==True:
        pygame.mixer.Sound.stop(test)
        pygame.mixer.Sound.play(menu, loops=-1)
        cambiarmusica  = False
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
                        menuloop=False

    while charselect:
        #cambiar_musica(cambiarmusica,charselect,menu,test)
        if cambiarmusica == True:
            pygame.mixer.Sound.stop(menu)
            pygame.mixer.Sound.play(test, loops=-1)
            cambiarmusica = False
        mouspos=pygame.mouse.get_pos()

        FPS = 5
        milliseconds = clock.tick(FPS)  # milisec despues del ultimo frame
        seconds = milliseconds * 1000.0 # seconds q pasaron del utimo frame
        playtime += seconds
        cycletime += seconds
        #personajes se mueven
        arquera.poner(73,73,background)    
        guerrero.poner(73,196,background)
        arquera.picnr += 1
        guerrero.picnr += 1
        if arquera.picnr > 19:
            arquera.picnr = 0
            guerrero.picnr = 0
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
                        Prota=prota(ven,posx,posy,'Arq')
                        pygame.mixer.Sound.play(click1)
                        juego=True;background= pygame.image.load(os.path.join("media","fase_01.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        charselect = False
                    elif (62<mouspos[0]<350)and (190<mouspos[1]<255):
                        Prota=prota(ven,posx,posy,'Gue')
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
        
        mouspos=pygame.mouse.get_pos()
        centrx,centry=(Prota.posx+Prota.sprtx/2), (Prota.posy+Prota.sprty/2)
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
                print len(balas) #comentario para revisar estado de balas DEBUGGER 
            nb+=1
        #condicionales de stand y direccion
        if (Prota.der and Prota.izq and Prota.arr and Prota.aba) == False:
            Prota.standf=True
        if (Prota.der or Prota.izq or Prota.arr or Prota.aba) == True:
            Prota.standf=False
        if cycletime > interval:
            Prota.mover(background)
            for f in foes:
                f.buscar(Prota)
                f.mover(background)
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
                if event.key == pygame.K_d: Prota.der  =True
                if event.key == pygame.K_a: Prota.izq  = True
                if event.key == pygame.K_w: Prota.arr  = True
                if event.key == pygame.K_s: Prota.aba  = True
            elif event.type == pygame.KEYUP:
                #if soltar tecla
                if event.key == pygame.K_d: Prota.der  =False
                if event.key == pygame.K_a: Prota.izq  = False
                if event.key == pygame.K_w: Prota.arr  = False
                if event.key == pygame.K_s: Prota.aba  = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    foes.append(foe(ven,random.randint(0,dimx),random.randint(0,dimy),'Foe'))
                    foes[-1].vel=1
                    #ven.blit(warning,(random.randint(0,dimx),random.randint(0,dimy)))
                    balas.append(proyect(ven,Prota.posx,Prota.posy,9,background,direccion(angulo((mouspos[0]-centrx),(mouspos[1]-centry)))))
                    balas[len(balas)-1].poner()
                    pygame.mixer.Sound.play(click1)

        Prota.desp(dimx,dimy,background)
        for f in foes:
                f.desp(dimx,dimy,background)
        pygame.display.flip()

    while pausa:
        mouspos=pygame.mouse.get_pos()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    if (540<mouspos[0]<741)and (280<mouspos[1]<314): #Continue
                        print 'Pause: Continue'
                        #cambiarmusica = True
                        pygame.mixer.Sound.play(click1)
                        juego=True;background= pygame.image.load(os.path.join("media","fase_01.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        pausa=False
                    elif (540<mouspos[0]<741)and (327<mouspos[1]<358): #Restart
                        print 'Pause: Restart'
                        pygame.mixer.Sound.play(click1)
                        posx=300;posy=300
                        juego=True;background= pygame.image.load(os.path.join("media","fase_01.png"))
                        background = background.convert()
                        ven.blit(background,(0,0))
                        pausa=False
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
pygame.quit()
