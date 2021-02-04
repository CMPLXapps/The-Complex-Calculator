#!usr/bin/env python3
import keyboard
import sys
sys.path.append('..')
from pytools import *
import time
import shutil
def load():
	comp.clear()
	terminalWidth, terminalHeight = shutil.get_terminal_size()
	print('\n(Version 4.0.0)\n\n')
	print(' _____                __                                    __                                      '.center(terminalWidth))
	print('/_  _/  /7  __      ,\'_/  _   _      _   /7  __ _ __      ,\'_/  _   /7  __       /7  _   /7  _   _  '.center(terminalWidth))
	print(' / /   / \\,\'o/     / /_ ,\'o| / \\\'\\  /o| // ,\'o/ \\V,\'     / /_ ,\'o| // ,\',\' /7/7 // ,\'o| /_7,\'o| //7 '.center(terminalWidth))
	print('/_/   /n_/|_(      |__/ |_,\'/_nn_/ /_,\'//  |_( ,\'n\\      |__/ |_,7//  \\_\\ /__/ //  |_,7//  |_,\'//   '.center(terminalWidth))
	print('                                  //                                                                '.center(terminalWidth))
	print('   _     _     _     _     _     _     _       _  '.center(terminalWidth))
	print('  / \\   / \\   / \\   / \\   / \\   / \\   / \\     / \\ '.center(terminalWidth))
	print(' ( V ) ( e ) ( r ) ( s ) ( i ) ( o ) ( n )   ( 4 )'.center(terminalWidth))
	print('  \\_/   \\_/   \\_/   \\_/   \\_/   \\_/   \\_/     \\_/ '.center(terminalWidth))
	print('\n' * (terminalHeight - 14))
	print('\n')
	print('Press ENTER to Continue'.center(terminalWidth))
	print('(Or press Q or ESC to quit)'.center(terminalWidth))
	while True:
		if keyboard.is_pressed('enter'):
			break
		elif keyboard.is_pressed('q') or keyboard.is_pressed('esc'):
			sys.exit()
		else:
			continue
	return