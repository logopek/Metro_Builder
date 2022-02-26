import random

import pygame

color = 1

abc = 'qwertyuiopasdfghjklzxcvbnm'
class Metro_station(pygame.sprite.Sprite, pygame.font.Font):
    def __init__(self):
        super().__init__()
        global color
        self.colors = ['red', 'green', 'blue', 'black']
        self.image = pygame.image.load(f'Assets/{self.colors[color]}.png')
        self.rect = self.image.get_rect(bottomright=pygame.mouse.get_pos())
        self.text = pygame.font.SysFont('Segoe UI', 15, bold=True).render(''.join(random.choices(abc, k=7)), False, (0, 0, 0))

    def ru(self):
        return self.image, self.rect, self.text


def nextIndex():
    global color
    if color == 3:
        color = 0
    else:
        color += 1


def main():
    screen = pygame.display.set_mode((1000, 1000))
    screen.fill((255, 255, 255))
    # move = False
    pygame.display.set_caption('Metro Builder')
    pygame.display.flip()
    done = False
    sprites = []
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                # move = False

                object = Metro_station().ru()
                print(object)
                screen.blit(object[0], object[1])
                screen.blit(object[2], (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] - 15))
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                nextIndex()

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
