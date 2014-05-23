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
    if dx == 0: ## NOOOOO CERO NOOOO x3
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
        self.prox=36;self.proy=36
        self.arr=pygame.image.load(os.path.join("media","Arrow.png"))
        self.arr.convert()
        self.arr=self.rotar()
    def poner(self,):
        self.surf.blit(self.arr,(self.posx,self.posy))
    def comprovar(self):
        if 0< self.posx < 1243 and 0< self.posy < 684:
            return True
        else:
            return False
    def rotar(self):
        if self.dire=="nn":self.arr=pygame.transform.rotate(self.arr,180);self.arr.convert()
        elif self.dire=="ne":self.arr=pygame.transform.rotate(self.arr,135);self.arr.convert()
        elif self.dire=="no":self.arr=pygame.transform.rotate(self.arr,225);self.arr.convert()
        elif self.dire=="oo":self.arr=pygame.transform.rotate(self.arr,270);self.arr.convert()
        elif self.dire=="so":self.arr=pygame.transform.rotate(self.arr,315);self.arr.convert()
        elif self.dire=="se":self.arr=pygame.transform.rotate(self.arr,45);self.arr.convert()
        elif self.dire=="ee":self.arr=pygame.transform.rotate(self.arr,90);self.arr.convert()
        return self.arr

    def mover(self):
        if self.dire=="nn":
            if self.comprovar():
                self.surf.blit(self.back.subsurface((self.posx,self.posy,self.prox,self.proy)),(self.posx,self.posy))
                self.arr.convert()
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
class foe():
    def __init__(self,sur,px,py,arrspt):
        self.surf=surf
        self.posx=px
        self.posy=py
        self.spt=arrspt
    def poner(self):
        return ''
class prota():
    def __init__(self,sur,back,px,py,clase):
        self.surf=sur
        self.back=back
        self.posx=px
        self.posy=py
        if clase == 'Gue':
            spritegue = pygame.image.load(os.path.join("media","Gue45x57.png"))
            spritegue.convert()
            gue=[]
            self.sprtx=45
            self.sprty=57
            init_sprite(gue,spritegue,self.sprtx,self.sprty)
            self.arspt=gue
        elif clase == 'Arq':
            spritesheet = pygame.image.load(os.path.join("media","Arq44x76.png"))
            spritesheet.convert()
            arq=[]
            self.sprtx=48
            self.sprty=76
            init_sprite(arq,spritesheet,self.sprtx,self.sprty)
            self.arspt=arq
        self.picnr=0 #recorre los sprites segun peticion
        #inicio de variables de movimiento
        self.der=False;self.aba=False;self.izq=False;self.arr=False
        self.standf=True;self.standb=False
        self.pnj=self.arspt[self.picnr] #la surface del personaje segun estado
    def poner(self,xx,yy):
        self.surf.blit(self.back.subsurface((self.posx,self.posy,self.sprtx,self.sprty)),(xx,yy))
        self.surf.blit(self.pnj,(xx,yy))
        self.pnj=self.arspt[self.picnr]
    # def mover(self,dir):
    #     #codigo de movimiento
