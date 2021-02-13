import os
import shutil
import sys
import re
import pathlib

from system.PATH import *
from ast import literal_eval
from colorama import Fore, Style, Back

# default theme
INPUT_FORE, OUTPUT_FORE, ERRORS_FORE, SUCCESS_FORE = 'YELLOW', 'MAGENTA', 'RED', 'GREEN'
INPUT_BACK, OUTPUT_BACK, ERRORS_BACK, SUCCESS_BACK = 'RESET', 'RESET', 'RESET', 'RESET'
INPUT_EFFECT, OUTPUT_EFFECT, ERRORS_EFFECT, SUCCESS_EFFECT = 'NORMAL', 'NORMAL', 'NORMAL', 'NORMAL'
try:
	with open(pathlib.Path(f'{ROOT}/THEME.pqtheme'), 'r') as f:
		SEARCH = re.compile(r"^.+ = \'[A-Z]+\'")
		for theme_item in f.readlines():
			theme_item = theme_item.strip('\n')
			if SEARCH.search(theme_item):
				exec(theme_item)
except:
	print(f'{Fore.RED}[ THEME-ERROR ] UNABLE TO LOAD THE THEME FILE, USING THE DEFAULT THEME{Style.RESET_ALL}')


def coloured(msg: str, colour: str = 'CYAN', effect: str = 'NORMAL', back: str = 'RESET') -> str:
	effect = eval(f'Style.{effect.upper()}')
	colour = eval(f'Fore.{colour.upper()}')
	back = eval(f'Back.{back.upper()}')
	return f'{effect}{back}{colour}{msg}{Style.RESET_ALL}'


class Out:
	@classmethod
	def out(cls, msg: str):
		print(coloured(msg, OUTPUT_FORE, OUTPUT_EFFECT, OUTPUT_BACK))

	@classmethod
	def err(cls, msg: str):
		print(coloured(msg, ERRORS_FORE, ERRORS_EFFECT, ERRORS_BACK))

	@classmethod
	def inp(cls, prmt: str):
		return input(f'{coloured(prmt, INPUT_FORE, INPUT_EFFECT, INPUT_BACK)} ')

	@classmethod
	def success(cls, msg: str):
		print(coloured(msg, SUCCESS_FORE, SUCCESS_EFFECT, SUCCESS_BACK))
