__author__ = 'jan01koelling'
from math import sqrt
import pygame
from pygame.locals import *
c = [0,0]
def mal(a,b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]

    ansx = (x1*x2-y1*y2)
    ansy = (x1*y1+x2*y1)
    ans = [ansx,ansy]
    return (ans)

def plus(a,b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    ans = [(x1+x2),(y1+y2)]
    return(ans)

def minus(a,b):
    x1 = a[0]
    x2 = b[0]
    y1 = a[1]
    y2 = b[1]
    ans = [(x1-x2),(y1-y2)]
    return(ans)
def pixelberechnung(koordinate):
    x = koordinate[0]
    y = koordinate[1]
    i = 0
    z = [0,0]
    zn = z
    while(i<100):
        z = mal(z,z)
        z = minus(z,c)
        zn =sqrt(plus(mal(x,x),mal(y,y)))
        i = i + 1
        if(zn >= 2):
            return(i)
    return (i)
done = False

screen = pygame.display.set_mode([800,800])
pygame.display.set_caption('Mandelbrotyumyumyum')
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
pygame.screen.flip()