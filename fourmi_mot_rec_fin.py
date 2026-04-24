import pygame
import sys
import random

pygame.init()

dim_h=random.randint(0,100)
dim_w=random.randint(100,100)

cell_size=5
scr_h=dim_h*cell_size
scr_w=dim_w*cell_size

grid_h=dim_h
grid_w=dim_w

black=(0,0,0)
white=(255,255,255)

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
                
    def exp_grid_e(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[0]*(grid_w+1) for _ in range(grid_h)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=1
        grid_h+=0
        
        self.x+=0
        self.y+=0
        
        scr_h+=cell_size*0
        scr_w+=cell_size*1
        pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_o(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[0]*(grid_w+1) for _ in range(grid_h)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x+1]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=1
        grid_h+=0
        
        self.x+=1
        self.y+=0
        
        scr_h+=cell_size*0
        scr_w+=cell_size*1
        pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_s(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[0]*(grid_w) for _ in range(grid_h+1)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=0
        grid_h+=1
        
        self.x+=0
        self.y+=0
        
        scr_h+=cell_size*1
        scr_w+=cell_size*0
        pygame.display.set_mode((scr_w, scr_h))
        
    def exp_grid_n(self):
        global grid_h, grid_w, scr_h, scr_w
        new_grid=[[0]*(grid_w) for _ in range(grid_h+1)]
        
        for y in range (grid_h):
            for x in range(grid_w):
                new_grid[y+1][x]=self.grid[y][x]
        
        self.grid=new_grid
        grid_w+=0
        grid_h+=1
        
        self.x+=0
        self.y+=1
        
        scr_h+=cell_size*1
        scr_w+=cell_size*0
        pygame.display.set_mode((scr_w, scr_h))

scr = pygame.display.set_mode((scr_w, scr_h))
pygame.display.set_caption("Fourmi de Langton (motif rectangulaire fini)")

font=pygame.font.Font(None, 24)

ant=langton_ant()
clock = pygame.time.Clock()

a=(grid_w//2, grid_h//2)
while 1 :
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    if a[0]>=grid_w:
        ant.exp_grid_e()
    if a[0]<0:
        ant.exp_grid_o()
    if a[1]>=grid_h:
        ant.exp_grid_s()
    if a[1]<0:
        ant.exp_grid_n()
    a=ant.move()
    scr.fill(white)
    ant.draw(scr)
    cpt+=1
    txt = font.render("étape : "+str(cpt),1,(255,255,255))
    scr.blit(txt, (10, 10))
    pygame.display.flip()
    #clock.tick(3)
    


