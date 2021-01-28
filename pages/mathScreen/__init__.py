from STDIMPORTS import *
from INCLIMPORTS import *
from HANDLERS import *
import graphScreen
#-------------------
terminalWidth, terminalHeight = SH.get_terminal_size()
hashFill = fore.darkgray + ('#' * (terminalHeight - 80) / 2) + fore.white
#-------------------
def hashLine(x):
	for i in range(0, x):
		print(fore.darkgray + ('#' * terminalWidth) + fore.white)
#-------------------
class load:
	def screen():
		PT.clear()
		print(f'{fore.lightyellow} ___          _                                                              _     _    '.center(terminalWidth))
		print(f'{fore.lightyellow}| __|  _ _   | |_   ___   _ _     _  _   ___   _  _   _ _     _ __    __ _  | |_  | |_  '.center(terminalWidth))
		print(f'{fore.lightyellow}| _|  | \' \\  |  _| / -_) | \'_|   | || | / _ \\ | || | | \'_|   | \'  \\  / _` | |  _| | \' \\ '.center(terminalWidth))
		print(f'{fore.lightyellow}|___| |_||_|  \\__| \\___| |_|      \\_, | \\___/  \\_,_| |_|     |_|_|_| \\__,_|  \\__| |_||_|'.center(terminalWidth))
		print(f'{fore.lightyellow}                                   |__/                                                  '.center(terminalWidth))
		print(f'{fore.lightcyan}==Help==History==Graph==Back==Reload==Quit' + ('=' * (terminalWidth - 35)) + '(Type One)=='.center(terminalWidth) + fore.white)
	class help():
		def all():
			PT.clear()
			helpscreens.all()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.variables()
				elif keyboard.is_pressed('left'):
					load.help.trig()
				else:
					continue
		def variables():
			PT.clear()
			helpscreens.variables()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.constants()
				elif keyboard.is_pressed('left'):
					load.help.all()
		def constants():
			PT.clear()
			helpscreens.constants()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.math()
				elif keyboard.is_pressed('left'):
					load.help.variables()
		def math():
			PT.clear()
			helpscreens.math()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.statistics()
				elif keyboard.is_pressed('left'):
					load.help.contants()
		def statistics():
			PT.clear()
			helpscreens.statistics()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.trig()
				elif keyboard.is_pressed('left'):
					load.help.math()
		def trig():
			PT.clear()
			helpscreens.trig()
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.all()
				elif keyboard.is_pressed('left'):
					load.help.statistics()
	def main():
		while True:
			load().screen()
			continue