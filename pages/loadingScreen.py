#!usr/bin/env python3
import time
import sys
sys.path.append('..')
from pytools import *
import shutil
def load():
	comp.clear()
	terminalWidth, terminalHeight = shutil.get_terminal_size()
	print('\n' * 4)
	print('      ::::::::         :::   :::       :::::::::       :::        :::    :::'.center(terminalWidth))
	print('    :+:    :+:       :+:+: :+:+:      :+:    :+:      :+:        :+:    :+: '.center(terminalWidth))
	print('   +:+             +:+ +:+:+ +:+     +:+    +:+      +:+         +:+  +:+   '.center(terminalWidth))
	print('  +#+             +#+  +:+  +#+     +#++:++#+       +#+          +#++:+     '.center(terminalWidth))
	print(' +#+             +#+       +#+     +#+             +#+         +#+  +#+     '.center(terminalWidth))
	print('#+#    #+#      #+#       #+#     #+#             #+#        #+#    #+#     '.center(terminalWidth))
	print('########       ###       ###     ###             ########## ###    ###      '.center(terminalWidth))
	print('\n' * (terminalHeight - 11))
	print('Loading...')
	time.sleep(2)
	return