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

   
    


    
def control_scenes():
    global a
    global b
    global c
    global d
    global e
    draw_scene1(a,b,c)
    if(c>360):      #timer to jump to next display
        glClear(GL_COLOR_BUFFER_BIT)
        draw_scene2(d)
        d+=20       #plane takeoff on x in 2nd display
        
    if(a>500.0):    #window position during take off
        
        a=0.0
        b=0.0
        
    if(c>750):          #timer to jump to 3rd display
        
        draw_scene3(e)
        e+=20           #plane takeoff on x in 3rd display
        if(e>250):      #timer to call blast function
            
            demolition()
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
        control_scenes()
        update()
        pygame.display.flip()
        pygame.time.wait(180)


main()