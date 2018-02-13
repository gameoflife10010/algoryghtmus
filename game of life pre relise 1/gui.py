import berechnung
import pygame
import time
feldmas = 50
pygame.init()
screen = pygame.display.set_mode([berechnung.zellenyachse * feldmas,berechnung.zellenyachse *feldmas])
clock = pygame.time.Clock()
done = False
def drawzellen(zellen = berechnung.zellen):
        i = 0
        x = 1
        y = 1
        max = berechnung.zellenxachse * berechnung.zellenyachse - 1
        while (i <= max):
            if(berechnung.Getzelle(x,y) == 1):
                pygame.draw.rect(screen,[0,255,0],[(y-1)*feldmas,(x-1)*feldmas, feldmas,feldmas])
            elif(berechnung.Getzelle(x,y) == 0):
                pygame.draw.rect(screen,[255,0,0],[(y-1)*feldmas,(x-1)*feldmas, feldmas,feldmas])
            i = i + 1
            if (y == berechnung.zellenyachse):
                x = x + 1
                y = 1
            else:
                y = y + 1

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    drawzellen(berechnung.zellen)
    pygame.display.flip()
    clock.tick(30)
    time.sleep(1)
    berechnung.zellen = berechnung.Fraim()[:]
