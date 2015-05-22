import os
import pygame
import pickle

def load_from_fs():
    girls = {}
    for fold in os.listdir('./data'):
        if os.path.isdir('./data/' + fold):
            girls[fold] = []

    for girl in girls:
        for file in os.listdir('./data/' + girl):
            if not os.path.isdir('./data/' + girl + '/' + file):
                girls[girl].append('./data/' + girl + '/' + file)
        if len(girls[girl]) == 0:
            girls[girl].append(None)

    return girls

def load_from_file(file):
    with open(file, 'r') as fin:
        return pickle.load(fin)

def save_to_file(file, obj):
    with open(file, 'w') as fout:
        pickle.dump(obj, fout)

def discard(girls, bad):
    for key in bad:
        if key in girls:
            del girls[key]

def main():
    girl = 0
    photo = 0
    size_x, size_y = 800, 600
    done = False
    girls = load_from_fs()
    good = {}
    bad = {}
    pygame.init()
    window = pygame.display.set_mode((size_x, size_y))

    img = pygame.image.load(girls[girls.keys()[girl]][photo]).convert()
    upd = False
    window.blit(img, (0, 0))
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYUP:
                upd = True
                if event.key == pygame.K_s:
                    girl = (girl - 1) % len(girls)
                    photo = 0
                elif event.key == pygame.K_w:
                    girl = (girl + 1) % len(girls)
                    photo = 0
                elif event.key == pygame.K_a:
                    photo = (photo + 1) % len(girls[girls.keys()[girl]])
                elif event.key == pygame.K_d:
                    photo = (photo + 1) % len(girls[girls.keys()[girl]])
                elif event.key == pygame.K_g:
                    good[girls.keys()[girl]] = girls[girls.keys()[girl]]
                    photo = 0
                    del girls[girls.keys()[girl]]
                elif event.key == pygame.K_b:
                    bad[girls.keys()[girl]] = girls[girls.keys()[girl]]
                    del girls[girls.keys()[girl]]
                    photo = 0
                elif event.key == pygame.K_u:
                    good = load_from_file('good')
                    bad = load_from_file('bad')
                    discard(girls, good)
                    discard(girls, bad)
                    print '%d good, %d bad, %d remains' % tuple(map(len, (good, bad, girls)))
                elif event.key == pygame.K_f:
                    save_to_file('good', good)
                    save_to_file('bad', bad)
                    save_to_file('remains', girls)
                elif event.key == pygame.K_r:
                    girls = load_from_file('remains')

            if upd:
                try:
                    upd = False
                    print girl, photo, girls.keys()[girl]
                    img = pygame.image.load(girls[girls.keys()[girl]][photo]).convert()
                    window.blit(img, (0, 0))
                except Exception as e:
                    print e


        pygame.display.update()

main()
