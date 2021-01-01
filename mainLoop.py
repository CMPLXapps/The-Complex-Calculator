import os
import keyboard
from pages import *
os.system('title The Complex Calculator 4 :: Version 4.0.0')
print('\n\n>> Maximize Your Screen Now <<'.center(50))
print('\n(Press Enter When you\'re ready)')
while True:
	if keyboard.is_pressed('enter'):
		break
loadingScreen.load()
while True:
	titleScreen.load()
	mathScreen.load.main()