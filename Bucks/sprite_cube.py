import pygame
import os

game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'sprites')

class CubeTop(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'cube_1.png')).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.y -= 100
        self.initialPos = self.rect.y
    def ChangeSprite(self, sprite):
        self.image = pygame.image.load(os.path.join(img_folder, sprite)).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
    def Show(self, show):
        if show:
            self.rect.y = self.initialPos 
        else:
            self.rect.y = self.initialPos - 1337

class CubeLeft(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'cube_3.png')).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x -= 75
        self.initialPos = self.rect.x
    def ChangeSprite(self, sprite):
        self.image = pygame.image.load(os.path.join(img_folder, sprite)).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
    def Show(self, show):
        if show:
            self.rect.x = self.initialPos
        else:
            self.rect.x = self.initialPos - 1337

class CubeRight(pygame.sprite.Sprite):
    def __init__(self, WIDTH, HEIGHT):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(os.path.join(img_folder, 'cube_6.png')).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
        self.rect = self.image.get_rect()
        self.rect.center = (WIDTH / 2, HEIGHT / 2)
        self.rect.x += 75
        self.initialPos = self.rect.x
    def ChangeSprite(self, sprite):
        self.image = pygame.image.load(os.path.join(img_folder, sprite)).convert()
        self.size = self.image.get_size()
        self.image = pygame.transform.scale(self.image, (int(self.size[0]/2), int(self.size[1]/2)))
    def Show(self, show):
        if show:
            self.rect.x = self.initialPos
        else:
            self.rect.x = self.initialPos - 1337