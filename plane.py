import pygame
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
from pygame.locals import *
from OpenGL.GL.shaders import *
from compnents import *


def rectangular_body():
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)#rectangular body
        glVertex2f(0.0,30.0)
        glVertex2f(0.0,55.0)
        glVertex2f(135.0,55.0)
        glVertex2f(135.0,30.0)
        glEnd()


def const_plane():
        glColor3f(1.0,1.0,1.0)
        glBegin(GL_POLYGON)
        glVertex2f(135.0,55.0)
        glVertex2f(150.0,50.0)
        glVertex2f(155.0,45.0)
        glVertex2f(160.0,40.0)
        glVertex2f(135.0,40.0)
        glEnd()

# draw outline of upper tirangle

def outline_upper_triangle():
        glColor3f(0.0,0.0,0.0)
        glBegin(GL_LINE_LOOP)
        glVertex2f(135.0,55.0)
        glVertex2f(150.0,50.0)
        glVertex2f(155.0,45.0)
        glVertex2f(160.0,40.0)
        glVertex2f(135.0,40.0)
        glEnd()
# draw the lower triangle
def lower_triangle():
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(135.0,40.0)
        glVertex2f(160.0,40.0)
        glVertex2f(160.0,37.0)
        glVertex2f(145.0,30.0)
        glVertex2f(135.0,30.0)
        glEnd()
# draw the back wing 
def back_wing():
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(0.0,55.0)
        glVertex2f(0.0,80.0)
        glVertex2f(10.0,80.0)
        glVertex2f(40.0,55.0)
        glEnd()

# this will draw the the left side wing
def left_wing():
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(65.0,55.0)
        glVertex2f(50.0,70.0)
        glVertex2f(75.0,70.0)
        glVertex2f(90.0,55.0)
        glEnd()
# the right side wing
def right_wing():
        glColor3f(1.0,0.0,0.0)
        glBegin(GL_POLYGON)
        glVertex2f(70.0,40.0)
        glVertex2f(100.0,40.0)

        glVertex2f(80.0,15.0)
        glVertex2f(50.0,15.0)
        glEnd()