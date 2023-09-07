import math
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
from OpenGL_accelerate import *

clamp = lambda value, minv, maxv: max(min(value, maxv), minv)
remap = lambda value, min1, max1, min2, max2: min2 + (value - min1) * (max2 - min2) / (max1 - min1)

class Window():
    __b = None
    __s = None
    __s2 = None
    __mx1 = None
    __my1 = None
    __mup = False
    __mx2 = None
    __my2 = None
    __k=None
    __muk = False
    __w = None
    __d = None
    __mx3 = None
    __my3 = None
    __muw = False
    def __init__(self,x,y,w,h):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.fcolor = 1,1,1
        self.scolor = 0,0,0
        self.bgcol = 0,0,0,5
        self.swidth = 2
        self.angle = 0
        self.bgcolor()
        self.coffset=Vector(0,0)
        self.scale=1


    def run(self,setup,func,fr=30):
        self.func = func
        def showScreen():
            glMatrixMode(GL_PROJECTION)
            glLoadIdentity()
            glOrtho(self.coffset.x-self.w*self.scale/2,self.coffset.x+self.w*self.scale/2,self.coffset.y-self.h*self.scale/2,self.coffset.y+self.h*self.scale/2, -1,1)
            glMatrixMode(GL_MODELVIEW)
            glLoadIdentity()
            glClearColor(self.bgcol[0],self.bgcol[1],self.bgcol[2],self.bgcol[3])
            glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
            glLoadIdentity()
            self.func()
            glutSwapBuffers()

        def timer1(x):
            glutPostRedisplay()
            glutTimerFunc(x,timer1,x)

            
        glutInit()
        glutInitDisplayMode(GLUT_RGBA)
        glutInitWindowSize(self.w, self.h)
        glutInitWindowPosition(self.x, self.y)
        wind = glutCreateWindow(b"Window")
        glutDisplayFunc(showScreen)
        glViewport(0,0,int(self.w), int(self.h))
        
        glEnable(GL_VERTEX_PROGRAM_POINT_SIZE)
        setup()
        glutIgnoreKeyRepeat(1)
        glutTimerFunc(0,timer1,int(1000/fr))
        glutMainLoop()

    def camera(self,v,scale=1):
        self.coffset=v
        self.scale=scale

    def strokeWidth(self,x):
        self.swidth = x

    def rotate(self,ang):
        self.angle=ang

    def rect(self,v,w,h):
        glLineWidth(self.swidth)
        corner = []
        v1 = Vector(w/2,h/2)
        v1.addangle(self.angle)
        corner.append(v1)
        v2 = Vector(-w/2, h/2)
        v2.addangle(self.angle)
        corner.append(v2)
        v3 = Vector(-w/2, -h/2)
        v3.addangle(self.angle)
        corner.append(v3)
        v4 = Vector(+w/2, -h/2)
        v4.addangle(self.angle)
        corner.append(v4)

        c2 = []
        for i in range(len(corner)):
            temv = Vector(v.x,v.y)
            temv.add(corner[i])
            c2.append(temv)

        corner = c2

        
        glColor3f(self.fcolor[0],self.fcolor[1],self.fcolor[2])
        glBegin(GL_QUADS)
        for i in range(len(c2)):
            glVertex2f(corner[i].x,corner[i].y)
        glEnd()

        glLineWidth(self.swidth)
        glColor3f(self.scolor[0],self.scolor[1],self.scolor[2])
        glBegin(GL_LINES)
        
        glVertex2f(corner[0].x,corner[0].y)
        glVertex2f(corner[1].x,corner[1].y)

        glVertex2f(corner[1].x,corner[1].y)
        glVertex2f(corner[2].x,corner[2].y)

        glVertex2f(corner[2].x,corner[2].y)
        glVertex2f(corner[3].x,corner[3].y)

        glVertex2f(corner[3].x,corner[3].y)
        glVertex2f(corner[0].x,corner[0].y)

        glEnd()

    def circle(self,v,d,q=20):
        glLineWidth(self.swidth)
        dir = Vector(0,0)
        dir.mag(d/2)
        arr = []
        for i in range(0,360,q):
            dir.setangle(i+self.angle)
            p = Vector(v.x,v.y)
            p.add(dir)
            arr.append((p.x,p.y))

        glColor3f(self.fcolor[0],self.fcolor[1],self.fcolor[2])
        glBegin(GL_POLYGON)
        for j in arr:
            glVertex2f(j[0],j[1])
        glEnd()

        glColor3f(self.scolor[0],self.scolor[1],self.scolor[2])
        glBegin(GL_LINE_LOOP)
        for j in arr:
            glVertex2f(j[0],j[1])
        glEnd()



    def line(self,v1,v2):
        glLineWidth(self.swidth)
        glColor3f(self.scolor[0],self.scolor[1],self.scolor[2])
        glBegin(GL_LINES)
        glVertex2f(v1.x,v1.y)
        glVertex2f(v2.x,v2.y)
        glEnd()

    def point(self,v):
        glPointSize(self.swidth)
        glColor3f(self.scolor[0],self.scolor[1],self.scolor[2])
        glBegin(GL_POINTS)
        glVertex2f(v.x,v.y)
        glEnd()

    def mouseclick(self):
        def f(button,state,mousex,mousey):
            Window.__b = button
            Window.__s = state
            Window.__mx1 = mousex
            Window.__my1 = mousey
            Window.__mup = True
        glutMouseFunc(f)
        if Window.__mup ==True:
            Window.__mup = False
            return Vector(Window.__mx1-(self.w/2),-Window.__my1+(self.h/2)),Window.__b,Window.__s

    def mousewheel(self):
        def f(wheel,direction,mousex,mousey):
            Window.__w = wheel
            Window.__d = direction
            Window.__mx3 = mousex
            Window.__my3 = mousey
            Window.__muw = True
        glutMouseWheelFunc(f)
        if Window.__muw ==True:
            Window.__muw = False
            return Vector(Window.__mx3-(self.w/2),-Window.__my3+(self.h/2)),Window.__w,Window.__d



    def timer(self,func,millisecs,value=1):
        glutTimerFunc(millisecs,func,value)

    def keyboard(self):
        def f(key,mx,my):
            Window.__mx2 = mx
            Window.__my2 = my
            Window.__k = int.from_bytes(key,"big")
            Window.__muk = True
            Window.__s2 = "DOWN"
        def f2(key,mx,my):
            Window.__mx2 = mx
            Window.__my2 = my
            Window.__k = int.from_bytes(key,"big")
            Window.__muk = True
            Window.__s2 = "UP"
        glutKeyboardFunc(f)
        if Window.__muk == True:
            Window.__muk = False
            return Vector(Window.__mx2-(self.w/2),-Window.__my2+(self.h/2)),Window.__k,Window.__s2
        glutKeyboardUpFunc(f2)
        if Window.__muk == True:
            Window.__muk = False
            return Vector(Window.__mx2-(self.w/2),-Window.__my2+(self.h/2)),Window.__k,Window.__s2


    def write(self,v,string,size=1):
        w=0
        for s in string:
            w+=glutStrokeWidth(GLUT_STROKE_ROMAN,ctypes.c_int(ord(s)))
        glPushMatrix()
        glLineWidth(self.swidth)
        glColor3f(self.scolor[0],self.scolor[1],self.scolor[2])
        glTranslatef(v.x-((w/2)*size/10),v.y,0)
        glScale(size/10,size/10,0)
        for s in string:
            glutStrokeCharacter(GLUT_STROKE_ROMAN,ctypes.c_int(ord(s)))
        glPopMatrix()




    def bgcolor(self,r=100,g=100,b=100,a=255):
        r = remap(r,0,255,0,1)
        g = remap(g,0,255,0,1)
        b = remap(b,0,255,0,1)
        a = remap(a,0,255,0,1)
        self.bgcol = r,g,b,a
        

    def fill(self,r=255,g=255,b=255):
        r = remap(r,0,255,0,1)
        g = remap(g,0,255,0,1)
        b = remap(b,0,255,0,1)
        self.fcolor = r,g,b

    def stroke(self,r=0,g=0,b=0):
        r = remap(r,0,255,0,1)
        g = remap(g,0,255,0,1)
        b = remap(b,0,255,0,1)
        self.scolor = r,g,b
    


