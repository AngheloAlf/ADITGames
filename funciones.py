import pygame,math
from pygame.locals import *
def init_sprite(arq,spritesheet,sprtx,sprty):
    for alf in range(1,11,1): # recorrer 10 elementos para arq
       arq.append(spritesheet.subsurface((sprtx*(alf-1),0,sprtx,sprty)))
    for nbr in range(len(arq)):
        arq[nbr].set_colorkey((255,255,255)) # blanco = alpha
        arq[nbr] = arq[nbr].convert_alpha()
        print "alpha en =", nbr
def angulo(dx,dy):
    # """Angulos desde 0 a 360 en sentido HORARIO 
    # el 0 esta arriba!
    # """
    if dx == 0: ## Special case to prevent zero-division
        if dy > 0:
            return 180
        elif dy < 0:
            return 0
        else:
            return None
    oa = float(dy)/float(dx)
    theta = math.degrees(math.atan(oa)) + 90.0
    if dx > 0:
        return theta
    else:
        return 180+theta
    return theta
# def cambiar_musica(cambiarmusica,charselect,parar,comenz):
# 	#pygame.mixer.init(frequency=44100, size=-16, channels=2, buffer=4096)
# 	if cambiarmusica == True and charselect == True:
# 	    pygame.mixer.Sound.stop(parar)
# 	    pygame.mixer.Sound.play(comenz, loops=-1)
# 	    cambiarmusica = False
#     #return cambiarmusica