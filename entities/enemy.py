import pygame
from tools.colours import WHITE
from tools.globals import SCREEN_HEIGHT, SCREEN_WIDTH


class Enemy(pygame.sprite.Sprite):
	def __init__(self, health, image, spawn_pos_x, spawn_pos_y):
		super().__init__()
		# temp
		self.image = image
		self.health = health

		self.rect = self.image.get_rect()

		self.rect.x = spawn_pos_x
		self.rect.y = spawn_pos_y

	def move_right(self, pixels):
		if not self.rect.x > 30 + SCREEN_WIDTH:
			self.rect.x += pixels

	def move_left(self, pixels):
		if not self.rect.x < 0:
			self.rect.x -= pixels

	def move_down(self, pixels):
		if not self.rect.y + 30 > SCREEN_HEIGHT:
			self.rect.y += pixels

	def move_up(self, pixels):
		if not self.rect.y < 0:
			self.rect.y -= pixels

	def move_upright(self, pixels):
		self.move_right(pixels)
		self.move_up(pixels)

	def move_upleft(self, pixels):
		self.move_left(pixels)
		self.move_up(pixels)

	def move_downright(self, pixels):
		self.move_right(pixels)
		self.move_down(pixels)

	def move_downleft(self, pixels):
		self.move_left(pixels)
		self.move_down(pixels)


class EnemyBullet(pygame.sprite.Sprite):
	def __init__(self, width, height, color, spawn_pos_x, spawn_pos_y):
		super().__init__()

		self.image = pygame.Surface([width, height])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)

		pygame.draw.rect(self.image, color, [0, 0, width, height])

		self.rect = self.image.get_rect()

		self.rect.x = spawn_pos_x
		self.rect.y = spawn_pos_y
