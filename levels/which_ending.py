from entities.button import Button
from tools.images import emilia_unhovered, emilia_hovered, rem_unhovered, rem_hovered


def which_ending(sprites):
	emilia_button = Button("emilia_button", emilia_unhovered.convert(), emilia_hovered.convert(), 0, 0)
	rem_button = Button("rem_button", rem_unhovered.convert(), rem_hovered.convert(), 450, 0)

	sprites.add(emilia_button, rem_button)