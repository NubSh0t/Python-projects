from window import Window,Vector,clamp,remap
import math
import random

class boundary():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2
    
    def show(self):
        window.line(self.v1,self.v2)



class ray():
    def __init__(self,v1,v2):
        self.v1 = v1
        self.v2 = v2

    def intersect(self,boundarys):
        x1 = self.v1.x
        y1 = self.v1.y
        x2 = self.v2.x
        y2 = self.v2.y
        min = float('inf')
        minV = None
        for i in boundarys:
            x3 = i.v1.x
            y3 = i.v1.y
            x4 = i.v2.x
            y4 = i.v2.y
            div = (x1-x2)*(y3-y4)-(y1-y2)*(x3-x4)
            if div != 0:
                t=(x1-x3)*(y3-y4)-(y1-y3)*(x3-x4)
                t /= div
                u = (x2-x1)*(y1-y3)-(y2-y1)*(x1-x3)
                u /= div
                v = Vector(x1+t*(x2-x1),y1+t*(y2-y1))
                dist = self.v1.dist(v)
                if dist < min and t <= 1 and t >= 0 and u <= 1 and u >=0:
                    min = dist
                    minV = v
        window.line(self.v1,minV)
        window.circle(minV,3)
        return min

def angtovect(v,angle,mag):
    v = Vector(v.x,v.y)
    vect = Vector(0,0)
    vect.setangle(angle)
    vect.mag(mag)
    v.add(vect)
    return v

window = Window(0,0,1200,600)
window.stroke(255,255,255)
boundarys = []
boundarys.append(boundary(Vector(-25,-275),Vector(-25,275)))
boundarys.append(boundary(Vector(-575,-275),Vector(-575,275)))
boundarys.append(boundary(Vector(-575,-275),Vector(-25,-275)))
boundarys.append(boundary(Vector(-575,275),Vector(-25,275)))
boundarys.append(boundary(Vector(-200,-300),Vector(-100,-50)))

sc = []
ang = 0

def draw():
    global ang,sc
    window.line(Vector(0,-300),Vector(0,300))
    for i in boundarys:
        i.show()
    for i in range(80):
        r = ray(Vector(-300,0),angtovect(Vector(-300,0),ang-20+(i/2),1000))
        length = r.intersect(boundarys)
        length *=math.cos(math.radians(-20+(i/2)))
        length/=550
        l = remap(length,0,1,300,0)
        c = remap(length,0,1,250,50)
        sc.insert(0,(l,c))
    sn = len(sc)
    for i in range(sn):
        window.stroke(sc[i][1],sc[i][1],sc[i][1])
        window.fill(sc[i][1],sc[i][1],sc[i][1])
        window.rect(Vector(25+(550/sn)*i+(550/sn)/2,0),(550/sn),sc[i][0]*2)
        window.stroke(255,255,255)
    sc=[]
    ang+=1

def setup():
    pass

window.run(setup,draw)
