from window import Window,Vector,remap,clamp

win=Window(0,0,800,800)
win.bgcolor(200,200,200)

n=0
s=0
d=False
r=False
l=False

class car():
    def __init__(self):
        self.dir=Vector(0,1)
        self.pos=Vector(0,1)
        self.prev=[]

    def show(self):
        win.strokeWidth(4)
        for i in range(len(self.prev)-1):
            c = remap(i,0,len(self.prev)-1,150,100)
            win.stroke(c,c,c)

            dir=self.prev[i][1].copy()
            dir.mag(0.5)
            a=self.prev[i][0].copy()
            b=self.prev[i+1][0].copy()
            a.sub(dir)
            b.add(dir)
            dir.mag(8)
            dir.addangle(-90)
            a.add(dir)
            b.add(dir)
            win.line(a,b)

            dir=self.prev[i][1].copy()
            dir.mag(0.5)
            a=self.prev[i][0].copy()
            b=self.prev[i+1][0].copy()
            a.sub(dir)
            b.add(dir)
            dir.mag(8)
            dir.addangle(90)
            a.add(dir)
            b.add(dir)
            win.line(a,b)

        win.strokeWidth(2)
        win.stroke(50,50,50)
        win.rotate(self.dir.angle)
        win.rect(self.pos,40,30)

    def update(self):
        self.pos.add(self.dir)
        win.camera(c.pos)
        self.prev.append((self.pos.copy(),self.dir.copy()))
        if len(self.prev) > 50:
            self.prev.pop(0)

    def steer(self,n):
        self.dir.addangle(n)

    def move(self,n):
        self.dir.mag(n)


c=car()


def setup():
    pass

def draw():
    global n,s,d,r,l
    win.stroke(100,100,100)

    c.update()

    c.show()

    key=win.keyboard()
    if key !=None:
        if key[1]==119:
            if key[2]=="DOWN":
                d=True
            else:
                d=False

        elif key[1]==97:
            if key[2]=="DOWN":
                r=True
            else:
                r=False

        elif key[1]==100:
            if key[2]=="DOWN":
                l=True
            else:
                l=False


    if d:
        n+=0.5
    else:
        n-=1

    if r:
        s+=0.5
    elif l:
        s-=0.5
    else:
        s=0

    n=clamp(n,0,50)
    s=clamp(s,-5,5)
    c.move(n)
    if n > 0:
        c.steer(s)

def  grid():
    pass

win.run(setup,draw,60)
