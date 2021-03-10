#!usr/bin/env python3
from STDIMPORTS import *
from INCLIMPORTS import *
from HANDLERS import *
import graphScreen
#-------------------

terminalWidth, terminalHeight = SH.get_terminal_size()

hashFill = fore.darkgray + ('#' * (terminalHeight - 80) / 2) + fore.white

def hashLine(x):
	for i in range(0, x):
		 return fore.darkgray + ('#' * terminalWidth) + fore.white

class ColorFormattingParentClass:

	def __init__(self):
		self.colordict = {
			'<yellow>': '\u001b[93m',
			'<gray>': '\u001b[90m',
			'<white>': '\u001b[97m',
			'<reset>': '\u001b[0m'
			'<hf>': hashFill,
		}

	def parseHashLine(self, string):
		while True:
			hashIndex = string.find('<hl')
			if hashIndex != -1:
				str_beg = string[:hashIndex]
				str_end = string[string[hashIndex+1:].find('>')+1:]
				workingSubStr = (string.replace('<hl', '@')[hashIndex+1:])
				hashInt = workingSubStr[:workingSubStr.find('>')]
				string = str_beg + hashLine()

	def __call__(self, string):
		for i in list(self.colordict.keys()):
			string = string.replace(i, colordict[i])
		return string

def ReadAndCenter(fp, centerLength):
	with open(fp, 'r') as readfile:
		for i in readfile.readlines():
			print(i.center(centerlength))

CFormat = ColorFormattingParentClass()

#-------------------

class load:
	def screen():
		PT.clear()
		print(f'{fore.lightyellow} ___          _                                                              _     _    '.center(terminalWidth))
		print('| __|  _ _   | |_   ___   _ _     _  _   ___   _  _   _ _     _ __    __ _  | |_  | |_  '.center(terminalWidth))
		print('| _|  | \' \\  |  _| / -_) | \'_|   | || | / _ \\ | || | | \'_|   | \'  \\  / _` | |  _| | \' \\ '.center(terminalWidth))
		print('|___| |_||_|  \\__| \\___| |_|      \\_, | \\___/  \\_,_| |_|     |_|_|_| \\__,_|  \\__| |_||_|'.center(terminalWidth))
		print('                                   |__/                                                  '.center(terminalWidth))
		print(f'{fore.white}Press (ESC) for more options'.center(terminalWidth))
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