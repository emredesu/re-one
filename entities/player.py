import pygame
from tools.colours import WHITE, RED
from tools.globals import SCREEN_HEIGHT, SCREEN_WIDTH


class Player(pygame.sprite.Sprite):
	def __init__(self, image):
		super().__init__()

		self.image = image

		self.rect = self.image.get_rect()

		self.rect.x = int(SCREEN_WIDTH / 2)
		self.rect.y = SCREEN_HEIGHT - 40

	def move_right(self, pixels):
		if not self.rect.x + 30 > SCREEN_WIDTH:
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

	def reset_position(self):
		self.rect.x = int(SCREEN_WIDTH / 2)
		self.rect.y = SCREEN_HEIGHT - 40


class PlayerBullet(pygame.sprite.Sprite):
	def __init__(self, spawn_pos_x, spawn_pos_y):
		super().__init__()

		self.image = pygame.Surface([6, 6])
		self.image.fill(WHITE)
		self.image.set_colorkey(WHITE)
		# temp
		pygame.draw.rect(self.image, RED, [0, 0, 6, 6])

		self.rect = self.image.get_rect()

		self.rect.x = spawn_pos_x
		self.rect.y = spawn_pos_y
