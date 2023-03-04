import pygame


class Button:
    def __init__(self, x, y, image, display_surface):

        self.clicked = False
        self.screen = display_surface
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self):

        action = False

        self.screen.blit(self.image, (self.rect.x, self.rect.y))

        pos = pygame.mouse.get_pos()

        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] == 1 and self.clicked == False:
                self.clicked = True
                action = True

        return action
