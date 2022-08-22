import math

import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLU import *

PI = math.pi
circulo_pontos = 200

pygame.init()
display = (800, 400)
pygame.display.set_mode(display, DOUBLEBUF | OPENGL)

def tabela():
    glBegin(GL_LINES)
    #EIXOX
    glColor3f(0, 0, 0)
    glVertex2f (10, 0)
    glVertex2f (-10, 0)
    #EixoY0
    glVertex2f (0, 5)
    glVertex2f (0, -5)
    #EixoY1
    glVertex2f (5, 5)
    glVertex2f (5, -5)
    #EixoY2
    glVertex2f (-5, 5)
    glVertex2f (-5, -5)
    glEnd()

def quadrado():
    glBegin(GL_QUADS)
    glColor3f(1.0, 0.4, 0.0)
    glVertex2f (-6, 1)
    glVertex2f (-9, 1)
    glVertex2f (-9, 4)
    glVertex2f (-6, 4)
    glEnd()

def triangulo():
    glBegin(GL_TRIANGLES)
    glColor3f(0.0, 0.0, 2.4)
    glVertex2f(-4, 1)
    glVertex2f(-1, 1)
    glVertex2f(-2.5, 4)
    glEnd()

def poligono():
    glBegin(GL_POLYGON)
    glColor3f(0.0, 2.4, 0.0)
    glVertex2f(1, 1)
    glVertex2f(4, 1)
    glVertex2f(4, 3)
    glVertex2f(2.5, 4)
    glVertex2f(1, 3)
    glEnd()

def triotriangulo():
    glPolygonMode(GL_FRONT_AND_BACK, GL_LINE)
    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(2.4, 0.0, 0.0)
    glVertex2f(6, 1)
    glVertex2f(6.75, 3)
    glVertex2f(7.5, 1)
    glVertex2f(8.25, 3)
    glVertex2f(9., 1)
    glEnd()
    glPolygonMode(GL_FRONT_AND_BACK, GL_FILL)

def saojoao():
    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    glColor3f(0.0, 0.0, 0.0)
    glVertex2f(-6, -4)
    glVertex2f(-7.5, -2.5)
    glVertex2f(-9, -4)
    glVertex2f(-9, -1)
    glVertex2f(-6, -1)
    glEnd()
    glLineWidth(1)

def xis():
    glLineWidth(5)
    glBegin(GL_LINES)
    glColor3f(0, 255, 255)
    glVertex2f(-5, 0)
    glVertex2f(0, -5)
    glVertex2f(0, 0)
    glVertex2f(-5, -5)
    glEnd()
    glLineWidth(1)

def tabela2():
    for i in range (1, 5):
        glLineWidth(6)
        glBegin(GL_LINES)
        glColor3f(255, 0, 255)
        glVertex2f(i, 0)
        glVertex2f(i, -5)
        glVertex2f(0, -i)
        glVertex2f(5, -i)
        glEnd()
        glLineWidth(1)

def circulo():

    glLineWidth(3)
    glBegin(GL_LINE_LOOP)
    for f in range(circulo_pontos):
        glColor3f(255, 255, 0)
        angle = 2 * PI * f / circulo_pontos
        x = math.cos(angle) + 7.5
        y = math.sin(angle) - 2.5
        glVertex2f(x, y)
    glEnd()
    glLineWidth(1)

def ultimo():
    glBegin(GL_QUADS)
    glColor3f(0.2, 0.2, 0.2)
    glVertex2f (5, 0)
    glVertex2f (10, 0)
    glVertex2f (10, -5)
    glVertex2f (5, -5)
    glEnd()


def main():
    gluPerspective(45, (display[0] / display[1]), 0.1, 50.0)

    glTranslate(0.0, 0.0, -12)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:

                pygame.quit()
                quit()

        glClearColor(1.0, 1.0, 1.0, 1)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLineWidth(2.0)

        tabela()
        circulo()
        quadrado()
        triangulo()
        poligono()
        triotriangulo()
        saojoao()
        xis()
        tabela2()
        ultimo()
        circulo()

        pygame.display.flip()
        pygame.time.wait(20)

main()