import os
from readchar import readkey, key

lab = """..###################
....#...#...........#
#.#.#.###.###.#####.#
#.#.....#...#.#.#...#
###.#.#.###.#.#.#.#.#
#.#.#.#.#...#.#.#.#.#
#.#.###.#.#####.#.###
#...#.#.....#.#.....#
#####.#.###.#.#######
#...#.....#.#.......#
#.#.#####.###.#.###.#
#.#.#.#...#...#.#.#.#
#.#.#.#.###.#####.###
#.#.#.#.....#.....#.#
#.###.#.###.#.#####.#
#.........#.....#...#
#.###.#######.###.###
#.#...#...#.........#
#.###.#.#####.#####.#
#...#.....#.....#...#
###################.#"""

[0][0]
[19][20]

def mostrar(mapa):
    # join en cadenas
    for fila in mapa:
        linea = ""
        for char in fila:
            linea += char
        print(linea)
matriz = []
for linea in lab.split("\n"):
    matriz.append(list(linea))
matriz[0][0] = "P"


def cls_terminal():
    os.system('cls' if os.name=='nt' else 'clear')

def display_map(mapa):
    cls_terminal()
    for row in mapa:
        print("".join(row))

def main_loop(mapa, initial_pos, final_pos):
    px, py = initial_pos

    while (px, py) != final_pos:
        display_map(mapa)

        key = readkey()
        if key == key.UP:
            n_px = px - 1
            n_py = py
        elif key == key.UP:
            n_px = px
            n_py = py - 1
        elif key == key.LEFT:
            n_px = px + 1
            n_py = py
        elif key == key.RIGHT:
            n_px = px
            n_py = py + 1
        else:
            px = 0
            py = 0