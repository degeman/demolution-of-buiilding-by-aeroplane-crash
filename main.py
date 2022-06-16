import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from OpenGL.GL.shaders import *
from compnents import *
from scenes import *
from plane import *
a=b=c=d=e=0.0

def update():
    global a
    global b
    global c
   
    a+=20.0   #Plane position takeoff on x axis
    b-=10.0    #Road Strip backward movement
    c+=15      #take off at certain angle on y axis
    if(b<=-78.0):   # moving of run way
        b=0.0
    
   


    


     


def road():
    global b
    draw_road(b)
    

def scene2():
    global d

    draw_scene2(d)
   

def scene3():
    global e
    draw_scene3(e)
   
    

def scene1():
    global a
    global b
    global c
    global d
    global e
    
    glClear(GL_COLOR_BUFFER_BIT)
    road()
    glPushMatrix()
    glTranslated(a,c,0.0)

    rectangular_body()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    const_plane()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    outline_upper_triangle()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    lower_triangle()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    back_wing()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    left_wing()
    glPopMatrix()

    glPushMatrix()
    glTranslated(a,c,0.0)
    right_wing()
    glPopMatrix()
    if(c>360):      #timer to jump to next display
        
        scene2()
        d+=20       #plane takeoff on x in 2nd display
        
    if(a>500.0):    #window position during take off
        
        a=0.0
        b=0.0
        
    if(c>750):          #timer to jump to 3rd display
        
        scene3()
        e+=20           #plane takeoff on x in 3rd display
        if(e>250):      #timer to call blast function
            
            blast()
            e=250
    glFlush()    










def main():
   


   
   
    running =True
    pygame.init()
    display = (800, 400)
    pygame.display.set_mode(display, DOUBLEBUF | OPENGL)
    glClearColor(0.2,0.4,1.0,0.0)
    glLoadIdentity()
    gluOrtho2D(0.0,499.0,0.0,499.0)
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
        scene1()
        update()
        pygame.display.flip()
        pygame.time.wait(180)


main()