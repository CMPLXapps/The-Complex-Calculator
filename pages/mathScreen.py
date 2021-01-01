import keyboard
import sys
sys.path.append('..')
from varHandler import *
from resources import graph, processing
from resources.style import fore, reset, formatting, back
from resources.mathFunctions import *
from resources.constantsContainer import *
import com.cmplx.pymodels.base as comp
import shutil
def vars():
	global terminalWidth, terminalHeight, hashFill
	terminalWidth, terminalHeight = shutil.get_terminal_size()
	hashFill = fore.darkgray + ('#' * (terminalHeight - 80) / 2) + fore.white
vars()
def hashLine(x):
	for i in range(0, x):
		print(fore.darkgray + ('#' * terminalWidth) + fore.white)
class load:
	def screen():
		comp.clear()
		print(f'{fore.lightyellow} ___          _                                                              _     _    '.center(terminalWidth))
		print(f'{fore.lightyellow}| __|  _ _   | |_   ___   _ _     _  _   ___   _  _   _ _     _ __    __ _  | |_  | |_  '.center(terminalWidth))
		print(f'{fore.lightyellow}| _|  | \' \\  |  _| / -_) | \'_|   | || | / _ \\ | || | | \'_|   | \'  \\  / _` | |  _| | \' \\ '.center(terminalWidth))
		print(f'{fore.lightyellow}|___| |_||_|  \\__| \\___| |_|      \\_, | \\___/  \\_,_| |_|     |_|_|_| \\__,_|  \\__| |_||_|'.center(terminalWidth))
		print(f'{fore.lightyellow}                                   |__/                                                  '.center(terminalWidth) + reset.styling)
		print(f'{fore.lightcyan}==Help==History==Graph==Back==Reload==Quit' + ('=' * (terminalWidth - 35)) + '(Type One)=='.center(terminalWidth) + reset.styling)
	class help():
		def all():
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   {fore.white}All{reset.styling}   Variables   Constants   Math   Statistics   Trigonometry   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|  Dealing with Variables  | Example: "a" to reference,                        |{hashFill}')
			print(f'{hashFill}+--------------------------+          "edit_a or edita" to edit                |{hashFill}')
			print(f'{hashFill}|  Functions for editing:    - set(value) --Sets the value                     |{hashFill}')
			print(f'{hashFill}|                            - revert() --Reverts to old value                 |{hashFill}')
			print(f'{hashFill}| sv, save_variables, svar   - clear() --Sets back to zero                     |{hashFill}')
			print(f'{hashFill}|  to save all variables                (Variables are lettered a-f)           |{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|        Constants         |     - pi or π                                     |{hashFill}')
			print(f'{hashFill}+--------------------------+     - tau (2 x π)                                 |{hashFill}')
			print(f"{hashFill}|                                - eul (Euler's Number, or e, don't use e,     |{hashFill}")
			print(f"{hashFill}|                                          it's the name of one of the         |{hashFill}")
			print(f'{hashFill}|                                            programmable variables.)          |{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|       General Math       |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}|Basic Math: x + y, x - y, x * y, x / y                                        |{hashFill}')
			print(f'{hashFill}|Whole Division (quotient and remainder): x /& n or wdiv(x, n)                 |{hashFill}')
			print(f'{hashFill}|Powers: exp(x, n), x ** n, x^n                                                |{hashFill}')
			print(f'{hashFill}|Modulus (remainder): x % n                                                    |{hashFill}')
			print(f'{hashFill}|Absolute Value: absv(), |x|                                                   |{hashFill}')
			print(f'{hashFill}|Factorial: factorial(x), fact(x), !x                                          |{hashFill}')
			print(f'{hashFill}|Square Root: sqrt(x)                                                          |{hashFill}')
			print(f'{hashFill}|Cube Root: cbrt(x)                                                            |{hashFill}')
			print(f'{hashFill}|Tesseract Root: tsrt(x)                                                       |{hashFill}')
			print(f'{hashFill}|Nth Root: root(x, n)                                                          |{hashFill}')
			print(f'{hashFill}|Logarithm: log(x) (Log Base 10), log(x, n) (Log Base N), ln(x) (Natural Log)  |{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|        Statistics        |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|       Trigonometry       |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}+------------------------------------------------------------------------------+{hashFill}')
			if terminalHeight < 40:
				hashLine(2)
			else:
				hashLine(terminalHeight - 38)
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
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   All   {fore.white}Variables{reset.styling}   Constants   Math   Statistics   Trigonometry   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|  Dealing with Variables  | Example: "a" to reference,                        |{hashFill}')
			print(f'{hashFill}+--------------------------+          "edit_a or edita" to edit                |{hashFill}')
			print(f'{hashFill}|  Functions for editing:    - set(value) --Sets the value                     |{hashFill}')
			print(f'{hashFill}|                            - revert() --Reverts to old value                 |{hashFill}')
			print(f'{hashFill}| sv, save_variables, svar   - clear() --Sets back to zero                     |{hashFill}')
			print(f'{hashFill}|  to save all variables                (Variables are lettered a-f)           |{hashFill}')
			print(f'{hashFill}+------------------------------------------------------------------------------+{hashFill}')
			hashLine(terminalHeight - 12)
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.constants()
				elif keyboard.is_pressed('left'):
					load.help.all()
		def constants():
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   All   Variables   {fore.white}Constants{reset.styling}   Math   Statistics   Trigonometry   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|        Constants         |     - pi or π                                     |{hashFill}')
			print(f'{hashFill}+--------------------------+     - tau (2 x π)                                 |{hashFill}')
			print(f"{hashFill}|                                - eul (Euler's Number, or e, don't use e,     |{hashFill}")
			print(f"{hashFill}|                                       it's the name of one of the            |{hashFill}")
			print(f'{hashFill}|                                         programmable variables.)             |{hashFill}')
			print(f'{hashFill}+------------------------------------------------------------------------------+{hashFill}')
			hashLine(terminalHeight - 12)
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.math()
				elif keyboard.is_pressed('left'):
					load.help.variables()
		def math():
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   All   Variables   Constants   {fore.white}Math{reset.styling}   Statistics   Trigonometry   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|       General Math       |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}|Basic Math: x + y, x - y, x * y, x / y                                        |{hashFill}')
			print(f'{hashFill}|Whole Division (quotient and remainder): x /& n or wdiv(x, n)                 |{hashFill}')
			print(f'{hashFill}|Powers: exp(x, n), x ** n, x^n                                                |{hashFill}')
			print(f'{hashFill}|Modulus (remainder): x % n                                                    |{hashFill}')
			print(f'{hashFill}|Absolute Value: absv(), |x|                                                   |{hashFill}')
			print(f'{hashFill}|Factorial: factorial(x), fact(x), !x                                          |{hashFill}')
			print(f'{hashFill}|Square Root: sqrt(x)                                                          |{hashFill}')
			print(f'{hashFill}|Cube Root: cbrt(x)                                                            |{hashFill}')
			print(f'{hashFill}|Tesseract Root: tsrt(x)                                                       |{hashFill}')
			print(f'{hashFill}|Nth Root: root(x, n)                                                          |{hashFill}')
			print(f'{hashFill}|Logarithm: log(x) (Log Base 10), log(x, n) (Log Base N), ln(x) (Natural Log)  |{hashFill}')
			print(f'{hashFill}+------------------------------------------------------------------------------+{hashFill}')
			hashLine(terminalHeight - 12)
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.statistics()
				elif keyboard.is_pressed('left'):
					load.help.contants()
		def statistics():
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   All   Variables   Constants   Math   {fore.white}Statistics{reset.styling}   Trigonometry   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|        Statistics        |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}+------------------------------------------------------------------------------+{hashFill}')
			hashLine(terminalHeight - 12)
			while True:
				if keyboard.is_pressed('esc'):
					load.main()
				elif keyboard.is_pressed('right'):
					load.help.trig()
				elif keyboard.is_pressed('left'):
					load.help.math()
		def trig():
			hashLine(2)
			print(f'{hashFill}+----------------------------------------------------------------ESC to close--+{hashFill}')
			print(f'{hashFill}|{reset.styling}    <   All   Variables   Constants   Math   Statistics   {fore.white}Trigonometry{reset.styling}   >    {fore.white}|{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			print(f'{hashFill}|       Trigonometry       |                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+                                                   |{hashFill}')
			print(f'{hashFill}+--------------------------+---------------------------------------------------+{hashFill}')
			hashLine(terminalHeight - 12)
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