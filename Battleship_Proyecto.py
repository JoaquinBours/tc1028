#Joaquin Robinson Bours
#A00232355
#Santiago Robinson Bours
#A00232346
#22 de Octubre del 2021
#TC1028-G4



#%%
def leeBattleship(): #Leemos el archivo del battleship
    Battleship = [] #y lo convirtimos a matriz
    fo = open("battleship.txt",'r')
    while True:
        linea = fo.readline()
        if(not linea):
            break
        linea=linea.strip('\n')
        listaLinea = linea.split(' ')
        Battleship.append(listaLinea)
    fo.close()
    return Battleship
    
    
def leeControl(): #Leemos el archivo del control
    Control = [] #y lo convirtimos a matriz
    fo = open("control.txt",'r')
    while True:
        linea = fo.readline()
        if(not linea):
            break
        linea=linea.strip('\n')
        listaLinea = linea.split(' ')
        Control.append(listaLinea)
    fo.close()
    return Control


def rowcol(Battleship,renglon,columna): #Me dice si es renglon o columna
    if columna < (len(Battleship[renglon])-1): #Te avisa si estas en la orilla
        if (Battleship[renglon][columna+1] == 'T'):
            return 'h'
    elif columna > 0:
        if (Battleship[renglon][columna-1] == 'T'):
            return 'h'
    else:
        return 'v'    


def combate(Battleship, Control, Jugador):
    points=0
    renglon= int(input('Que renglon desea atacar? (Escoge del 0 al 19)'))
    columna= int(input('Que columna desea atacar? (Escoge del 0 al 19)'))
    #print con columnas y renglones
    print(Battleship[renglon][columna])
    if (Battleship[renglon][columna]== 'T'):
        print('Hundiste una nave')
        t = open('battleship.txt','r')
        tablero = t.read()
        t.close()
        tb = []
        for i in list(tablero):
            if i == '0' or i == 'T' or i == '1' or i == '2':
                tb.append(i)
        if rowcol(Battleship,renglon,columna) == 'h':
            Battleship[renglon][columna]=Jugador
            points=1
            print('La nave esta horizontal')
            col=columna
            while True: #Esto fue para hicerse hacia la izquierda
                if col>0 and Battleship[renglon][col-1]=='T':
                    points = points+1
                    Battleship[renglon][col-1] = Jugador
                    tb[renglon*20+col-1] = Jugador
                    col = col-1
                else:
                    break
            col=columna
            while True: #Esto es para la derecha
                if col<(len(Battleship[renglon])-1) and Battleship[renglon][col+1]=='T':
                    points = points+1
                    Battleship[renglon][col+1] = Jugador
                    tb[renglon*20+col+1] = int(Jugador) 
                    col = col+1  
                else:
                    break
            t = open('battleship.txt','w')
            
            for j in range(20):
                table = ''
                for i in range(20):
                    table = table + str(tb[i+j*20])+' '
                table = table + '\n'
                t.write(table) 
            t.close()
            for i in range(20):
                for j in range(20):
                    print(Battleship[i][j],end='')
                print()
            print('Tus puntos son: ', points)
        else:
            print('Fallaste')
    else:
        print('Fallaste buddy!')


def main():
    Jugador = '0'
    Battleship = leeBattleship()
    Control = leeControl()
    print('Bienvenido al juego del Battleship')
    print('Primero verificaremos si es tu turno')
    turno=Control[-1][0]
    if(turno=="1"):
        Jugador = '1'
        print("Es el turno de Paulo")
    if (turno=="2"):
        Jugador = '2'
        print("Es el turno de Gabriel")
    combate(Battleship,Control, Jugador)
main()