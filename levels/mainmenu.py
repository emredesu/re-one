from entities.button import Button
from tools.images import play_unhovered, play_hovered, howtoplay_unhovered, howtoplay_hovered, exit_unhovered, exit_hovered, github_unhovered, github_hovered, main_menu_bg


def mainmenu(sprite_group):
	play_button = Button("play_button", play_unhovered.convert(), play_hovered.convert(), 850, 20)
	howtoplay_button = Button("howtoplay_button", howtoplay_unhovered.convert(), howtoplay_hovered.convert(), 850, 90)
	exit_button = Button("exit_button", exit_unhovered.convert(), exit_hovered.convert(), 850, 160)
	github_button = Button("github_button", github_unhovered.convert(), github_hovered.convert(), 860, 530)

	sprite_group.add(play_button, howtoplay_button, exit_button, github_button)
