from GAME import *

#   Interactive objects

class Ball(Move_obj):
    def __init__(self, radius, x, y, color = "Red"):
        super().__init__(self, x, y)
        self.radius = radius
        self.color = color

    def update(self):
        pass

class Raquet(Wall, Move_obj):
    def __init__(self, pos, width, height, filename, border, speed):
        Wall.__init__(self, pos[0], pos[1], width, height, filename)
        self.surf = pygame.Surface((10, 10))
        self.image.fill((50,50,50))
        self.rect = self.image.get_rect()
        self.rect.center = (self.width / 2, self.height / 2)
        self.border = border
        self.speed = speed

    def update(self, *args): #ARGS => 1: dy;
        if (4 < self.rect.y < 600): #  So that it does not fly out of the window
            self.rect.y += args[0]
        print(self.rect.y, self.rect.center[1])


        # args[1].blit(self.image,(self.rect.x, self.rect.y))
        # args[1].blit(args[2],(self.rect.x, self.rect.y))
        # args[1].blit(self.image, self.rect)


    def draw(self, *args): #ARGS => 1: screen;
        args[0].blit(self.image,(self.rect.x, self.rect.y))



# class Basic_Wall(Wall):
#     def __init__(self, x, y, width, height, color = "Gray"):
#         super().__init__(self,  x, y, width, height)
#         self.color = color
#
#
#     def update(self, *args):
#         pass


class Gate(Wall):
    def __init__(self, x, y, width, height):
        super().__init__(x, y, width, height)
        self.condition = True

    def update(self, *args):
        pygame.draw.rect(args[0], (0,0,0), (self.x, self.y, self.width, self.height))
