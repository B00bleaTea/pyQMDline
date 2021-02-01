import os

ROOT = os.path.abspath('.')
pyQMD_PATH = {"STOP": "pyQMDline",
			"boot": True,

			"system-folder": f"{ROOT}/system",

			"media": f"{ROOT}/system/system-folders/media",
			"documents": f"{ROOT}/system/system-folders/documents",
			"trash": f"{ROOT}/system/system-folders/trash",

			"autorun": [f'{ROOT}/LICENSE/__license__.py',
						f'{ROOT}/system/system-folders/EMPTY_TRASH.py'],

			"theme-file": f"{ROOT}/THEME.pqtheme",

			"version": "1.3",
			"phase": "beta"}

# this in the PATH of your download of pyQMDline
# if you don't know what you're doing it's possible that you'll break it
# AKA. don't touch anything if you're not experienced enough
