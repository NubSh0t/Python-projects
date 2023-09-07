from window import Window,Vector,remap,clamp
import math

arr = []
Size=400
updated=True


def rpath(node):
    path = [node]
    while node.parent != None:
        node = node.parent
        path.append(node)
    return path

def h(node1,node2):
    value = math.sqrt(pow(node1.x-node2.x,2)+pow(node1.y-node2.y,2))
    return value

def Astar(snode,enode,h,arr,checkl=500):
    openset = []
    closeset = []

    snode.parent = None
    snode.gval = 0
    snode.fval = h(snode,enode)
    check = 0

    openset.append(snode)

    while len(openset) > 0:
        openset.sort(key = lambda x:x.fval)

        current = openset[0]
        check+=1
        
        if (current.x == enode.x and current.y == enode.y) or check > checkl:
            path= rpath(current)
            for p in path:
                arr[p.y][p.x]=2
            arr[path[0].y][path[0].x]=3
            arr[path[len(path)-1].y][path[len(path)-1].x]=3
            return

        openset.remove(current)
        current.child()

        for i in range(len(current.neighbours)):
            if arr[current.neighbours[i].y][current.neighbours[i].x] == 0:
                ten_gval= current.gval+h(current,current.neighbours[i])
                n = None
                for j in range(len(closeset)):
                    if closeset[j].x == current.neighbours[i].x and closeset[j].y ==current.neighbours[i].y:
                        n = closeset[j]
                if n == None :
                    a = current.neighbours[i]
                    a.parent = current
                    a.gval = ten_gval
                    a.fval = a.gval + h(current.neighbours[i],enode)
                    closeset.append(a)
                    k = None
                    for j in range(len(openset)):
                        if openset[j].x == current.neighbours[i].x and openset[j].y ==current.neighbours[i].y:
                            k = openset[j]
                    if k == None:
                        openset.append(a)
                else:
                    if ten_gval < n.gval:
                        n.parent = current
                        n.gval = ten_gval
                        n.fval = n.gval + h(n,enode)

class node():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.neighbours = []

    def child(self):
        if self.x-1 >= 0:
            self.neighbours.append(node(self.x-1,self.y))

        if self.y-1 >= 0:
            self.neighbours.append(node(self.x,self.y-1))

        if self.x+1 <= grid-1:
            self.neighbours.append(node(self.x+1,self.y))

        if self.y+1 <= grid-1:
            self.neighbours.append(node(self.x,self.y+1))

def abc(x,y):
    global arr,updated
    y = int(remap(clamp(y,-Size,Size),-Size,Size,grid,0))
    x = int(remap(clamp(x,-Size,Size),-Size,Size,0,grid))
    if arr[y][x] == 1:
        arr[y][x] = 0
    elif arr[y][x] == 2:
        arr[y][x] = 1
        updated=True
    else:
        arr[y][x] = 1

def hij(x,y):
    global en,updated
    y = int(remap(clamp(y,-Size,Size),-Size,Size,grid,0))
    x = int(remap(clamp(x,-Size,Size),-Size,Size,0,grid))
    if x < grid and y < grid:
        en.x,en.y = x,y
        updated=True

window = Window(0,0,Size*2,Size*2)
window.bgcolor(255,255,255)
grid = 20
sn = node(0,0)
en = node(4,4)

for i in range(grid):
    arr.append([])
    for j in range(grid):
        arr[i].append(0)

def draw():
    global updated
    m =window.mouseclick()
    if m != None:
        if m[1]== 0 and m[2]==0:
            abc(m[0].x,m[0].y)
        elif m[1]== 2 and m[2]==0:
            hij(m[0].x,m[0].y)

    if updated:
        for i in range(len(arr)):
            for j in range(len(arr[i])):
                if arr[i][j]==2 or arr[i][j]==3:
                    arr[i][j]=0
        Astar(sn,en,h,arr)
        updated=False

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            x = remap(j,0,grid-1,-Size+Size/grid,Size-Size/grid)
            y = remap(i,0,grid-1,Size-Size/grid,-Size+Size/grid)
            if arr[i][j] == 1:
                window.fill(0,0,0)
            elif arr[i][j] == 2:
                window.fill(0,0,255)
            elif arr[i][j] == 3:
                window.fill(0,255,0)
            else:
                window.fill(255,255,255)
            window.rect(Vector(x,y),(Size*2/grid)-0.5,(Size*2/grid)-0.5)
            
    

def setup():
    window.stroke(False)

window.run(setup,draw)
