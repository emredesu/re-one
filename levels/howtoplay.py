from entities.button import Button
from entities.image import Image
from tools.images import howtoplay, back_hovered, back_unhovered


def how_to_play(sprite_group, other_sprite_group):
	howtoplay_image = Image(howtoplay.convert(), 0, 0)
	back_button = Button("back_button", back_unhovered.convert(), back_hovered.convert(), 880, 400)

	other_sprite_group.add(howtoplay_image)
	sprite_group.add(back_button)
