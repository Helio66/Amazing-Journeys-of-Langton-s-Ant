crypted=str(input("message to decrypt : "))
decryption_key=tuple(map(int,input("decryption key with the shape x y : ").split()))
nb=int(input("number of iterations : "))
d=int(input("initial direction : "))

def decrypt(grid,p,nb,d):
    
    dim_h=len(grid)
    dim_w=7
    
    grid_h=dim_h
    grid_w=dim_w
    
    cpt = 0
    
    Dir=[(0,-1), (1,0), (0,1), (-1, 0)]
    
    class langton_ant:
        def __init__(self):
            self.x=p[0]
            self.y=p[1]
            self.dir=(d+2)%4
            self.grid=grid
            
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
            
            self.x%=grid_w
            self.y%=grid_h
            return self.grid

    ant=langton_ant()
    if nb==0:
        mess2=[[grid[i][j] for j in range(grid_w)] for i in range(grid_h)]
    for i in range(nb) :
        if i==nb-1:
            mess2=ant.move()
        else:
            ant.move()
        cpt+=1
    return mess2

alpha=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ','.',',','?','!',':',
      'A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','é','è','\'','à','ù','-']

alph=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 
       't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 
       'X', 'Y', 'Z', '!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', 
       '`', '{', '|', '}', '~', ' ', '\t', '\n', '¤', '£', 'µ','é', 'è', 'ç', 'à', 'ù', '€', '°', '☺', '☻', '♥', '♦', '♣', '♠', '•', '◘', '○', '◙', '♂',
       '♀', '♪', '♫', '☼', '►', '◄', '↕', '¶', '§', 'µ']

def findmax(n):
    i=0
    maxi=0
    while 2**i <= n:
        maxi=i
        i+=1
    return maxi

def ten2two(n):
    i=findmax(n)
    n2=[0 for _ in range(7)]
    while n!=0:
        n2[i]=1
        n-=2**i
        i=findmax(n)
    return n2

def two2ten(n2):
    n=0
    for i in range (len(n2)):
        if n2[i]==1:
            n+=2**i
    return n

def str2seq(S, a):
    L=[]
    for s in S:
        i=0
        while s!=a[i]:
            i+=1
        n2=ten2two(i)
        L.append(n2)
    return L

def seq2str(L,a):
    S=''
    for l in L:
        i=two2ten(l)
        S+=a[i]
    return S

print("decrypted message :", seq2str(decrypt(str2seq(crypted, alph),decryption_key,nb,d),alph))

