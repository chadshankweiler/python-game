import pygame
from settings import *
from support import *
from timer import Timer
from random import randint

class Generic(pygame.sprite.Sprite):
    def __init__(self, pos, surf, groups, z = LAYERS['main']):
        super().__init__(groups)
        self.image = surf
        self.rect = self.image.get_rect(topleft = pos)
        self.z = z
        self.hitbox = self.rect.copy().inflate(-self.rect.width * 0.2, -self.rect.height * 0.75)

class Water(Generic):
    def __init__(self, pos, frames, groups):

        # Animation Setup
        self.frames = frames
        self.frame_index = 0
        self.animation = []

        # Sprite
        super().__init__(
                pos = pos, 
                surf = self.frames[self.frame_index],
                groups = groups,
                z = LAYERS['water']
                )


        pass

    def animate(self,dt):
        self.frame_index += 5 * dt
        if self.frame_index >= len(self.frames):
            self.frame_index = 0
        self.image = self.frames[int(self.frame_index)]

    def update(self,dt):
        self.animate(dt)

class WildFlower(Generic):
    def __init__(self, pos, frames, groups):
        super().__init__(pos, frames, groups)
        self.hitbox = self.rect.copy().inflate(-20, -self.rect.height *0.9)


class Tree(Generic):
    def __init__(self, pos, frames, groups, name, player_add = ''):
        super().__init__(pos, frames, groups)

        # Tree Attributes
        self.health = 5
        self.alive = True
        stump_path = f'../graphics/stumps/{"small" if name == "Small" else "large"}.png'
        self.stump_surf = pygame.image.load(stump_path).convert_alpha()

        # Apples 
        self.apple_surf = pygame.image.load('../graphics/fruit/apple.png')
        self.apple_pos = APPLE_POS[name]
        self.apple_sprites = pygame.sprite.Group()
        self.create_fruit()
        
        self.player_add = player_add

    def create_fruit(self):
        for pos in self.apple_pos:
            if randint(0,10) < 2:
                x = pos[0] + self.rect.left
                y = pos[1] + self.rect.top
                Generic(
                        pos = (x, y),
                        surf = self.apple_surf,
                        groups = [self.apple_sprites, self.groups()[0]],
                        z = LAYERS['fruit'])


