import pygame


class Button(pygame.sprite.Sprite):

    def __init__(self, name):
        super().__init__()
        self.name = "Button"

class LevelButton(Button):

    def __init__(self):
        super().__init__("level button")


