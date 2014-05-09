import pygame,math,os
from pygame.locals import *
def init_sprite(arq,spritesheet,sprtx,sprty):
    for alf in range(1,21,1): # recorrer 10 elementos para arq
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
class proyect():
    def __init__(self,sur,pox,poy,velo,back,dirr):
        self.surf=sur
        self.posx=pox
        self.posy=poy
        self.dire=dirr
        self.vel=velo
        self.back=back
        self.prox=14;self.proy=36
        self.arr=pygame.image.load(os.path.join("media","Arrow.png"))
    def poner(self,):
        self.surf.blit(self.arr,(self.posx,self.posy))
    def comprovar(self):
        if 0< self.posx < 1265 and 0< self.posy < 682:
            return True
        else:
            return False

    def mover(self):
        if self.dire=="nn":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posy-=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="ne":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx+=self.vel
                self.posy-=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="no":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx-=self.vel
                self.posy-=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="ss":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posy+=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="se":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx+=self.vel
                self.posy+=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="so":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx-=self.vel
                self.posy+=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="ee":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx+=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
        elif self.dire=="oo":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.posx-=self.vel
                self.surf.blit(self.arr,(self.posx,self.posy))
    def __del__(self):
        class_name = self.__class__.__name__
def direccion(angulo):
    if (337.5<=angulo<360 or 0<=angulo<22.5):
        return 'nn'
    if 22.5<= angulo < 67.5:
        return 'ne'
    if 67.5<=angulo<112.5:
        return 'ee'
    if 112.5<=angulo<157.5:
        return 'se'
    if 157.5<=angulo<202.5:
        return 'ss'
    if 202.5<=angulo<247.5:
        return 'so'
    if 247.5<=angulo<292.5:
        return 'oo'
    if 292.5<=angulo<337.5:
        return 'no'

