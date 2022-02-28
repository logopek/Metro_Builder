import random

import pygame

color = 1
prevposes = {  # initialize previous positions
    'red': (),
    'green': (),
    'blue': (),
    'black': ()
}
abc = 'qwertyuiopasdfghjklzxcvbnm'  # random symbols


class Metro_station(pygame.sprite.Sprite, pygame.font.Font):
    '''Initialize metro station'''

    def __init__(self):
        super().__init__()
        global color
        self.colors = ['red', 'green', 'blue', 'black']  # colors list
        self.image = pygame.image.load(f'Assets/{self.colors[color]}.png')  # path to now color
        self.rect = self.image.get_rect(
            bottomright=(pygame.mouse.get_pos()[0] + 20, pygame.mouse.get_pos()[1] + 10))  # create rect of image
        self.text = pygame.font.SysFont('Segoe UI', 15, bold=True).render(''.join(random.choices(abc, k=7)), False,
                                                                          (0, 0, 0))  # name of station


class Lines(pygame.sprite.Sprite):
    def __init__(self):
        self.colors = ['red', 'green', 'blue', 'black']  # against

    def draw(self, newpos, prevpos, surface):
        '''Main task is draw line'''
        try:
            self.nowprevpos = prevposes[self.colors[color]]  # get previous position of now color
            pygame.draw.line(surface=surface, color=self.colors[color], start_pos=(newpos[0] + 10, newpos[1] + 1),
                             end_pos=self.nowprevpos, width=5)  # drawing a line
        except:
            pass


def nextIndex():
    global color
    # color index to create right circle
    if color == len(Metro_station().colors) - 1:
        color = 0  # setting 0 if index greater than list length
    else:
        color += 1  # add index


def main():
    global prevposes  # change global previous positions
    screen = pygame.display.set_mode((1000, 1000))  # create display
    screen.fill((255, 255, 255))  # fill white
    colors = ['red', 'green', 'blue', 'black']  # against colors
    pygame.display.set_caption('Metro Builder')
    pygame.display.flip()
    done = False
    while not done:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:  # quit
                done = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:  # unpressed left mouse button

                object = Metro_station()  # new Metro_station

                newpos = (pygame.mouse.get_pos())  # new position (its mouse position
                Lines().draw(pygame.mouse.get_pos(), prevposes[colors[color]], screen)  # drawing line
                screen.blit(object.image, object.rect)  # drawing metro

                screen.blit(object.text, (pygame.mouse.get_pos()[0] + 10, pygame.mouse.get_pos()[1] - 15))  # draw text

                prevposes[colors[color]] = (pygame.mouse.get_pos())  # change previous position
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                nextIndex()  # new index

        pygame.display.flip()


if __name__ == '__main__':
    pygame.init()
    main()
