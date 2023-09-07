from window import Window,Vector,remap
import random

win = Window(0,0,800,800)
Board = []
for i in range(4):
    Board.append([])
    for j in range(4):
        Board[i].append(0)


def empty(Board):
    emp = []
    for i in range(4):
        for j in range(4):
            if Board[i][j]==0:
                emp.append((i,j))
    return emp

a=empty(Board)
num = random.randint(0,len(a)-1)
num2 = random.random()
if num2 < 0.9:
    Board[a[num][0]][a[num][1]]=1
else:
    Board[a[num][0]][a[num][1]]=2
b=empty(Board)
num = random.randint(0,len(b)-1)
num2 = random.random()
if num2 < 0.9:
    Board[b[num][0]][b[num][1]]=1
else:
    Board[b[num][0]][b[num][1]]=2


def show():
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            win.strokeWidth(5)
            win.stroke(30,30,30)
            r= remap(Board[i][j],0,15,150,250)
            g= remap(Board[i][j],0,15,150,70)
            b= remap(Board[i][j],0,15,150,20)
            win.fill(r,g,b)
            win.rect(Vector(-300+j*200,300-i*200),200,200)
            if Board[i][j]!=0:
                win.strokeWidth(4)
                win.write(Vector(-300+j*200,280-i*200),str(pow(2,Board[i][j])),4)

def tick(Board):
    a = empty(Board)
    num=random.randint(0,len(a)-1)
    num2 = random.random()
    if num2 < 0.9:
        Board[a[num][0]][a[num][1]]=1
    else:
        Board[a[num][0]][a[num][1]]=2

def move(Board):
    moved=False
    key = win.keyboard()
    if key != None and key[2]=="DOWN":
        if key[1] == 119: #up
            for j in range(4):
                i=0
                while i<3:
                    if Board[i][j]==0:
                        if Board[i+1][j]!=0 :
                            Board[i][j]=Board[i+1][j]
                            Board[i+1][j]=0
                            moved=True
                            i=-1
                    else: 
                        if Board[i][j]==Board[i+1][j]:
                            Board[i][j]+=1
                            Board[i+1][j]=0
                            moved=True
                            i=-1
                    i+=1

        elif key[1] == 97: #left
            for i in range(4):
                j=0
                while j<3:
                    if Board[i][j]==0:
                        if Board[i][j+1]!=0 :
                            Board[i][j]=Board[i][j+1]
                            Board[i][j+1]=0
                            moved=True
                            j=-1
                    else: 
                        if Board[i][j]==Board[i][j+1]:
                            Board[i][j]+=1
                            Board[i][j+1]=0
                            moved=True
                            j=-1
                    j+=1

        elif key[1] == 100: #right
            for i in range(4):
                j=3
                while j>0:
                    if Board[i][j]==0:
                        if Board[i][j-1]!=0 :
                            Board[i][j]=Board[i][j-1]
                            Board[i][j-1]=0
                            moved=True
                            j=4
                    else: 
                        if Board[i][j]==Board[i][j-1]:
                            Board[i][j]+=1
                            Board[i][j-1]=0
                            moved=True
                            j=4
                    j-=1

        elif key[1] == 115: #down
            for j in range(4):
                i=3
                while i>0:
                    if Board[i][j]==0:
                        if Board[i-1][j]!=0 :
                            Board[i][j]=Board[i-1][j]
                            Board[i-1][j]=0
                            moved=True
                            i=4
                    else: 
                        if Board[i][j]==Board[i-1][j]:
                            Board[i][j]+=1
                            Board[i-1][j]=0
                            moved=True
                            i=4
                    i-=1
    
    return moved
        


def setup():
    pass

def draw():
    show()
    if move(Board):
        tick(Board)

win.run(setup,draw,10)
