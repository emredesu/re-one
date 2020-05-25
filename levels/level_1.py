import random
from tools.colours import BLACK
from entities.enemy import *
from tools.images import basic_enemy_one, felix


def level_1_preboss(enemy_sprite_group):
	enemy_spawn_y = 40

	for i in range(3):
		enemy_spawn_x = 5
		for x in range(25):
			new_enemy = Enemy(50, basic_enemy_one.convert(), enemy_spawn_x, enemy_spawn_y)
			enemy_sprite_group.add(new_enemy)
			enemy_spawn_x += 40
		enemy_spawn_y += 40


def level_1_preboss_bullets(enemy_sprite_group, enemy_bullet_group):
	enemy = random.choice(enemy_sprite_group.sprites())
	enemy_bullet = EnemyBullet(10, 10, BLACK, enemy.rect.x + 3, enemy.rect.y + 12)
	enemy_bullet_group.add(enemy_bullet)


def level_1_boss(enemy_sprite_group):
	boss = Enemy(3000, felix.convert(), 400, 10)
	enemy_sprite_group.add(boss)


def level_1_boss_attack(enemy_bullet_group):
	width = random.randrange(0, SCREEN_WIDTH - 100)
	bullet_line_1 = EnemyBullet(width, 10, BLACK, 0, 0)
	bullet_line_2 = EnemyBullet(SCREEN_WIDTH - width - 90, 10, BLACK, width + 90, 0)
	enemy_bullet_group.add(bullet_line_1, bullet_line_2)
