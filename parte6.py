def string_to_matrix(maze_string):
    lines = maze_string.strip().split('\n')
    maze_matrix = list(map(list, lines))
    return maze_matrix


from functools import reduce

def leer_mapa(map1.txt):
    with open(map1.txt, 'r') as archivo:
        lineas = archivo.readlines()
    
    mapa = reduce(lambda acumulado, linea: acumulado + linea.strip(), lineas, '')
    
    coordenadas = []
    for y, fila in enumerate(lineas):
        for x, celda in enumerate(fila):
            if celda == 'X':
                coordenadas.append((x, y))
    
    return mapa, coordenadas

nombre_archivo = 'map1.txt'
mapa, coordenadas = leer_mapa(map1.txt)
print("map1.txt:")
print(mapa)
print("Coordenadas de 'X':")
print(coordenadas)
