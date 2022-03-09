import main_class_lib as Pix

import pgzero, pgzrun, pygame
import math, sys, random
# from enum import Enum


class Game:
    def __init__(self, width = 360, height = 480, name = "Busy_game", FPS = 120 ):
        self.name = name
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.FPS = FPS
        self.running = True


    def game_cycle(self, *args):
            self.clock.tick(self.FPS)


    def start(self):
        pygame.init()
        # pygame.mixer.init()
        pygame.display.set_caption(self.name)
        # self.game_cycle()


    def events(self, *args):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            for fnk in args:
                fnk()


    def hang_on_key(self, funk, key):
        pass


    def collisions_find(self):
        pass


# class Object(pygame.sprite.Sprite):
#     def __init__(self):
#         pass

class Wall(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x = x
        self.y = y
        self.width = width
        self.height = height



class Move_obj(pygame.sprite.Sprite):
    def __init(self, x, y, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.rect = self.image.get_rect(center=(x, y))
        self.x  = x
        self.y  = y
        self.vx = 0
        sekf.vy = 0

    def update(self):
        pass


class Counter:
    def __init__(self):
        self.count = 0

    def count(self, value = 1):
        self.count += value

    def reset(self, value = 0):
        self.count = value

# class Multi_Counter:
#     def __init__(self,)




#






    # def game_cycle(fnk):
    #     def wraper(self):
    #         fnk(self)
    #         while self.running:
    #             self.clock.tick(self.FPS)
    #             for event in pygame.event.get():
    #                 # check for closing window
    #                 if event.type == pygame.QUIT:
    #                     self.running = False
    #     return wraper
    #
    #
    # @game_cycle
    # def start(self):
    #     pygame.init()
    #     # pygame.mixer.init()
    #     pygame.display.set_caption(self.name)
