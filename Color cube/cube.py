from window import Window,Vector

detail=50 #number of detail (smaller means more detailed but more time to render)

win=Window(0,0,1200,800)
win.strokeWidth(detail)

def setup():
    pass

def draw():
    global detail
    for i in range(0,250,detail):
        for j in range(0,250,detail):
            for k in range(0,250,detail):
                win.stroke(i,j,k)
                win.point(Vector(i+k-250,j+k-250))
    detail-=1

win.run(setup,draw,5)
