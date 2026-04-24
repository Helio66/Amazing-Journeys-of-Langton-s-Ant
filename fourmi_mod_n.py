import pygame
import sys
import random
import math

pygame.init()

n=int(input("Nombre de fourmis à représenter"))
d=int(input("Densité des fourmis sur l'écran (nombre par carré de côté 100)"))

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
        
            self.x[i]%=grid_w
            self.y[i]%=grid_h
    
    def draw(self, scr):
        for y in range (grid_h):
            for x in range (grid_w):
                color = self.grid[y][x]
                pygame.draw.rect(scr, color, (x*cell_size, y*cell_size, cell_size, cell_size))

scr = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Fourmi de Langton (mod n)")

font=pygame.font.Font(None, 24)

ant=langton_ant()
clock = pygame.time.Clock()

while 1 :
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    ant.move()
    scr.fill(white)
    ant.draw(scr)
    cpt+=1
    txt = font.render("étape : "+str(cpt),1,(255,255,255))
    scr.blit(txt, (10, 10))
    pygame.display.flip()
    #clock.tick(3)
    