class Vector():
    def __init__(self,x,y):
        self.len = math.sqrt(pow(x,2)+pow(y,2))
        self.angle = math.degrees(math.atan2(y,x))
        self.x = x
        self.y = y
        self.update()

    def update(self):
        self.x = math.cos(math.radians(self.angle))*self.len
        self.y = math.sin(math.radians(self.angle))*self.len

    def add(self,v2):
        self.x += v2.x 
        self.y += v2.y
        self.len = math.sqrt(pow(self.x,2)+pow(self.y,2))
        self.angle = math.degrees(math.atan2(self.y,self.x))
        self.update()
        return self

    def sub(self,v2):
        self.x -= v2.x 
        self.y -= v2.y
        self.len = math.sqrt(pow(self.x,2)+pow(self.y,2))
        self.angle = math.degrees(math.atan2(self.y,self.x))
        self.update()
        return self
    
    def multiply(self,n):
        self.len *= n
        self.update()
        return self

    def clamp(self,min,max):
        self.len = clamp(self.len,min,max)
        self.update()
        return self

    def divide(self,n):
        self.len /= n
        self.update()
        return self

    def addangle(self,a):
        self.angle += a
        self.update()
        return self

    def setangle(self,a):
        self.angle = a
        self.update()
        return self

    def mag(self,n):
        self.len = n
        self.update()
        return self

    def normalize(self):
        self.len = 1
        self.update()
        return self

    def random(self,mag):
        self.len = mag
        self.angle = random.randint(-180,180)
        self.update()
        return self

    def copy(self):
        return Vector(self.x,self.y)
        
    def dist(self,v2):
        return math.sqrt(pow(self.x-v2.x,2)+pow(self.y-v2.y,2))

    def ang(self,v2):
        return math.degrees(math.atan2(v2.y-self.y,v2.x-self.x))

    def dotproduct(self,v2):
        return self.len * v2.len * math.cos(math.radians(v2.angle-self.angle))
