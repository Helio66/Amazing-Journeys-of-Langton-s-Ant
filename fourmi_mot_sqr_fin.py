import pygame
import sys
import random

pygame.init()

dim=random.randint(1,200)

cell_size=5
scr_h=dim*cell_size
scr_w=dim*cell_size

grid_h=dim
grid_w=dim

black=(255,255,255)
white=(50,50,50)

cpt = 0

Dir=[(0,-1), (1,0), (0,1), (-1, 0)]

class langton_ant:
    def __init__(self):
        self.x=grid_w//2
        self.y=grid_h//2
        self.dir=0
        self.grid=[[random.randint(0,1) for _ in range (grid_w)] for _ in range (grid_h)]
        
    def move(self):
        crt_cell=self.grid[self.y][self.x]
        if crt_cell==0:
            self.grid[self.y][self.x]=1
            self.dir=(self.dir + 1)%4
        else:
            self.grid[self.y][self.x]=0
            self.dir=(self.dir - 1)%4  
            
        self.x+=Dir[self.dir][0]
        self.y+=Dir[self.dir][1]
        return (self.x, self.y)
        
    def draw(self, scr):
        for y in range (grid_h):
            for x in range (grid_w):
                color = white if self.grid[y][x]==0 else black
                pygame.draw.rect(scr, color, (x*cell_size, y*cell_size, cell_size, cell_size))
                
    def exp_grid(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[0]*(grid_w+2) for _ in range(grid_h+2)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y+1][x+1]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=2
        grid_h+=2
        
        self.x+=1
        self.y+=1
        
        scr_h+=cell_size*2
        scr_w+=cell_size*2
        pygame.display.set_mode((scr_w, scr_h))

scr = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Fourmi de Langton (motif carré fini)")

font=pygame.font.Font(None, 24)

ant=langton_ant()
clock = pygame.time.Clock()

a=(grid_w//2, grid_h//2)
while 1 :
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if a[0]>=grid_w or a[0]<0 or a[1]>=grid_h or a[1]<0:
        ant.exp_grid()
    a=ant.move()
    scr.fill(white)
    ant.draw(scr)
    cpt+=1
    txt = font.render("étape : "+str(cpt),1,(255,255,255))
    scr.blit(txt, (10, 10))
    pygame.display.flip()
    #clock.tick(3)
    



