import os

from ast import literal_eval
from colorama import Fore, Style


def coloured(msg: str, colour: str = 'CYAN') -> str:
	colour = eval(f'Fore.{colour.upper()}')
	return f'{colour}{msg}{Style.RESET_ALL}'


class Out:
	@classmethod
	def out(cls, msg: str):
		print(coloured(msg, 'magenta'))

	@classmethod
	def err(cls, msg: str):
		print(coloured(msg, 'red'))

	@classmethod
	def inp(cls, prmt: str):
		return input(f'{coloured(prmt, "yellow")} ')
