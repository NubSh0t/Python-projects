from window import Window,remap,Vector
from random import randint

Board = [[" "," "," "],[" "," "," "],[" "," "," "]]
scores = {"X":10,"Tie":0,"O":-10}
player = ["X","O"]
win = Window(0,0,600,600)
win.bgcolor(255,255,255)
cp = randint(0,1)
if cp==0:
    text='ai turn'
else:
    text="human turn"

win.strokeWidth(3)

def draw():
    global cp,count,Board,text
    if check(Board) == None:
        v = Vector(200,280)
        if cp==0:
            text='ai turn'
        else:
            text="human turn"
        win.write(v,text,2)
        show(Board)
        if cp == 1:
            human(Board)
        else:
            ai(Board)
            
    else:
        v = Vector(0,0)
        win.write(v,check(Board),3)
        win.timer(reset,100)

def reset(value):
    global Board,cp,text
    Board = [[" "," "," "],[" "," "," "],[" "," "," "]]
    cp = randint(0,1)
    text=''
    win.mouseclick()


def show(B):
    for i in range(2):
        v1 = Vector(200*i-100,300)
        v2 = Vector(200*i-100,-300)
        win.line(v1,v2)
        v1 = Vector(300,200*i-100)
        v2 = Vector(-300,200*i-100)
        win.line(v1,v2)

    for i in range(3):
        for j in range(3):
            x = remap(j,0,2,-200,200)
            y = remap(i,0,2,200,-200)
            if B[i][j] == "X":
                v1 = Vector(x-50,y-50)
                v2 = Vector(x+50,y+50)
                win.line(v1,v2)
                v1 = Vector(x-50,y+50)
                v2 = Vector(x+50,y-50)
                win.line(v1,v2)
            elif B[i][j] == "O":
                v1 = Vector(x,y)
                win.circle(v1,100)

def check(B):
    n = 0
    for i in range(3):
        for j in range(3):
            if B[i][j] == " ":
                n += 1
                
    if n == 0:
        return "Tie"

    for i in range(3):
        if B[0][i] == B[1][i] and B[0][i] == B[2][i] and B[0][i] != " ":
            return B[0][i]
        elif B[i][0] == B[i][1] and B[i][0] == B[i][2] and B[i][0] != " ":
            return B[i][0]
    if B[0][0] == B[1][1] and B[1][1] == B[2][2] and B[0][0] != " ":
        return B[0][0]
    if B[0][2] == B[1][1] and B[1][1] == B[2][0] and B[0][2] != " ":
        return B[0][2]

def human(B):
    global cp,text
    def f(v):
        if v == None:
            return
        global cp
        x = int(remap(v[0].x,-300,100,0,2))
        y = int(remap(v[0].y,300,-100,0,2))
        if x >=0 and x <= 2 and y >=0 and y <= 2 and B[y][x] == " ":
            B[y][x] = "O"
            cp = 0
    f(win.mouseclick())

def ai(B):
    global cp,text
    record = float('-inf')
    for i in range(3):
        for j in range(3):
            if B[i][j] == " ":
                B[i][j] = "X"
                score = minimax(B,False,float('-inf'),float('inf'),0)
                B[i][j] = " "
                if score > record:
                    record = score
                    moves = (i,j)
    B[moves[0]][moves[1]] = "X"
    cp = 1

def minimax(board,isMax,alpha,beta,depth):
    result = check(board)
    if result != None:
        return scores[result]

    if isMax == True:
        record = float('-inf')
        for x in range(9):
            i=x//3
            j=x%3
            if Board[i][j] == " ":
                Board[i][j] = "X"
                score = minimax(Board,False,alpha,beta,depth+1) - depth
                Board[i][j] = " "
                record = max(score,record)
                if record>=beta:
                    break
                alpha = max(alpha,record)
            
        return record
    else:
        record = float('inf')
        for x in range(9):
            i=x//3
            j=x%3
            if Board[i][j] == " ":
                Board[i][j] = "O"
                score = minimax(Board,True,alpha,beta,depth+1) + depth
                Board[i][j] = " "
                record = min(score,record)
                if record<=alpha:
                    break
                beta = min(beta,record)
            
        return record

if __name__ == "__main__":
    def setup():
        pass
    win.run(setup,draw)
