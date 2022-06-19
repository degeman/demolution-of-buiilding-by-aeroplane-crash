import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from OpenGL.GL.shaders import *
from compnents import *
from plane import *
from compnents import *

def draw_scene2(d,c=300.0):
    # glClear(GL_COLOR_BUFFER_BIT)
    glPushMatrix()
    glTranslated(d,c,0.0)

    rectangular_body()
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)

    const_plane()
    
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)

    outline_upper_triangle()
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)

    lower_triangle()
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)

    back_wing()
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)

    left_wing()
    glPopMatrix()
    glPushMatrix()
    glTranslated(d,c,0.0)
    
    right_wing()
    glPopMatrix()
def draw_scene1(a,b,c):
   
    
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_road(b)
    draw_scene2(a,c)
    

def draw_scene3(e):
    glClear(GL_COLOR_BUFFER_BIT)
    
    draw_scene2(e)
    draw_field()
    building()