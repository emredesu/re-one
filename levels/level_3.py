from entities.enemy import *
from tools.colours import BLACK, GREEN
from tools.images import basic_enemy_three, ram
import random


def level_3_preboss(enemy_sprite_group, player):
	player.reset_position()
	enemy_spawn_y = 40
	for i in range(3):
		enemy_spawn_x = 0
		for x in range(15):
			new_enemy = Enemy(150, basic_enemy_three.convert(), enemy_spawn_x, enemy_spawn_y)
			enemy_sprite_group.add(new_enemy)
			enemy_spawn_x += 40
		enemy_spawn_y += 40


def level_3_preboss_bullets(enemy_sprite_group, enemy_bullet_group):
	enemy = random.choice(enemy_sprite_group.sprites())
	enemy_bullet = EnemyBullet(12, 12, BLACK, enemy.rect.x + 3, enemy.rect.y + 12)
	enemy_bullet_group.add(enemy_bullet)


def level_3_boss(enemy_sprite_group):
	boss = Enemy(7000, ram.convert(), 0, 10)
	enemy_sprite_group.add(boss)


def level_3_boss_attack(enemy_bullet_group):
	bullet_spawn_pos_x = 0
	for i in range(25):
		yet_another_lone_bullet_among_all_the_bullets_isnt_life_lonely_sometimes = EnemyBullet(30, 30, GREEN, bullet_spawn_pos_x, 0)
		enemy_bullet_group.add(yet_another_lone_bullet_among_all_the_bullets_isnt_life_lonely_sometimes)
		bullet_spawn_pos_x += 40
