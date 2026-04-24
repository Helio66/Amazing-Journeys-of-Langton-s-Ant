import pygame
import sys
import random
import math
import matplotlib.pyplot as plt
import numpy as np
import imageio as iio
import os

pygame.init()
name=str(input("Nom de l'enregistrement : "))
n=int(input("Nombre de fourmis à représenter : "))
d=int(input("Densité des fourmis sur l'écran (nombre par carré de côté 100) (approximatif) : "))
nb_images=int(input("Nombre d'images à obtenir"))
nb_étapes=int(input("nombre d'étapes souhaitées"))
frq_images=nb_étapes//nb_images

scr_h=int(math.sqrt((n*10000)/d))
scr_w=int(math.sqrt((n*10000)/d))
cell_size=2
grid_h=scr_h//cell_size
grid_w=scr_w//cell_size

white=[50,50,50]
colors=[]
while len(colors)<n:
    test=False
    r=random.randint(0,255)
    g=random.randint(0,255)
    b=random.randint(0,255)
    if n>=6:
        e=256//(n//3)
    else:
        e=50
    for c in colors:
        if c[0]-e<=r<=c[0]+e and c[1]-e<=g<=c[1]+e and c[2]-e<=b<=c[2]+e :
            test=True
    if test==False:
        colors.append([r,g,b])

cpt=0

Dir=[(0,-1), (1,0), (0,1), (-1, 0)]

class langton_ant:
    def __init__(self):
        self.x=[random.randint(10,grid_w -10) for _ in range(n)]
        self.y=[random.randint(10,grid_h -10) for _ in range(n)]
        self.dir=[random.randint(0,3) for _ in range(n)]
        self.grid=[[[50,50,50]]*grid_w for _ in range (grid_h)]
        
    def init(self):
        return (self.x, self.y)
        
    def move(self):
        crt_cell=[self.grid[self.y[i]][self.x[i]] for i in range(n)]
        for i in range(n):
            if crt_cell[i]==white:
                self.grid[self.y[i]][self.x[i]]=colors[i]
                self.dir[i]=(self.dir[i] + 1)%4
            else:
                self.grid[self.y[i]][self.x[i]]=white
                self.dir[i]=(self.dir[i] - 1)%4
            
        for i in range(n):
            self.x[i]+=Dir[self.dir[i]][0]
            self.y[i]+=Dir[self.dir[i]][1]
        
            #self.x[i]%=grid_w
            #self.y[i]%=grid_h
        return ((self.x, self.y), self.grid)
    
    '''def draw(self, scr):
        for y in range (grid_h):
            for x in range (grid_w):
                color = self.grid[y][x]
                pygame.draw.rect(scr, color, (x*cell_size, y*cell_size, cell_size, cell_size))'''
                
    def exp_grid_e(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[white]*(grid_w+1) for _ in range(grid_h)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=1
        grid_h+=0
        
        #self.x+=0
        #self.y+=0
        
        scr_h+=cell_size*0
        scr_w+=cell_size*1
        #pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_o(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[white]*(grid_w+1) for _ in range(grid_h)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x+1]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=1
        grid_h+=0
        
        for i in range (n):
            self.x[i]+=1
        #self.y+=0
        
        scr_h+=cell_size*0
        scr_w+=cell_size*1
        #pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_s(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[white]*(grid_w) for _ in range(grid_h+1)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=0
        grid_h+=1
        
        #self.x+=0
        #self.y+=0
        
        scr_h+=cell_size*1
        scr_w+=cell_size*0
        #pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_n(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[white]*(grid_w) for _ in range(grid_h+1)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y+1][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=0
        grid_h+=1
        
        #self.x+=0
        for i in range (n):
            self.y[i]+=1
        
        scr_h+=cell_size*1
        scr_w+=cell_size*0
        #pygame.display.set_mode((scr_w, scr_h))


ant=langton_ant()
a=ant.init()
stock=[]
while cpt<=nb_étapes :
    for i in range (n):
        if a[0][i]>=grid_w:
            ant.exp_grid_e()
        if a[0][i]<0:
            ant.exp_grid_o()
        if a[1][i]>=grid_h:
            ant.exp_grid_s()
        if a[1][i]<0:
            ant.exp_grid_n()
    img=ant.move()[1]
    if cpt%frq_images==0:
        img2=[[[img[y][x][i] for i in range(3)] for x in range(grid_w)] for y in range(grid_h)]
        stock.append(img2)
        print(cpt)
    cpt+=1
    
    
'''while 1 :
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    for i in range (n):
        if a[0][i]>=grid_w:
            ant.exp_grid_e()
        if a[0][i]<0:
            ant.exp_grid_o()
        if a[1][i]>=grid_h:
            ant.exp_grid_s()
        if a[1][i]<0:
            ant.exp_grid_n()
    a=ant.move()
    scr.fill(white)
    ant.draw(scr)
    cpt+=1
    txt = font.render("étape : "+str(cpt),1,(255,255,255))
    scr.blit(txt, (10, 10))
    pygame.display.flip()
    #clock.tick(3)'''

numi=0
while 1:
    try:
        os.remove(f"images/{numi}.jpg")
    except OSError:
        break
    numi+=1 

for i in range(nb_images):
    plt.imshow(stock[i])
    plt.savefig(f"images/{i}.jpg")

frames=np.stack([iio.imread(f"images/{i}.jpg") for i in range(nb_images)], axis=0)
iio.mimwrite(name+'.gif', frames)

print("c'est fini bro")
    

