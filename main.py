import os
import math
import time
import random

# Taille de la carte
WIDTH, HEIGHT = 20, 20

# Joueur
player_x, player_y = WIDTH // 2, HEIGHT // 2
player_direction = 0  # 0: Nord, 1: Est, 2: Sud, 3: Ouest

# Arbres
trees = [(random.randint(0, WIDTH - 1), random.randint(0, HEIGHT - 1))
         for _ in range(10)]


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def draw_view():
    view = [['.' for _ in range(5)] for _ in range(5)]

    for tree in trees:
        dx = tree[0] - player_x
        dy = tree[1] - player_y
        distance = math.sqrt(dx**2 + dy**2)

        if distance < 5:
            angle = math.atan2(dy, dx) - math.pi / 2 * player_direction
            x = int(2 + 2 * math.sin(angle))
            y = min(4, int(4 - distance))
            if 0 <= x < 5 and 0 <= y < 5:
                view[y][x] = 'T'

    for row in view:
        print(' '.join(row))


def draw_map():
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if (x, y) == (player_x, player_y):
                print('P', end='')
            elif (x, y) in trees:
                print('T', end='')
            else:
                print('.', end='')
        print()


def move(dx, dy):
    global player_x, player_y
    new_x, new_y = player_x + dx, player_y + dy
    if 0 <= new_x < WIDTH and 0 <= new_y < HEIGHT:
        player_x, player_y = new_x, new_y


def cut_tree():
    for tree in trees:
        if abs(tree[0] - player_x) <= 1 and abs(tree[1] - player_y) <= 1:
            trees.remove(tree)
            return True
    return False


while True:
    clear_screen()
    print("Vue à la première personne:")
    draw_view()
    print("\nCarte:")
    draw_map()
    print("\nPosition:", player_x, player_y)
    print("Direction:", ["Nord", "Est", "Sud", "Ouest"][player_direction])
    print(
        "\nCommandes: w (avancer), s (reculer), a (gauche), d (droite), c (couper), q (quitter)"
    )

    action = input("Action: ").lower()

    if action == 'w':
        dx = [0, 1, 0, -1][player_direction]
        dy = [-1, 0, 1, 0][player_direction]
        move(dx, dy)
    elif action == 's':
        dx = [0, -1, 0, 1][player_direction]
        dy = [1, 0, -1, 0][player_direction]
        move(dx, dy)
    elif action == 'a':
        player_direction = (player_direction - 1) % 4
    elif action == 'd':
        player_direction = (player_direction + 1) % 4
    elif action == 'c':
        if cut_tree():
            print("Arbre coupé!")
        else:
            print("Pas d'arbre à proximité.")
        time.sleep(1)
    elif action == 'q':
        break
    else:
        print("Commande non reconnue.")
        time.sleep(1)

print("Merci d'avoir joué!")
