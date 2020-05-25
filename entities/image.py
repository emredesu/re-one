import pygame


class Image(pygame.sprite.Sprite):
	def __init__(self, image, posx, posy):
		super().__init__()

		self.image = image
		self.rect = self.image.get_rect()

		self.rect.x = posx
		self.rect.y = posy
