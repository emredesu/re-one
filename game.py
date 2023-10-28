import pygame
from entities.player import Player, PlayerBullet
from sys import getrecursionlimit
from tools.images import player_ded_bg, level_1_bg, level_2_bg, level_3_bg, level_4_bg, kanna_stage_two, subaru, emilia_ending, rem_ending
from datetime import timedelta
from time import time
import webbrowser
# todo: find a better way to import levels
from levels.mainmenu import *
from levels.howtoplay import *
from levels.level_1 import *
from levels.level_2 import *
from levels.level_3 import *
from levels.level_4 import *
from levels.which_ending import *


def game():
	pygame.mixer.pre_init(44100, -16, 1, 512)
	pygame.init()
	start_time = time()

	fail_sfx = pygame.mixer.Sound("sfx/fail.wav")
	pew_sfx = pygame.mixer.Sound("sfx/pew.wav")
	pew_sfx.set_volume(0.2)
	success_sfx = pygame.mixer.Sound("sfx/success.wav")
	ding = pygame.mixer.Sound("sfx/ding.wav")
	ding.set_volume(0.3)

	normal_music_file = pygame.mixer.Sound("music/Kommisar - 信仰の奇跡.ogg")
	normal_music_file.set_volume(0.3)
	boss_music_file = pygame.mixer.Sound("music/boss.wav")
	boss_music_file.set_volume(0.3)
	mainmenu_music_file = pygame.mixer.Sound("music/mainmenu.ogg")
	mainmenu_music_file.set_volume(0.4)
	normal_music = pygame.mixer.Channel(0)
	boss_music = pygame.mixer.Channel(1)
	mainmenu_music = pygame.mixer.Channel(2)
	normal_music.play(normal_music_file, loops=-1)
	boss_music.play(boss_music_file, loops=-1)
	mainmenu_music.play(mainmenu_music_file, loops=-1)
	normal_music.pause()
	boss_music.pause()

	font = pygame.font.Font(None, 24)

	pygame.display.set_caption("re:one")

	screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
	logo = pygame.image.load("sprites/logo.png")
	pygame.display.set_icon(logo)
	clock = pygame.time.Clock()

	level_1_bg_converted = level_1_bg.convert_alpha()
	level_2_bg_converted = level_2_bg.convert_alpha()
	level_3_bg_converted = level_3_bg.convert_alpha()
	level_4_bg_converted = level_4_bg.convert_alpha()
	main_menu_bg_converted = main_menu_bg.convert_alpha()
	emilia_ending_converted = emilia_ending.convert_alpha()
	rem_ending_converted = rem_ending.convert_alpha()

	sprites = pygame.sprite.Group()
	secondary_sprites = pygame.sprite.Group()
	player_bullets = pygame.sprite.Group()
	enemies = pygame.sprite.Group()
	enemy_bullets = pygame.sprite.Group()

	player = Player(subaru.convert())

	current_level = "main_menu"
	mainmenu(sprites)

	# game state vars #
	bullet_time = 0
	timer = 0
	timer_2 = 0
	score = 0
	finish_time_readable = "xd"
	highscore = int(open("highscore.txt", "r").read())
	github_opened = False
	go_right = True
	go_down = True
	player_alive = False
	is_boss = False

	score_text = font.render("Score: {}".format(str(score)), True, CYAN, None)

	def clear_enemy_bullets():
		for enemybullet in enemy_bullets:
			enemybullet.kill()

	def clear_all_sprites():
		# todo: find a better way to do this
		for enemybulletsprite in enemy_bullets:
			enemybulletsprite.kill()
		for normalsprite in sprites:
			normalsprite.kill()
		for playerbulletsprite in player_bullets:
			playerbulletsprite.kill()
		for enemysprite in enemies:
			enemysprite.kill()
		for othersprite in secondary_sprites:
			othersprite.kill()

	def create_bullet():
		if player_alive:
			pew_sfx.play()
			new_bullet = PlayerBullet(player.rect.x + 10, player.rect.y - 12)
			player_bullets.add(new_bullet)

	def player_death():
		normal_music.stop()
		boss_music.stop()
		nonlocal current_level, player_alive
		current_level = "ded"
		player_alive = False

		clear_all_sprites()
		fail_sfx.play()
		screen.blit(player_ded_bg, (0, 0))

	def level_clear():
		boss_music.pause()
		success_sfx.play()
		pygame.time.wait(8000)

	def is_highscore():
		if score > highscore:
			return True
		else:
			return False

	# noinspection PyArgumentList
	pygame.key.set_repeat(1, 1)

	game_running = True

	while game_running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				if is_highscore():
					open("highscore.txt", "w").write(str(score))
				game_running = False

			keys = pygame.key.get_pressed()
			if keys[pygame.K_LEFT]:
				player.move_left(3)
			if keys[pygame.K_LEFT] and keys[pygame.K_LSHIFT]:
				player.move_left(6)
			if keys[pygame.K_RIGHT]:
				player.move_right(3)
			if keys[pygame.K_RIGHT] and keys[pygame.K_LSHIFT]:
				player.move_right(6)
			if keys[pygame.K_UP]:
				player.move_up(3)
			if keys[pygame.K_UP] and keys[pygame.K_LSHIFT]:
				player.move_up(6)
			if keys[pygame.K_DOWN]:
				player.move_down(3)
			if keys[pygame.K_DOWN] and keys[pygame.K_LSHIFT]:
				player.move_down(6)
			if keys[pygame.K_r]:
				try:
					pygame.quit()
					game()
				except RecursionError:
					print("I don't think you should ever see this but if you do see this you restarted the game more than {} times \n and you'll need to reopen the game. I'm sorry if this happened ;-;".format(getrecursionlimit()))
			if keys[pygame.K_SPACE]:
				time_now = pygame.time.get_ticks()
				if bullet_time + BULLET_COOLDOWN < time_now:
					create_bullet()
					bullet_time = time_now

		for bullet in player_bullets:
			if bullet.rect.y <= 0:
				bullet.kill()
			bullet.rect.y -= 5

		for bullet in enemy_bullets:
			if bullet.rect.y >= SCREEN_HEIGHT:
				bullet.kill()
			if current_level == 1:
				bullet.rect.y += 2
			if current_level == 2:
				bullet.rect.y += 4
			if current_level == 3 and not is_boss:
				bullet.rect.y += 5
			if current_level == 3 and is_boss:
				bullet.rect.y += 3
			if current_level == 4 and not is_boss:
				if len(enemies) > 15:
					bullet.rect.y += 7
				else:
					bullet.rect.y += 5
			if current_level == 4 and is_boss:
				bullet.rect.y += 10

			if pygame.sprite.groupcollide(sprites, enemy_bullets, False, True):
				player_death()

		for enemy in enemies:
			if enemy.health <= 0:
				enemy.kill()
				if not is_boss:
					ding.play()
				if not is_boss:
					score += current_level * 200
				else:
					score += current_level * 5000
				score_text = font.render("Score: {}".format(str(score)), True, CYAN, None)
			if pygame.sprite.spritecollideany(enemy, player_bullets):
				enemy.health -= 50
			if pygame.sprite.spritecollideany(player, enemies):
				player_death()

		# main menu #
		if current_level == "main_menu":
			for button in sprites:
				if button.is_hovered():
					button.image = button.hovered_image
				else:
					button.image = button.unhovered_image

				if button.is_clicked():
					if button.name == "play_button":
						clear_all_sprites()
						sprites.add(player)
						current_level = 1
						mainmenu_music.stop()
						normal_music.unpause()
						player_alive = True
						level_1_preboss(enemies)
					elif button.name == "howtoplay_button":
						clear_all_sprites()
						current_level = "howtoplay"
						how_to_play(sprites, secondary_sprites)
					elif button.name == "exit_button":
						game_running = False
					elif button.name == "github_button":
						if not github_opened:
							webbrowser.open("https://github.com/emredesu/re-one")  # putting this in a while loop was not a good idea ;-;
							github_opened = True

		# how to play screen #
		if current_level == "howtoplay":
			for button in sprites:
				if button.is_hovered():
					button.image = button.hovered_image
				else:
					button.image = button.unhovered_image

				if button.is_clicked():
					clear_all_sprites()
					github_opened = False
					current_level = "main_menu"
					mainmenu(sprites)

		collide_list = pygame.sprite.groupcollide(player_bullets, enemies, True, False)

		# level 1 #
		if current_level == 1 and not is_boss:
			if pygame.time.get_ticks() - timer > LEVEL_1_PREBOSS_BULLET_TIMER:
				level_1_preboss_bullets(enemies, enemy_bullets)
				timer = pygame.time.get_ticks()

		if current_level == 1 and is_boss:
			if pygame.time.get_ticks() - timer > LEVEL_1_BOSS_BULLET_TIMER:
				level_1_boss_attack(enemy_bullets)
				timer = pygame.time.get_ticks()

		if current_level == 1 and len(enemies) == 0 and not is_boss:
			clear_enemy_bullets()
			normal_music.pause()
			boss_music.unpause()
			is_boss = True
			level_1_boss(enemies)

		if current_level == 1 and len(enemies) == 0 and is_boss:
			clear_enemy_bullets()
			is_boss = False
			level_clear()
			current_level = 2
			level_2_preboss(enemies, player)
			normal_music.unpause()

		# level 2 #
		if current_level == 2 and not is_boss:
			if pygame.time.get_ticks() - timer > LEVEL_2_PREBOSS_BULLET_TIMER:
				level_2_preboss_bullets(enemies, enemy_bullets)
				timer = pygame.time.get_ticks()

		if current_level == 2 and is_boss:
			if pygame.time.get_ticks() - timer > LEVEL_2_BOSS_BULLET_TIMER_1:
				level_2_boss_attack_1(enemy_bullets)
				timer = pygame.time.get_ticks()
			if pygame.time.get_ticks() - timer_2 > LEVEL_2_BOSS_BULLET_TIMER_2:
				level_2_boss_attack_2(enemy_bullets)
				timer_2 = pygame.time.get_ticks()

		if current_level == 2 and len(enemies) == 0 and not is_boss:
			clear_enemy_bullets()
			normal_music.pause()
			boss_music.unpause()
			is_boss = True
			level_2_boss(enemies)

		if current_level == 2 and len(enemies) == 0 and is_boss:
			clear_enemy_bullets()
			is_boss = False
			level_clear()
			current_level = 3
			level_3_preboss(enemies, player)
			normal_music.unpause()

		# level 3 #
		if current_level == 3 and not is_boss:
			if go_right:
				for enemy in enemies:
					enemy.rect.x += 1
					if enemies.sprites()[0].rect.x >= 400:
						go_right = False
			if not go_right:
				for enemy in enemies:
					enemy.rect.x -= 1
					if enemies.sprites()[0].rect.x <= 0:
						go_right = True

			if pygame.time.get_ticks() - timer > LEVEL_3_PREBOSS_BULLET_TIMER:
				level_3_preboss_bullets(enemies, enemy_bullets)
				timer = pygame.time.get_ticks()

		if current_level == 3 and len(enemies) == 0 and not is_boss:
			clear_enemy_bullets()
			normal_music.pause()
			boss_music.unpause()
			is_boss = True
			go_right = True
			level_3_boss(enemies)

		if current_level == 3 and is_boss:
			if go_right:
				for enemy in enemies:
					enemy.rect.x += 2
					if enemies.sprites()[0].rect.x >= SCREEN_WIDTH - 200:
						go_right = False
			if not go_right:
				for enemy in enemies:
					enemy.rect.x -= 2
					if enemies.sprites()[0].rect.x <= 0:
						go_right = True

			if pygame.sprite.groupcollide(player_bullets, enemy_bullets, True, True):
				pass

			if pygame.time.get_ticks() - timer > LEVEL_3_BOSS_BULLET_TIMER:
				level_3_boss_attack(enemy_bullets)
				timer = pygame.time.get_ticks()

		if current_level == 3 and is_boss and len(enemies) == 0:
			clear_enemy_bullets()
			is_boss = False
			level_clear()
			current_level = 4
			level_4_preboss(enemies, player)
			normal_music.unpause()

		# level 4 #
		if current_level == 4 and not is_boss:
			if pygame.sprite.groupcollide(player_bullets, enemy_bullets, True, True):
				pass

			if go_right:
				for enemy in enemies:
					enemy.rect.x += 5
					if enemies.sprites()[0].rect.x >= 400:
						go_right = False
			if not go_right:
				for enemy in enemies:
					enemy.rect.x -= 5
					if enemies.sprites()[0].rect.x <= 0:
						go_right = True

			if len(enemies) > 15:
				if pygame.time.get_ticks() - timer > LEVEL_4_PREBOSS_BULLET_TIMER:
					level_4_preboss_bullets(enemies, enemy_bullets)
					timer = pygame.time.get_ticks()
			else:
				if pygame.time.get_ticks() - timer > LEVEL_4_PREBOSS_BULLET_PITY_TIMER:
					level_4_preboss_bullets(enemies, enemy_bullets)
					timer = pygame.time.get_ticks()

		if current_level == 4 and len(enemies) == 0 and not is_boss:
			clear_enemy_bullets()
			normal_music.pause()
			boss_music.unpause()
			is_boss = True
			level_4_boss(enemies)

		if current_level == 4 and is_boss:
			if go_down:
				for boss in enemies:
					boss.rect.y += 1
					if boss.rect.y + 200 >= SCREEN_HEIGHT:
						boss.rect.y -= SCREEN_HEIGHT - 210
						go_down = False

			if not go_down:
				for boss in enemies:
					boss.image = kanna_stage_two.convert()
				if pygame.time.get_ticks() - timer > LEVEL_4_BOSS_BULLET_TIMER:
					level_4_boss_attack(enemy_bullets)
					timer = pygame.time.get_ticks()

		if current_level == 4 and is_boss and len(enemies) == 0:
			game_completion_bonus = 200000
			score += game_completion_bonus
			clear_all_sprites()
			level_clear()
			finish_time = time() - start_time
			time_bonus = 500000 - int(finish_time * 100)
			if not time_bonus < 0:
				score += time_bonus
			finish_time_readable = str(timedelta(seconds=finish_time))[:-7]
			current_level = "win"
			which_ending(sprites)

		if current_level == "win":
			for button in sprites:
				if button.is_hovered():
					button.image = button.hovered_image
				else:
					button.image = button.unhovered_image

				if button.is_clicked():
					clear_all_sprites()
					if button.name == "emilia_button":
						current_level = "emilia_ending"
					elif button.name == "rem_button":
						current_level = "rem_ending"

		if current_level == 1:
			screen.blit(level_1_bg_converted, (0, 0))
		elif current_level == 2:
			screen.blit(level_2_bg_converted, (0, 0))
		elif current_level == 3:
			screen.blit(level_3_bg_converted, (0, 0))
		elif current_level == 4:
			screen.blit(level_4_bg_converted, (0, 0))
		elif current_level == "main_menu":
			screen.blit(main_menu_bg_converted, (0, 0))
		elif current_level == "win":
			screen.fill(WHITE)
			question_text = font.render("Congratulations, you beat the game! Now, who will you give a hug to?", True, BLACK, None)
			screen.blit(question_text, (10, 650))
		elif current_level == "emilia_ending":
			screen.blit(emilia_ending_converted, (0, 0))
			game_over_text = font.render("You beat the game in {} with a score of {} which is {} highscore{}".format(
				finish_time_readable, score, "a" if is_highscore() else "not a", "!" if is_highscore() else ". :c"), True, BLACK, None)
			screen.blit(game_over_text, (10, 15))

		elif current_level == "rem_ending":
			screen.blit(rem_ending_converted, (0, 0))
			game_over_text = font.render("You beat the game in {} with a score of {} which is {} highscore{}".format(
				finish_time_readable, score, "a" if is_highscore() else "not a", "!" if is_highscore() else ". :c"), True, BLACK, None)
			screen.blit(game_over_text, (340, 25))

		# render score #
		if current_level not in ["main_menu", "howtoplay", "win", "emilia_ending", "rem_ending"]:
			screen.blit(score_text, (0, 10))

		sprites.draw(screen)
		secondary_sprites.draw(screen)
		player_bullets.draw(screen)
		enemies.draw(screen)
		enemy_bullets.draw(screen)
		pygame.display.flip()

		clock.tick(120)


if __name__ == "__main__":
	game()
