from Pin_Pong_lib import *


PLAYER_SPEED = 5
BALL_SPEED   = 50
GATE_WIDTH   = 25


class Pin_Pong(Game):
    def __init__(self, width = 700, height = 500):
        self.width = width
        self.height = height
        self.surf = pygame.Surface((200, 150))
        super().__init__(self, name = "Pin Pong")

    ###
        # self.gate_l = Gate(0, 0, GATE_WIDTH, self.height)
        # self.gate_r = Gate(self.width - GATE_WIDTH, 0, GATE_WIDTH, self.height)
        self.requet_l = Raquet((50, self.height/2), 20, self.height, "./images/bat00.png", (0,self.height), PLAYER_SPEED)

        # all_sprites = pygame.sprite.Group()
        # all_sprites.add(self.requet_l)


    def start(self):
        super().start()
        self.screen = pygame.display.set_mode((self.width, self.height))

        ########
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                # self.events(event)
            self.key_events()


            self.game_cycle()


    def draw(self):
        self.requet_l.draw(self.screen)


    def game_cycle(self):

        self.screen.fill((255, 255, 255))
        # self.gate_r.update(self.screen)
        # self.gate_l.update(self.screen)

        # self.requet_l.update(5, self.screen)
        # pygame.display.update()

        self.draw()

        pygame.display.flip()

        super().game_cycle()


    def collisions_find(self):
            pass


    def key_events(self):
            keys = pygame.key.get_pressed()
            if keys[pygame.K_z]:
                 self.requet_l.update(int(PLAYER_SPEED))
            elif keys[pygame.K_a]:
                 self.requet_l.update(int(-PLAYER_SPEED))

    # Not used NOW!
    def events(self, event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                self.requet_l.update(int(PLAYER_SPEED))
            elif event.key == pygame.K_z:
                self.requet_l.update(int(-PLAYER_SPEED))
