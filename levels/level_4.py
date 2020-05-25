from entities.enemy import Enemy, EnemyBullet
from tools.colours import *
from random import choice, randrange
from tools.globals import *
from tools.images import kanna_stage_one, basic_enemy_four


def level_4_preboss(enemy_sprite_group, player):
	player.reset_position()
	enemy_spawn_y = 40
	for i in range(3):
		enemy_spawn_x = 0
		for x in range(15):
			new_enemy = Enemy(200, basic_enemy_four.convert(), enemy_spawn_x, enemy_spawn_y)
			enemy_sprite_group.add(new_enemy)
			enemy_spawn_x += 40
		enemy_spawn_y += 40


def level_4_preboss_bullets(enemy_sprite_group, enemy_bullet_group):
	enemy = choice(enemy_sprite_group.sprites())
	enemy_bullet = EnemyBullet(20, 20, GREEN, enemy.rect.x + 5, enemy.rect.y + 12)
	enemy_bullet_group.add(enemy_bullet)


def level_4_boss(enemy_sprite_group):
	boss_spawn_x = 50
	for i in range(3):
		boss = Enemy(6666, kanna_stage_one, boss_spawn_x, 10)
		boss_spawn_x += 350
		enemy_sprite_group.add(boss)


def level_4_boss_attack(enemy_bullet_group):
	bullet = EnemyBullet(15, 15, BLACK, randrange(0, SCREEN_WIDTH - 15), 0)
	enemy_bullet_group.add(bullet)
