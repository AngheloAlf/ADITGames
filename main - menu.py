import pygame, sys, os, random
from pygame.locals import *
pygame.init() #inicia pygame
#inicia la ventana y su nombre
dimx=1280;dimy=720 #dimensiones de la ventana
char=""
while True:
   char=raw_input("Arquera [A] o Guerrero [G]?? ")
   if char=="A" or char=="G":
      break
   else:print "Intente nuevamente"
if char=="A":
   sprtx=48;sprty=76
   spritesheet = pygame.image.load(os.path.join("media","Arq44x76.png"))
else:
   sprtx=45;sprty=57
   spritesheet = pygame.image.load(os.path.join("media","Gue45x57.png"))
#sprtx=48;sprty=76;#48x76 arq // 45*57 gue
#spritesheet = pygame.image.load(os.path.join("media","Arq44x76.png"))
warning=pygame.image.load(os.path.join("media","warn.png"))
ven=pygame.display.set_mode((dimx,dimy),pygame.FULLSCREEN)
spritesheet.convert();warning.convert()
pygame.display.set_caption("Nombre del juego")
background = pygame.image.load(os.path.join("media","background_resized.png"))
backgroundrect = background.get_rect()
#background.fill((255,255,255)) # relleno de fondo a cambiar por imagen
background = background.convert()  
ven.blit(background,(0,0))

#Codigo de musica
main_dir = os.path.split(os.path.abspath(__file__))[0]
data_dir = os.path.join(main_dir, 'media')         ##para que la musica este en la carpeta media
pygame.mixer.init(frequency=22050, size=-16, channels=8, buffer=4096) ##iniciador de mixer
sound=pygame.mixer.Sound(os.path.join(data_dir, "overworld1.ogg"))      ##musica de fondo(test)
paso=pygame.mixer.Sound(os.path.join(data_dir, "wood1.ogg"))         ##sonido cuando caminas
menu=pygame.mixer.Sound(os.path.join(data_dir, "menu.ogg"))     ##prueba useless :C
#menu.set_volume(0.3)       ##volumen de GR
#paso.set_volume(1.0)       ##volumen de los pasos
pygame.mixer.Sound.play(menu) ##se reproduce la musica de fondo
click1=pygame.mixer.Sound(os.path.join(data_dir, "hit1.ogg"))


arq=[]
for alf in range(1,11,1): # recorrer 10 elementos para arq
   arq.append(spritesheet.subsurface((sprtx*(alf-1),0,sprtx,sprty)))
for nbr in range(len(arq)):
    arq[nbr].set_colorkey((255,255,255)) # blanco = alpha
    arq[nbr] = arq[nbr].convert_alpha()
    print "alpha en =", nbr

clock = pygame.time.Clock()        #clock para milisec.
juego = False
menuloop=True
FPS = 65                   #FPS dejemos la caga con los fps :D okno C:
playtime = 0
cycletime = 0
interval = .10 # cuanto tiempo esta cada imagen app .-.
picnr = 0
posx=300;posy=300 #posiciones de img
der= False;aba=False;izq=False;arr= False # variables de movimiento en falso
standf=True;standb=False #detenido hacia adelante o atras
while menuloop:
    mouspos=pygame.mouse.get_pos()
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego = False # X de la ventana
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    juego = False; sys.exit() # ESC salir
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.mouse.get_pressed()[0]==True:
                    if (522<mouspos[0]<788)and (284<mouspos[1]<320):
                        #ven.blit(warning,(random.randint(0,dimx),random.randint(0,dimy)))
                        pygame.mixer.Sound.play(click1)
                        juego=True;background.fill((255,255,255))
                        background = background.convert()
                        ven.blit(background,(0,0))
                    if (588<mouspos[0]<724)and (436<mouspos[1]<470):
                        pygame.mixer.Sound.play(click1)
                        juego = False; sys.exit() # exit del "menu"

    while juego:
        milliseconds = clock.tick(FPS)  # milisec despues del ultimo frame
        seconds = milliseconds / 1000.0 # seconds q pasaron del utimo frame
        playtime += seconds
        cycletime += seconds
        mypicture = arq[picnr]
        mouspos=pygame.mouse.get_pos()
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
            if standb:
                picnr=3
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))                
            if (der or izq or aba)and (not arr):
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                picnr += 1
                if picnr >= 3:
                    picnr = 1            
            if arr:
                if picnr!=5:
                    picnr=4
                ven.blit(background.subsurface((posx,posy,sprtx,sprty)),(posx,posy)) 
                ven.blit(mypicture, (posx,posy))
                picnr += 1
                pygame.mixer.Sound.play(paso) #reproduce el sonido de los pasos cuando caminas
                if picnr >= 6:
                    picnr = 4
            cycletime = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                juego = False # X de la ventana
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    juego = False; sys.exit() # ESC salir
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
                   if (522<mouspos[0]<788)and (284<mouspos[1]<320):
                      ven.blit(warning,(random.randint(0,dimx),random.randint(0,dimy)))
                      pygame.mixer.Sound.play(click1)
                   if (588<mouspos[0]<724)and (436<mouspos[1]<470):
                      juego = False; sys.exit() # exit del "menu"
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
    pygame.display.flip()
