from copy import deepcopy
from window import Window,Vector
from time import time
import random

remap = lambda value, min1, max1, min2, max2: min2 + (value - min1) * (max2 - min2) / (max1 - min1)
win = Window(0,0,800,800)
Board = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]

gradient=[
    [[10,9,8,7],[3,4,5,6],[2,1,0,0],[0,0,0,0]],
    [[7,8,9,10],[6,5,4,3],[0,0,1,2],[0,0,0,0]],
    [[0,0,0,0],[2,1,0,0],[3,4,5,6],[10,9,8,7]],
    [[0,0,0,0],[0,0,1,2],[6,5,4,3],[7,8,9,10]],

    [[10,3,2,0],[9,4,1,0],[8,5,0,0],[7,6,0,0]],
    [[7,6,0,0],[8,5,0,0],[9,4,1,0],[10,3,2,0]],
    [[0,2,3,10],[0,1,4,9],[0,0,5,8],[0,0,6,7]],
    [[0,0,6,7],[0,0,5,8],[0,1,4,9],[0,2,3,10]]
]

def score(b):
    score=0

    for i in range(4):

        # monotonicity of board
        if b[i][0]>=b[i][1] and b[i][1]>=b[i][2]and b[i][2]>=b[i][3]:
            score+=16

        elif b[i][0]<=b[i][1] and b[i][1]<=b[i][2]and b[i][2]<=b[i][3]:
            score+=16
        else:
            score-=16

        if b[0][i]>=b[1][i] and b[1][i]>=b[2][i] and b[2][i]>=b[3][i]:
            score+=16

        elif b[0][i]<=b[1][i] and b[1][i]<=b[2][i] and b[2][i]<=b[3][i]:
            score+=16
        else:
            score-=16

        for j in range(4):
            if b[i][j]==0:
                score+=4

    maxi=-99999999999
    for grad in gradient:
        current=0
        for i in range(4):
            for j in range(4):
                current+=pow(2,grad[i][j])*pow(2.5,b[i][j])

        maxi=max(maxi,current)

    score+=maxi

    return score



def moves(B):
    boards=[]
    moved=False

    Board=deepcopy(B)
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

    if moved:
        boards.append(Board)
        moved=False

    Board=deepcopy(B)
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

    if moved:
        boards.append(Board)
        moved=False

    Board=deepcopy(B)
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

    if moved:
        boards.append(Board)
        moved=False

    Board=deepcopy(B)
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

    if moved:
        boards.append(Board)
        moved=False

    return boards



def empty(Board):
    emp = []
    for i in range(4):
        for j in range(4):
            if Board[i][j]==0:
                emp.append((i,j))
    return emp

a=empty(Board)
num1 = random.randint(0,len(a)-1)
num2 = random.randint(0,len(a)-1)
while num2==num1:
    num2 = random.randint(0,len(a)-1)

num3=random.random()
if num3 < 0.9:
    Board[a[num1][0]][a[num1][1]]=1
else:
    Board[a[num1][0]][a[num1][1]]=2
    
num3=random.random()
if num3 < 0.9:
    Board[a[num2][0]][a[num2][1]]=1
else:
    Board[a[num2][0]][a[num2][1]]=2

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
    if len(a)>0:
        num=random.randint(0,len(a)-1)
        num2 = random.random()
        if num2 < 0.9:
            Board[a[num][0]][a[num][1]]=1
        else:
            Board[a[num][0]][a[num][1]]=2


def ai(Board,depth,prob=1,state=False,alpha=float("-inf"),beta=float("inf")):
    if depth == 0 or prob <0.001:
        return score(Board)

    if state:
        maxi=float("-inf")
        for b in moves(Board):

            maxi=max(ai(b,depth-1,prob,False,alpha,beta),maxi)

            if maxi >= beta:
                break

            alpha = max(maxi, alpha)

        return maxi
        
    else:
        mini=float("inf")
        arr=empty(Board)

        for i in range(len(arr)):

            Board[arr[i][0]][arr[i][1]]=1
            mini=min(ai(Board,depth-1,prob*0.9,True,alpha,beta),mini)
            Board[arr[i][0]][arr[i][1]]=0
            if mini <= alpha:
                break

            Board[arr[i][0]][arr[i][1]]=2
            mini=min(ai(Board,depth-1,prob*0.1,True,alpha,beta),mini)
            Board[arr[i][0]][arr[i][1]]=0
            if mini <= alpha:
                break

            beta = min(mini, beta)

        return mini

def search(Board,t):
    st=time()
    maxi=float("-inf")
    best=Board
    for i in range(15):
        if time()-st>=t:
            break5
        for move in moves(Board):

            s=ai(move,i)
            if s>=maxi:
                maxi=s
                best=move
        

    return best



def setup():
    pass

def draw():
    global Board
    show()
    Board=search(Board,0.01)
    tick(Board)
    

win.run(setup,draw)
