import time
import sys
sys.path.append('..')
import com.cmplx.pymodules.base as comp
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