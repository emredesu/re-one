from entities.enemy import *
from tools.colours import BLACK, MAGENTA
import random
from tools.images import basic_enemy_two, beatrice


def level_2_preboss(enemy_sprite_group, player):
	player.reset_position()
	enemy_spawn_y = 40
	for i in range(3):
		enemy_spawn_x = 200
		for x in range(15):
			new_enemy = Enemy(100, basic_enemy_two.convert(), enemy_spawn_x, enemy_spawn_y)
			enemy_sprite_group.add(new_enemy)
			enemy_spawn_x += 40
		enemy_spawn_y += 40


def level_2_preboss_bullets(enemy_sprite_group, enemy_bullet_group):
	enemy = random.choice(enemy_sprite_group.sprites())
	enemy_bullet = EnemyBullet(10, 10, BLACK, enemy.rect.x + 3, enemy.rect.y + 12)
	enemy_bullet_group.add(enemy_bullet)


def level_2_boss(enemy_sprite_group):
	boss = Enemy(5000, beatrice.convert(), 400, 10)
	enemy_sprite_group.add(boss)


line_1_width = 0


def level_2_boss_attack_1(enemy_bullet_group):
	global line_1_width
	line1_width = random.randrange(0, SCREEN_WIDTH - 100)
	bullet_line_1 = EnemyBullet(line1_width, 10, BLACK, 0, 0)
	bullet_line_2 = EnemyBullet(SCREEN_WIDTH - line1_width - 70, 10, BLACK, line1_width + 70, 0)
	enemy_bullet_group.add(bullet_line_1, bullet_line_2)


def level_2_boss_attack_2(enemy_bullet_group):
	bullet = EnemyBullet(15, 15, MAGENTA, random.choice(list(range(0, line_1_width + 100)) + list(range(line_1_width + 170, SCREEN_WIDTH))), 0)
	enemy_bullet_group.add(bullet)
