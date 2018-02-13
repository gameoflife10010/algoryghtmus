zellenxachse = 3 #beispiels wert für die anzahl der zeilen
zellenyachse = 3 #beispiels wert für die anzahl der spalten
zellen = []


def Befüllen(zellen=zellen): # befüllt die list
    i = 1
    while (i <= zellenxachse * zellenyachse):
        i = i + 1
        zellen.append(1)


def Position(xachse, yachse): # gibt die position einer zelle in einer liste wieder
    position = (xachse - 1) * zellenxachse + yachse - 1
    if (zellenxachse < xachse or zellenyachse < yachse):
        print("die koordinate (" + int(xachse) + "/" + int(yachse) + ") exestiert nicht")
    return int(position)


def Getzelle(xachse, yachse): # gibt den wert einer zelle wieder
    xachse = int(xachse)
    yachse = int(yachse)
    pos = Position(xachse, yachse)
    return zellen[pos]


def Setzelle(xachse, yachse, wert): # setzt den wert einer zelle neu
    int(wert)
    if (wert != 0 and wert != 1):
        print("der Wert " + wert + " ist nicht binär")
    zellen[Position(xachse, yachse)] = wert


def Nachbarn(xachse, yachse): # prüft die anzahl an lebenden nachbar zellen (dopplungen kommen vor)
    if (xachse == 1):
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

    elif (xachse == zellenxachse):  # unterekante

        if (yachse == 1):  # unten links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse + 1)
        elif (yachse == zellenyachse):  # unten rechts
            lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse - 1)
        else:  # nur untere kante
            lebendenachbarn = Getzelle(xachse - 1, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse - 1) + \
                              + Getzelle(xachse, yachse + 1) + Getzelle(xachse, yachse - 1)

    elif (yachse == 1):  # linke kante
        if (xachse == 1):  # oben links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse + 1)
        elif (xachse == zellenxachse):  # unten links
            lebendenachbarn = Getzelle(xachse, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse - 1, yachse + 1)

        else:  # nur links
            lebendenachbarn = Getzelle(xachse - 1, yachse + 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse + 1) + \
                              + Getzelle(xachse + 1, yachse + 1) + Getzelle(xachse + 1, yachse)


    elif (yachse == zellenyachse):  # rechte kante

        if (xachse == 1):  # rechts oben
            lebendenachbarn = Getzelle(xachse, yachse - 1) + Getzelle(xachse + 1, yachse) + \
                              Getzelle(xachse + 1, yachse - 1)

        elif (xachse == zellenxachse):  # rechts unten

            lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse - 1)

        else:  # nur rechte kante
            lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                              Getzelle(xachse, yachse - 1) + \
                              + Getzelle(xachse + 1, yachse - 1) + Getzelle(xachse + 1, yachse)

    else:  # nicht am rand
        lebendenachbarn = Getzelle(xachse - 1, yachse - 1) + Getzelle(xachse - 1, yachse) + \
                          Getzelle(xachse - 1, yachse + 1) + Getzelle(xachse, yachse - 1) + \
                          Getzelle(xachse, yachse + 1) + Getzelle(xachse + 1, yachse - 1) + \
                          Getzelle(xachse + 1, yachse) + Getzelle(xachse + 1, yachse + 1)

    return lebendenachbarn


def Zellenentwicklung(xachse, yachse): # berechnet nach der anzahl der nachbar zellen den zustand einer zelle in der nächsten runde
    nachbarn = Nachbarn(xachse, yachse)
    if (Getzelle(xachse, yachse) == 1): # die zelle lebt
        if (nachbarn <= 1):
            return 0
        if (nachbarn == 2 or nachbarn == 3):
            return 1
        if (nachbarn > 3):
            return 0
    elif (Getzelle(xachse, yachse) == 0 and nachbarn == 3): # die zelle ist tod
        return 1
    elif (Getzelle(xachse, yachse) == 0 ): # die zelle ist tod
        return 0
    else:

        print("die Zelle (" + str(xachse) + "/" + str(yachse) + ") besitzt keinen boolischen wert " + str(
            Getzelle(xachse, yachse)) + " Nachbarn " + str(nachbarn) + " leben " + str(Getzelle(xachse, yachse)))

def Fraim(zellen=zellen): # gibt den status der zellen in der nächste runde in form einer liste zurück
    zellebearbeitung = zellen[:]
    i = 0
    x = 1
    y = 1
    max = zellenxachse * zellenyachse - 1
    while (i <= max):
        # print(i)
        pos = Position(x, y)
        zellebearbeitung[pos] = Zellenentwicklung(x, y)
        i = i + 1
        if (y == zellenyachse):
            x = x + 1
            y = 1
        else:
            y = y + 1
    return zellebearbeitung

def display(zellen): # zeigt das zellen raster an
    i = 0
    z = 0
    while (i < zellenxachse):
        i = i + 1
        list = []
        while (z < zellenyachse * i):
            list.append(zellen[z])
            z = z + 1
        print(list)
    print("\n")


Befüllen()

Setzelle(1, 1, 0)
Setzelle(2, 1, 0)
Setzelle(2, 3, 0)
Setzelle(1, 3, 0)
Setzelle(3, 1, 0)
Setzelle(3, 3, 0)
#display(zellen)
#display(Fraim())
#zel = Fraim()[:]
#zellen = Fraim()[:]
#display(zellen)
