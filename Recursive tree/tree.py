from window import Window,Vector,clamp
from random import randint

w=Window(0,0,800,800)
w.bgcolor(0,0,0)

class line():
    def __init__(self,pos,length,angle,depth=0):
        self.pos=pos.copy()
        self.l=length
        self.ang=angle
        self.depth=depth
        self.children=[]

    def show(self,depth=0):
        if self.depth>=depth:
            temp=self.pos.copy()
            t=Vector(0,self.l)
            t.setangle(self.ang)
            temp.add(t)
            if self.children!=[]:
                w.stroke(10*(self.depth+1)+20,10*(self.depth+1)+20,10*(self.depth+1)+20)
            else:
                w.stroke(200,200,200)
            w.line(self.pos,temp)

        for c in self.children:
            c.show()

    def child(self,max=50):
        if self.depth >= max:
            return
        if self.children == []:
            temp=self.pos.copy()
            t=Vector(0,self.l)
            t.setangle(self.ang)
            temp.add(t)
            self.children.append(line(temp.copy(),self.l*randint(70,90)/100,self.ang+randint(5,50),self.depth+1))
            self.children.append(line(temp.copy(),self.l*randint(70,90)/100,self.ang-randint(5,50),self.depth+1))
        for c in self.children:
            c.child(max)

    def copy(self):
        return self

n=0
l=line(Vector(0,-300),100,90)
prev=None

def setup():
    pass

def draw():
    global n,l,prev
    if n > 12:
        prev=l.copy()
        #l=line(Vector(0,-300),100,90)
        n=0
    else:
        l.child(n)
        l.show()
        n+=1
        if prev!=None:
            l.show(12)

w.run(setup,draw)
