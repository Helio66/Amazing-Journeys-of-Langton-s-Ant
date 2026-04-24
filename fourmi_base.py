import pygame
import sys

pygame.init()

scr_h=400
scr_w=400
cell_size=5
grid_h=scr_h//cell_size
grid_w=scr_w//cell_size

black=(255,255,255)
white=(50,50,50)

cpt=0

Dir=[(0,-1), (1,0), (0,1), (-1, 0)]

class langton_ant:
    def __init__(self):
        self.x=grid_w//2
        self.y=grid_h//2
        self.dir=0
        self.grid=[[0]*grid_w for _ in range (grid_h)]
        
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

scr = pygame.display.set_mode((scr_w, scr_h))
font=pygame.font.Font(None, 24)
pygame.display.set_caption("Fourmi de Langton (base)")

ant=langton_ant()
clock = pygame.time.Clock()

a=(grid_w//2, grid_h//2)
while 1 :
    for e in pygame.event.get():
        if e.type==pygame.QUIT:
            pygame.quit()
            sys.exit()
    while 1 :
        for e in pygame.event.get():
            if e.type==pygame.QUIT:
                pygame.quit()
                sys.exit()
        if a[0]>=grid_w or a[0]<0 or a[1]>=grid_h or a[1]<0:
            break
        a=ant.move()
        scr.fill(white)
        ant.draw(scr)
        cpt+=1
        txt = font.render("étape : "+str(cpt),1,(255,255,255))
        scr.blit(txt, (10, 10))
        pygame.display.flip()
        #clock.tick(3)
        
    
