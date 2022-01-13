import pygame
import sprite_cube
import threading

class Render:
    def __init__(self):
        self.WIDTH = 800
        self.HEIGHT = 600
        self.FPS = 30

        self.isRunning = False
        self.isWaitButton = False
        self.StringScores = ""
        self.StringWhoPushing = ""
        self.NominalBucks = ""

        th = threading.Thread(target=self.Run, args=())
        th.start()

    def blit_text(self, surface, text, pos, font, color=pygame.Color('black')):
        words = [word.split(' ') for word in text.splitlines()]  # 2D array where each row is a list of words.
        space = font.size(' ')[0]  # The width of a space.
        max_width, max_height = surface.get_size()
        x, y = pos
        for line in words:
            for word in line:
                word_surface = font.render(word, 0, color)
                word_width, word_height = word_surface.get_size()
                if x + word_width >= max_width:
                    x = pos[0]  # Reset the x.
                    y += word_height  # Start on new row.
                surface.blit(word_surface, (x, y))
                x += word_width + space
            x = pos[0]  # Reset the x.
            y += word_height  # Start on new row.

    def Run(self):
        pygame.init()
        pygame.mixer.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))
        pygame.display.set_caption("Bucks")
        self.clock = pygame.time.Clock()

        self.all_sprites = pygame.sprite.Group()
        self.CubeTop = sprite_cube.CubeTop(self.WIDTH, self.HEIGHT)
        self.CubeTop.Show(False)
        self.all_sprites.add(self.CubeTop)
        self.CubeLeft = sprite_cube.CubeLeft(self.WIDTH, self.HEIGHT)
        self.CubeLeft.Show(False)
        self.all_sprites.add(self.CubeLeft)
        self.CubeRight = sprite_cube.CubeRight(self.WIDTH, self.HEIGHT)
        self.CubeRight.Show(False)
        self.all_sprites.add(self.CubeRight)

        self.GAME_FONT = pygame.font.SysFont('Comic Sans MS', 24)

        self.isRunning = True
        while self.isRunning:
            self.clock.tick(self.FPS)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        self.isWaitButton = False
            
            self.screen.fill((128, 166, 255))
            if(self.isWaitButton):
                text_surface = self.GAME_FONT.render("Пробел - бросить кость", False, (255, 0, 0))
                self.screen.blit(text_surface, (500, 500))

            text_surface = self.GAME_FONT.render(self.StringWhoPushing, False, (255, 0, 0))
            self.screen.blit(text_surface, (270, 10))
            text_surface = self.GAME_FONT.render(self.NominalBucks, False, (255, 255, 255))
            self.screen.blit(text_surface, (520, 380))
            self.blit_text(self.screen, self.StringScores, (15, 420), self.GAME_FONT)

            self.all_sprites.update()
            self.all_sprites.draw(self.screen)
            pygame.display.flip()
        pygame.quit()