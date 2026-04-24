import random
import matplotlib.pyplot as plt
import keyboard
import cv2
import numpy as np
import ffmpeg
import imageio as iio
import subprocess
import os

def showpic(img):
    plt.imshow(img)
    plt.show()
    return

name=str(input("Nom de l'enregistrement : "))
n=int(input("Nombre de fourmis à représenter"))
nb_images=int(input("Nombre d'images à onbtenir"))
nb_étapes=int(input("nombre d'étapes souhaitées"))
frq_images=nb_étapes//nb_images

scr_h=2400
scr_w=2400
cell_size=8
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
        return self.grid

ant=langton_ant()

stock=[]
while cpt<=nb_étapes :
    img=ant.move()
    if cpt%frq_images==0:
        img2=[[[img[y][x][i] for i in range(3)] for x in range(grid_w)] for y in range(grid_h)]
        stock.append(img2)
    cpt+=1
    print(cpt)
    

#showpic(stock[cpt-1])

#iio.imwrite('test3.gif', stock[cpt-1], format='gif')

#for i in range(cpt):
#   plt.imshow(stock[i])
#   plt.savefig(f"images/{i}.jpg")

#frames=np.stack([iio.imread(f"images/{i}.jpg") for i in range(cpt)], axis=0)
#iio.mimwrite('test4.gif', frames)

#supprimer les images déjà présentes

numi=0
while 1:
    try:
        os.remove(f"images/{numi}.jpg")
    except OSError:
        break
    numi+=1 

#version plus efficace avec que qq images à chaque fois pour avoir peut être bcp plus d'étapes :
   
for i in range(nb_images):
    plt.imshow(stock[i])
    plt.savefig(f"images/{i}.jpg")

frames=np.stack([iio.imread(f"images/{i}.jpg") for i in range(nb_images)], axis=0)
iio.mimwrite(name+'.gif', frames)
    
#codec=cv2.VideoWriter_fourcc(*'FFV1')
#fps=60
#width, height = grid_w, grid_h

#out = cv2.VideoWriter('output_video9.mov', codec, fps, (width, height))

#for i in range(cpt):
 #   img=np.array(stock[i])
  #  out.write(img)
    
#out.release()
#cv2.destroyAllWindows()

# Exécution de FFmpeg via subprocess pour plus de contrôle
#command = [
#    'ffmpeg',
 #   '-framerate', '60',  # Fréquence d'images
  #  '-i', 'image_%03d.png',  # Modèle des images
   # '-c:v', 'ffv1',  # Codec FFV1
    #'-compression_level', '0',  # Moins de compression
    #'output_video.avi'  # Fichier de sortie
#]

#subprocess.run(command)


#ffmpeg -i output_video9.mp4 -c:v libx264 -crf 18 -preset slow -tune film output_video_high_quality.mp4
print("c'est fini bro")

    