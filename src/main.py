#!usr/bin/env python3
import os
import modules.keyboard.keyboard as keyboard
from pages import *
print('\n\n>> Maximize Your Screen Now <<'.center(50))
print('\n(Press ENTER or ESCAPE when you\'re ready)')
while True:
	if keyboard.is_pressed('enter') or keyboard.is_pressed('esc'):
		break
loadingScreen.load()
while True:
	titleScreen.load()
	mathScreen.load.main()