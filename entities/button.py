import pygame


class Button(pygame.sprite.Sprite):
	def __init__(self, name, unhovered_image, hovered_image, pos_x, pos_y):
		super().__init__()

		self.name = name

		self.image = unhovered_image

		self.unhovered_image = unhovered_image
		self.hovered_image = hovered_image

		self.rect = self.image.get_rect()
		self.rect.x = pos_x
		self.rect.y = pos_y

	def is_hovered(self):
		return self.rect.collidepoint(pygame.mouse.get_pos())

	def is_clicked(self):
		return pygame.mouse.get_pressed()[0] and self.rect.collidepoint(pygame.mouse.get_pos())