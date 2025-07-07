
import random, time, copy, sys

try:
    import bext
except ImportError:
    print('This program requires the bext module, which you')
    print('can install by following the instructions at')
    print('https://pypi.org/project/Bext/')
    sys.exit()

PAUSE_LENGTH = 0.5
WIDTH = 79
HEIGHT = 20
TREE = 'A'
FIRE = '@'
EMPTY = ' '
LAKE = '~'  # Water feature that acts as a firebreak

INITIAL_TREE_DENSITY = 20  # 1-100
GROW_CHANCE = 1            # 1-100
FIRE_CHANCE = 40           # 1-100

def main():
    forest = createNewForest()
    while True:
        displayForest(forest)
        nextForest = copy.copy(forest)
        for x in range(WIDTH):
            for y in range(HEIGHT):
                if forest[(x, y)] == TREE:
                    for ix in [-1, 0, 1]:
                        for iy in [-1, 0, 1]:
                            if (ix != 0 or iy != 0) and (0 <= x + ix < WIDTH) and (0 <= y + iy < HEIGHT):
                                if forest.get((x + ix, y + iy)) == FIRE:
                                    nextForest[(x, y)] = FIRE
                                    break
                elif forest[(x, y)] == FIRE:
                    nextForest[(x, y)] = EMPTY
                elif forest[(x, y)] == EMPTY:
                    if random.randint(1, 100) <= GROW_CHANCE:
                        nextForest[(x, y)] = TREE
        forest = nextForest
        time.sleep(PAUSE_LENGTH)

def createNewForest():
    forest = {'width': WIDTH, 'height': HEIGHT}
    for x in range(WIDTH):
        for y in range(HEIGHT):
            lake_start_x = WIDTH // 2 - 5
            lake_end_x = WIDTH // 2 + 5
            lake_start_y = HEIGHT // 2 - 2
            lake_end_y = HEIGHT // 2 + 2
            if lake_start_x <= x <= lake_end_x and lake_start_y <= y <= lake_end_y:
                forest[(x, y)] = LAKE
            elif random.randint(1, 100) <= INITIAL_TREE_DENSITY:
                forest[(x, y)] = TREE
            else:
                forest[(x, y)] = EMPTY
    return forest

def displayForest(forest):
    bext.clear()
    for y in range(HEIGHT):
        for x in range(WIDTH):
            if forest[(x, y)] == TREE:
                bext.fg('green')
                print(TREE, end='')
            elif forest[(x, y)] == FIRE:
                bext.fg('red')
                print(FIRE, end='')
            elif forest[(x, y)] == LAKE:
                bext.fg('blue')
                print(LAKE, end='')
            else:
                print(EMPTY, end='')
        print()
    bext.fg('reset')
    print('Grow: {}%  Fire: {}%  Press Ctrl-C to quit.'.format(GROW_CHANCE, FIRE_CHANCE))

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        sys.exit()
