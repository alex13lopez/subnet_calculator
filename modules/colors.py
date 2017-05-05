# -*- UTF-8 -*-

import os


if os.name == "posix":
	# Font colors:
	class fcolors:
		CYAN = '\033[96m'
		MAGENTA = '\033[95m'
		GREY = '\033[94m'
		GREEN = '\033[92m'
		YELLOW = '\033[93m'
		RED = '\033[91m'
		RESET = '\033[0m'
		BOLD = '\033[1m'
		UNDERLINE = '\033[4m'

	# Background colors:
	class bcolors:
		BLACK = "\u001b[40m"
		RED = "\u001b[41m"
		GREEN = "\u001b[42m"
		YELLOW = "\u001b[43m"
		BLUE = "\u001b[44m"
		MAGENTA = "\u001b[45m"
		CYAN = "\u001b[46m"
		WHITE = "\u001b[47m"

else:
	# We empty the vars since windows does not support ANSI representation unless you have ANSICON which is not available for Windows 10
	class fcolors:
		CYAN = ''
		MAGENTA = ''
		GREY = ''
		GREEN = ''
		YELLOW = ''
		RED = ''
		RESET = ''
		BOLD = ''
		UNDERLINE = ''

	class bcolors:
		BLACK = ''
		RED = ''
		GREEN = ''
		YELLOW = ''
		BLUE = ''
		MAGENTA = ''
		CYAN = ''
		WHITE = ''
