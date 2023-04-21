# SANCHEZ CALVIMONTES PABLO
# INGENIERIA DE SISTEMAS
# SIS 420 - INTELIGENCIA ARTIFICIAL
# ING PACHECO LORA CARLOS 


# PRIMER PARCIAL - EJERCICIO 1
# ===================================================== #

import random
import time


# funcion que genera un laberinto segun las dimenciones que le mandemos como parametro

def generarLaberinto(filas, columnas):
    laberintoTemporal = []
    for row in range(0, filas):
        fila = []
        for column in range(0, columnas):
            if (row == 0 or column == 0 or row == filas-1 or column == columnas - 1):
                fila.append("#")
            else:
                fila.append(" ")
        laberintoTemporal.append(fila)

    return laberintoTemporal
#print(generarLaberinto(10,10))

# funcion que dibuja el laberinto enviado por consola

def dibujarLaberinto(laberinto):
    for row in laberinto:
        print("".join(row))

# laberinto = generarLaberinto( 12, 12 )
# print(dibujarLaberinto(laberinto))

# funcion que genera automaticamente las paredes del laberinto segun la cantidad que el usuario escoja

def generarParedes(laberinto, numeroParedes):
    if( numeroParedes == 0 ):
        return
    
    x,y = [ random.randint( 1, len( laberinto ) -2 ), random.randint( 1, len( laberinto[ 0 ] ) - 2) ]
    if (laberinto[x][y] == " "):
        if (laberinto[x][y - 1] == " " or
                laberinto[x][y + 1] == " " or
                laberinto[x + 1][y] == " " or
                laberinto[x - 1][y] == " "):

            laberinto[x][y] = "#"
            numeroParedes = numeroParedes - 1
    return generarParedes(laberinto, numeroParedes)


# funcion que genera el sujeto que buscara la meta en el laberinto

def generarCoordenadasInicio(laberinto=None, jugador=None):
    x, y = [1,1]

    if (laberinto[x][y] == " "):
        laberinto[x][y] = jugador
        return [x, y]
    else:
        return generarCoordenadasInicio(laberinto, jugador)

# funcion que genera la meta en el laberinto

def generarCoordenadasMeta1(laberinto, jugador, meta):
    x, y = [10,4]
    if (laberinto[x][y] != "#" and laberinto[x][y] != jugador):
        laberinto[x][y] = meta
        return [x, y]
    else:
        return generarCoordenadasMeta1(laberinto, jugador, meta)
def generarCoordenadasMeta2(laberinto, jugador, meta):
    x, y = [10,10]
    if (laberinto[x][y] != "#" and laberinto[x][y] != jugador):
        laberinto[x][y] = meta
        return [x, y]
    else:
        return generarCoordenadasMeta2(laberinto, jugador, meta)
def generarCoordenadasMeta3(laberinto, jugador, meta):
    x, y = [6,10]
    if (laberinto[x][y] != "#" and laberinto[x][y] != jugador):
        laberinto[x][y] = meta
        return [x, y]
    else:
        return generarCoordenadasMeta3(laberinto, jugador, meta)


# funcion recursiva que resolvera el laberinto
def resolverLaberinto(laberinto, coordJugador):

    print("-"*len(laberinto)*2)
    dibujarLaberinto(laberinto)

    x, y = coordJugador
    listaCamino = []
    visitado = []
    meta = []

    movimientos = [[x-1, y], [x+1, y], [x, y-1], [x, y+1]]

    for [coordX, coordY] in movimientos:
        if (laberinto[coordX][coordY] == " "):
            listaCamino.append([coordX, coordY])
        if (laberinto[coordX][coordY] == "."):
            visitado.append([coordX, coordY])
        if (laberinto[coordX][coordY] == "S"):
            meta.append([coordX, coordY])

    if (len(meta) > 0):
        print("FIN")
        return

    if (len(listaCamino) > 0):
        moverX, moverY = listaCamino[random.randint(0, len(listaCamino)-1)]
        laberinto[moverX][moverY] = laberinto[x][y]
        laberinto[x][y] = "."
        return resolverLaberinto(laberinto,  [moverX, moverY])
    elif (len(visitado) > 0):
        moverX, moverY = visitado[random.randint(0, len(visitado)-1)]
        laberinto[moverX][moverY] = laberinto[x][y]
        laberinto[x][y] = "."
        return resolverLaberinto(laberinto,  [moverX, moverY])
    else:
        print("sin solucion")
        return

# funcion que inicia el programa

## main function
def inicio():
    try:
        filas = 12
        columnas = 12
        numParedes = 30
    except:
        pass

    print("Dimencion del laberinto: "+str(filas)+" x "+str(columnas))

    return [filas, columnas, numParedes]

filas, columnas, numParedes = inicio()

laberinto = generarLaberinto(filas, columnas)
generarParedes(laberinto, numParedes)

coordenadasJugador = generarCoordenadasInicio(laberinto, "E")
coordenadasMeta = generarCoordenadasMeta1(laberinto, "*", "S"), generarCoordenadasMeta2(laberinto, "*", "S"), generarCoordenadasMeta3(laberinto, "*", "S")

print("Inicio: E")
print("Meta: S")

TiempoInicio = time.time()

resolverLaberinto(laberinto, coordenadasJugador)
TiempoFin = time.time()

print("Tiempo transcurrido: "+ str(TiempoFin - TiempoInicio) + " segundos")
