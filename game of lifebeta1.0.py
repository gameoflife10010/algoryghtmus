
zellenxachse = 25
zellenyachse = 25
zellen = []
def Befüllen():
    i = 1
    while(i <=zellenxachse * zellenxachse):
        i = i+1
        zellen.append(1)

def Position(xachse, yachse):
    position = (xachse - 1)*zellenxachse + yachse
    if(zellenxachse < xachse or zellenyachse < yachse):
        print("die koordinate (" + xachse + "/" + yachse + ") exestiert nicht")
    return int(position)

def Getzelle(xachse, yachse):
    xachse = int(xachse)
    yachse = int(yachse)
    pos = Position(xachse, yachse)
    return zellen[pos]

def Setzelle(xachse, yachse, wert):
    int(wert)
    if(wert != 0 and wert != 1):
        print("der Wert " + wert + " ist nicht binär")
    zellen[Position(xachse, yachse)] = wert
def Nachbarn(xachse, yachse):
    if(xachse == 1):
        print()
        if (yachse == 1):  # oben links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse + 1)
        elif (yachse == zellenyachse):  # oben rechts
            lebendenachbarn = Getzelle(xachse, yachse - 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse - 1)
        else:  # nur obere kante
            lebendenachbarn = Getzelle(xachse + 1, yachse + 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse - 1) + \
                              + Getzelle(xachse, yachse + 1) + Getzelle(xachse, yachse - 1)

    elif(xachse == zellenxachse): #unterekante

        if (yachse == 1): # unten links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse + 1)
        elif (yachse == zellenyachse): #unten rechts
            lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse - 1)
        else: #nur untere kante
            lebendenachbarn = Getzelle(xachse - 1, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse - 1) + \
                              + Getzelle(xachse, yachse + 1) + Getzelle(xachse, yachse - 1)

    elif(yachse == 1): # linke kante
        print()
        if (xachse == 1): # oben links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse + 1)
        elif (xachse == zellenxachse): # unten links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse + 1)

        else: # nur links
            lebendenachbarn = Getzelle(xachse - 1, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse + 1) + \
                              + Getzelle(xachse + 1, yachse + 1) + Getzelle(xachse + 1, yachse)


    elif(yachse == zellenyachse): # rechte kante

            if(xachse == 1): #rechts oben
                 lebendenachbarn = Getzelle(xachse, yachse - 1) + Getzelle(xachse + 1, yachse) +\
                                   Getzelle(xachse + 1, yachse - 1)

            elif(xachse == zellenxachse): # rechts unten

                 lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) +\
                                   Getzelle(xachse, yachse - 1)

            else: # nur rechte kante
                lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                    Getzelle(xachse, yachse - 1) + \
                    + Getzelle(xachse + 1, yachse - 1) + Getzelle(xachse + 1, yachse)

    else: # nicht am rand
        lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse -1, yachse) + \
                              Getzelle(xachse -1, yachse +1) + Getzelle(xachse, yachse - 1) + \
                              Getzelle(xachse, yachse + 1) + Getzelle(xachse + 1, yachse - 1) + \
                              Getzelle(xachse + 1, yachse) +Getzelle(xachse + 1, yachse + 1)

    return lebendenachbarn

def Zellenentwicklung(xachse, yachse):
    nachbarn = Nachbarn(xachse, yachse)
    if(Getzelle(xachse, yachse) == 1):
        if(nachbarn <= 1):
            Setzelle(xachse, yachse,0)
            return
        if (nachbarn == 2 or nachbarn == 3):
            return
        if (nachbarn > 3):
            Setzelle(xachse, yachse, 0)
            return
    elif(Getzelle(xachse, yachse) == 0 and nachbarn == 3):
        Setzelle(xachse, yachse, 1)
        return
    else:
        print("die Zelle (" + xachse + "/" + yachse + ") besitzt keinen boolischen wert")


def Fraim():
    i = 1
    x = 1
    y = 1
    max = zellenxachse * zellenyachse
    while(i <= max):

        Zellenentwicklung(x, y)
        i = i + 1
        y = y + 1
        if(y == zellenyachse):
            x = x +1
            y = 1

Befüllen()
Fraim()
print(zellen)
print(len(zellen))
print(Nachbarn(5,25))
